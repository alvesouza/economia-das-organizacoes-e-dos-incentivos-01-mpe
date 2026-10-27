# Plan: quizzes, NotebookLM audio, TTS, notes and book-exercise lists for Lectures 1–8

User request (2026-10-25): "write quiz of questions for each lecture, write notebooklm audio,
tts, notes and exercises from book exercises". No question round (memory
`feedback-skip-question-rounds`); defaults are copied from the Lecture 1 deliverables.

## Defaults

| Deliverable | Default | Pattern file |
|---|---|---|
| Quiz | 3 quizzes × 10 questions per lecture, by subtopic; `Simulados/quiz-lectureNN-K-<slug>-2026-10-25.md`; validated with `.claude/quiz-validate.py` | `Simulados/quiz-lecture01-*` |
| NotebookLM audio | 2 parts, Custom Prompt, hard depth, < 5,000 chars, no language line; `NotebookLM/audio/lecture-NN-audio-part{1,2}.md` | `NotebookLM/audio/lecture-01-*` |
| TTS | one plain-text narration of the lecture's notes, math in words; `Leituras/lecture-NN-notes-narrated.txt` | `Leituras/aula-01-notes-narrated.txt` |
| Notes | already exist for L01–L08; reconcile L02 with `Aula/Lecture02.pdf`; one PDF per unit via `notes_pdf.py` | `/notes` Step 4b |
| Exercises | practice list of book exercises reproduced verbatim, tiered; `Listas/pratica-lecture-NN.md`; candidates from the study guide's "After class" line | `Listas/pratica-lecture-01.md` |

Graded in-class cases stay spoiler-free. Solutions for the new practice lists: not in scope.
L03–L08 have no slides yet: their deliverables follow the estimated notes and say so.

## Steps

1. One agent per lecture, in parallel: L01 (TTS only), L02 (notes reconcile + all four),
   L03–L08 (quiz, audio, TTS, exercises). Agents do not edit shared indexes.
2. Main loop, after the agents: update `NotebookLM/README.md`, `Map/study-guide.md`
   (project-material column and "After class" lines), `Map/exercises-index.md`,
   `Notas/00-index.md`; copy `Aula/Lecture02.pdf` into `NotebookLM/sources/`.
3. Compile notes PDFs sequentially (MiKTeX installs packages on demand; parallel runs race):
   `python -I ~/.claude/commands/templates/notes_pdf.py Notas/L01 … Notas/L08`; check
   `pdffonts` (no Type 3) and no `Missing character`.
4. Verify: every quiz passes the validator; every audio prompt < 5,000 chars; every list row
   has a statement block.

## Done (2026-10-25)

All steps complete; agent reports in `.agent/notes/lecture-batch-reports.md`. Verified: 21 new
quizzes PASS the validator (10 Q each); 16 audio prompts 4,581–4,992 chars, no language line;
8 narrations 19,952–29,289 words; 7 lists, all embedded figures exist; 8 notes PDFs (49–73 pp.,
no Type 3, no missing characters). PDF build fixes: double-backslash row breaks written with a single backslash in `Notas/L02/L02-03`, `L02-04`; a tab eaten from `\tfrac` in `Notas/L03/L03-11` (pre-existing).
