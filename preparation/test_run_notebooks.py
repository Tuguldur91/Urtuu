"""Checks for the offline runner; no external test framework is needed."""

import json
from pathlib import Path
import tempfile
import unittest

from run_notebooks import run_notebook


class OfflineRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def notebook(self, sources, name="practice.ipynb"):
        path = self.directory / name
        notebook = {
            "nbformat": 4, "nbformat_minor": 5,
            "metadata": {"keep": "user settings"},
            "cells": [{"cell_type": "markdown", "metadata": {}, "id": "intro",
                       "source": ["Keep this lesson."],
                       "attachments": {"image.svg": {"image/svg+xml": "<svg/>"}}}],
        }
        for i, source in enumerate(sources):
            notebook["cells"].append({
                "cell_type": "code", "id": f"code-{i}", "metadata": {},
                "source": source.splitlines(keepends=True), "execution_count": 99,
                "outputs": [{"output_type": "stream", "name": "stdout", "text": "stale"}],
            })
        path.write_text(json.dumps(notebook), encoding="utf-8")
        return path, notebook

    def test_state_output_order_and_final_expression(self):
        path, original = self.notebook([
            "value = 40\nprint('ready')",
            "import sys\nprint('out')\nprint('err', file=sys.stderr)\nvalue + 2",
        ])
        notebook, success = run_notebook(path, write=True)
        self.assertTrue(success)
        outputs = notebook["cells"][2]["outputs"]
        self.assertEqual([o["output_type"] for o in outputs], ["stream", "stream", "execute_result"])
        self.assertEqual([o["name"] for o in outputs[:2]], ["stdout", "stderr"])
        self.assertEqual(outputs[-1]["data"]["text/plain"], "42")
        self.assertEqual(outputs[-1]["execution_count"], 2)
        self.assertEqual(notebook["metadata"], original["metadata"])
        self.assertEqual(notebook["cells"][0], original["cells"][0])
        self.assertEqual(json.loads(path.read_text()), notebook)

    def test_svg_and_relative_asset_without_writing(self):
        path, original = self.notebook([
            "from pathlib import Path\n"
            "class Picture:\n"
            "    def _repr_svg_(self): return Path('asset.svg').read_text()\n"
            "Picture()",
        ])
        (self.directory / "asset.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        previous = Path.cwd()
        notebook, success = run_notebook(path)
        self.assertTrue(success)
        self.assertIn("image/svg+xml", notebook["cells"][1]["outputs"][0]["data"])
        self.assertEqual(Path.cwd(), previous)
        self.assertEqual(json.loads(path.read_text()), original)

    def test_error_stops_and_clears_later_outputs(self):
        path, _ = self.notebook(["print('before')\nraise ValueError('bad input')", "print('unreachable')"])
        previous = Path.cwd()
        notebook, success = run_notebook(path, write=True)
        self.assertFalse(success)
        self.assertEqual(notebook["cells"][1]["outputs"][-1]["ename"], "ValueError")
        self.assertEqual(notebook["cells"][2]["outputs"], [])
        self.assertIsNone(notebook["cells"][2]["execution_count"])
        self.assertEqual(Path.cwd(), previous)

    def test_notebooks_do_not_share_variables(self):
        first, _ = self.notebook(["secret = 1"], "first.ipynb")
        second, _ = self.notebook(["secret"], "second.ipynb")
        self.assertTrue(run_notebook(first)[1])
        notebook, success = run_notebook(second)
        self.assertFalse(success)
        self.assertEqual(notebook["cells"][1]["outputs"][0]["ename"], "NameError")

    def test_nonstandard_import_is_reported(self):
        path, _ = self.notebook(["import package_not_in_standard_library"])
        notebook, success = run_notebook(path)
        self.assertFalse(success)
        error = notebook["cells"][1]["outputs"][0]
        self.assertEqual(error["ename"], "ImportError")
        self.assertIn("Not a standard-library module", error["evalue"])


if __name__ == "__main__":
    unittest.main()
