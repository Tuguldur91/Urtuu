"""Run this pack's trusted Python notebook cells using only the standard library.

This is a small runner for plain Python, stdout/stderr, final expressions, and
the Signal notebook's SVG output. It is not a Jupyter kernel: IPython magics,
widgets, top-level await, and JavaScript Markdown blocks are not supported.
"""

import argparse
import ast
from contextlib import chdir, redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import sys
import traceback


class NotebookStream(io.TextIOBase):
    """Record printed output in notebook order, including interleaved stderr."""

    def __init__(self, outputs, name):
        self.outputs = outputs
        self.name = name

    def write(self, text):
        if text:
            if (self.outputs and self.outputs[-1].get("output_type") == "stream"
                    and self.outputs[-1]["name"] == self.name):
                self.outputs[-1]["text"] += text
            else:
                self.outputs.append({"output_type": "stream", "name": self.name, "text": text})
        return len(text)

    def flush(self):
        pass


def run_cell(source, namespace, outputs, count, filename):
    tree = ast.parse(source, filename=filename)
    # Check explicit imports for accidental package dependencies. This is not a
    # security sandbox; run only trusted notebooks, just as with ordinary Python.
    for node in ast.walk(tree):
        modules = []
        if isinstance(node, ast.Import):
            modules = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                raise ImportError("This practice runner supports standard-library imports only")
            modules = [node.module]
        for module in modules:
            if module.split(".")[0] not in sys.stdlib_module_names:
                raise ImportError(f"Not a standard-library module: {module}")

    last_expression = None
    if tree.body and isinstance(tree.body[-1], ast.Expr):
        last_expression = ast.Expression(tree.body.pop().value)
    with redirect_stdout(NotebookStream(outputs, "stdout")), redirect_stderr(NotebookStream(outputs, "stderr")):
        exec(compile(tree, filename, "exec"), namespace)
        if last_expression is not None:
            result = eval(compile(last_expression, filename, "eval"), namespace)
            if result is not None:
                data = {"text/plain": repr(result)}
                svg_renderer = getattr(result, "_repr_svg_", None)
                if callable(svg_renderer):
                    svg = svg_renderer()
                    if svg is not None:
                        data["image/svg+xml"] = svg
                outputs.append({
                    "output_type": "execute_result",
                    "execution_count": count,
                    "data": data,
                    "metadata": {},
                })


def run_notebook(path, write=False):
    """Return (executed notebook, success); optionally save output to the file."""
    path = Path(path).resolve()
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            cell["execution_count"] = None
            cell["outputs"] = []

    success = True
    count = 0
    with chdir(path.parent):
        for index, cell in enumerate(notebook["cells"], start=1):
            if cell["cell_type"] != "code":
                continue
            count += 1
            cell["execution_count"] = count
            try:
                run_cell("".join(cell["source"]), namespace, cell["outputs"], count,
                         f"{path.name}:cell-{index}")
            except Exception as error:
                cell["outputs"].append({
                    "output_type": "error",
                    "ename": type(error).__name__,
                    "evalue": str(error),
                    "traceback": traceback.format_exception(error),
                })
                success = False
                break  # Later cells may depend on the failed cell.

    if write:
        path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return notebook, success


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebooks", nargs="*", type=Path,
                        help="Notebook paths (default: all six beside this script)")
    parser.add_argument("--write", action="store_true", help="Save execution counts and outputs in the notebooks")
    parser.add_argument("--show-output", action="store_true", help="Also print each cell's text output in the terminal")
    args = parser.parse_args()
    paths = args.notebooks or sorted(Path(__file__).resolve().parent.glob("[0-9][0-9]_*.ipynb"))
    if not paths:
        parser.error("No practice notebooks found")

    all_passed = True
    total = 0
    for path in paths:
        try:
            notebook, success = run_notebook(path, write=args.write)
        except (OSError, ValueError) as error:
            print(f"FAIL {path}: {error}", file=sys.stderr)
            all_passed = False
            continue
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        count = sum(cell["execution_count"] is not None for cell in code_cells)
        total += count
        all_passed = all_passed and success
        status = "PASS" if success else "FAIL"
        saved = "; outputs saved" if args.write else "; outputs not saved (use --write)"
        print(f"{status} {path.name}: {count}/{len(code_cells)} cells{saved}")
        for cell in code_cells:
            for output in cell["outputs"]:
                if output["output_type"] == "error":
                    print(f"  Cell {cell['execution_count']}: {output['ename']}: {output['evalue']}", file=sys.stderr)
                elif args.show_output:
                    if output["output_type"] == "stream":
                        print(output["text"], end="")
                    elif output["output_type"] == "execute_result":
                        print(output["data"]["text/plain"])
        if args.show_output:
            print()
    print(f"Executed {total} Python cells across {len(paths)} notebooks. JavaScript Markdown is not executed.")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
