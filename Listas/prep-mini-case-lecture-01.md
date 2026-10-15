---
tags: [lista, pratica, lecture-01, mini-case, topic/static-games]
date: 2026-10-14
---

# Preparation list — Lecture 1 mini case (where to open the pharmacy?)

Builds every skill the mini case (slides 31–33, `Aula/Lecture01.pdf`) asks for, on **different
settings**, so the case itself stays unsolved. Nothing here is answered. Work each block before
the matching case question.

| Case question | Skill | Block below |
|---|---|---|
| (a) normal form; $u_A(s_A, s_B)$ for $s_A < s_B$, $s_A = s_B$, $s_A > s_B$ | piecewise payoffs on a line | A |
| (b) one location strictly dominated by another; is any location strictly dominant? | checking dominance against **every** rival choice | B |
| (c) IESDS round by round; surviving profile | bookkeeping $S_i^k$; knowledge behind each round | C |
| (d) locations minimizing total walking; compare with (c) | welfare on a line; the median | D |
| (e) assumptions; prices; real examples | modelling judgement | E |

**Spoiler warning.** These project files contain the general answer to the case; open them only
after you hand it in: `Simulados/quiz-lecture01-3-iesds-2026-10-13.md` (section "space"),
`Listas/lista-lecture-01.tex` Block 3 (Q5–Q6), and item 18 of
`Listas/pratica-lecture-01-solutions.pdf`.

---

## Reading first (45 min)

- Slides 13–14 (normal form, $s_{-i}$), 23 (strict and weak dominance), 28–29 (IESDS, $S_i^k$, $S_i^\infty$)
- Tadelis (2013) §3.2 (pp. 47–52), §4.1 (pp. 59–63), §4.2 (pp. 63–69)

## The warm-up streets (used in Blocks A–D)

Two kiosks each choose one block on a short street, simultaneously. Each customer walks to the
nearest kiosk; if both are equally distant (including when both choose the same block) the
block's customers split evenly. Each kiosk maximizes the number of customers it serves.

| Street | Blocks | Customers per block, from block 1 |
|---|---|---|
| S1 | 5 | 2, 1, 1, 1, 3 |
| S2 | 5 | 4, 1, 1, 1, 1 |
| S3 | 6 | 1, 1, 2, 1, 1, 1 |

---

## Block A — Writing the game (for case question a)

- **A1.** For S1, write $G = (I, \{S_i\}, \{u_i\})$ explicitly and fill the full 5×5 payoff matrix.
- **A2.** For two kiosks at blocks $x < y$ on any street, which blocks does each kiosk serve, and which (if any) are split? Express it with the midpoint $(x + y)/2$, separating the cases where it falls on a block and between two blocks.
- **A3.** For S1, write kiosk A's payoff as a formula with three cases, $s_A < s_B$, $s_A = s_B$, $s_A > s_B$, using sums of customers over ranges of blocks. Check your formula against three cells of A1's matrix.
- **A4.** The game is **constant-sum**: what is $u_A + u_B$ in every cell? Use it to halve the work in A1.
- **Book:** Tadelis Exercise 3.6 (p. 58): piecewise payoffs written by cases.

## Block B — Dominance (for case question b)

- **B1.** In S1, show whether block 1 is strictly dominated by block 2. List every inequality you must check (how many are there?), including the rival at block 1 and at block 2.
- **B2.** In S1, list **all** pairs (dominated, dominator). Is every dominated block dominated by its inner neighbour?
- **B3.** In S2, is block 1 dominated? Explain the difference from S1 in terms of where the customers are.
- **B4.** In S1 and S2, is any block strictly dominant? State precisely what you would have to show for "yes" and what a single counterexample cell does for "no".
- **B5.** Strict vs. weak: find, in S1 or S2, a pair of blocks where one weakly but not strictly dominates the other, if any. Why does the lecture's IESDS use strict dominance only?
- **Book:** Muñoz-Garcia & Toro-Gonzalez Ch. 1 Ex. 13 (p. 26, answer in the book).

## Block C — IESDS (for case question c)

- **C1.** Run IESDS on S1. For each round $k$, write $S_A^k$ and $S_B^k$ and name the dominator of each removed block.
- **C2.** Run IESDS on S2 and on S3. Which streets end with a single profile? For the one that does not, explain why elimination stops.
- **C3.** For S1: which round's removals need only rationality, and which need "A knows that B is rational", "B knows that A knows …"? How many levels of knowledge does your C1 answer use?
- **C4.** Guess a rule linking the surviving block(s) to the distribution of customers (hint: half of all customers lie on each side of …). Test the rule on S1–S3 before trusting it.
- **Book:** Tadelis Exercise 4.5 (p. 77); Gibbons Problem 1.2 (p. 48); then **Tadelis Exercise 4.10 (p. 78)**, the book's closest analogue of the case (do it before reading its solution).

## Block D — Welfare (for case question d)

- **D1.** One kiosk only: on S1, which block minimizes customers' total walking distance (customers × blocks walked)? Why is it a median, not the mean?
- **D2.** Two kiosks on S1: find the pair of blocks that minimizes total walking. (Tip: once the pair is fixed, each customer uses the nearer kiosk, so each kiosk should be the median of the customers it serves.)
- **D3.** Compare D2 with your C1 survivor. Who gains and who loses from the IESDS outcome: kiosks, customers, both? Use the constant-sum fact from A4.
- **D4.** Is the IESDS profile Pareto optimal **for the two kiosks**? Does Pareto optimality for the kiosks say anything about customers' welfare?

## Block E — Assumptions and extensions (for case question e)

No answers to compute; write three or four sentences for each.

- **E1.** List every assumption of the warm-up streets (simultaneous moves, fixed and equal prices, inelastic demand, nearest store, even split, two firms, one store each, discrete blocks). For each, say whether you think the prediction would change without it.
- **E2.** Prices: if the kiosks first chose locations and then prices, what would clustering do to the price stage? Read Cabral (2017) §14.2 (pp. 354, 358–360) on Hotelling's linear city.
- **E3.** A third kiosk: guess what happens to IESDS with three kiosks on S1 (do not compute; just predict and note why it is harder).
- **E4.** Collect two real examples of clustering (stores of competing chains side by side, petrol stations, political platforms) and two of spreading out. For each, which assumption from E1 best explains it?
- **Preview reading (Lecture 2):** Tadelis §5.2.5 (p. 93), Hotelling and voting.

---

## Checklist before class

- [ ] I can write a piecewise payoff for a location game without looking at notes.
- [ ] I can state strict dominance with its quantifier ("for all $s_{-i}$") and count the inequalities.
- [ ] I can tell "strictly dominated" from "not a best reply to this particular rival choice".
- [ ] I can record IESDS as $S_i^0 \supseteq S_i^1 \supseteq \dots$ and name the dominator at each step.
- [ ] I can explain why the median minimizes total distance.
- [ ] I have one clustering and one spreading-out example ready.

Suggested time: Blocks A–B 1 h, C 45 min, D 30 min, E 30 min.
