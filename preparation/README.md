# ОВТОО 2026: offline preparation notebooks

Six practice notebooks based on the station descriptions in `../urtuu.md`. These are inferred practice tasks, not official questions. Each notebook has embedded visuals, a worked example, three core exercises, an expanded bank of 15 possible station tasks, four extra practice questions, and separate solutions.

| Notebook | Focus |
|---|---|
| [01 Decode](01_decode.ipynb) | Representations, Caesar, Atbash, acrostics, grids, keyed ciphers, physical clue chains |
| [02 Log trace](02_log_trace.ipynb) | Deletion versus moves, permissions, sessions, request IDs, time zones, misleading statuses |
| [03 Signal](03_signal.ipynb) | Embedded Morse audio, waveform, stereo, spectrograms, tone mappings, keypad tones |
| [04 Glitch](04_glitch.ipynb) | UI testing plus JavaScript types, DOM events, forms, callbacks, fetch, and stale responses |
| [05 Mysterious graph](05_mysterious_graph.ipynb) | Routes, connectivity, Euler trails, coloring, trees, prerequisites, matching, stateful mazes |
| [06 Finale](06_finale.ipynb) | Computing quiz, JavaScript traces, logic, SQL, networking, and verified file reconstruction |

## Open and practice

Open the notebooks in JupyterLab, Jupyter Notebook, or an editor with notebook support and select a Python 3 kernel. Executable notebook cells use only Python's standard library. The Glitch notebook also contains JavaScript examples in Markdown: read them on paper or run them separately as described below. Your notebook application and kernel must already be installed before going offline. SVG illustrations and the audio player are embedded; `signal_practice.wav` is also provided for local playback and waveform analysis. Keep the folder together.

Run cells from top to bottom. Stop before the solutions and attempt the exercises on paper or in the provided work cell. Running all cells reveals solutions. Some viewers require trusting the notebook to render inline audio; the WAV works independently.

## Explore more station possibilities

Each notebook's **More station possibilities** section lists 15 variations, what might reveal each one, and a first approach: 90 scenarios across the pack. Study priorities describe a learning order, not the likelihood of an official question. The guidelines confirm only the broad station descriptions; tools, ciphers, algorithms, and quiz subjects remain unspecified.

Use the four **Extra practice** questions in each notebook to rehearse unfamiliar variations, then check the answers at the end. Allow another 10–15 minutes per notebook. The Signal WAV still practices Morse; the additional signal formats are recognition and paper exercises, not extra recordings.

## JavaScript at Glitch

[04 Glitch](04_glitch.ipynb) includes a JavaScript mini-course and eight debugging exercises with broken snippets, explanations, and corrected code. Topics include string/number conversion, checkbox state, missing callback returns, event registration, default form submission, loop closures, HTTP error handling, and out-of-order search responses.

Allow 20–30 additional minutes. JavaScript blocks are study material, not Python cells. Five exercises run in Node.js or a browser console; three use a browser DOM and a supplied blank-tab form helper. All examples work without a server or internet connection, and the fetch/search exercises use fake local responses. No JavaScript runtime is needed for paper practice. Use these tools at the competition only if organizers provide them.

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
