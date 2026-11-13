# ОВТОО 2026: offline preparation notebooks

Six practice notebooks based on the station descriptions in `../urtuu.md`. These are inferred practice tasks, not official questions. Each notebook has an embedded visual, a worked example, three exercises, and a separate solution section.

| Notebook | Focus |
|---|---|
| [01 Decode](01_decode.ipynb) | Binary, hex, Base64, Caesar, layered clues |
| [02 Log trace](02_log_trace.ipynb) | HTTP logs, timeline, evidence, audit correlation |
| [03 Signal](03_signal.ipynb) | Embedded audio, Morse, waveform, sampling |
| [04 Glitch](04_glitch.ipynb) | Validation, pagination, interface bug reports |
| [05 Mysterious graph](05_mysterious_graph.ipynb) | BFS, Dijkstra, Euler trails, coloring |
| [06 Finale](06_finale.ipynb) | Computing quiz and verified file reconstruction |

## Open and practice

Open the notebooks in JupyterLab, Jupyter Notebook, or an editor with notebook support and select a Python 3 kernel. The exercise code uses only Python's standard library. Your notebook application and kernel must already be installed before going offline. SVG illustrations and the audio player are embedded; `signal_practice.wav` is also provided for local playback and waveform analysis. Keep the folder together.

Run cells from top to bottom. Stop before the solutions and attempt the exercises on paper or in the provided work cell. Running all cells reveals solutions. Some viewers require trusting the notebook to render inline audio; the WAV works independently.

## Suggested preparation

- Session 1: Decode and Log trace, 35 minutes each; review mistakes for 20 minutes.
- Session 2: Signal and Glitch, 35 minutes each; review mistakes for 20 minutes.
- Session 3: Graph and Finale, 40 minutes each; review mistakes for 20 minutes.
- Session 4: Repeat weak exercises without looking at solutions and simulate a local-network, no-internet event.

Rotate the lead role among four teammates. Record evidence and recovered fragments in a shared paper log. Ask organizers about provided software and permitted paper notes; the guidelines prohibit personal electronic devices and do not list installed tools. The official scoring is 15 points for each of the first five stations, 25 for Finale, and up to 10 extra for restoring the missing file. Practice quiz scoring here is separate.

All illustrations and audio were generated locally for this pack; there are no external asset dependencies.

## Start here if the topics are new

Each notebook now includes a beginner mini-course before its exercises: vocabulary, step-by-step concepts, possible station tasks, and learning priorities. Allow 20–30 additional minutes per notebook for the lessons. Read the lesson, explain one concept to a teammate, work through the example, then attempt the exercises. The possible-task tables are predictions; only the explicitly marked guideline descriptions are confirmed.

## Visual learning

Each notebook includes a new “Learn it visually” section with an explanatory diagram, a reading guide, and a short question with a collapsible answer. Diagrams are embedded and also saved in `assets/`. They require no downloads or Python packages.

Online references were located, but the workspace could not resolve the image-download host, so the added diagrams were created locally. Optional online reference charts: [International Morse Code](https://commons.wikimedia.org/wiki/File:International_Morse_Code.svg) and [client–server illustration](https://commons.wikimedia.org/wiki/File:Client-server_model.svg). These links are supplementary; all notebook content works offline.
