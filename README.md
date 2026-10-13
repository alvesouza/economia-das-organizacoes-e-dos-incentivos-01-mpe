# Economia das Organizações e dos Incentivos — MPE Insper

Study project for **ECONOMIA DAS ORGANIZAÇÕES E DOS INCENTIVOS: TEORIA E APLICAÇÕES**
(Mestrado Profissional em Economia, 30 h). Main book: Milgrom & Roberts (1992),
*Economics, Organization, and Management*.

> **Books:** all five are in `Livros/`, Milgrom & Roberts included (mapped section by section).
> Varian is the *with Calculus* edition (2014), not the 8th edition the syllabus cites. See [`Livros/BOOKS.md`](Livros/BOOKS.md) and [`Map/books-index.md`](Map/books-index.md).

## Topics

| # | Topic | Aulas | M&R | Rules |
|---|---|---|---|---|
| 01 | Does organization matter? (Ford × GM × Toyota) | 1 | Ch. 1; Ch. 4 pp. 106–113 | [rules/01](rules/01_organizacoes_importam.md) |
| 02 | Bargaining | 2–3 | Ch. 2 pp. 35–39; Ch. 5 pp. 140–149 | [rules/02](rules/02_barganha.md) |
| 03 | Efficiency and economic organization (+ NEPKE kidney exchange) | 4–5 | Ch. 2 | [rules/03](rules/03_eficiencia_organizacao.md) |
| 04 | Coordination through the market | 6 | Ch. 3 | [rules/04](rules/04_coordenacao_mercado.md) |
| 05 | Coordination through management (+ Eddie Lampert at Sears) | 7–8 | Ch. 4; Ch. 3 pp. 78–85 | [rules/05](rules/05_coordenacao_management.md) |
| 06 | Bounded rationality, information and contracts | 9 | Ch. 5 | [rules/06](rules/06_racionalidade_limitada_contratos.md) |
| 07 | Adverse selection and its control (+ labour-market signaling) | 10–12 | Ch. 5 | [rules/07](rules/07_selecao_adversa.md) |
| 08 | Moral hazard (+ 1980s US S&L crisis) | 13–14 | Ch. 6 | [rules/08](rules/08_risco_moral.md) |
| 09 | Managing moral hazard in an organization | 15–16 | Ch. 7 | [rules/09](rules/09_gestao_risco_moral.md) |

Draft class plan, 16 sessions in syllabus order, anchored in M&R pages: [Map/study-guide.md](Map/study-guide.md). Full programme: [rules/11_curso_programa.md](rules/11_curso_programa.md).

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
