# Plan: statements inside the solutions PDFs, hard conceptual quizzes per topic, push

User request (2026-11-13): "include in the solution, the texts of each question too, right before
their respective solutions. Then write conceptual quizzes (hard) of 10 questions for each topic.
After all that push to origin."

## 1. Statements in the 8 practice-list solutions PDFs

- `Listas/make_statements.py`: for each `Listas/pratica-lecture-0N.md`, split the `#### n. Label`
  blocks, drop the HTML id comment and the "Moved here from" line, rewrite `figures/` to
  `../figures/` and Obsidian links to plain text, convert with pandoc (markdown + tex math →
  LaTeX fragment) to `Listas/pratica-lecture-0N-solutions/stmt/item-NN.tex`.
- `Listas/statement-hook.tex` (input just before `\begin{document}` of each `main.tex`): pandoc
  support macros, `\statementboxn{n}` (prints the statement block between two rules, warns if the
  file is missing), and a redefined 4-argument `exsol` (L2–L8) whose heading is followed by the
  statement instead of the sentence "it is not repeated here". L1's 5-argument `exsol` gets the
  same treatment in its own `main.tex`.
- The statement text is the list's block verbatim (source line, statement, referred-to material,
  notes); the list stays the single source, the script regenerates the fragments.
- Recompile all 8 (twice), copy to `Listas/pratica-lecture-0N-solutions.pdf`, `pdffonts` check,
  verify every item has a statement (no "no statement" warnings), spot-check rendered pages.
- Not in scope: the `lista-reais-*` solutions (statements live in `lista-reais-lectures-01-05/
  block*.tex`); offered as follow-up.

## 2. Hard conceptual quizzes, one per topic T1–T19 (10 questions each, 190 in all)

- Format: the project quiz MD consumed by `quiz.html`, per `.claude/commands/quiz-gen.md`; files
  `Simulados/quiz-topic-TNN-<slug>-hard-2026-11-13.md`; validated by `.claude/quiz-validate.py`.
- Conceptual, hard: misconceptions, edge cases, "which statement is true", counterexamples; no
  plug-in computation. Grounded in Tadelis sections and the real slides (L1–L5) or the estimated
  units (T11, T13–T19), cited per question. Distinct from the existing per-lecture quizzes
  (no reuse of their stems).
- Work split: 4 parallel agents (T1–T5, T6–T10, T11–T15, T16–T19). Each runs the validator.

## 3. Commit and push

- Stage the new and changed work of this session (cases, homework, NotebookLM prompts, lists,
  solutions, quizzes, maps, notes, plans). Check `.gitignore` and sizes first; follow precedent for
  third-party PDFs (`Cases/Brexit/` PDFs, `Aula/*.pdf`).
- Commit on `master` (the repo's practice), push to `origin`, report the commit hash.
