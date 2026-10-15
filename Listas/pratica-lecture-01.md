---
tags: [lista, pratica, lecture-01, topic/static-games]
date: 2026-10-13
---

# Practice plan — Lecture 1 (Static games of complete information I: dominance and IESDS)

24 existing book exercises, cited by number and page only, in one sequence of rising
complexity. Sources: Tadelis (2013), the book the slides follow; Muñoz-Garcia & Toro-Gonzalez
(2019), worked answers after every exercise; Gibbons (1992); MWG (1995). Lecture slides:
`Aula/Lecture01.pdf`. Class plan: [[Map/study-guide|study guide]]; book map:
[[Map/books-index|books-index]]. Worked solutions: `Listas/pratica-lecture-01-solutions.pdf`.
Exam-style list for the same lecture: `Listas/lista-lecture-01.tex`.

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise. MWG 8.B.1–8.B.7:
in the MWG solutions manual (`Livros/`). Gibbons 1.2: in an unofficial, unfinished manual
(`D:/Livros/Mercado/Economia/`, not copied). Tadelis: none in the book; the preface (p. xiii)
says about half are solved on Princeton UP's website (not checked).

**Verification.** Pages come from the book map built on 2026-10-13 (`Map/books-index.md`,
offsets in `Livros/book-registry.json`). Spot-checked in the PDFs on the same day: Tadelis
exercises 3.1–3.7 on p. 58 and 4.1–4.10 on pp. 76–78; Muñoz-Garcia Ex. 12 on p. 23.

**Not here on purpose.** The in-class mini case (pharmacies on a 7-block avenue, slides 31–33)
is graded in-class work; item 18 is the book's closest analogue. Tadelis 4.8–4.9 (beauty
contest, rationalizability), 5.2–5.3 and 6.2–6.3 (dominance by mixed strategies) belong to
Lecture 2.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Representing a game: normal form, strategies, trees to matrices | 6 | 25% | every later step starts from a correct matrix; the slides spend a third of the lecture here |
| B2 | Dominance, dominant-strategy equilibrium, Pareto optimality | 5 | 21% | the lecture's first solution concept and its two lessons |
| B3 | IESDS and common knowledge of rationality | 9 | 37% | the lecture's main tool, and the one the in-class case applies; densest in the books (all four have exercises) |
| B4 | Applications: auctions and spatial competition | 4 | 17% | the second-price auction and location examples from the slides |

| Level | Items | Count |
|---|---|---|
| Foundations (build a matrix, apply a definition, run IESDS on a small game) | 1–8 | 8 |
| Exam (proofs of the basic propositions, continuous strategies, multi-step modelling) | 9–18 | 10 |
| Advanced (MWG, order of elimination, Cournot with $n$ firms, auctions) | 19–24 | 6 |

---

## Tier 1 — Foundations

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 1 | B1 | Tadelis | Ch. 3, Exercises | 3.2 | 58 | Turning a verbal two-player story into a payoff matrix (a zero-sum case) |
| 2 | B1 | Tadelis | Ch. 3, Exercises | 3.4 | 58 | The same for a stag-hunt story; which payoff orderings make it one |
| 3 | B1 | Muñoz-Garcia | Ch. 1 | Ex. 2 | 4 | Reading strategy sets off a game tree and writing the matrix |
| 4 | B1 | Muñoz-Garcia | Ch. 1 | Ex. 5 | 8 | The prisoner's dilemma as a tree and as a matrix |
| 5 | B2 | Muñoz-Garcia | Ch. 1 | Ex. 13 | 26 | Finding dominant and dominated strategies, then eliminating |
| 6 | B3 | Tadelis | Ch. 4, Exercises | 4.5 | 77 | IESDS round by round on a 3×3 matrix |
| 7 | B3 | Gibbons | §1.1, Problems | 1.2 | 48 | IESDS on a 3×3 matrix (the pure Nash part previews Lecture 2) |
| 8 | B3 | Muñoz-Garcia | Ch. 1 | Ex. 9 | 17 | Games where IESDS removes nothing, and what that says about its bite |

