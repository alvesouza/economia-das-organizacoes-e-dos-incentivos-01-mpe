# Plan: solutions PDF for `Listas/pratica-aula-01-02.md` (2026-10-13)

Rule: `rules/00_estilo_avaliacao.md` §9 (user said yes). Output:
`Listas/pratica-aula-01-02-solutions/` with `main.tex` (preamble + `\input` of item01–item30 in
plan order), one `itemNN.tex` per exercise, one `check_<group>.py` per group, and the compiled
`Listas/pratica-aula-01-02-solutions.pdf`.

Per item: number + page + one-line "what is asked" (never the statement, CLAUDE.md scope rule),
method with book section, derivation/argument, interpretation, verification. Discursive (FFT, RQ,
Cabral rp) items get structured argued answers tied to the course sections; quantitative items get
full derivations and a sympy/numpy check.

Fan-out (4 parallel subagents, disjoint files):
- A — M&R Ch. 1 and Ch. 4: items 1, 2, 5, 11, 14, 15, 24 (FFT 1.1–1.3, FFT 4.1–4.3, Math 4.2).
- B — Cabral: items 3, 4, 9, 10, 12, 13, 19, 25, 30 (1.1, 3.9, 5.1, 7.6, 3.14, 3.11, 7.14, 3.20, 13.10).
- C — M&R Ch. 2 + Varian: items 6, 7, 8, 16, 17, 23, 26, 27 (32 RQ 3, 35 RQ 1–2, Q 2.1–2.4, FFT 2.5).
- D — M&R Ch. 5 + MWG: items 18, 20, 21, 22, 28, 29 (FFT 5.1–5.2, Q 5.4–5.5, 9.B.13, 9.B.12).

Then: assemble, compile twice, `pdffonts`, render-check, run all check scripts, report.
