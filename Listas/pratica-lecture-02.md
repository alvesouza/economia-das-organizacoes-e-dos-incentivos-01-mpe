---
status: aligned
tags: [lista, pratica, lecture-02, topic/static-games, topic/nash-equilibrium, topic/mixed-strategies]
date: 2026-11-12
---

# Practice plan — Lecture 2 (Static games of complete information II: best responses, Nash equilibrium, Cournot, Bertrand and mixed strategies)

> **Re-aligned on 2026-11-12** to the real Lecture 2 slides (`Aula/Lecture02.pdf`). The list lost 3
> items, which moved to Lecture 3 (`Listas/pratica-lecture-03.md`): Tadelis 6.5 (old #16), Gibbons
> 1.14 (old #20) and Tadelis 6.3 (old #24). The 22 items below are renumbered 1–22 in rising
> difficulty; the "Old #" column gives each item's number in the 25-item list of commit `fe47ead`.
> Statements are the old transcriptions, unchanged; each source line now also carries the PDF page
> and whether the source gives the answer, and four statements gained the book material they refer
> to (Prop. 5.1, the Battle of the Sexes matrix, the Bertrand and Hotelling setups).

22 existing book exercises in one sequence of rising complexity, each reproduced verbatim under
its tier table (transcribed from the PDF text layers and checked against the rendered page images
on 2026-10-25). Sources: Tadelis (2013), the book the slides follow; Muñoz-Garcia & Toro-Gonzalez
(2019), worked answers after every exercise; Gibbons (1992); MWG (1995). Lecture slides:
`Aula/Lecture02.pdf` (slide numbers below are the printed ones, 1–56). Class plan: [[Map/study-guide|study guide]]; book map:
[[Map/books-index|books-index]]; notes: [[Notas/L02/L02-00-map|Lecture 2 notes]]. Detailed
solutions: `Listas/pratica-lecture-02-solutions.pdf` (sources in `Listas/pratica-lecture-02-solutions/`).

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise. MWG 8.C.1, 8.D.2,
8.D.3, 8.D.6: the MWG solutions manual (`Livros/`) covers the Chapter 8 exercises (not checked item
by item). Gibbons 1.3–1.12: in an unofficial, unfinished manual (`D:/Livros/Mercado/Economia/`,
not copied). Tadelis: none in the book; the preface (p. xiii) says about half are solved on
Princeton UP's website (not checked).

**Verification.** Every page below was checked in the PDF on 2026-10-25 by rendering the page
(offsets in `Livros/book-registry.json`): Tadelis exercises 5.1–5.3 on p. 95, 5.5, 5.6 and 5.8 on pp. 96–97,
5.12 on p. 98, 5.15 on p. 99, 6.1 on p. 123, 6.8 on p. 125; Gibbons 1.3, 1.5–1.7
on pp. 49–50, 1.12 on p. 51; MWG 8.C.1 on p. 262 (the study guide's "After class" line
says p. 263, where 8.D.1–8.D.4 start), 8.D.2–8.D.3 on p. 263, 8.D.6 on p. 264; Muñoz-Garcia Ch. 2
Ex. 2 on p. 41, Ex. 7 on p. 48, Ch. 3 Ex. 1 on pp. 86–87. Matrices were re-typed from the page
images, not from the `.md` conversions. The PDF pages in brackets are viewer pages (1-based).

**Not here on purpose.** The in-class mini case (work or shirk: monitoring remote work, slides
53–55) is graded in-class work. Its closest book analogues, Tadelis 6.4 "Monitoring" (pp. 123–124)
and 6.12 "The Tax Man" (p. 126), are left out so this list does not solve the case; do them after
the graded case is returned. Gibbons 1.2 (p. 48) is already item 7 of
`Listas/pratica-lecture-01.md`. Dominance by mixed strategies (Tadelis 6.3, §6.3) moved to
Lecture 3. The tragedy of the commons and Hotelling voting are in Tadelis but **were not covered
in class**: Hotelling appears only as the last item, flagged as reading.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Best responses, rationalizability, and Nash equilibrium versus IESDS | 6 | 27% | slides 8–17 (best response, rationalizability, Nash equilibrium) prove both directions (Props. 1–2, slides 16–17) and flag weakly dominated equilibria; proofs are the exam's favourite |
| B2 | Pure Nash equilibria in matrices: coordination, dilemmas, multiplicity | 3 | 14% | battle of the sexes, side of the road and the prisoner's dilemma (slides 9, 14, 18); quick to drill |
| B3 | Oligopoly: Cournot (duopoly, $n$ firms, cartel) and Bertrand | 7 | 31% | the longest stretch of the slides (20–40) and the lecture's main application |
| B4 | Mixed strategies, the principle of indifference, existence | 5 | 23% | slides 42–51: expected payoffs, the indifference proof, the battle of the sexes in mixed strategies, Nash's theorem |
| B5 | Reading, not covered in class: Hotelling | 1 | 5% | in Tadelis Ch. 5 and the notes, absent from the slides |

| Level | Items | Count |
|---|---|---|
| Foundations (best replies in a matrix, a first Cournot, a first $2\times2$ mixed equilibrium) | 1–8 | 8 |
| Exam (the propositions' proofs, Cournot with $n$ firms and asymmetric costs, the cartel as a prisoner's dilemma, Bertrand, a mixed equilibrium in an applied game) | 9–17 | 9 |
| Advanced (MWG rationalizability, the dollar-grid auction, the discrete Bertrand grid, existence in $2\times2$ games, one reading item) | 18–22 | 5 |

---

## Tier 1 — Foundations

| # | Old # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|---|
| 1 | 1 | B2 | Muñoz-Garcia | Ch. 2 | Ex. 2 | 41 | Best responses cell by cell and the two pure equilibria of the battle of the sexes |
| 2 | 2 | B2 | Tadelis | Ch. 5, Exercises | 5.6 | 96 | Building a matrix from parameters, then finding the pure equilibria (hawk-dove) |
| 3 | 3 | B1 | Tadelis | Ch. 5, Exercises | 5.5 | 96 | A best-response correspondence with three players, then the pure equilibria |
| 4 | 4 | B2 | Gibbons | §1.1, Problems | 1.3 | 49 | Continuous strategies with a continuum of pure equilibria (splitting a dollar) |
| 5 | 5 | B3 | Muñoz-Garcia | Ch. 2 | Ex. 7 | 48 | The Cournot duopoly with general $a$, $b$, $c$: first-order condition, best response, crossing |
| 6 | 6 | B4 | Muñoz-Garcia | Ch. 3 | Ex. 1 | 86–87 | Chicken: no dominated strategy, two pure equilibria, the mixed one and its best-response graph |
| 7 | 7 | B4 | Tadelis | Ch. 6, Exercises | 6.1 | 123 | All equilibria of the battle of the sexes from the best-response correspondences (slides 47–50 redone) |
| 8 | 8 | B4 | Gibbons | §1.3, Problems | 1.12 | 51 | A $2\times2$ game with no pure equilibrium: the mixed one by indifference |

### Statements

#### 1. Muñoz-Garcia Ex. 2 (Ch. 2)

<!-- id: Muñoz-Garcia Ch. 2 Ex. 2 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 2, Exercise 2 "Battle of the Sexes", p. 41 [PDF p. 54]. Answer in the source: yes, a worked answer follows the exercise. Reproduced verbatim (statement only; the book's worked answer follows it).

> A husband and a wife are leaving work, and do not remember which event they are attending to tonight. Both of them, however, remember that last night's argument was about either attending to the football game (the most preferred event for the husband) or the opera (the most preferred event for the wife). To make matters worse, their cell phones broke, so they cannot call each other to confirm which event they are attending to. As a consequence, they must simultaneously and independently decide whether to attend to the football game or the opera.
>
> The payoff matrix in Fig. 2.4 describes the preference of the husband (wife) for the football game (opera, respectively), but also indicates that both players prefer to be together rather than being alone (even if they are alone at their most preferred event). Find the set of Nash Equilibria of this game.
>
> | *Housband* [sic] \ *Wife* | *Football* | *Opera* |
> |---|---|---|
> | *Football* | 3, 1 | 0, 0 |
> | *Opera* | 0, 0 | 1, 3 |
>
> *Fig. 2.4* Battle of the sexes game (Normal-form representation)

#### 2. Tadelis 5.6

<!-- id: Tadelis 5.6 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.6 "Hawk-Dove", p. 96 [PDF p. 115]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim (with the book's footnote 12).

> **Hawk-Dove:** The following game has been widely used in evolutionary biology to understand how fighting and display strategies by animals could coexist in a population. For a typical Hawk-Dove game there are resources to be gained (e.g., food, mates, territories), denoted as $v$. Each of two players can choose to be aggressive, as Hawk ($H$), or compromising, as Dove ($D$). If both players choose $H$ then they split the resources but lose some payoff from injuries, denoted as $k$. Assume that $k > \frac{v}{2}$. If both choose $D$ then they split the resources but engage in some display of power that carries a display cost $d$, with $d < \frac{v}{2}$. Finally, if player $i$ chooses $H$ while $j$ chooses $D$ then $i$ gets all the resources while $j$ leaves with no benefits and no costs.
>
> a. Describe this game in a matrix.
>
> b. Assume that $v = 10$, $k = 6$, and $d = 4$. What outcomes can be supported as pure-strategy Nash equilibria?$^{12}$
>
> *Footnote 12.* In the evolutionary biology literature, the analysis performed is of a very different nature. Instead of considering the Nash equilibrium analysis of a static game, the analysis is a dynamic one in which successful strategies "replicate" in a large population. This analysis is part of a methodology called evolutionary game theory. For more on the subject see Gintis (2000).

#### 3. Tadelis 5.5

<!-- id: Tadelis 5.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.5 "Public Good Contribution", p. 96 [PDF p. 115]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Public Good Contribution:** Three players live in a town, and each can choose to contribute to fund a streetlamp. The value of having the streetlamp is 3 for each player, and the value of not having it is 0. The mayor asks each player to contribute either 1 or nothing. If at least two players contribute then the lamp will be erected. If one player or no players contribute then the lamp will not be erected, in which case any person who contributed will not get his money back.
>
> a. Write out or graph each player's best-response correspondence.
>
> b. What outcomes can be supported as pure-strategy Nash equilibria?

#### 4. Gibbons 1.3

<!-- id: Gibbons 1.3 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.1 Problems, Problem 1.3, p. 49 [PDF p. 57]. Answer in the source: none (Gibbons prints no answers). Reproduced verbatim.

> 1.3. Players 1 and 2 are bargaining over how to split one dollar. Both players simultaneously name shares they would like to have, $s_1$ and $s_2$, where $0 \le s_1, s_2 \le 1$. If $s_1 + s_2 \le 1$, then the players receive the shares they named; if $s_1 + s_2 > 1$, then both players receive zero. What are the pure-strategy Nash equilibria of this game?

#### 5. Muñoz-Garcia Ex. 7 (Ch. 2)

<!-- id: Muñoz-Garcia Ch. 2 Ex. 7 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 2, Exercise 7 "Cournot Game of Quantity Competition", p. 48 [PDF p. 61]. Answer in the source: yes, a worked answer follows the exercise. Reproduced verbatim (statement only; the book's worked answer follows it).

> Consider an industry with two firms competing in quantities, i.e., Cournot competition. For simplicity, assume that firms are symmetric in costs, $c > 0$, with no fixed costs and that they face a linear inverse demand $p(Q) = a - bQ$, where $a > c$, $b > 0$, and $Q$ denotes aggregate output. Note that the assumption $a > c$ implies that the highest willingness to pay for the first unit is larger than the marginal cost that firms must incur in order to produce the first unit, thus indicating that a positive production level is profitable in this industry. If firms simultaneously and independently select their output level, $q_1$ and $q_2$, find the Nash Equilibrium (NE) of the Cournot game of quantity competition.

#### 6. Muñoz-Garcia Ex. 1 (Ch. 3)

<!-- id: Muñoz-Garcia Ch. 3 Ex. 1 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 3, Exercise 1 "Game of Chicken", pp. 86–87 [PDF p. 99–100]. Answer in the source: yes, a worked answer follows the exercise. Reproduced verbatim (statement only; the book's worked answer follows it).

> Consider the game of Chicken (depicted in Fig. 3.1), in which two players driving their cars against each other must decide whether or not to swerve.
>
> **Part (a)** Is there any strictly dominated strategy for Player 1? And for Player 2?
>
> **Part (b)** What are the best responses for Player 1? And for Player 2?
>
> **Part (c)** Can you find any pure strategy Nash Equilibrium (psNE) in this game?
>
> **Part (d)** Find the mixed strategy Nash Equilibrium (msNE) of the game. *Hint*: denote by $p$ the probability that Player 1 chooses Straight and by $(1 - p)$ the probability that he chooses to Swerve. Similarly, let $q$ denote the probability that Player 2 chooses Straight and $(1 - q)$ the probability that she chooses to Swerve.
>
> **Part (e)** Show your result of part (d) by graphically representing every player $i$'s best response function $BRF_i(s_j)$, where $s_j = \{Swerve, Straight\}$ is the strategy selected by player $j \neq i$.
>
> | *Player 1* \ *Player 2* | Straight | Swerve |
> |---|---|---|
> | Straight | 0,0 | 3,1 |
> | Swerve | 1,3 | 2,2 |
>
> *Fig. 3.1* Game of Chicken

#### 7. Tadelis 6.1

<!-- id: Tadelis 6.1 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 6.1 "Best Responses in the Battle of the Sexes", p. 123 [PDF p. 142]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Best Responses in the Battle of the Sexes:** Use the best-response correspondences in the Battle of the Sexes game to find all the Nash equilibria. (Follow the approach used for the example in Section 6.2.3.)

**Referred to in the statement.** The Battle of the Sexes (Tadelis §3.3, pp. 53–54 [PDF p. 72–73]) (reproduced from the book):

> Alex and Chris are a couple, and they need to choose where to meet this evening, with no means of communicating. Both prefer being together over not being together, but Alex prefers opera ($O$) to football ($F$), while Chris prefers the opposite.
>
> | Alex \ Chris | $O$ | $F$ |
> |---|---|---|
> | $O$ | 2, 1 | 0, 0 |
> | $F$ | 0, 0 | 1, 2 |

#### 8. Gibbons 1.12

<!-- id: Gibbons 1.12 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.3 Problems, Problem 1.12, p. 51 [PDF p. 59]. Answer in the source: none (Gibbons prints no answers). Reproduced verbatim.

> 1.12. Find the mixed-strategy Nash equilibrium of the following normal-form game.
>
> |   | $L$ | $R$ |
> |---|---|---|
> | $T$ | 2,1 | 0,2 |
> | $B$ | 1,2 | 3,0 |

## Tier 2 — Exam level

| # | Old # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|---|
| 9 | 9 | B1 | Tadelis | Ch. 5, Exercises | 5.1 | 95 | Proving Prop. 5.1: a dominant-strategy equilibrium, unique IESDS survivor or unique rationalizable profile is the unique Nash equilibrium (slides 16–17) |
| 10 | 10 | B1 | Tadelis | Ch. 5, Exercises | 5.2 | 95 | A weakly dominant-strategy equilibrium next to another Nash equilibrium (the slides' note on weakly dominated equilibria) |
| 11 | 11 | B1 | Tadelis | Ch. 5, Exercises | 5.3 | 95–96 | When a unique pure equilibrium is, and is not, the unique IESDS survivor ($2\times2$ vs $3\times3$) |
| 12 | 12 | B3 | Tadelis | Ch. 5, Exercises | 5.8 | 96–97 | Cournot with $n$ firms and the competitive limit (slides 26–27) |
| 13 | 13 | B3 | Gibbons | §1.2, Problems | 1.5 | 49 | The cartel output against the Cournot output as a prisoner's dilemma (slide 25) |
| 14 | 14 | B3 | Gibbons | §1.2, Problems | 1.6 | 49 | Cournot with asymmetric costs: the interior equilibrium and the corner where one firm exits |
| 15 | 15 | B3 | Gibbons | §1.2, Problems | 1.7 | 49–50 | Uniqueness of $p_1 = p_2 = c$ in homogeneous Bertrand (slides 35–38) |
| 16 | 17 | B4 | Tadelis | Ch. 6, Exercises | 6.8 | 125 | Pure equilibria with three players, then a symmetric mixed one by indifference |
| 17 | 18 | B1 | MWG | §8.D, Exercises | 8.D.2 | 263 | Proving the slides' Prop. 2: a unique IESDS survivor is a Nash equilibrium |

### Statements

#### 9. Tadelis 5.1

<!-- id: Tadelis 5.1 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.1, p. 95 [PDF p. 114]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Prove Proposition 5.1.**

**Referred to in the statement.** Proposition 5.1 (Tadelis pp. 80–81 [PDF p. 99–100]) (reproduced from the book):

> **Proposition 5.1** Consider a strategy profile $s = (s_1, s_2, \ldots, s_n)$. If $s$ is either
>
> 1. a strict dominant strategy equilibrium,
> 2. the unique survivor of IESDS, or
> 3. the unique rationalizable strategy profile,
>
> then $s$ is the unique Nash equilibrium.

#### 10. Tadelis 5.2

<!-- id: Tadelis 5.2 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.2 "Weak Dominance", p. 95 [PDF p. 114]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Weak Dominance:** A strategy $s^W \in S$ is a weakly dominant strategy equilibrium if $s_i^W \in S_i$ is a weakly dominant strategy for all $i \in N$, that is, if $v_i(s_i^W, s_{-i}) \ge v_i(s_i', s_{-i})$ for all $s_i' \in S_i$ and for all $s_{-i} \in S_{-i}$. Provide an example of a game for which there is a weakly dominant strategy equilibrium as well as another Nash equilibrium.

#### 11. Tadelis 5.3

<!-- id: Tadelis 5.3 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.3 "Nash and IESDS", pp. 95–96 [PDF p. 114–115]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Nash and IESDS:** Consider a two-player game with $m$ pure strategies for each player that can be represented by an $m \times m$ matrix.
>
> a. Show that if $m = 2$ and the game has a unique pure-strategy Nash equilibrium then this is the unique strategy profile that survives IESDS.
>
> b. Show that if $m = 3$ and the game has a unique pure-strategy equilibrium then it may not be the only strategy profile that survives IESDS.

#### 12. Tadelis 5.8

<!-- id: Tadelis 5.8 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.8 "The $n$-Firm Cournot Model", pp. 96–97 [PDF p. 115–116]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim (the printed "$Q = q_i + \cdots + q_n$" is kept as printed).

> **The $n$-Firm Cournot Model:** Suppose there are $n$ firms in the Cournot oligopoly model. Let $q_i$ denote the quantity produced by firm $i$, and let $Q = q_i + \cdots + q_n$ denote the aggregate production. Let $P(Q)$ denote the market clearing price (when demand equals $Q$) and assume that the inverse demand function is given by $P(Q) = a - Q$, where $Q \le a$. Assume that firms have no fixed cost and that the cost of producing quantity $q_i$ is $cq_i$ (all firms have the same marginal cost, and assume that $c < a$).
>
> a. Model this as a normal-form game.
>
> b. What is the Nash (Cournot) equilibrium of the game in which firms choose their quantities simultaneously?
>
> c. What happens to the equilibrium price as $n$ approaches infinity? Is this familiar?

#### 13. Gibbons 1.5

<!-- id: Gibbons 1.5 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.2 Problems, Problem 1.5, p. 49 [PDF p. 57]. Answer in the source: none (Gibbons prints no answers). Reproduced verbatim.

> 1.5. Consider the following two finite versions of the Cournot duopoly model. First, suppose each firm must choose either half the monopoly quantity, $q_m/2 = (a - c)/4$, or the Cournot equilibrium quantity, $q_c = (a - c)/3$. No other quantities are feasible. Show that this two-action game is equivalent to the Prisoners' Dilemma: each firm has a strictly dominated strategy, and both are worse off in equilibrium than they would be if they cooperated. Second, suppose each firm can choose either $q_m/2$, or $q_c$, or a third quantity, $q'$. Find a value for $q'$ such that the game is equivalent to the Cournot model in Section 1.2.A, in the sense that $(q_c, q_c)$ is a unique Nash equilibrium and both firms are worse off in equilibrium than they could be if they cooperated, but neither firm has a strictly dominated strategy.

#### 14. Gibbons 1.6

<!-- id: Gibbons 1.6 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.2 Problems, Problem 1.6, p. 49 [PDF p. 57]. Answer in the source: none (Gibbons prints no answers). Reproduced verbatim.

> 1.6. Consider the Cournot duopoly model where inverse demand is $P(Q) = a - Q$ but firms have asymmetric marginal costs: $c_1$ for firm 1 and $c_2$ for firm 2. What is the Nash equilibrium if $0 < c_i < a/2$ for each firm? What if $c_1 < c_2 < a$ but $2c_2 > a + c_1$?

#### 15. Gibbons 1.7

<!-- id: Gibbons 1.7 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.2 Problems, Problem 1.7, pp. 49–50 [PDF p. 57–58]. Answer in the source: none (Gibbons prints no answers). Reproduced verbatim.

> 1.7. In Section 1.2.B, we analyzed the Bertrand duopoly model with differentiated products. The case of homogeneous products yields a stark conclusion. Suppose that the quantity that consumers demand from firm $i$ is $a - p_i$ when $p_i < p_j$, 0 when $p_i > p_j$, and $(a - p_i)/2$ when $p_i = p_j$. Suppose also that there are no fixed costs and that marginal costs are constant at $c$, where $c < a$. Show that if the firms choose prices simultaneously, then the unique Nash equilibrium is that both firms charge the price $c$.

#### 16. Tadelis 6.8

<!-- id: Tadelis 6.8 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 6.8 "Market Entry", p. 125 [PDF p. 144]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Market Entry:** Three firms are considering entering a new market. The payoff for each firm that enters is $\frac{150}{n}$, where $n$ is the number of firms that enter. The cost of entering is 62.
>
> a. Find all the pure-strategy Nash equilibria.
>
> b. Find the symmetric mixed-strategy equilibrium in which all three players enter with the same probability.

#### 17. MWG 8.D.2

<!-- id: MWG 8.D.2 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 8 Exercises, Exercise 8.D.2^B, p. 263 [PDF p. 142]. Answer in the source: none in the book (the MWG solutions manual covers Chapter 8). Reproduced verbatim.

> Show that if there is a unique profile of strategies that survives iterated removal of strictly dominated strategies, this profile is a Nash equilibrium.

## Tier 3 — Advanced

| # | Old # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|---|
| 18 | 19 | B1 | MWG | §8.C, Exercises | 8.C.1 | 262 | Rationalizability is at least as sharp as IESDS when IESDS is unique |
| 19 | 21 | B3 | MWG | §8.D, Exercises | 8.D.3 | 263 | A first-price auction on a dollar grid: strict vs weak dominance, existence and uniqueness of equilibrium |
| 20 | 22 | B3 | Tadelis | Ch. 5, Exercises | 5.12 | 98 | Bertrand with asymmetric costs on a one-cent grid: counting the equilibria |
| 21 | 23 | B4 | MWG | §8.D, Exercises | 8.D.6 | 264 | Existence of a mixed equilibrium in every $2\times2$ game via best-response correspondences (the theorem of slide 51, proved for $2\times2$) |
| 22 | 25 | B5 | Tadelis | Ch. 5, Exercises | 5.15 | 99 | **Reading, not covered in class.** Hotelling with a continuum of voters: the median-voter equilibrium |

### Statements

#### 18. MWG 8.C.1

<!-- id: MWG 8.C.1 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 8 Exercises, Exercise 8.C.1^A, p. 262 [PDF p. 142]. Answer in the source: none in the book (the MWG solutions manual covers Chapter 8). Reproduced verbatim.

> Argue that if elimination of strictly dominated strategies yields a unique prediction in a game, this prediction also results from eliminating strategies that are never a best response.

#### 19. MWG 8.D.3

<!-- id: MWG 8.D.3 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 8 Exercises, Exercise 8.D.3^B, p. 263 [PDF p. 142]. Answer in the source: none in the book (the MWG solutions manual covers Chapter 8). Reproduced verbatim.

> Consider a first-price sealed-bid auction of an object with two bidders. Each bidder $i$'s valuation of the object is $v_i$, which is known to both bidders. The auction rules are that each player submits a bid in a sealed envelope. The envelopes are then opened, and the bidder who has submitted the highest bid gets the object and pays the auctioneer the amount of his bid. If the bidders submit the same bid, each gets the object with probability $\frac{1}{2}$. Bids must be in dollar multiples (assume that valuations are also).
>
> **(a)** Are any strategies strictly dominated?
>
> **(b)** Are any strategies weakly dominated?
>
> **(c)** Is there a Nash equilibrium? What is it? Is it unique?

#### 20. Tadelis 5.12

<!-- id: Tadelis 5.12 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.12 "Asymmetric Bertrand", p. 98 [PDF p. 117]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim.

> **Asymmetric Bertrand:** Consider the Bertrand game with $c_1(q_1) = q_1$ and $c_2(q_2) = 2q_2$ and demand equal to $p = 100 - q$, in which firms must choose prices in increments of \$0.01. We have seen in Section 5.2.4 that one possible Nash equilibrium is $(p_1^*, p_2^*) = (1.99, 2.00)$.
>
> a. Show that there are other Nash equilibria for this game.
>
> b. How many Nash equilibria does this game have?

**Referred to in the statement.** The Bertrand game of Tadelis §5.2.4 (pp. 88–91 [PDF p. 107–110]) (reproduced from the book):

> Demand is given by $p = 100 - q$; each firm posts a price $p_i$ for otherwise identical goods, all buyers buy from the firm whose price is lowest, and if there is a tie the market splits equally between the two firms. In the asymmetric example $c_1 = 1$ and $c_2 = 2$ and prices are limited to increments of $\epsilon = 0.01$; the book then says that "one possible Nash equilibrium (you are asked to find more in exercise 5.12 at the end of this chapter) is $(p_1, p_2) = (1.99, 2.00)$."

#### 21. MWG 8.D.6

<!-- id: MWG 8.D.6 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 8 Exercises, Exercise 8.D.6^B, p. 264 [PDF p. 143]. Answer in the source: none in the book (the MWG solutions manual covers Chapter 8). Reproduced verbatim.

> Consider any two-player game of the following form (where letters indicate arbitrary payoffs):
>
> | Player 1 \ Player 2 | $b_1$ | $b_2$ |
> |---|---|---|
> | $a_1$ | $u, v$ | $\ell, m$ |
> | $a_2$ | $w, x$ | $y, z$ |
>
> Show that a mixed strategy Nash equilibrium always exists in this game. [*Hint:* Define player 1's strategy to be his probability of choosing action $a_1$ and player 2's to be his probability of choosing $b_1$; then examine the best-response correspondences of the two players.]

#### 22. Tadelis 5.15

<!-- id: Tadelis 5.15 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 5.15 "Hotelling's Continuous Model", p. 99 [PDF p. 118]. Answer in the source: none (the preface, p. xiii, says about half of the exercises are solved on Princeton UP's website). Reproduced verbatim. **Reading, not covered in class** (Tadelis §5.2.5, pp. 93–95).

> **Hotelling's Continuous Model:** Consider Hotelling's model, in which citizens are a continuum of voters on the interval $A = [-a, a]$, with uniform distribution $U(a)$.
>
> a. What is the best response of candidate $i$ if candidate $j$ is choosing $a_j > 0$?
>
> b. Show that the unique Nash equilibrium is $a_1 = a_2 = 0$.
>
> c. Show that for a general distribution $F(\cdot)$ over $[-a, a]$ the unique Nash equilibrium is where each candidate chooses the policy associated with the median voter.

**Referred to in the statement.** Hotelling's model (Tadelis §5.2.5, pp. 92–94 [PDF p. 111–113]) (reproduced from the book):

> Two politicians, each caring only about being elected; each candidate $i$ chooses a platform $a_i$ (the policy of the citizen for whom it is ideal); each citizen votes for the candidate whose platform is closest to his preferences (an indifferent citizen tosses a coin); a candidate wins if a majority votes for him, and candidates prefer winning to a tie and a tie to losing.
>
> *Remark.* In the more common representation of the Hotelling competition model, the citizens are a continuum of voters, given by the interval $A = [\underline{a}, \overline{a}]$, with distribution $F(a)$ to determine the distribution of each political preference. We define the median voter as that voter $a_m$ for which $\Pr\{a \le a_m\} = \frac12$. For example, if $F(\cdot)$ is uniform then $a_m = \frac{\underline{a}+\overline{a}}{2}$.

**Optional extras.**
- Tadelis 5.4 (p. 96, splitting pizza) and MWG 8.D.4 (p. 263, splitting 100 dollars, with dominance parts): more continua of equilibria, after item 4.
- Gibbons 1.13 (p. 51, two workers applying to two firms): pure and mixed equilibria in an applied $2\times2$ game, after item 8.
- Tadelis 6.6 (p. 124, declining industry): a $3\times3$ game where weak dominance shrinks the support of the unique mixed equilibrium.
- Muñoz-Garcia Ch. 2 Ex. 16 (p. 76, Cournot with efficiency changes) and Ch. 3 Ex. 10 (p. 114, rock-paper-scissors): worked answers in the book.
- Reading, not covered in class: Tadelis 5.7 (p. 96, the $n$-player commons), 4.8–4.9 (p. 78, the beauty contest); Gibbons 1.8 (p. 50, voting with two and three candidates); MWG 8.D.5 (pp. 263–264, ice-cream vendors).

---

## Suggested study order

1. **Best responses and Nash equilibrium.** Read Tadelis §4.3 (pp. 69–76) and §5.1 (pp. 79–83) with slides 9–18, then do items **1–4**, then **9–11** and **17**.
2. **Cournot and Bertrand.** Read Tadelis §5.2.3–5.2.4 (pp. 87–93) and Gibbons §1.2.A–B (pp. 14–22) with slides 20–40, then do **5**, then **12–15**.
3. **Mixed strategies.** Read Tadelis §6.1–6.2 (pp. 101–114) and Gibbons §1.3.A (pp. 29–40) with slides 42–50, then do **6–8**, then **16**.
4. **Existence and the formal side.** Read Tadelis §6.4 (pp. 117–123) and MWG §8.C-8.D (pp. 242–253), then do **18, 21**, then **19, 20**.
5. **Reading item.** Only after the rest: **22** (not covered in class).

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Best responses, beliefs, rationalizability | Ch. 4, §4.3 | p. 69–76 | Foundations |
| Nash equilibrium; relation to IESDS and rationalizability; multiple equilibria | Ch. 5, §5.1–5.2.1 | p. 79–84 | Foundations |
| Cournot; Bertrand | Ch. 5, §5.2.3–5.2.4 | p. 87–93 | Exam |
| Tragedy of the commons; Hotelling voting (not covered in class) | Ch. 5, §5.2.2, §5.2.5 | p. 84–87, 93–95 | Advanced |
| Exercises 5.1–5.3, 5.5, 5.6, 5.8, 5.12, 5.15 | Ch. 5, Exercises | p. 95–99 | Exam |
| Mixed strategies, beliefs, mixed Nash equilibrium, indifference | Ch. 6, §6.1–6.2 | p. 101–114 | Exam |
| Nash's existence theorem | Ch. 6, §6.4 | p. 117–123 | Exam |
| Exercises 6.1, 6.8 | Ch. 6, Exercises | p. 123, 125 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Motivation and definition of Nash equilibrium | §1.1.C | p. 8–14 | Foundations |
| Cournot; Bertrand | §1.2.A–B | p. 14–22 | Exam |
| Mixed strategies and existence | §1.3 | p. 29–48 | Exam |
| Problems 1.3, 1.5–1.7, 1.12 | §1.5 Problems | p. 49–51 | Exam |

### MWG — Mas-Colell, Whinston & Green (1995)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Rationalizable strategies | §8.C | p. 242–245 | Advanced |
| Nash equilibrium, mixed strategies, existence | §8.D | p. 246–253 | Advanced |
| Exercises 8.C.1, 8.D.2, 8.D.3, 8.D.6 | Ch. 8, Exercises | p. 262–264 | Advanced |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Pure-strategy Nash equilibrium: exercises with worked answers | Ch. 2 | p. 37–84 | Foundations |
| Mixed strategies: exercises with worked answers | Ch. 3 | p. 85–151 | Exam |

## Consolidated Exercises

| Item | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 9 | 5.1 | Tadelis | p. 95 | Proof of Prop. 5.1 | Exam |
| 10 | 5.2 | Tadelis | p. 95 | Weakly dominant-strategy equilibrium and another NE | Exam |
| 11 | 5.3 | Tadelis | p. 95–96 | Unique NE vs unique IESDS survivor | Exam |
| 3 | 5.5 | Tadelis | p. 96 | Three-player best-response correspondence | Foundations |
| 2 | 5.6 | Tadelis | p. 96 | Hawk-dove | Foundations |
| 12 | 5.8 | Tadelis | p. 96–97 | Cournot with $n$ firms | Exam |
| 20 | 5.12 | Tadelis | p. 98 | Asymmetric Bertrand on a cent grid | Advanced |
| 22 | 5.15 | Tadelis | p. 99 | Hotelling, continuum of voters (reading) | Advanced |
| 7 | 6.1 | Tadelis | p. 123 | Battle of the sexes, all equilibria | Foundations |
| 16 | 6.8 | Tadelis | p. 125 | Market entry, symmetric mixing | Exam |
| 4 | 1.3 | Gibbons | p. 49 | Splitting a dollar | Foundations |
| 13 | 1.5 | Gibbons | p. 49 | Finite Cournot as a prisoner's dilemma | Exam |
| 14 | 1.6 | Gibbons | p. 49 | Cournot with asymmetric costs | Exam |
| 15 | 1.7 | Gibbons | p. 49–50 | Homogeneous Bertrand | Exam |
| 8 | 1.12 | Gibbons | p. 51 | Mixed equilibrium of a $2\times2$ game | Foundations |
| 18 | 8.C.1 | MWG | p. 262 | IESDS vs never-best-response elimination | Advanced |
| 17 | 8.D.2 | MWG | p. 263 | Unique IESDS survivor is a NE | Exam |
| 19 | 8.D.3 | MWG | p. 263 | First-price auction on a grid | Advanced |
| 21 | 8.D.6 | MWG | p. 264 | Existence in $2\times2$ games | Advanced |
| 1 | Ex. 2 (Ch. 2) | Muñoz-Garcia | p. 41 | Battle of the sexes, pure NE | Foundations |
| 5 | Ex. 7 (Ch. 2) | Muñoz-Garcia | p. 48 | Cournot duopoly | Foundations |
| 6 | Ex. 1 (Ch. 3) | Muñoz-Garcia | p. 86–87 | Chicken, pure and mixed | Foundations |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Best responses and Nash equilibrium | Tadelis §4.3, §5.1 p. 69–83; slides 9–18 | Muñoz-Garcia Ch. 2 Ex. 2; Tadelis 5.5, 5.6, 5.1, 5.2, 5.3; Gibbons 1.3; MWG 8.D.2 | 2.5–3 h |
| 2 | Cournot and Bertrand | Tadelis §5.2.3–5.2.4 p. 87–93; Gibbons §1.2.A–B p. 14–22; slides 20–40 | Muñoz-Garcia Ch. 2 Ex. 7; Tadelis 5.8; Gibbons 1.5, 1.6, 1.7 | 2–2.5 h |
| 3 | Mixed strategies and indifference | Tadelis §6.1–6.2 p. 101–114; Gibbons §1.3.A p. 29–40; slides 42–50 | Muñoz-Garcia Ch. 3 Ex. 1; Tadelis 6.1, 6.8; Gibbons 1.12 | 1.5–2 h |
| 4 | Existence and the formal side | Tadelis §6.4 p. 117–123; MWG §8.C-8.D p. 242–253; slide 51 | MWG 8.C.1, 8.D.3, 8.D.6; Tadelis 5.12 | 2–2.5 h |
| 5 | Reading, not covered in class | Tadelis §5.2.5 p. 93–95 | Tadelis 5.15 | 0.5 h |
