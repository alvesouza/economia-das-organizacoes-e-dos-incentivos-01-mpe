# Plan: solutions PDF for `Listas/pratica-lecture-01.md` (2026-10-13)

Mirror `Listas/pratica-aula-01-02-solutions/`: `main.tex` (same preamble, `exsol` environment,
`\input` of item01-item24 in the plan's tier order), one `itemNN.tex` per exercise, check
scripts, compiled `main.pdf` copied to `Listas/pratica-lecture-01-solutions.pdf`.

Numbering: the tier tables (items 1-24, also used by "Suggested study order"). The plan's
"Consolidated Exercises" table numbers the same 24 exercises in a different order; not used.

Per item: number + page + one-line "what is asked" (never the statement), method with book
section and lecture slide, derivation, interpretation, verification (which check script, and
agreement or disagreement with Munoz-Garcia's answer / MWG solutions manual / Kumar's
unofficial Gibbons manual). Lecture notation: G = (I, {S_i}, {u_i}), S_i^k, S_i^infty,
"iterated-elimination equilibrium"; IESDS rounds remove all strictly dominated strategies at once.

Checks:
- check_A.py: finite matrices (items 1-8, 10, 14, 16-19): brute-force IESDS (lecture's
  simultaneous definition), weak-deletion routes, payoff tables built from the stories.
- check_B.py: continuous/symbolic (items 9, 13, 15, 21): sympy best responses, interval recursions.
- check_C.py: proofs and auctions (items 11, 12, 20, 22, 23, 24): random-game order-independence,
  pure-dominance tests, second-price/proxy grids.

Statements read from rendered PDF pages (matrices checked on the image). Findings so far:
Munoz-Garcia Fig. 1.4 cell (L, aar) printed as (10,0), should be (0,0); MWG manual 8.B.1 ignores
the corner h_i >= 0 (alpha <= 0, beta < 0 also gives a dominant strategy h_i = 0); manual 8.B.3
does not prove uniqueness; Tadelis 4.4(b) fails strictly with a positive increment capped at
the bid; Tadelis 4.2(b) needs Tadelis's ">= only" definition (impossible under the lecture's).
