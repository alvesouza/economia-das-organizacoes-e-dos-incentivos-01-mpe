---
tags: [notes, lecture-01, pitfalls, true-false, self-test]
date: 2026-10-16
status: taught
source: "Aula/Lecture01.pdf; Tadelis (2013) Ch. 3, §4.1-4.2 (pp. 43-69); MWG §8.B (pp. 236-240); Cabral §7.1, §14.2; True/False items original, macro-1 style (rules/00_estilo_avaliacao.md)"
---

# Lecture 1 · Pitfalls and a True/False self-test

> Prev: [[L01-09-formulas]] · Next: [[L01-11-python]] · Map: [[L01-00-map]]

---

## Part I — the confusions this lecture produces

### 1 · "For each $s_{-i}$ something beats it" is not "dominated"

Dominance needs **one** alternative that wins against **every** $s_{-i}$. Counterexample: rows
T $=(3,0)$, M $=(1,1)$, B $=(0,3)$ against L, R. For each column some row beats M, yet neither T
nor B beats it in both columns; M is not dominated by a pure strategy
([[L01-04-dominance]] §7.1).

### 2 · Strict vs weak

Weak dominance allows ties. It does not follow from rationality alone, is not robust to small
payoff changes, and its iterated version depends on the order (MWG Figure 8.B.3 ends at three
different places; [[L01-06-iesds]] §6). Truthful bidding in a second-price auction is weakly,
**not** strictly, dominant ([[L01-04-dominance]] §6).

### 3 · Equilibrium = strategies, not payoffs

"The equilibrium is $(-4,-4)$" is wrong; it is (F, F), with payoffs $(-4,-4)$ (Tadelis p. 61).

### 4 · Pareto optimal vs equilibrium vs fair

The PD's equilibrium (F, F) is the only profile that is **not** Pareto optimal; (M, F) and
(F, M) **are** Pareto optimal although grossly unequal (Tadelis p. 57). Pareto optimality says
"no waste", not "best" and not "equal" ([[L01-05-pareto-social-dilemmas]] §1).

### 5 · Mutual knowledge is not common knowledge

"Everyone knows E" is level 1; IESDS round $k$ needs level $k-1$ of knowledge **of rationality**.
The exam announcement heard by a daydreaming student fails at level 2 (Tadelis p. 45;
[[L01-02-information-and-strategies]] §2).

### 6 · A strategy is not an action (once anyone observes anything)

If Pair sees your letter before writing, Pair has $2^2=4$ strategies, not 2. Writing the matrix
with 2 columns throws away the contingent plans ([[L01-02-information-and-strategies]] §3.1).

### 7 · "Dominant strategy" vs "the dominant-strategy outcome is good"

In the partnership, $S$ is dominant whenever $c>y/n$; it is **also efficient** only when $c\ge y$.
The dilemma is the band between ([[L01-05-pareto-social-dilemmas]] §3).

### 8 · IESDS in one shot vs iteratively

In matrix (4.1) M and D are **not** dominated in the original game; they become dominated only
after C is removed. Checking dominance once and stopping misses rounds 2 and 3
([[L01-06-iesds]] §3).

### 9 · IESDS reaches its limit, not a point, in Cournot

After any finite number of rounds the Cournot interval has width $45/2^{k-1}>0$; the prediction
$q=30$ is the intersection of all rounds ([[L01-07-cournot-iesds]] §4). And with three firms the
interval stops shrinking after round 1 (§6).

### 10 · The location game's survivor needs fixed prices

The middle-block prediction on the avenue is a result about locations **at given, equal prices**.
With price competition, clustering invites a price war and firms may spread out (Cabral p. 360;
[[L01-08-spatial-competition]] §6).

### 11 · "Weakly dominant equilibria need not be unique" depends on the definition

True with Tadelis's remark (p. 63: $\le$ everywhere, no strictness required); false with the
slides' definition (strict somewhere), under which each player has at most one weakly dominant
strategy ([[L01-04-dominance]] §7).

---

## Part II — True/False (original items)

Scoring as in the course: $\max\{0,\ \text{correct}-\text{wrong}/2\}$. Cover the verdict
column, decide, then read the justification.

