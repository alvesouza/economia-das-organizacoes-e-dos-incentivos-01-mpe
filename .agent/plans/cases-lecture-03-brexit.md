# Plan: Lecture 3 mini case (two versions) + Brexit case document

User request (2026-11-03): "solve the case in lecture 3 one version in detail and another with a
short version, and work on this case too, elaborate a document in detail Cases\Brexit".

## 1. Mini case "Work or shirk?" (`Aula/Lecture03.pdf`, slides 77–78 = deck slides 41–42)

Inspection game. Rows employee W/S, columns manager M/N:
(W,M) = (w−g, v−w−h), (W,N) = (w−g, v−w), (S,M) = (0, −h), (S,N) = (w, −w);
w = 10, g = 2, v = 20, h = 1. Questions (a)–(e) on slide 78. Graded in-class item, hand-in date
past (Oct 27); solved on request, as `Resolucao/mini-case-lecture-01` was.

Results (to be verified by script): no pure NE (cycle) when 0 < g < w and 0 < h < w;
p* = Pr(S) = h/w = 0.1, q* = Pr(M) = g/w = 0.2; payoffs employee w−g = 8, manager
(1−p*)(v−w) − h = v − w − hv/w = 8. (c) h = 0.5: p* = 0.05, q* = 0.2 (unchanged), manager 9.
(d) w = 20: p* = 0.05, q* = 0.1, manager −1, employee 18. (e) π(w) = v − w − hv/w, dπ/dh = −v/w;
the wage that maximizes π (ignoring participation) is √(hv) ≈ 4.47 > g. Commitment variant
(manager commits to q ≥ g/w before the employee moves, Lecture 3 link): p = 0, π = v − w − hg/w
= 9.8 > 8.

Outputs: `Resolucao/mini-case-lecture-03.tex/.pdf` (detailed), `Resolucao/mini-case-lecture-03-short.tex/.pdf`
(one to two pages, hand-in style), `Resolucao/mini-case-lecture-03-check.py`. Model on
`Resolucao/mini-case-lecture-01.tex` and its check script. pdflatex, lmodern + cmap.

## 2. Brexit (`Cases/Brexit/`, instructions `intrucoes.md`, tasks (i)–(vii))

The Darden PDFs forbid uploading to AI systems: the writing agent gets only the figures below,
never the PDFs, and the document does not reproduce case text.

Figures (£bn costs): hard Brexit UK 35, EU 18; preparation costs 5, all-or-nothing, mitigates
12.5 (2.5 per £); soft deals (UK, EU): favorable (19, 13), neutral (23, 9), unfavorable (27, 5);
preparation sunk in a soft Brexit; Parliament passes a presented deal with prob. 0.8;
rejecting outright gives hard Brexit plus an unquantified political cost r ≥ 0. EU wants
low costs and to deter other exits.

Game: UK Prepare/Not → EU offers F/Nt/U (baseline: observes preparation) → UK Present/Reject →
Nature pass 0.8 / fail 0.2. Results with r = 0: after N the UK presents all, EU offers U:
(−28.6, −7.6); after P the UK presents only F (present iff c ≤ 22.5 + r/p), EU offers F:
(−24.7, −14.0); UK prepares. Thresholds: r < 0.4 → (P, F); 0.4 < r < 3.6 → (P, Nt), UK −27.9;
r > 3.6 → (N, U), UK −28.6. Unobservable preparation: no pure NE; UK prepares w.p. 8/13, EU
offers F w.p. 11/36 and U otherwise; UK ≈ −26.64, EU −14. Joint cost: (P,F) 38.7 vs (N,U) 36.2.
EU deterrence premium k per favorable deal: F offered after P iff k ≤ 5.

Output: `Cases/Brexit/brexit-game.tex/.pdf` with check script `Cases/Brexit/brexit-check.py`:
(i)–(vii) in order, TikZ tree, backward induction step by step, SPE as full strategy profile,
sensitivity (r, p, k), unobservable variant, in-class decision guide (UK and EU roles),
(vii) comparison guide. English.
