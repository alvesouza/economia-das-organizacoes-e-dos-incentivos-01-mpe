# NotebookLM prompts — Economia das Organizações e dos Incentivos

**Open any prompt file → Ctrl+A → Ctrl+C → paste into NotebookLM (slides → slide creation field; audio → Audio Overview Customize field or as Source).**

Before generating: check **Settings → Output language** in NotebookLM (English, for every type, audio included). The prompts carry no language line; the setting decides the language of everything the notebook produces.

| File | Type | Lecture/Book | Words | Chars | Paste into |
|---|---|---|---|---|---|
| `audio/lecture-01-audio-part1.md` | Audio (Custom Prompt, hard) | Lecture 1, part 1/2: what a game is, normal form, complete information and common knowledge, the grade game, solution-concept criteria, strict/weak dominance, dominant-strategy equilibrium, prisoner's dilemma and Pareto, partnership game, second-price auction | 765 | 4,832 | Audio Overview → Customize |
| `audio/lecture-01-audio-part2.md` | Audio (Custom Prompt, hard) | Lecture 1, part 2/2: IESDS and common knowledge of rationality, its properties (uniqueness of the dominant-strategy survivor, order independence, existence), Cournot by IESDS (2 vs. 3 firms), spatial competition (method only; the graded mini case is not solved) | 759 | 4,992 | Audio Overview → Customize |

The Aula 1–2 audio prompts listed here before (`audio/aula-01-*`, `audio/aula-02-*`, built on the superseded M&R plan) are no longer in `audio/`.

Slide and Audio Customize fields truncate silently at ~6,000 chars. All prompts are kept under 5,000 chars for safety.

All course materials should be uploaded as separate sources in the same NotebookLM notebook; these prompts guide how NotebookLM processes them. Upload everything in `NotebookLM/sources/`. For Lecture 1 the essential sources are `Aula_Lecture01 - Static Games of Complete Information I.pdf` (copy of `Aula/Lecture01.pdf`) and the Tadelis, Gibbons, Muñoz-Garcia, MWG and Cabral `Livro_*.pdf` files (added 2026-10-14).