| # | Claim | Verdict |
|---|---|---|
| 1 | In a static game the players must choose at the same instant. | F |
| 2 | Complete information requires that the payoff functions be common knowledge, not merely known by everyone. | T |
| 3 | If $s_i$ is strictly dominated, then $s_i$ is not a best response to any $s_{-i}\in S_{-i}$. | T |
| 4 | If for every $s_{-i}$ some strategy of player $i$ pays more than $s_i$, then $s_i$ is strictly dominated. | F |
| 5 | A game can have two different strict dominant-strategy equilibria. | F |
| 6 | Replacing every payoff $u_i$ by $e^{u_i}$ can change which strategies survive IESDS. | F |
| 7 | In the prisoner's dilemma of the slides, (M, F) is Pareto optimal. | T |
| 8 | A strict dominant-strategy equilibrium is always Pareto optimal. | F |
| 9 | In the $n$-partner game, effort is strictly dominant if and only if $c<y$. | F |
| 10 | Raising $n$ at fixed $y$ and $c$ can turn effort from dominant into a social dilemma. | T |
| 11 | Bidding one's value in a second-price auction is a strictly dominant strategy. | F |
| 12 | In a finite game, the set that survives IESDS does not depend on the order in which strictly dominated strategies are removed. | T |
| 13 | In a finite game, IESDS can eliminate every strategy of some player. | F |
| 14 | The second round of IESDS in matrix (4.1) requires player 1 to know that player 2 is rational. | T |
| 15 | If IESDS leaves a unique profile, that profile is a strict dominant-strategy equilibrium. | F |
| 16 | In Tadelis's Cournot game, after three rounds of IESDS each firm's surviving set is $[22.5,33.75]$. | T |
| 17 | In that game, IESDS selects $q_1=q_2=30$ after finitely many rounds. | F |
| 18 | In linear Cournot with an interior solution, a higher rival cost $c_2$ raises firm 1's predicted quantity. | T |
| 19 | On the 7-block avenue, block 4 is a strictly dominant location. | F |
| 20 | The IESDS outcome on the avenue minimizes customers' total walking distance. | F |
| 21 | In the location game every profile is Pareto optimal for the two chains. | T |
| 22 | A mafia sanction $z$ on finking makes (M, M) the strict dominant-strategy equilibrium for any $z>0$. | F |

### Justifications

1. **F.** "Simultaneous" means without observing the others' choices; timing is irrelevant (Tadelis p. 44; Gibbons p. 4). Studying two days apart is static if neither sees the other's effort.
2. **T.** Tadelis requires the four components, payoffs included, to be common knowledge (p. 45); mutual knowledge would not support reasoning about the others' reasoning.
3. **T.** If $s_i'$ beats $s_i$ at every $s_{-i}$, then at any given $s_{-i}$ the strategy $s_i$ is not optimal (Tadelis Prop. 4.3, p. 70).
4. **F.** The quantifiers are in the wrong order: dominance needs one $s_i'$ against all $s_{-i}$. Rows $(3,0),(1,1),(0,3)$: M is beaten in each column by a different row, and by no single row (Part I, 1).
5. **F.** Prop. 4.1: two strictly dominant strategies for the same player would each have to beat the other everywhere.
6. **F.** $e^{x}$ is strictly increasing, so every inequality between two of $i$'s payoffs at a fixed $s_{-i}$ is preserved; dominance is ordinal ([[L01-02-information-and-strategies]] §4.1).
7. **T.** Only (M, F) gives player 2 as much as $-1$, so no other profile keeps player 2 at least as well off; nothing Pareto dominates it (Tadelis p. 57).
8. **F.** The PD's (F, F) is Pareto dominated by (M, M) — Lesson 2.
9. **F.** Effort is dominant iff $c<y/n$; $c<y$ is the condition for all-E to Pareto dominate all-S.
10. **T.** The threshold $y/n$ falls with $n$ while $y$ does not: e.g. $y=6$, $c=2.5$ — effort dominant at $n=2$ ($3>2.5$), dilemma at $n=3$ ($2<2.5<6$).
11. **F.** Weakly: against a highest rival bid below both one's value and the alternative bid, the two bids pay the same.
12. **T.** MWG pp. 239–240 (Exercise 8.B.4): a strategy dominated against a set of profiles stays dominated against any subset.
13. **F.** In a finite game, a strategy that is best against some fixed surviving $s_{-i}$ cannot be strictly dominated, so each $S_i^k$ stays nonempty. (With infinite sets it can happen: $S=[0,1)$, $u=s$.)
14. **T.** Round 2 removes M and D because column C is gone, which player 1 can use only if he knows player 2 is rational ([[L01-06-iesds]] §3).
15. **F.** Matrix (4.1) has a unique survivor (U, L) but no dominant strategy for either player.
16. **T.** $[0,45]\to[22.5,45]\to[22.5,33.75]$ (Tadelis p. 66).
17. **F.** The width is $45/2^{k-1}>0$ after every finite round; 30 is the limit.
18. **T.** $q_1^*=(a-2c_1+c_2)/(3b)$, so $\partial q_1^*/\partial c_2=1/(3b)>0$: a weaker rival produces less, and firm 1's best response to less is more ([[L01-07-cournot-iesds]] §5).
19. **F.** Against a rival at block 1, block 2 pays 6 and block 4 only 5; no block is a best reply to every location.
20. **F.** $(4,4)$ gives total walking 12; $\{2,5\}$ gives 6.
21. **T.** The game is constant-sum ($u_A+u_B=7$), so any gain for one chain is a loss for the other.
22. **F.** M beats F for each player iff $z>1$ (Tadelis pp. 62–63); with $0<z\le1$ fink stays (weakly, at $z=1$) at least as good.

> **Quizzes generated from this unit** belong in `Simulados/` (`/quiz-gen` can take
> [[L01-09-formulas]] and this note as source); the existing ones are
> `Simulados/quiz-lecture01-{1,2,3}-*.md`.

---

## Links

- Map: [[L01-00-map]] · formulas: [[L01-09-formulas]] · code: [[L01-11-python]].
- Style rules for T/F items: [[../../rules/00_estilo_avaliacao|rules/00_estilo_avaliacao]].
