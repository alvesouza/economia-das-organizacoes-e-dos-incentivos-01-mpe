---
tags: [lista, pratica, lecture-03, topic/mixed-strategies, topic/dynamic-games]
date: 2026-11-12
status: aligned
---

# Practice plan — Lecture 3 (Mixed strategies and dynamic games)

**Re-aligned on 2026-11-12** to the real slides `Aula/Lecture03.pdf` ("Lecture 3: Mixed strategies
and dynamic games", 90 slides: Bertrand with capacity constraints and the Edgeworth paradox, slides
4–14; mixed strategies, the principle of indifference and the battle of the sexes, 15–36; game trees,
information sets, strategies, perfect recall, backward induction, subgames and SPE, 37–70; Stackelberg
and the Cuban missile crisis, 71–72; the mini case "work or shirk", 73–79; appendix on capacity
constraints, 80–90). The list replaces the estimated Lecture 3 list of 2026-10-25: the 15 exercises on
extensive form, backward induction and subgame perfection are kept from it, and three exercises on
mixed strategies move in from the old Lecture 2 list. The Stackelberg, entry-deterrence and
time-inconsistency exercises of the old Lecture 3 list move to Lecture 4's list
(`Listas/pratica-lecture-04.md`). Every item keeps the verbatim statement block verified on
2026-10-25, with a "Moved here from" line giving its old list and number.

18 existing book exercises in one sequence of rising complexity, each reproduced verbatim under its
tier table. Sources: Tadelis (2013), Ch. 6–8, the book the slides follow; Muñoz-Garcia &
Toro-Gonzalez (2019), Ch. 4, worked answers after every exercise; Gibbons (1992), Ch. 1–2; MWG
(1995), §9.B. Lecture slides: `Aula/Lecture03.pdf`. Class plan: [[Map/study-guide|study guide]]; book map:
[[Map/books-index|books-index]]; notes: [[Notas/L03/L03-00-map|Lecture 3 notes]]. Worked solutions:
`Listas/pratica-lecture-03-solutions.pdf` (source `Listas/pratica-lecture-03-solutions/`), every number
asserted by `check_L03.py`.

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise. MWG 9.B.4 and
9.B.5: in the MWG solutions manual (`Livros/`). Gibbons 1.14 and 2.1: in an unofficial, unfinished
manual (`D:/Livros/Mercado/Economia/`, not copied). Tadelis: none in the book; the preface (p. xiii)
says about half are solved on Princeton UP's website (not checked).

**Verification.** Statements were transcribed from the PDF text layers and checked against the
rendered page images on 2026-10-20 and 2026-10-25 (the old lists), and are copied here unchanged.
Pages: Tadelis exercises 6.3 on p. 123 and 6.5 on p. 124; 7.1–7.2 on p. 147, 7.4 and 7.6 on pp.
148–149, 7.9 on pp. 149–150, 7.10 and Fig. 7.14 on p. 150; 8.5 on p. 170, 8.10–8.11 on pp. 172–173
(PDF index = printed page + 18). Muñoz-Garcia Ch. 4 Ex. 3 on p. 160, Ex. 4 on p. 163, Ex. 9 on pp.
176–177 (offset 11). Gibbons Problem 1.14 on p. 51 and 2.1 on p. 130 (offset 6). MWG 9.B.4–9.B.5 on
p. 302 (2-up scan: PDF page index 161, left half). Game trees are cropped from the book pages into
`Listas/figures/`.

**Not in this list on purpose.** The slides' Edgeworth example (capacity constraints) has no exercise
among the four books' lists; read the appendix slides 80–90. Stackelberg (slide 71) and the Cuban
missile crisis (slide 72) are practised in Lecture 4's list together with the entry-deterrence and
commitment exercises. The mini case (slides 73–79) is graded in-class work; its analogues Tadelis
6.4 "Monitoring" and 6.12 "The Tax Man" stay out so the list does not solve the case. Tadelis 6.3
(item 15) and Gibbons 1.14 (item 14) go beyond the slides: 6.3 is strict dominance by mixed
strategies (reading, Tadelis §6.3), 1.14 extends the proposition that a Nash equilibrium survives
IESDS to mixed equilibria, which the principle of indifference (slides 21–26) proves.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Mixed strategies: indifference, mixed equilibria, mixed dominance | 3 | 17% | slides 15–36 (22 of 79 content slides); the principle of indifference is proved in class |
| B2 | Describing a dynamic game: trees, information sets, Nature, strategies, normal form and Nash equilibria of a tree, mixed vs behavioral | 6 | 33% | slides 41–58; every later step needs the strategy sets right |
| B3 | Backward induction and subgame perfection: proper subgames, SPE, Nash equilibria that are not SPE | 8 | 44% | slides 59–70, Example 3 and the Cuban missile crisis; the lecture's solution concept, densest in all four books |
| B4 | Backward induction with continuous actions | 1 | 6% | the Rotten Kid theorem; Stackelberg itself is in Lecture 4's list |

