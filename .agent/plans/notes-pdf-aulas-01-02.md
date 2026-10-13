# Plan: in-depth PDF notes for Aulas 1–2 (2026-10-13)

Request: "write a pdf for class 01 and class 02, in depth". Defaults taken from this session's
answers: Bargaining = whole topic (draft Aulas 2–3), graduate depth, English, Python checks.

## Output
`Aula/notes-aulas-01-02/`: `main.tex` (preamble, title, TOC), `part1.tex` (Aula 1),
`part2.tex` (Bargaining), `check_part2.py` (sympy/numpy check of every Part II number),
`main.pdf`. pdflatex with lmodern + cmap; verify `pdffonts` (all Type 1, uni = yes).

## Part I — Aula 1 (source: `Aula/aula-01-notes.md`, already verified)
Convert to LaTeX at the same depth: question; Ford, GM, Toyota (tables); HBC/Salomon/Eastern
Europe; four patterns and coordination × motivation; complementarities (definition,
increasing differences, Topkis by implicit function, two-choice model with multiplier, substitutes
flip, strong complementarity); Figure 4.3 made exact (EOQ form, table, saddle remark); the cube
and the valley; NUMMI and evidence; common mistakes; exercises (number + page). Figures: 2×2
table, best replies of Fig. 4.3 (pgfplots), the valley path.

## Part II — Bargaining (sources read this session: M&R pp. 35–39, 133–149; Varian pp. 581–583,
670, 687; MWG 9.AA pp. 296–299; Cabral pp. 96–99)
1. Problem: determinacy vs indeterminacy (M&R p. 140).
2. Wealth effects: three conditions, value index, compensating transfer; original WTP/WTA
   counterexample (log utility) showing allocation depends on rights when wealth effects exist.
3. Value maximization principle: statement, proof (both directions), Fig. 2.1 (TikZ),
   footnote-10 limit.
4. Coase theorem: statement, transaction-cost corollary, Cabral steel plant, Varian §35.2,
   limits (p. 39), rival views (Marxian, Harvard school).
5. Division: Nash bargaining solution under TU (derived), generalized weights.
6. Alternating offers: finite horizon closed form (T odd/even), Varian three-day game,
   Rubinstein uniqueness (Shaked–Sutton bounds), shares with δ1 ≠ δ2, limits; figure of
   convergence.
7. Commitment and the ultimatum game: M&R p. 133/139, reputation; Varian p. 583 evidence.
8. Private information: M&R Table 5.2/5.3 example with both IC constraints, reversed
   probabilities, revelation principle, informational rent.
9. Incentive efficiency: split-the-difference with uniform values; derive the linear
   equilibrium (s = 1/4 + 2S/3, b = 1/12 + 2B/3), trade iff B > S + 1/4; probability 9/32,
   surplus share 27/32; figure of the trade region.
10. Many participants: public project, N = 2 (p ≤ 2/3, q ≤ 1.5p/(3p − 1)), N = 3 (≈ .44;
    q ≤ 8/9 at p = 1/2), large N (M&R's ≈ 2/7, cited).
11. Bargaining costs, measurement costs, De Beers, bargaining chips; one-line hold-up model
    as preview of Topic 6.
12. Common mistakes; exercises by number and page (from `Listas/pratica-aula-01-02.md`).
Worked examples are original; no exercise statement is reproduced.

## Checks
`check_part2.py` asserts every closed form and number in Part II. Compile twice, `pdffonts`.
