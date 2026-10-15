# Plan: exam-style list for Lecture 1 (step 4 of lecture-01-replan.md)

Procedure: `.claude/commands/exam-gen.md`, graduate level (style §8), symbolic, complete format.
Parameters fixed by the caller (no AskUserQuestion). Model: `Listas/lista-aulas-01-02.tex`.

## Blocks (3 x 25 pts; objective a-d + discursive a-e, 3 pts each)

1. Normal form, dominance, social dilemmas.
   - Q1 a) n-partner E/S partnership with synergy theta: set of c giving a social dilemma.
     b) second-price auction with reserve r: truthful weakly dominant, no bid strictly
     dominated, IESDS removes nothing. c) T: strict DSE is invariant to small payoff
     perturbations in finite games. d) F: n-player, Pareto improvements on a strict DSE need
     every player off the dominant strategy (true for n = 2 only).
   - Q2 partnership with continuous effort, shares alpha_i: dominant strategy (graph), Pareto
     set, no balanced sharing rule is efficient, equal split is second best, loss (n-1)^2/n^2,
     parameter analysis.
2. IESDS.
   - Q3 a) parametric 3x3, unique survivor iff 1<x<4 in 4 rounds. b) weak-dominance order
     dependence (matrix found by search). c) F: S_i^infty can be empty (infinite S_i).
     d) T: order independence of strict IESDS in finite games.
   - Q4 Cournot duopoly with asymmetric costs by IESDS: interval recursion, widths halve,
     survivor incl. corner, n >= 3 stops after round 1, parameter analysis. Graph: nested
     rectangles.
3. Integrative spatial competition (own setting: gas stations on a highway with n towns).
   - Q5 a) rounds and survivors for general n. b) continuum: IESDS removes only {0,1}.
     c) T: constant-sum => every profile Pareto optimal for the chains. d) F: distance ratio
     <= 2 fails for n = 6 (9/4).
   - Q6 payoffs for general n, IESDS by induction (parity), continuum contrast (invariance),
     travel-distance optimum vs IESDS (ratio exactly 2 for odd n), zoning-by-halves variant,
     parameter analysis in n. Graph: travel distance per resident.

## Verification
`Listas/lista-lecture-01-check.py`: brute-force IESDS on every matrix, all weak-elimination
orders, Cournot interval recursion vs closed form, spatial survivors and distances for n up to
40, continuum witnesses at random draws, sympy closed forms, distractors != keys.
Compile both PDFs with pdflatex (2x), pdffonts, clean aux; answer key 10-15 pages.