| Level | Items | Count |
|---|---|---|
| Foundations (a first mixed equilibrium, draw a tree, count strategies, solve a small game by backward induction) | 1–7 | 7 |
| Exam (Nature and imperfect information, subgames with simultaneous stages, mixed vs behavioral strategies, sequential vetoes) | 8–13 | 6 |
| Advanced (mixed dominance and IESDS, proofs, the Rotten Kid theorem, Maskin's SPE exercise) | 14–18 | 5 |


---

## Tier 1 — Foundations

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 1 | B1 | Tadelis | Ch. 6, Exercises | 6.5 | 124 | Building a matrix from a story, best-response graphs, a mixed equilibrium |
| 2 | B2 | Tadelis | Ch. 7, Exercises | 7.1 | 147 | Counting pure strategies: the product over information sets |
| 3 | B3 | Muñoz-Garcia | Ch. 4 | Ex. 3 | 160 | Backward induction in the sequential prisoner's dilemma, and comparison with the simultaneous game |
| 4 | B2 | Tadelis | Ch. 7, Exercises | 7.2 | 147 | From a verbal story to a tree; terminal nodes, information sets, strategies, and an "unappealing" Nash equilibrium |
| 5 | B3 | Muñoz-Garcia | Ch. 4 | Ex. 4 | 163 | Backward induction in the sequential Battle of the Sexes: the first-mover advantage |
| 6 | B2 | Tadelis | Ch. 7, Exercises | 7.6 | 148–149 | Choosing payoffs that represent preferences, then every Nash equilibrium of the entry game |
| 7 | B3 | Muñoz-Garcia | Ch. 4 | Ex. 9 | 176–177 | The 100-stage centipede solved from the last stage back |

### Statements

#### 1. Tadelis 6.5


<!-- id: Tadelis 6.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 6.5 "Cops and Robbers", p. 124 [PDF 143]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 2 list, item 16.

> **Cops and Robbers:** Player 1 is a police officer who must decide whether to patrol the streets or to hang out at the coffee shop. His payoff from hanging out at the coffee shop is 10, while his payoff from patrolling the streets depends on whether he catches a robber, who is player 2. If the robber prowls the streets then the police officer will catch him and obtain a payoff of 20. If the robber stays in his hideaway then the officer's payoff is 0. The robber must choose between staying hidden or prowling the streets. If he stays hidden then his payoff is 0, while if he prowls the streets his payoff is $-10$ if the officer is patrolling the streets and 10 if the officer is at the coffee shop.
>
> a. Write down the matrix form of this game.
>
> b. Draw the best-response function of each player.
>
> c. Find the Nash equilibrium of this game. What kind of game does this game remind you of?

#### 2. Tadelis 7.1


<!-- id: Tadelis 7.1 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.1 "Strategies", p. 147 [PDF 166]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 1.

> **Strategies:** Imagine an extensive-form game in which player $i$ has $K$ information sets.
>
> a. If the player has an identical number of $m$ possible actions in each information set, how many pure strategies does he have?
>
> b. If the player has $m_k$ actions in information set $k \in \{1, 2, \ldots, K\}$, how many pure strategies does the player have?

#### 3. Muñoz-Garcia Ex. 3


<!-- id: Muñoz-Garcia Ch. 4 Ex. 3 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 4, Exercise 3 "Sequential Version of the Prisoner's Dilemma Game", p. 160 [PDF 172]. Reproduced verbatim (statement only; the book's worked answer follows it).

**Moved here from:** old Lecture 3 list, item 3.

> Consider the game tree in Fig. 4.9, representing the sequential-move version of the Prisoner's dilemma game, where player 1 acts first, and observing its move player 2 responds.
>
> ![Fig. 4.9 Prisoner's dilemma sequential-move game](figures/munoz-garcia-4-3.png)
>
> *Fig. 4.9* Prisoner's dilemma sequential-move game
>
> (a) Find the best responses of the second mover, for each of the first mover's actions.
>
> (b) Find the first mover's equilibrium action and describe the subgame perfect Nash equilibrium of the game.
>
> (c) Does the equilibrium behavior in the sequential-move game differ from its simultaneous-move version?

#### 4. Tadelis 7.2


<!-- id: Tadelis 7.2 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.2 "Strategies and Equilibrium", p. 147 [PDF 166]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 2.

> **Strategies and Equilibrium:** Consider a two-player game in which player 1 can choose $A$ or $B$. The game ends if he chooses $A$ while it continues to player 2 if he chooses $B$. Player 2 can then choose $C$ or $D$, with the game ending after $C$ and continuing again with player 1 after $D$. Player 1 can then choose $E$ or $F$, and the game ends after each of these choices.
>
> a. Model this as an extensive-form game tree. Is it a game of perfect or imperfect information?
>
> b. How many terminal nodes does the game have? How many information sets?
>
> c. How many pure strategies does each player have?
>
> d. Imagine that the payoffs following choice $A$ by player 1 are $(2, 0)$, those following $C$ by player 2 are $(3, 1)$, those following $E$ by player 1 are $(0, 0)$, and those following $F$ by player 1 are $(1, 2)$. What are the Nash equilibria of this game? Does one strike you as more "appealing" than the other? If so, explain why.

#### 5. Muñoz-Garcia Ex. 4


<!-- id: Muñoz-Garcia Ch. 4 Ex. 4 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 4, Exercise 4 "Sequential Version of the Battle of the Sexes Game", p. 163 [PDF 175]. Reproduced verbatim (statement only; the book's worked answer follows it). *Note (not in the book):* part (a) as printed swaps the roles; the wife moves first, so read it as the husband's best responses to each of the wife's actions, which is what the book's answer computes.

**Moved here from:** old Lecture 3 list, item 4.

> Consider the game tree in Fig. 4.13, representing the sequential-move version of the Battle of the Sexes game, where wife acts first, and observing its move husband responds.
>
> ![Fig. 4.13 Battle of the sexes sequential-move game](figures/munoz-garcia-4-4.png)
>
> *Fig. 4.13* Battle of the sexes sequential-move game
>
> (a) Find the best responses of the wife, for each of the husband's actions.
>
> (b) Find the husband's equilibrium action and describe the subgame perfect Nash equilibrium of the game.
>
> (c) Does the equilibrium behavior in the sequential-move game differ from its simultaneous-move version?

#### 6. Tadelis 7.6


<!-- id: Tadelis 7.6 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.6 "Entering an Industry", pp. 148–149 [PDF 167–168]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 5.

> **Entering an Industry:** A firm (player 1) is considering entering an established industry with one incumbent firm (player 2). Player 1 must choose whether or not to enter the industry. If player 1 enters the industry then player 2 can either accommodate the entry or fight the entry by waging a price war. Player 1's most-preferred outcome is entering with player 2 not fighting, and its least-preferred outcome is entering with player 2 fighting. Player 2's most-preferred outcome is player 1 not entering, and its least-preferred outcome is player 1 entering with player 2 fighting.
>
> a. Model this as an extensive-form game tree (choose payoffs that represent the preferences).
>
> b. How many pure strategies does each player have?
>
> c. Find all the Nash equilibria of this game.

#### 7. Muñoz-Garcia Ex. 9


<!-- id: Muñoz-Garcia Ch. 4 Ex. 9 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 4, Exercise 9 "Centipede Game", pp. 176–177 [PDF 188–189]. Reproduced verbatim (statement only; the book's worked answer follows it). The figure is printed with the book's subgame boxes already drawn. *Note (not in the book):* the text says depositor 1 moves at the 100th stage, but Fig. 4.31 and the book's answer have depositor 2 as the last mover, choosing between $(99, 101)$ and $(100, 100)$; follow the figure.

**Moved here from:** old Lecture 3 list, item 7.

> Consider the game tree in Fig. 4.31, representing the so-called "centipede game" between depositor 1 and 2. In the first stage, depositor 1 chooses whether to take the money in the saving account, which yields a payoff of \$2 for him and \$0 for the other depositor, or keep the money in the account. If depositor 1 keeps the money in the account, the game continues to stage 2 where depositor 2 can take the money or keep it in the account for one more period. If he takes the money, he receives a payoff of \$3 while depositor 1 receives only \$1. If depositor 2 keeps the money in the account, then it's depositor 1's turn to choose whether to take the money or keep it for one more period. The game continues with depositors alternatively choosing whether to take the money until the 100th stage, when it is depositor 1's turn to move. Since the game tree has 100 branches pointing down, it is often called the "centipede" game since the game tree looks like an insect with 100 legs.
>
> a. Find the best response of the last mover.
>
> b. Anticipating equilibrium behavior in the 100th stage, find the best response of the previous-to-last mover (the depositor acting in stage 99).
>
> ![Fig. 4.31 Centipede sequential-form game](figures/munoz-garcia-4-9.png)
>
> *Fig. 4.31* Centipede sequential-form game
>
> c. Using your results in parts (a) and (b), find the subgame perfect Nash equilibrium of the game.


---

## Tier 2 — Exam level

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 8 | B2 | Tadelis | Ch. 7, Exercises | 7.4 | 148 | A four-move centipede with a growing pot: strategies, Nash equilibria, and how many outcomes they support |
| 9 | B2 | Tadelis | Ch. 7, Exercises | 7.9 | 149–150 | A move of Nature and an information set: tree, normal form and Nash equilibria |
| 10 | B2 | Tadelis | Ch. 7, Exercises | 7.10 | 150 | Mixed vs behavioral strategies, and what breaks without perfect recall (Kuhn) |
| 11 | B3 | Tadelis | Ch. 8, Exercises | 8.5 | 170 | A simultaneous game, then the same game behind an adoption decision: proper subgames and SPE |
| 12 | B3 | Tadelis | Ch. 8, Exercises | 8.10 | 172 | A safe option before a simultaneous stage: subgames, normal form, Nash vs SPE |
| 13 | B3 | Tadelis | Ch. 8, Exercises | 8.11 | 172–173 | Sequential vetoes: SPE, Nash equilibria that are not SPE, and the value of removing an option |

### Statements

#### 8. Tadelis 7.4


<!-- id: Tadelis 7.4 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.4 "Centipedes", p. 148 [PDF 167]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 9.

> **Centipedes:** Imagine a two-player game that proceeds as follows. A pot of money is created with \$6 in it initially. Player 1 moves first, then player 2, then player 1 again, and finally player 2 again. At each player's turn to move, he has two possible actions: grab ($G$) or share ($S$). If he grabs he gets $\frac{2}{3}$ of the current pot of money, the other player gets $\frac{1}{3}$ of the pot, and the game ends. If he shares then the size of the current pot is multiplied by $\frac{3}{2}$ and the next player gets to move. At the last stage at which player 2 moves, if he chooses $S$ then the pot is still multiplied by $\frac{3}{2}$, player 2 gets $\frac{1}{3}$ of the pot, and player 1 gets $\frac{2}{3}$ of the pot.
>
> a. Model this as an extensive-form game tree. Is it a game of perfect or imperfect information?
>
> b. How many terminal nodes does the game have? How many information sets?
>
> c. How many pure strategies does each player have?
>
> d. Find the Nash equilibria of this game. How many outcomes can be supported in equilibrium?
>
> e. Now imagine that at the last stage at which player 2 moves, if he chooses to share then the pot is equally split among the players. Does your answer to part (d) change?

#### 9. Tadelis 7.9


<!-- id: Tadelis 7.9 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.9 "The Dean's Dilemma", pp. 149–150 [PDF 168–169]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 10.

> **The Dean's Dilemma:** A student stole the DVD player from the student lounge. The dean of students (player 1) suspects the student (player 2) and begins collecting evidence. However, evidence collection is a random process, and concrete evidence will be available to the dean only with probability $\frac{1}{2}$. The student knows that the evidence-gathering process is under way but does not know whether the dean has collected evidence or not. The game proceeds as follows: The dean realizes whether or not he has evidence and can then choose his action, whether to accuse the student ($A$) or bounce the case ($B$) and forget it. Once accused, the student has two options: he can either confess ($C$) or deny ($D$). Payoffs are realized as follows: If the dean bounces the case then both players get 0. If the dean accuses the student and the student confesses, the dean gains 2 and the student loses 2. If the dean accuses the student and the student denies, then payoffs depend on the evidence: If the dean has no evidence then he loses face, which gives him a loss of 4, while the student gains glory, which gives him a payoff of 4. If, however, the dean has evidence then he is triumphant and gains 4, while the student is put on probation and loses 4.
>
> a. Draw the game tree that represents the extensive form of this game.
>
> b. Write down the matrix that represents the normal form of the extensive form you drew in (a).
>
> c. Solve for the Nash equilibria of the game.

#### 10. Tadelis 7.10


<!-- id: Tadelis 7.10 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 7.10 "Perfect and Imperfect Recall", p. 150 [PDF 169]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 11.

> **Perfect and Imperfect Recall:** Consider the game depicted in Figure 7.14.
>
> ![Figure 7.14 Exercise 7.10](figures/tadelis-7-10.png)
>
> a. What are the pure-strategy sets for each player?
>
> b. Show that for any behavioral strategy for player 1 there is a mixed strategy that leads to the same distribution over the terminal nodes regardless of the strategy chosen by player 2.
>
> c. Show that for any behavioral strategy for player 2 there is a mixed strategy that leads to the same distribution over the terminal nodes regardless of the strategy chosen by player 1.
>
> d. Now imagine that the game does not have perfect recall so that player 2's bottom two information sets are now one large information set. Can you find an example showing that the claim in (c) is no longer true?

#### 11. Tadelis 8.5


<!-- id: Tadelis 8.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.5 "Technology Adoption", p. 170 [PDF 189]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 12.

> **Technology Adoption:** During the adoption of a new technology a CEO (player 1) can design a new task for a division manager. The new task can be either high level ($H$) or low level ($L$). The manager simultaneously chooses to invest in good training ($G$) or bad training ($B$). The payoffs from this interaction are given by the following matrix:
>
> | Player 1 \ Player 2 | $G$ | $B$ |
> |:---:|:---:|:---:|
> | $H$ | 5, 4 | −5, 2 |
> | $L$ | 2, −2 | 0, 0 |
>
> a. Present the game in extensive form (a game tree) and solve for all the Nash equilibria and subgame-perfect equilibria.
>
> b. Now assume that before the game is played the CEO can choose not to adopt this new technology, in which case the payoffs are (1, 1), or to adopt it, in which case the game is played. Present the *entire* game in extensive form. How many proper subgames does it have?
>
> c. Solve for all the Nash equilibria and subgame-perfect equilibria of the game described in (b).

#### 12. Tadelis 8.10


<!-- id: Tadelis 8.10 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.10 "Playing It Safe", p. 172 [PDF 191]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 13.

> **Playing It Safe:** Consider the following dynamic game: Player 1 can choose to play it safe (denote this choice by $S$), in which case both he and player 2 get a payoff of 3 each, or he can risk playing a game with player 2 (denote this choice by $R$). If he chooses $R$ then they play the following simultaneous-move game:
>
> | Player 1 \ Player 2 | $A$ | $B$ |
> |:---:|:---:|:---:|
> | $C$ | 8, 0 | 0, 2 |
> | $D$ | 6, 6 | 2, 2 |
>
> a. Draw a game tree that represents this game. How many proper subgames does it have?
>
> b. Are there other game trees that would work? Explain briefly.
>
> c. Construct the matrix representation of the normal form of this dynamic game.
>
> d. Find all the Nash and subgame-perfect equilibria of the dynamic game.

#### 13. Tadelis 8.11


<!-- id: Tadelis 8.11 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 8.11 "Resident Assistant Selection with a Twist", pp. 172–173 [PDF 191–192]. Reproduced verbatim. Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 3 list, item 14.

> **Resident Assistant Selection with a Twist:** Two staff managers in the ΠΒΦ sorority, the house manager (player 1) and kitchen manager (player 2), must select a resident assistant from a pool of three candidates: $\{a, b, c\}$. Player 1 prefers $a$ to $b$, and $b$ to $c$. Player 2 prefers $b$ to $a$, and $a$ to $c$. The process that is imposed on them is as follows: First, the house manager vetoes one of the candidates and announces the veto to the central office for staff selection and to the kitchen manager. Next the kitchen manager vetoes one of the remaining two candidates and announces it to the central office. Finally the director of the central office assigns the remaining candidate to be a resident assistant at ΠΒΦ.
>
> a. Model this as an extensive-form game (using a game tree) in which a player's most-preferred candidate gives a payoff of 2, the second most-preferred candidate gives a payoff of 1, and the last candidate gives 0.
>
> b. Find the subgame-perfect equilibrium for this game. Is it unique?
>
> c. Are there Nash equilibria that are not subgame-perfect equilibria?
>
> d. Now assume that before the two players play the game, player 2 can send an alienating e-mail to one of the candidates, which would result in that candidate withdrawing her application. Would player 2 choose to do this, and if so, with which candidate?


---

## Tier 3 — Advanced

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 14 | B1 | Gibbons | §1.3, Problems | 1.14 | 51 | The slides' Prop. 1 extended to mixed equilibria: strategies in the support survive IESDS |
| 15 | B1 | Tadelis | Ch. 6, Exercises | 6.3 | 123 | **Reading, not covered in class.** Strict dominance by mixed strategies; infinitely many dominating mixes |
| 16 | B3 | MWG | §9.B, Exercises | 9.B.4 | 302 | Proving that SPE payoffs are unique in finite zero-sum games of perfect information |
| 17 | B4 | Gibbons | §2.1, Problems | 2.1 | 130 | Backward induction with continuous actions: the Rotten Kid theorem |
| 18 | B3 | MWG | §9.B, Exercises | 9.B.5 | 302 | Strategy counts with and without observation; when SPE is multiple; when moving first guarantees the simultaneous-game payoff |

### Statements

#### 14. Gibbons 1.14


<!-- id: Gibbons 1.14 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §1.3 Problems, Problem 1.14, p. 51 [PDF 59]. Reproduced verbatim. Answer in the source: none (Gibbons prints no answers).

**Moved here from:** old Lecture 2 list, item 20.

> 1.14. Show that Proposition B in Appendix 1.1.C holds for mixed- as well as pure-strategy Nash equilibria: the strategies played with positive probability in a mixed-strategy Nash equilibrium survive the process of iterated elimination of strictly dominated strategies.

#### 15. Tadelis 6.3


<!-- id: Tadelis 6.3 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 6.3 "Mixed Dominance 2", p. 123 [PDF 142]. Reproduced verbatim. **Reading, not covered in class** (Tadelis §6.3, pp. 114–117). Answer in the source: none in the book (the preface, p. xiii, says about half are solved on Princeton UP's website; not checked).

**Moved here from:** old Lecture 2 list, item 24.

> **Mixed Dominance 2:** Consider the game used in Section 6.3:
>
> | Player 1 \ Player 2 | $L$ | $C$ | $R$ |
> |:---:|:---:|:---:|:---:|
> | $U$ | 5, 1 | 1, 4 | 1, 0 |
> | $M$ | 3, 2 | 0, 0 | 3, 5 |
> | $D$ | 4, 3 | 4, 4 | 0, 3 |
>
> a. Find a strategy different from $(\sigma_2(L), \sigma_2(C), \sigma_2(R)) = \left(0, \frac{1}{2}, \frac{1}{2}\right)$ that strictly dominates the pure strategy $L$ for player 2. Argue that you can find an infinite number of such strategies.
>
> b. Find a strategy different from $(\sigma_1(U), \sigma_1(M), \sigma_1(D)) = \left(0, \frac{1}{2}, \frac{1}{2}\right)$ that strictly dominates the pure strategy $U$ for player 1 in the game remaining after one stage of elimination. Argue that you can find an infinite number of such strategies.

#### 16. MWG 9.B.4


<!-- id: MWG 9.B.4 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 9 Exercises, Exercise 9.B.4^B, p. 302 [PDF 162]. Reproduced verbatim. Answer in the source: none in the book (see the MWG solutions manual in `Livros/`).

**Moved here from:** old Lecture 3 list, item 19.

> Prove that in a finite *zero-sum* game of perfect information, there are unique subgame perfect Nash equilibrium payoffs.

#### 17. Gibbons 2.1


<!-- id: Gibbons 2.1 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.6 Problems (Section 2.1), Problem 2.1, p. 130 [PDF 137]. Reproduced verbatim. Answer in the source: none (Gibbons prints no answers).

**Moved here from:** old Lecture 3 list, item 24.

> 2.1. Suppose a parent and child play the following game, first analyzed by Becker (1974). First, the child takes an action, $A$, that produces income for the child, $I_C(A)$, and income for the parent, $I_P(A)$. (Think of $I_C(A)$ as the child's income net of any costs of the action $A$.) Second, the parent observes the incomes $I_C$ and $I_P$ and then chooses a bequest, $B$, to leave to the child. The child's payoff is $U(I_C + B)$; the parent's is $V(I_P - B) + kU(I_C + B)$, where $k > 0$ reflects the parent's concern for the child's well-being. Assume that: the action is a nonnegative number, $A \geq 0$; the income functions $I_C(A)$ and $I_P(A)$ are strictly concave and are maximized at $A_C > 0$ and $A_P > 0$, respectively; the bequest $B$ can be positive or negative; and the utility functions $U$ and $V$ are increasing and strictly concave. Prove the "Rotten Kid" Theorem: in the backwards-induction outcome, the child chooses the action that maximizes the family's aggregate income, $I_C(A) + I_P(A)$, even though only the parent's payoff exhibits altruism.

#### 18. MWG 9.B.5


<!-- id: MWG 9.B.5 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 9 Exercises, Exercise 9.B.5^B (E. Maskin), p. 302 [PDF 162]. Reproduced verbatim. Answer in the source: none in the book (see the MWG solutions manual in `Livros/`).

**Moved here from:** old Lecture 3 list, item 20.

> (E. Maskin) Consider a game with two players, player 1 and player 2, in which each player $i$ can choose an action from a finite set $M_i$ that contains $m_i$ actions. Player $i$'s payoff if the action choices are $(m_1, m_2)$ is $\phi_i(m_1, m_2)$.
>
> (a) Suppose, first, that the two players move simultaneously. How many strategies does each player have?
>
> (b) Now suppose that player 1 moves first and that player 2 observes player 1's move before choosing her move. How many strategies does each player have?
>
> (c) Suppose that the game in (b) has multiple SPNEs. Show that if this is the case, then there exist two pairs of moves $(m_1, m_2)$ and $(m_1', m_2')$ (where either $m_1 \neq m_1'$ or $m_2 \neq m_2'$) such that either
>
> $$\text{(i)}\quad \phi_1(m_1, m_2) = \phi_1(m_1', m_2')$$
>
> or
>
> $$\text{(ii)}\quad \phi_2(m_1, m_2) = \phi_2(m_1', m_2').$$
>
> (d) Suppose that for any two pairs of moves $(m_1, m_2)$ and $(m_1', m_2')$ such that $m_1 \neq m_1'$ or $m_2 \neq m_2'$, condition (ii) is violated (i.e., player 2 is never indifferent between pairs of moves). Suppose also that there exists a pure strategy Nash equilibrium in the game in (a) in which $\pi_1$ is player 1's payoff. Show that in any SPNE of the game in (b), player 1's payoff is at least $\pi_1$. Would this conclusion necessarily hold for any *Nash* equilibrium of the game in (b)?
>
> (e) Show by example that the conclusion in (d) may fail either if condition (ii) holds for some strategy pairs $(m_1, m_2)$, $(m_1', m_2')$ with $m_1 \neq m_1'$ or $m_2 \neq m_2'$ or if we replace the phrase *pure strategy Nash equilibrium* with the phrase *mixed strategy Nash equilibrium*.

**Optional extras.**
- Tadelis 7.5 (veto power, p. 148), 7.7 (roommates voting, p. 149) and 7.8 with 8.3 (Brothers, pp. 149, 170): more trees, strategy sets and SPE.
- Tadelis 7.3 (tic-tac-toe, pp. 147–148): counting information sets in a large tree; needs a spreadsheet.
- Tadelis 8.1 and 8.2 (p. 170): mixed-strategy SPE of the voluntary Battle of the Sexes (read Fig. 8.2, p. 154) and of mutually assured destruction (read §8.3.3, pp. 163–166, Fig. 8.11); 8.1 is the slides' Example 2 of Lecture 4.
- Muñoz-Garcia Ch. 4 Ex. 2 (entry-predation, p. 156), Ex. 5–6 (sequential Pareto coordination and chicken, pp. 166, 169), Ex. 10 (trust and reciprocity, p. 177), Ex. 19–20 (backward induction drills, pp. 202, 204): all with worked answers.
- Gibbons 2.2 (Samaritan's dilemma, pp. 130–131) and 2.4 (two-period contribution game, pp. 131–132): continuous-action backward induction after item 17.

---

## Suggested study order

1. **Mixed strategies.** Read Tadelis §6.1–6.2 (pp. 101–114) and Gibbons §1.3.A (pp. 29–40) with slides 15–36, then do item **1**, then **14**; item **15** is reading (Tadelis §6.3, pp. 114–117).
2. **Describing a dynamic game.** Read Tadelis Ch. 7 (pp. 129–146) with slides 41–58, then do items **2, 4, 6**, then **8, 9, 10**.
3. **Backward induction.** Read Tadelis §8.1 (pp. 151–153) and Gibbons §2.1.A (pp. 57–61) with slides 59–64, then do **3, 5, 7**.
4. **Subgame perfection.** Read Tadelis §8.2 (pp. 153–159) and Gibbons §2.4.B (pp. 122–129) with slides 65–70, then do **11, 12, 13**, then **16, 18**.
5. **Continuous actions.** Do **17** after the Stackelberg slide (71); the Stackelberg exercises themselves are in Lecture 4's list.

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Mixed strategies, beliefs, mixed Nash equilibrium, indifference | Ch. 6, §6.1–6.2 | p. 101–114 | Foundations |
| Mixed dominance (not covered in class) | Ch. 6, §6.3 | p. 114–117 | Advanced |
| Exercises 6.3, 6.5 | Ch. 6, Exercises | p. 123–124 | Exam |
| Extensive form: game trees, information sets, perfect vs imperfect information | Ch. 7, §7.1 | p. 129–137 | Foundations |
| Pure, mixed and behavioral strategies; perfect recall | Ch. 7, §7.2 | p. 137–144 | Foundations |
| Nash equilibrium and paths of play | Ch. 7, §7.3 | p. 144–146 | Foundations |
| Exercises 7.1, 7.2, 7.4, 7.6, 7.9, 7.10 | Ch. 7, Exercises | p. 147–150 | Exam |
| Sequential rationality and backward induction; Zermelo | Ch. 8, §8.1 | p. 151–153 | Foundations |
| Subgame-perfect equilibrium | Ch. 8, §8.2 | p. 153–159 | Exam |
| Exercises 8.5, 8.10, 8.11 | Ch. 8, Exercises | p. 170–173 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Mixed strategies and existence | §1.3 | p. 29–48 | Exam |
| Backwards induction | §2.1.A | p. 57–61 | Foundations |
| Extensive form; subgame-perfect Nash equilibrium | §2.4 | p. 115–129 | Exam |
| Problems 1.14, 2.1 | §1.5 and §2.6, Problems | p. 51, 130 | Advanced |

### MWG — Mas-Colell, Whinston & Green (1995)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Extensive form | §7.C | p. 221–225 | Advanced |
| Sequential rationality, backward induction, subgame perfection | §9.A–9.B | p. 267–281 | Advanced |
| Exercises 9.B.4, 9.B.5 | Ch. 9, Exercises | p. 302 | Advanced |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Sequential-move games with complete information: exercises with worked answers | Ch. 4 | p. 153–214 | Foundations |

## Consolidated Exercises

| # | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 1 | 6.5 | Tadelis | p. 124 | Cops and robbers, mixed equilibrium | Foundations |
| 2 | 7.1 | Tadelis | p. 147 | Counting strategies | Foundations |
| 3 | Ex. 3 | Muñoz-Garcia | p. 160 | Sequential prisoner's dilemma | Foundations |
| 4 | 7.2 | Tadelis | p. 147 | Story to tree; Nash equilibria of a tree | Foundations |
| 5 | Ex. 4 | Muñoz-Garcia | p. 163 | Sequential Battle of the Sexes | Foundations |
| 6 | 7.6 | Tadelis | p. 148–149 | Entry game, Nash equilibria | Foundations |
| 7 | Ex. 9 | Muñoz-Garcia | p. 176–177 | 100-stage centipede | Foundations |
| 8 | 7.4 | Tadelis | p. 148 | Four-move centipede | Exam |
| 9 | 7.9 | Tadelis | p. 149–150 | Nature and information sets | Exam |
| 10 | 7.10 | Tadelis | p. 150 | Perfect and imperfect recall | Exam |
| 11 | 8.5 | Tadelis | p. 170 | Technology adoption: subgames | Exam |
| 12 | 8.10 | Tadelis | p. 172 | Safe option before a simultaneous stage | Exam |
| 13 | 8.11 | Tadelis | p. 172–173 | Sequential vetoes | Exam |
| 14 | 1.14 | Gibbons | p. 51 | Mixed equilibria survive IESDS | Advanced |
| 15 | 6.3 | Tadelis | p. 123 | Dominance by mixed strategies (reading) | Advanced |
| 16 | 9.B.4 | MWG | p. 302 | Zero-sum perfect information | Advanced |
| 17 | 2.1 | Gibbons | p. 130 | Rotten Kid theorem | Advanced |
| 18 | 9.B.5 | MWG | p. 302 | Observation, multiplicity, first-mover payoff | Advanced |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Mixed strategies | Tadelis §6.1–6.2 p. 101–114; Gibbons §1.3.A p. 29–40; slides 15–36 | Tadelis 6.5; Gibbons 1.14; Tadelis 6.3 (reading) | 1.5–2 h |
| 2 | Describing a dynamic game | Tadelis Ch. 7 p. 129–146; slides 41–58 | Tadelis 7.1, 7.2, 7.6, 7.4, 7.9, 7.10 | 2–2.5 h |
| 3 | Backward induction | Tadelis §8.1 p. 151–153; Gibbons §2.1.A p. 57–61; slides 59–64 | Muñoz-Garcia Ex. 3, 4, 9 | 1 h |
| 4 | Subgame perfection | Tadelis §8.2 p. 153–159; Gibbons §2.4 p. 115–129; slides 65–70 | Tadelis 8.5, 8.10, 8.11; MWG 9.B.4, 9.B.5 | 2.5–3 h |
| 5 | Continuous actions | Gibbons §2.1.A p. 57–61 | Gibbons 2.1 | 1 h |