## Tier 2 — Exam level

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 9 | B1 | Tadelis | Ch. 3, Exercises | 3.6 | 58 | Normal form with continuous strategies and piecewise payoffs |
| 10 | B1 | Tadelis | Ch. 3, Exercises | 3.7 | 58 | Normal form of a three-player threshold game |
| 11 | B2 | Tadelis | Ch. 4, Exercises | 4.1 | 76 | Proving that a strict dominant-strategy equilibrium is unique |
| 12 | B2 | Tadelis | Ch. 4, Exercises | 4.2 | 76 | Counterexamples on existence and uniqueness of weak dominant-strategy equilibrium |
| 13 | B2 | MWG | §8.B, Exercises | 8.B.1 | 262 | When each of $n$ firms has a strictly dominant level of a costly action |
| 14 | B3 | Muñoz-Garcia | Ch. 1 | Ex. 12 | 23 | What rationality alone removes vs. what common knowledge of rationality removes |
| 15 | B3 | Tadelis | Ch. 4, Exercises | 4.6 | 77 | IESDS with continuous strategies, by bounding best replies |
| 16 | B3 | Tadelis | Ch. 4, Exercises | 4.7 | 77–78 | Building a three-strategy game from win probabilities, then eliminating |
| 17 | B4 | Tadelis | Ch. 4, Exercises | 4.3 | 76 | A discrete first-price auction as a matrix; dominated bids and IESDS |
| 18 | B4 | Tadelis | Ch. 4, Exercises | 4.10 | 78 | A discrete location game: dominated locations and the surviving set (closest analogue of the pharmacy case) |

## Tier 3 — Advanced

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 19 | B3 | Muñoz-Garcia | Ch. 1 | Ex. 16 | 31 | Strict vs. weak iterated deletion, and how the order of deletion matters for weak |
| 20 | B3 | MWG | §8.B, Exercises | 8.B.4 | 262 | Proving that the order of deletion does not matter under strict dominance |
| 21 | B3 | MWG | §8.B, Exercises | 8.B.5 | 262 | Linear Cournot: IESDS pins down the outcome with two firms but not with three |
| 22 | B2 | MWG | §8.B, Exercises | 8.B.7 | 262 | Why a strictly dominant strategy must be pure (first contact with mixed strategies) |
| 23 | B4 | MWG | §8.B, Exercises | 8.B.3 | 262 | Truthful bidding in a second-price auction: weakly dominant, and the only such bid |
| 24 | B4 | Tadelis | Ch. 4, Exercises | 4.4 | 76–77 | Weak dominance of bidding one's value under proxy bidding |

**Optional extras.**
- Muñoz-Garcia Ch. 1 Ex. 6–8 (pp. 11–14) and Ex. 11 (p. 20, three players): more IESDS drill, all with answers.
- Muñoz-Garcia Ch. 1 Ex. 17 (p. 33): a second weak-deletion order example, after item 19.
- Tadelis 3.1, 3.3, 3.5 (p. 58): the other verbal-to-matrix stories, if items 1–2 felt slow.

---

## Suggested study order

1. **Representation.** Read Tadelis Ch. 3 (pp. 43–58), then do items **1–4**, then **9, 10**.
2. **Dominance.** Read Tadelis §4.1 (pp. 59–63), then do **5, 11, 12, 13**.
3. **IESDS.** Read Tadelis §4.2 (pp. 63–69) and Gibbons §1.1.A–B (pp. 2–7), then do **6, 7, 8, 14**, then **15, 16**.
4. **Applications.** Do **17, 18**, then compare 18 with your in-class answer to the pharmacy case.
5. **Advanced.** Read MWG §8.A–8.B (pp. 235–241). Do **19** before **20**, then **21**, and **22–24** last.

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Common knowledge; normal-form games; the prisoner's dilemma | Ch. 3, §3.1–3.2 | p. 43–52 | Foundations |
| Solution concepts; existence, uniqueness, invariance; Pareto optimality | Ch. 3, §3.3 | p. 52–58 | Foundations |
| Exercises 3.2, 3.4, 3.6, 3.7 | Ch. 3, Exercises | p. 58 | Exam |
| Dominance; dominant-strategy equilibrium; evaluation | Ch. 4, §4.1 | p. 59–63 | Foundations |
| IESDS; common knowledge of rationality; Cournot by IESDS; evaluation | Ch. 4, §4.2 | p. 63–69 | Exam |
| Exercises 4.1–4.7, 4.10 | Ch. 4, Exercises | p. 76–78 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Normal-form representation; IESDS | §1.1.A–B | p. 2–7 | Foundations |
| Problem 1.2 | §1.1, Problems | p. 48 | Foundations |

