# Economia das Organizações e dos Incentivos — MPE Insper

Study project for **ECONOMIA DAS ORGANIZAÇÕES E DOS INCENTIVOS: TEORIA E APLICAÇÕES**
(Mestrado Profissional em Economia, 4th term 2026, instructor Isabela Brandão Furtado). The syllabus
record names Milgrom & Roberts (1992); the course as taught is **game theory**, with slides that
follow Tadelis (2013), *Game Theory: An Introduction*. M&R supplies the organizational applications.

> **Books:** the five syllabus books plus Tadelis, Gibbons and Muñoz-Garcia & Toro-Gonzalez are in `Livros/`, all mapped section by section.
> Varian is the *with Calculus* edition (2014), not the 8th edition the syllabus cites. See [`Livros/BOOKS.md`](Livros/BOOKS.md) and [`Map/books-index.md`](Map/books-index.md).

## Lectures

| L | Date | Lecture | Tadelis | Material |
|---|---|---|---|---|
| 1 | Oct 13 | Static games: dominance, iterated elimination | Ch. 3; §4.1–4.2 | [practice plan](Listas/pratica-lecture-01.md) · `Listas/lista-lecture-01.tex` · 3 quizzes in `Simulados/` |
| 2 | Oct 20 | Static games: Nash equilibrium, mixed strategies | §4.3; Ch. 5–6 | |
| 3 | Oct 27 | Dynamic games: backward induction, subgame perfection | Ch. 7–8 | |
| 4 | Nov 3 | Multistage games and bargaining | Ch. 9, 11 | [rules/02](rules/02_barganha.md) · Aula 2 notes §5 |
| 5 | Nov 6 (Fri) | Repeated games I: cooperation | §10.1–10.3 | |
| 6 | Nov 10 | Repeated games II: collusion, relational contracts | §10.4–10.5 | |
| 7 | Nov 17 | Bayesian games, adverse selection and auctions | Ch. 12–13 | [rules/07](rules/07_selecao_adversa.md) |
| 8 | Nov 24 | Signaling and perfect Bayesian equilibrium | Ch. 15–16 | [rules/07](rules/07_selecao_adversa.md) |
| 9 | Dec 1 | Short-paper presentations | | |
| 10 | Dec 8 | Final exam | | |

Assessment: in-class exercises 10% · short paper (groups) 35% · final exam 55%. Class plan with
pages: [Map/study-guide.md](Map/study-guide.md). Full programme: [rules/11_curso_programa.md](rules/11_curso_programa.md).
The earlier 16-session M&R draft and its Aula 1–2 material (`Aula/aula-0*-notes.md`, the `quiz-aula0*`
quizzes, `Listas/*aulas-01-02*`) are kept as application background.

## Project structure

| Directory | What goes there |
|---|---|
| `Aula/` | Lecture slides and class scripts |
| `Listas/` | Exercise lists; `lista-exam.tex` is the template `/exam-gen` fills |
| `Monitoria/` | Tutorial / office-hour material |
| `Prova/` | Exams and solutions |
| `Simulados/` | Quiz MD files played by `quiz.html` |
| `Livros/` | Textbooks (gitignored), `BOOKS.md` (found/missing list), `book-registry.json` (page offsets) |
| `Resolucao/` | Generated exercise solutions |
| `Leituras/` | Chapter extracts and TTS narrations |
| `Map/` | Obsidian cross-reference maps |
| `NotebookLM/` | Prompts (`slides/`, `audio/`, `video/`) and `sources/` ready for bulk upload |
| `Notas/` | Study notes per lecture (`/notes`): `LNN/` map, section notes, figures, companions; index `Notas/00-index.md` |
| `Notebooks/` | Jupyter projects; created by the first `/lab-init` |
| `Videos/` | `/explainer` videos; created on first use |
| `rules/` | Topic rules (`00`–`11`) + Efficient Token governance packs |
| `.agent/` | `plans/` and `notes/` for the agent; `conventions.md` |
| `.claude/` | Local copies of all slash commands, settings, hooks, quiz validator |
| `tools/` | Efficient Token tooling (`sync_rules.py`, `token_report.py`, …) |

## Slash commands

| Command | What it does |
|---|---|
| `/convert Aula/` | Convert lecture PDFs to Markdown |
| `/summarize Aula/` | Summarize all lectures |
| `/list-exercises Listas/` | Extract all exercises |
| `/solution Listas/lista-1.md` | Solve the exercises in a list |
| `/exam-gen bargaining, adverse selection` | Exam-style list + answer key & rubric (LaTeX); asks depth, tangential topics and math level first |
| `/exam-grade Listas/lista-1.tex my-resolution.pdf` | Grade your own resolution against the rubric, with book references |
| `/exercise-plan moral hazard` | Practice plan pointing to real book exercises (number + page), weighted by subtopic and level |
| `/quiz-gen Simulados/` | Generate a quiz from MD question files |
| `/quiz-analyze <paste results>` | Analyze quiz performance and drive remediation |
| `/study-map .` | Rebuild the Obsidian cross-reference maps |
| `/notebooklm Aula/` | NotebookLM prompts (slides, audio, video); asks the unit and count per type first |
| `/speechify rules/07_selecao_adversa.md` | Narrated plain-text script for a TTS app; `--split`, `--short` |
| `/intake <file-or-dir>` | Front door for new material: converts, analyses, then asks in one round what to derive from it |
| `/lab moral hazard incentive intensity` | Jupyter project that simulates a mechanism; runs end to end and verifies its numbers |
| `/lab-init <slug>` | Scaffold `Notebooks/<slug>/` |
| `/lab-data <series>` | Fetch and cache data series with a provenance registry; `--offline` never touches the network |
| `/explainer signaling` | 3blue1brown-style narrated video (Manim + Speechify), compiled to a 1080p `.mp4` with subtitles |
| `/manim-kit <project>` | Drive the shared Manim drawing layer from `../Video explainer` |
| `/notes 2` | Study notes for a lecture under `Notas/LNN/`: map, one note per section, formulas, pitfalls, Python, figures; asks once whether to build companions. `--reconcile` updates an estimated unit once its slides arrive |
| `/companion <model>` | Interactive page for one model; only when asked, and asks in detail first |
| `/study-pack`, `/book-solutions`, `/tex-convert` | Study PDF from a remediation file; N&S-style solutions; book → LaTeX |

## Running quizzes

1. `cd` into the project directory
2. `python -m http.server`
3. Open `http://localhost:8000/quiz.html`
4. Select the quiz MD file to load

## Obsidian

Open the project root as a vault. `Map/` holds the cross-reference notes with wiki-links between
topics, books, lists and quizzes.

## NotebookLM workflow

1. Confirm NotebookLM → Settings → Output language is **English** (it applies to every type,
   audio included; prompts never carry a language line).
2. Upload everything in `NotebookLM/sources/`.
3. Run `/notebooklm Aula/` to generate prompts.
4. Open each prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM.

## Video tooling

Installed from `../Video explainer` (editable link, no copied code). `/explainer` still needs:
a **Speechify API key** in `.env` as `SPEECHIFY_API_KEY` (copy `.env.example`). Manim CE, ffmpeg
and LaTeX were detected at setup. Verify with `speechify-tts --check`.

## Agent governance

Efficient Token packs `core`, `context`, `codebase-work`, `model-routing`, `microeconomics`,
`game-theory`, `lang-python`. `CLAUDE.md` is held to a 900-token budget:
`python tools/token_report.py --budget`. After editing a pack: `python tools/sync_rules.py`
(CI runs `--check`).