### MWG — Mas-Colell, Whinston & Green (1995)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Normal form | §7.D | p. 228–231 | Advanced |
| Simultaneous-move games; dominant and dominated strategies | §8.A–8.B | p. 235–241 | Advanced |
| Exercises 8.B.1, 8.B.3, 8.B.4, 8.B.5, 8.B.7 | Ch. 8, Exercises | p. 262 | Advanced |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Dominance solvable games: exercises with worked answers | Ch. 1 | p. 1–36 | Foundations |

## Consolidated Exercises

| # | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 1 | 3.2 | Tadelis | p. 58 | Story to matrix (zero-sum) | Foundations |
| 2 | 3.4 | Tadelis | p. 58 | Story to matrix (stag hunt) | Foundations |
| 3 | 3.6 | Tadelis | p. 58 | Continuous strategies | Exam |
| 4 | 3.7 | Tadelis | p. 58 | Three-player normal form | Exam |
| 5 | 4.1 | Tadelis | p. 76 | Uniqueness of strict dominant-strategy equilibrium | Exam |
| 6 | 4.2 | Tadelis | p. 76 | Weak dominant-strategy equilibrium | Exam |
| 7 | 4.3 | Tadelis | p. 76 | First-price auction by IESDS | Exam |
| 8 | 4.4 | Tadelis | p. 76–77 | Proxy bidding | Advanced |
| 9 | 4.5 | Tadelis | p. 77 | IESDS on a 3×3 matrix | Foundations |
| 10 | 4.6 | Tadelis | p. 77 | IESDS with continuous strategies | Exam |
| 11 | 4.7 | Tadelis | p. 77–78 | Modelling then eliminating | Exam |
| 12 | 4.10 | Tadelis | p. 78 | Discrete location game | Exam |
| 13 | 1.2 | Gibbons | p. 48 | IESDS on a 3×3 matrix | Foundations |
| 14 | 8.B.1 | MWG | p. 262 | Dominant strategies with $n$ firms | Exam |
| 15 | 8.B.3 | MWG | p. 262 | Second-price auction | Advanced |
| 16 | 8.B.4 | MWG | p. 262 | Order independence of IESDS | Advanced |
| 17 | 8.B.5 | MWG | p. 262 | Cournot with two and three firms | Advanced |
| 18 | 8.B.7 | MWG | p. 262 | Strictly dominant strategies are pure | Advanced |
| 19 | Ex. 2 | Muñoz-Garcia | p. 4 | Tree to matrix | Foundations |
| 20 | Ex. 5 | Muñoz-Garcia | p. 8 | Prisoner's dilemma | Foundations |
| 21 | Ex. 9 | Muñoz-Garcia | p. 17 | IESDS without bite | Foundations |
| 22 | Ex. 12 | Muñoz-Garcia | p. 23 | Rationality vs. common knowledge | Exam |
| 23 | Ex. 13 | Muñoz-Garcia | p. 26 | Dominance, then IESDS | Foundations |
| 24 | Ex. 16 | Muñoz-Garcia | p. 31 | Strict vs. weak deletion | Advanced |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Representing a game | Tadelis Ch. 3 p. 43–58 | Tadelis 3.2, 3.4, 3.6, 3.7; Muñoz-Garcia Ex. 2, 5 | 1.5–2 h |
| 2 | Dominance and Pareto | Tadelis §4.1 p. 59–63 | Tadelis 4.1, 4.2; MWG 8.B.1; Muñoz-Garcia Ex. 13 | 1.5 h |
| 3 | IESDS and common knowledge | Tadelis §4.2 p. 63–69; Gibbons §1.1.B p. 4–7 | Tadelis 4.5, 4.6, 4.7; Gibbons 1.2; Muñoz-Garcia Ex. 9, 12 | 2–2.5 h |
| 4 | Auctions and location | Tadelis §4.2 (Cournot example p. 65) | Tadelis 4.3, 4.10 | 1 h |
| 5 | Advanced | MWG §8.A–8.B p. 235–241 | Muñoz-Garcia Ex. 16; MWG 8.B.3, 8.B.4, 8.B.5, 8.B.7; Tadelis 4.4 | 2.5–3 h |
