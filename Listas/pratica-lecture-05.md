---
tags: [lista, pratica, lecture-05, topic/repeated-games]
date: 2026-10-25
status: estimated
---

# Practice plan — Lecture 5 (Repeated games I: cooperation)

17 existing book exercises in one sequence of rising complexity, each reproduced verbatim under
its tier table (transcribed from the PDF page images on 2026-10-25). **Estimated unit:** the
lecture (Fri Nov 6) has no slides yet, so this plan follows the study guide's Lecture 5 block and
the books the slides will follow — Tadelis (2013) §10.1–10.3 and §10.6 (pp. 190–214) and Gibbons
(1992) §2.3.A–B (pp. 82–102) — instead of slide numbers. Reconcile when `Aula/Lecture05.pdf`
arrives. Other sources: Muñoz-Garcia & Toro-Gonzalez (2019), worked answers after every exercise;
Cabral (2017) §7.3; MWG (1995) App. A to Ch. 12. Class plan: [[Map/study-guide|study guide]];
book map: [[Map/books-index|books-index]]; notes: [[Notas/L05/L05-00-map|Lecture 5 notes]].

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise (items 6, 11, 13);
its Ch. 6 Ex. 7 (p. 299) is the same game as Gibbons 2.11 (item 8) and works it out. MWG
12.AA.1–12.AA.2: possibly in the MWG solutions manual (`Livros/`, not checked). Gibbons: an
unofficial, unfinished manual (`D:/Livros/Mercado/Economia/`, not copied). Tadelis: none in the
book. Cabral: none in the book.

**Verification.** Every page below was checked on 2026-10-25 against the rendered PDF page
(offsets in `Livros/book-registry.json`): Tadelis 10.2–10.9 on pp. 215–219; Gibbons 2.10–2.16 on
pp. 134–136; Muñoz-Garcia Ch. 6 Ex. 1 p. 274, Ex. 6 pp. 292–293, Ex. 9 p. 305; Cabral 7.8 p. 180,
7.12 p. 181, 7.13 p. 182 (its Figure 7.1 on p. 160); MWG 12.AA.1 p. 420, Prop. 12.AA.4 p. 421,
12.AA.2 p. 435.

**Not here on purpose — Lecture 6.** Tacit collusion, reputation and relational contracts:
Tadelis 10.1, 10.4, 10.6 (quality reputation, used in Lecture 6's list), 10.8, 10.10–10.12; Gibbons 2.13–2.15 (Bertrand/Cournot collusion) and 2.17
(efficiency wages); Muñoz-Garcia Ch. 6 Ex. 2–5 and 10; MWG 12.D.1–12.D.5 (oligopoly collusion);
Cabral 7.15 (a grim-strategy advertising agreement between firms). Muñoz-Garcia Ch. 6 Ex. 8
(three-player bargaining) is Lecture 4 material.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Finite repetition: unraveling, carrot and stick, definitions | 5 | 29% | Prop. 10.1 and the two-stage example are the lecture's first half; the definitions of strategy and subgame in a repeated game carry everything after |
| B2 | Infinite repetition: grim trigger, the critical discount factor, milder punishments | 7 | 41% | (10.3) and (10.5) are the lecture's one result to hold; densest in the books |
| B3 | One model, both horizons: finite vs infinite repetition of the same stage game | 2 | 12% | the comparison the lecture is built on, in an applied setting |
| B4 | Folk theorem: feasible and individually rational payoffs, Nash reversion | 3 | 18% | Theorem 10.1 and its formal side (MWG App. A to Ch. 12) |

| Level | Items | Count |
|---|---|---|
| Foundations (definitions, unraveling, grim trigger on a given matrix) | 1–6 | 6 |
| Exam (two-stage SPE with carrot and stick, length-$T$ punishments, continuous stage games, feasible sets) | 7–13 | 7 |
| Advanced (both horizons in one model with parameters, MWG proofs) | 14–17 | 4 |

---

## Tier 1 — Foundations

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 1 | B1 | Gibbons | §2.3, Problems | 2.12 | 135 | Defining strategy, subgame and SPE in a repeated game |
| 2 | B1 | Cabral | Ch. 7, Exercises | 7.8 | 180 | Why two stage equilibria let a twice-repeated game do new things (in words) |
| 3 | B1 | Cabral | Ch. 7, Exercises | 7.13 | 182 | Unraveling: the finitely repeated PD has a unique SPE |
| 4 | B2 | Tadelis | Ch. 10, Exercises | 10.2 | 215 | Grim trigger on a $3\times3$ PD variant; why two cooperative paths need different $\delta$ |
| 5 | B2 | Tadelis | Ch. 10, Exercises | 10.9 | 218–219 | Grim trigger with continuous quantities and externalities |
| 6 | B2 | Muñoz-Garcia | Ch. 6 | Ex. 1 | 274 | Temporary (one-, two-, ten-period) punishments vs grim trigger |

### Statements

#### 1. Gibbons 2.12

<!-- id: Gibbons 2.12 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.3 Problems, Problem 2.12, p. 135. Reproduced verbatim.

> 2.12. What is a strategy in a repeated game? What is a subgame in a repeated game? What is a subgame-perfect Nash equilibrium?

#### 2. Cabral 7.8

<!-- id: Cabral 7.8 -->
**Source.** Cabral (2017), *Introduction to Industrial Organization*, 2nd ed., Ch. 7 Exercises, Exercise 7.8 "Finitely repeated game", p. 180. Reproduced verbatim.

> **7.8. Finitely repeated game.** Consider a one-shot game with two equilibria and suppose this game is repeated twice. Explain in words why there may be equilibria in the two-period game which are different from the equilibria of the one-shot game.

#### 3. Cabral 7.13

<!-- id: Cabral 7.13 -->
**Source.** Cabral (2017), *Introduction to Industrial Organization*, 2nd ed., Ch. 7 Exercises, Exercise 7.13 "Finitely repeated game", p. 182. Reproduced verbatim; Figure 7.1 (p. 160), which the exercise refers to, is added below it.

> **7.13. Finitely repeated game.** Suppose that the game depicted in Figure 7.1 is repeated $T$ times, where $T$ is known. Show that the only subgame perfect equilibrium is for players to choose $(B, R)$ in every period.
>
> ![Cabral Figure 7.1, the "prisoner's dilemma" game: Player 1 chooses T or B, Player 2 chooses L or R; in each cell Player 1's payoff is lower left and Player 2's upper right: (T,L) = 5, 5; (T,R) = 3, 6; (B,L) = 6, 3; (B,R) = 4, 4](figures/cabral-7-1.png)
>
> *Figure 7.1* The "prisoner's dilemma" game (p. 160). In each cell, Player 1's payoff is in the lower left corner and Player 2's in the upper right corner.

#### 4. Tadelis 10.2

<!-- id: Tadelis 10.2 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 10.2 "Grim Trigger", p. 215. Reproduced verbatim.

> **Grim Trigger:** Consider the infinitely repeated game with discount factor $\delta < 1$ of the following variant of the Prisoner's Dilemma:
>
> | Player 1 \ Player 2 | $L$ | $C$ | $R$ |
> |:---:|:---:|:---:|:---:|
> | $T$ | 6, 6 | −1, 7 | −2, 8 |
> | $M$ | 7, −1 | 4, 4 | −1, 5 |
> | $B$ | 8, −2 | 5, −1 | 0, 0 |
>
> a. For which values of the discount factor $\delta$ can the players support the pair of actions $(M, C)$ played in every period?
>
> b. For which values of the discount factor $\delta$ can the players support the pair of actions $(T, L)$ played in every period? Why is your answer different from that for (a)?

#### 5. Tadelis 10.9

<!-- id: Tadelis 10.9 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 10.9 "Negative Externalities", pp. 218–219. Reproduced verbatim.

> **Negative Externalities:** Two firms are located adjacent to one another, and each imposes an external cost on the other: the detergent that firm 1 uses in its laundry business makes the fish that firm 2 catches in the lake taste funny, and the smoke that firm 2 uses to smoke its caught fish makes the clothes that firm 1 hangs out to dry smell funny. As a consequence each firm's profits are increasing in its own production and decreasing in the production of its neighbor. In particular if $q_1$ and $q_2$ are the firms' production levels then their per-period (stage-game) profits are given by $v_1(q_1, q_2) = (30 - q_2)q_1 - q_1^2$ and $v_2(q_1, q_2) = (30 - q_1)q_2 - q_2^2$.
>
> a. Draw the firms' best-response functions and find the Nash equilibrium of the stage-game. How does this compare to the Pareto-optimal stage-game profit levels?
>
> b. For which levels of discount factors can the firms support the Pareto-optimal level of quantities in an infinitely repeated game?

#### 6. Muñoz-Garcia Ex. 1

<!-- id: Muñoz-Garcia Ch. 6 Ex. 1 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 6, Exercise 1 "Infinitely Repeated Prisoner's Dilemma Game", p. 274. Reproduced verbatim (statement only; the book's worked answer follows it).

> Consider the infinitely repeated version of the following prisoner's dilemma game, where C denotes confess and NC represents not confess (Table 6.1):
>
> **Part (a)** Can players support the cooperative outcome (NC, NC) as a SPNE by using tit-for-tat strategies, whereby players punish deviations from NC in a past period by reverting to the stage-game Nash equilibrium where they both confess (C, C) for just one period, and then returning to cooperation?
>
> **Part (b)** Consider now that players play tit-for-tat, but reverting to the stage-game Nash equilibrium where they both confess (C, C) for two periods, and then players return to cooperation. Can the cooperative outcome (NC, NC) be supported as a SPNE?
>
> **Part (c)** Suppose that players use strategies that punish deviation from cooperation by reverting to the stage-game Nash equilibrium for ten periods before returning to cooperation. Compute the threshold discount factor, $\delta$, above which cooperation can be sustained as a SPNE of the infinitely repeated game.
>
> | Player 1 \ Player 2 | C | NC |
> |---|---|---|
> | C | 2, 2 | 6, 0 |
> | NC | 0, 6 | 3, 3 |
>
> *Table 6.1* Prisoner's dilemma game


## Tier 2 — Exam level

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 7 | B1 | Gibbons | §2.3, Problems | 2.10 | 134 | A two-stage SPE with player-specific punishments; solving for the parameter that sustains it |
| 8 | B1 | Gibbons | §2.3, Problems | 2.11 | 135 | Can a non-Nash first-stage payoff be reached? Building (or ruling out) carrot and stick |
| 9 | B2 | Tadelis | Ch. 10, Exercises | 10.3 | 215–216 | Length-$T$ punishments: the critical $\delta_T$ and why it falls with $T$ |
| 10 | B2 | Cabral | Ch. 7, Exercises | 7.12 | 181 | The best symmetric equilibrium at a given $\delta$, and with front-loaded payoffs |
| 11 | B2 | Muñoz-Garcia | Ch. 6 | Ex. 6 | 292–293 | Grim trigger in a continuous public-good game: Nash vs social optimum vs deviation |
| 12 | B2 | Tadelis | Ch. 10, Exercises | 10.5 | 216–217 | Grim trigger with continuous actions; how tightening the action set changes the threshold |
| 13 | B4 | Muñoz-Garcia | Ch. 6 | Ex. 9 | 305 | Drawing the feasible set and its individually rational part; $\delta$ for a target path |

### Statements

#### 7. Gibbons 2.10

<!-- id: Gibbons 2.10 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.3 Problems, Problem 2.10, p. 134. Reproduced verbatim.

> 2.10. The accompanying simultaneous-move game is played twice, with the outcome of the first stage observed before the second stage begins. There is no discounting. The variable $x$ is greater than 4, so that $(4,4)$ is not an equilibrium payoff in the one-shot game. For what values of $x$ is the following strategy (played by both players) a subgame-perfect Nash equilibrium?
>
> > Play $Q_i$ in the first stage. If the first-stage outcome is $(Q_1, Q_2)$, play $P_i$ in the second stage. If the first-stage outcome is $(y, Q_2)$ where $y \neq Q_1$, play $R_i$ in the second stage. If the first-stage outcome is $(Q_1, z)$ where $z \neq Q_2$, play $S_i$ in the second stage. If the first-stage outcome is $(y, z)$ where $y \neq Q_1$ and $z \neq Q_2$, play $P_i$ in the second stage.
>
> |   | $P_2$ | $Q_2$ | $R_2$ | $S_2$ |
> |---|---|---|---|---|
> | $P_1$ | 2, 2 | $x$, 0 | −1, 0 | 0, 0 |
> | $Q_1$ | 0, $x$ | 4, 4 | −1, 0 | 0, 0 |
> | $R_1$ | 0, 0 | 0, 0 | 0, 2 | 0, 0 |
> | $S_1$ | 0, −1 | 0, −1 | −1, −1 | 2, 0 |

#### 8. Gibbons 2.11

<!-- id: Gibbons 2.11 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.3 Problems, Problem 2.11, p. 135. Reproduced verbatim. (The same game is Muñoz-Garcia & Toro-Gonzalez Ch. 6 Ex. 7, p. 299, with a worked answer.)

> 2.11. The simultaneous-move game (below) is played twice, with the outcome of the first stage observed before the second stage begins. There is no discounting. Can the payoff $(4,4)$ be achieved in the first stage in a pure-strategy subgame-perfect Nash equilibrium? If so, give strategies that do so. If not, prove why not.
>
> |   | $L$ | $C$ | $R$ |
> |---|---|---|---|
> | $T$ | 3, 1 | 0, 0 | 5, 0 |
> | $M$ | 2, 1 | 1, 2 | 3, 1 |
> | $B$ | 1, 2 | 0, 1 | 4, 4 |

#### 9. Tadelis 10.3

<!-- id: Tadelis 10.3 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 10.3 "Not-So-Grim Trigger", pp. 215–216, with its footnote 12 (p. 216). Reproduced verbatim. (Here $T$ is the length of the punishment, not a payoff.)

> **Not-So-Grim Trigger:** Consider the infinitely repeated Prisoner's Dilemma with discount factor $\delta < 1$ described by the following matrix:
>
> | Player 1 \ Player 2 | $m$ | $f$ |
> |:---:|:---:|:---:|
> | $M$ | 4, 4 | −1, 5 |
> | $F$ | 5, −1 | 1, 1 |
>
> Instead of using grim-trigger strategies to support a pair of actions $(a_1, a_2)$ other than $(F, f)$ as a subgame-perfect equilibrium, assume that the players wish to choose a less draconian punishment called a "length-$T$ punishment" strategy. If there is a deviation from $(a_1, a_2)$ then the players will play $(F, f)$ for $T$ periods and then resume playing $(a_1, a_2)$. Let $\delta_T$ be the critical discount factor so that if $\delta > \delta_T$ then the adequately defined strategies will implement the desired path of play with length-$T$ punishment as the threat.
>
> a. Let $T = 1$. What is the critical value $\delta_1$ to support the pair of actions $(M, m)$ played in every period?
>
> b. Let $T = 2$. What is the critical value $\delta_T$ to support the pair of actions $(M, m)$ played in every period?¹²
>
> c. Compare the two critical values in (a) and (b). How do they differ and what is the intuition for this?
>
> ¹² Hint: You should encounter an equation of the form $a\delta^3 - (a + 1)\delta + 1 = 0$, for which it is easy to see that $\delta = 1$ is a root. In this case you know that the equation can be written in the form $(\delta - 1)(a\delta^2 + a\delta - 1) = 0$, and you can solve for the other relevant root of the cubic equation.

#### 10. Cabral 7.12

<!-- id: Cabral 7.12 -->
**Source.** Cabral (2017), *Introduction to Industrial Organization*, 2nd ed., Ch. 7 Challenging exercises, Exercise 7.12 "Ad games", p. 181. Reproduced verbatim.

> **7.12. Ad games.** Two firms must simultaneously choose their advertising budget; their options are $H$ or $L$. Payoffs are as follows: if both choose $H$, then each gets 5; if both choose $L$, then each gets 4; if firm 1 chooses $H$ and firm 2 chooses $L$, then firm 1 gets 8 and firm 2 gets 1; conversely, if firm 2 chooses $H$ and firm 1 chooses $L$, then firm 2 gets 8 and firm 1 gets 1.
>
> (a) Determine the Nash equilibria of the one-shot game.
>
> (b) Suppose the game is indefinitely repeated and that the relevant discount factor is $\delta = .8$. Determine the optimal symmetric equilibrium.
>
> (c) (challenge question) Now suppose that, for the first 10 periods, firm payoffs are twice the values represented in the above table. What is the optimal symmetric equilibrium?

#### 11. Muñoz-Garcia Ex. 6

<!-- id: Muñoz-Garcia Ch. 6 Ex. 6 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 6, Exercise 6 "Collusion in Donations in an Infinitely Repeated Public Good Game", pp. 292–293. Reproduced verbatim (statement only; the book's worked answer follows it; "Grim-Triger" is the book's spelling).

> Consider a public good game between two players, A and B. The utility function of every player $i = \{A, B\}$ is
>
> $$u_i(g_i) = (w - g_i)^{1/2}\left[m\left(g_i + g_j\right)\right]^{1/2}$$
>
> where the first term, $w - g_i$, represents the utility that the player receives from money (i.e., the amount of his wealth, $w$, not contributed to the public good). The second term indicates the utility he obtains from aggregate contributions to the public good, $g_i + g_j$, where $m \geq 0$ denotes the return from aggregate contributions. For simplicity, assume that both players have equal wealth levels $w$.
>
> (a) Find every player $i$'s best response function, $g_i(g_j)$. Interpret.
>
> (b) Find the Nash Equilibrium of this game, $g^*$.
>
> (c) Find the socially optimal contribution level, $g^{SO}$, that is, the donation that each player should contribute to maximize their joint utilities. Compare it with the Nash equilibrium of the game. Which of them yields the highest utility for every player $i$?
>
> (d) Consider the infinitely repeated version of the game. Show under which values of players' discount factor $\delta$ you can sustain cooperation, where cooperation is understood as contributing the socially optimal amount (the one that maximizes joint utilities) you found in part (c). For simplicity, you can consider a "Grim-Triger strategy" where every player starts cooperating (that is, donating $g^{SO}$ to the public good), and continues to do so if both players cooperated in all previous periods. However, if one or both players deviate from $g^{SO}$, he reverts to the Nash equilibrium of the unrepeated game, $g^*$, thereafter.

#### 12. Tadelis 10.5

<!-- id: Tadelis 10.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 10.5 "Negative Ad Campaigns Revisited", pp. 216–217. Reproduced verbatim.

> **Negative Ad Campaigns Revisited:** Recall exercise 5.14 from Chapter 5, in which each one of two political parties can choose to buy time on commercial radio shows to broadcast negative ad campaigns against its rival. These choices are made simultaneously. Government regulations forbid a party from buying more than 2 hours of negative campaign time, so that each party cannot choose an amount of negative campaigning above 2 hours. Given a pair of choices $(a_1, a_2)$, the payoff of party $i$ is given by the following function: $v_i(a_1, a_2) = a_i - 2a_j + a_i a_j - (a_i)^2$.
>
> a. Find the unique pure-strategy Nash equilibrium of the one-shot game.
>
> b. If the parties could sign a binding agreement on how much to campaign, what levels would they choose?
>
> c. Now assume that this game is repeated infinitely often, and the foregoing demonstrates the choices and payoffs per period. For which discount factors $\delta \in (0, 1)$ can the levels you found in (b) be supported as a subgame-perfect equilibrium of the infinitely repeated game?
>
> d. Despite the parties' ability to coordinate, as you have demonstrated in your answer to (c), the government is concerned about the parties' ability to run up to 2 hours a day of negative campaigning, and it is considering limiting negative campaigning to $\frac{1}{2}$ hour a day, so that now $a_i \in [0, \frac{1}{2}]$. Is this a good policy to limit negative campaigns further? Justify your answer with the relevant calculations. What is the intuition for your conclusion?

#### 13. Muñoz-Garcia Ex. 9

<!-- id: Muñoz-Garcia Ch. 6 Ex. 9 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 6, Exercise 9 "Representing Feasible, Individually Rational Payoffs", p. 305. Reproduced verbatim (statement only; the book's worked answer follows it).

> Consider an infinitely-repeated game where the stage game is depicted Table 6.6. Player 1 chooses rows and player 2 chooses columns. Players discount the future using a common discount factor $\delta$.
>
> **Part (a)** What outcomes in the stage-game are consistent with Nash equilibrium play?
>
> **Part (b)** Let $v_1$ and $v_2$ be the repeated game payoffs to player 1 and player 2 respectively. Draw the set of feasible payoffs from the repeated game, explaining any normalization you use.
>
> **Part (c)** Find the set of individually rational feasible set of payoffs.
>
> **Part (d)** Find a Nash equilibrium in which the players obtain (9, 9) each period. What restrictions on $\delta$ are necessary?
>
> | Player 1 \ Player 2 | $L$ | $R$ |
> |---|---|---|
> | $U$ | 9, 9 | 1, 10 |
> | $D$ | 10, 1 | 7, 7 |
>
> *Table 6.6* Simultaneous-move game

## Tier 3 — Advanced

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 14 | B3 | Tadelis | Ch. 10, Exercises | 10.7 | 217–218 | One stage game over 10 days and forever: price range and $\delta$ range in parameters |
| 15 | B3 | Gibbons | §2.3, Problems | 2.16 | 136 | Conditions for a Pareto-superior repeated-game outcome under Nash reversion (union–firm) |
| 16 | B4 | MWG | App. A to Ch. 12 | 12.AA.1 | 420 | Why Nash reversion cannot sustain a path below the stage Nash payoff |
| 17 | B4 | MWG | Ch. 12, Exercises | 12.AA.2 | 435 | Punishments harsher than Nash reversion: proving Prop. 12.AA.4 |

### Statements

#### 14. Tadelis 10.7

<!-- id: Tadelis 10.7 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 10.7 "Diluted Happiness", pp. 217–218. Reproduced verbatim.

> **Diluted Happiness:** Consider a relationship between a bartender and a customer. The bartender serves bourbon to the customer and chooses $x \in [0, 1]$, which is the proportion of bourbon in the drink served, while $1 - x$ is the proportion of water. The cost of supplying such a drink (standard 4-ounce glass) is $cx$, where $c > 0$. The customer, without knowing $x$, decides on whether or not to buy the drink at the market price $p$. If he buys the drink his payoff is $vx - p$, and the bartender's payoff is $p - cx$. Assume that $v > c$ and all payoffs are common knowledge. If the customer does not buy the drink he gets 0 and the bartender gets $-cx$. Because the customer has some experience, once the drink is bought and he tastes it, he learns the value of $x$, but this is only after he pays for the drink.
>
> a. Find all the Nash equilibria of this game.
>
> b. Now assume that the customer is visiting town for 10 days, and this "bar game" will be played on each of the 10 evenings that the customer is in town. Assume that each player tries to maximize the (nondiscounted) sum of his stage payoffs. Find all the subgame-perfect equilibria of this game.
>
> c. Now assume that the customer is a local, and the players perceive the game as repeated infinitely many times. Assume that each player tries to maximize the discounted sum of his stage payoffs, where the discount rate is $\delta \in (0, 1)$. What is the range of prices $p$ (expressed in the parameters of the problem) for which there exists a subgame-perfect equilibrium in which every day the bartender chooses $x = 1$ and the customer buys at the price $p$?
>
> d. For which values of $\delta$ (expressed in the parameters of the problem) can the price range that you found in (c) exist?

#### 15. Gibbons 2.16

<!-- id: Gibbons 2.16 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §2.3 Problems, Problem 2.16, p. 136. Reproduced verbatim. (The one-shot model it builds on is Gibbons §2.1.C, pp. 64–68: the union sets the wage, then the firm sets employment.)

> 2.16. In the model of wages and employment analyzed in Section 2.1.C, the backwards-induction outcome is not socially efficient. In practice, however, a firm and a union negotiate today over the terms of a three-year contract, then negotiate three years from today over the terms of a second contract, and so on. Thus, the relationship may be more accurately characterized as a repeated game, as in Espinosa and Rhee (1989).
>
> This problem derives conditions under which a subgame-perfect Nash equilibrium in the infinitely repeated game is Pareto-superior to the backwards-induction outcome of the one-shot game. Denote the union's utility and the firm's profit in the backwards-induction outcome of the one-shot game by $U^*$ and $\pi^*$, respectively. Consider an alternative utility-profit pair $(U, \pi)$ associated with an alternative wage-employment pair $(w, L)$. Suppose that the parties share the discount factor $\delta$ (per three-year period). Derive conditions on $(w, L)$ such that (1) $(U, \pi)$ Pareto-dominates $(U^*, \pi^*)$ and (2) $(U, \pi)$ is the outcome of a subgame-perfect Nash equilibrium of the infinitely repeated game, where $(U^*, \pi^*)$ is played forever following a deviation.

#### 16. MWG 12.AA.1

<!-- id: MWG 12.AA.1 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Appendix A to Ch. 12 "Infinitely Repeated Games and the Folk Theorem", Exercise 12.AA.1^A (in text), p. 420. Reproduced verbatim. (Context, not in the exercise: the stage game is a duopoly in which firm $i$ chooses $q_i$ and earns $\pi_i(q_1, q_2)$; $q^* = (q_1^*, q_2^*)$ is its Nash equilibrium; Nash reversion, Definition 12.AA.1 on p. 418, plays a prescribed outcome path until someone deviates and $q^*$ forever after.)

> **Exercise 12.AA.1:** Argue that no pair of actions $q$ such that $\pi_i(q_1, q_2) < \pi_i(q_1^*, q_2^*)$ for some $i$ can be sustained as a stationary SPNE outcome path using Nash reversion.

#### 17. MWG 12.AA.2

<!-- id: MWG 12.AA.2 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 12 Exercises, Exercise 12.AA.2^C, p. 435. Reproduced verbatim. **Added (not in the exercise):** the statement of Proposition 12.AA.4 and the definition of the minimax payoff it uses, both reproduced verbatim from p. 421, so the item can be worked without the book.

> **12.AA.2^C** Prove Proposition 12.AA.4. [*Hint:* Consider a strategy profile of the following form: the players are to play an outcome path involving some pair $(q_1, q_2)$ in period 1 and $(q_1^*, q_2^*)$ in every period thereafter. If either player deviates, this outcome path is restarted.]
>
> *Added from p. 421.* To consider this issue, it is useful to let $\underline{\pi}_i = \operatorname{Min}_{q_j}\left[\operatorname{Max}_{q_i} \pi_i(q_i, q_j)\right]$ denote player $i$'s *minimax payoff*.
>
> **Proposition 12.AA.4:** Consider an infinitely repeated game with $\delta > 0$ and $S_i \subset \mathbb{R}$ for $i = 1, 2$. Suppose also that $\pi_i(q)$ is differentiable at $q^* = (q_1^*, q_2^*)$, with $\partial \pi_i(q_i^*, q_j^*)/\partial q_j \neq 0$ for $j \neq i$ and $i = 1, 2$, and that $\pi_i(q_1^*, q_2^*) > \underline{\pi}_i$ for $i = 1, 2$. Then there is some SPNE with discounted payoffs to the two players of $(v_1', v_2')$ such that $(1 - \delta)v_i' < \pi_i(q_1^*, q_2^*)$ for $i = 1, 2$.


**Optional extras.**
- Muñoz-Garcia Ch. 6 Ex. 7 (p. 299): the game of item 8 with a full worked answer — check item 8 against it.
- Tadelis 10.12 (p. 219): the folk theorem on the trust game, after Lecture 6 introduces that game.
- Cabral 7.15 (p. 182): grim strategies on an advertising agreement, as a bridge to Lecture 6's collusion.

---

## Suggested study order

1. **Finite repetition.** Read Tadelis §10.1 (pp. 190–192) and Gibbons §2.3.A (pp. 82–88), then do items **1–3**, then **7, 8**.
2. **Grim trigger.** Read Tadelis §10.2–10.3 (pp. 192–201) and Gibbons §2.3.B (pp. 88–96), then do **4, 6**, then **9** (compare its thresholds with item 6).
3. **Continuous stage games.** Do **5, 11, 12**, then **10**.
4. **Folk theorem.** Read Tadelis §10.6 (pp. 209–214) and Gibbons pp. 96–102, then do **13**.
5. **Both horizons in one model.** Do **14** — it asks for the ten-times repeated game and the infinitely repeated one; contrast the two answers.
6. **Advanced.** Read MWG App. A to Ch. 12 (pp. 417–422). Do **15**, then **16**, and **17** last.

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Finitely repeated games; Prop. 10.1; the two-stage carrot-and-stick example | Ch. 10, §10.1 | p. 190–192 | Foundations |
| Infinitely repeated games: discounting, average payoffs, histories and strategies | Ch. 10, §10.2 | p. 192–196 | Foundations |
| Subgame-perfect equilibria; grim trigger; (10.3); one-stage deviation principle | Ch. 10, §10.3 | p. 196–201 | Exam |
| The folk theorem: feasible payoffs, Theorem 10.1, the alternating path | Ch. 10, §10.6 | p. 209–214 | Exam |
| Exercises 10.2, 10.3, 10.5, 10.7, 10.9 | Ch. 10, Exercises | p. 215–219 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Two-stage repeated games; carrot and stick; renegotiation | §2.3.A | p. 82–88 | Foundations |
| Infinitely repeated games; trigger strategies; Friedman's theorem | §2.3.B | p. 88–102 | Exam |
| Problems 2.10, 2.11, 2.12, 2.16 | §2.3, Problems | p. 134–136 | Exam |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Repeated games: exercises with worked answers | Ch. 6, Ex. 1, 6, 9 | p. 274–278, 292–299, 305–310 | Foundations |

### Cabral — Cabral (2017)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Repeated games: the indefinitely repeated PD | §7.3 | p. 172–174 | Foundations |
| Exercises 7.8, 7.12, 7.13 | Ch. 7, Exercises | p. 180–182 | Foundations |

### MWG — Mas-Colell, Whinston & Green (1995)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Finitely repeated Bertrand (unraveling) | §12.D | p. 400–401 | Advanced |
| Infinitely repeated games and the folk theorem; Nash reversion; minimax payoffs | App. A to Ch. 12 | p. 417–422 | Advanced |
| Exercises 12.AA.1, 12.AA.2 | App. A to Ch. 12; Ch. 12 Exercises | p. 420, 435 | Advanced |

## Consolidated Exercises

| # | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 1 | 10.2 | Tadelis | p. 215 | Grim trigger on a $3\times3$ PD variant | Foundations |
| 2 | 10.3 | Tadelis | p. 215–216 | Length-$T$ punishments | Exam |
| 3 | 10.5 | Tadelis | p. 216–217 | Grim trigger, continuous actions, regulation | Exam |
| 4 | 10.7 | Tadelis | p. 217–218 | Quality: ten days vs forever, in parameters | Advanced |
| 5 | 10.9 | Tadelis | p. 218–219 | Grim trigger with externalities | Foundations |
| 6 | 2.10 | Gibbons | p. 134 | Two-stage SPE, player-specific punishments | Exam |
| 7 | 2.11 | Gibbons | p. 135 | Non-Nash first stage in a two-stage game | Exam |
| 8 | 2.12 | Gibbons | p. 135 | Strategy, subgame, SPE in a repeated game | Foundations |
| 9 | 2.16 | Gibbons | p. 136 | Pareto-superior repeated outcome, union–firm | Advanced |
| 10 | Ex. 1 | Muñoz-Garcia | p. 274 | Temporary punishments | Foundations |
| 11 | Ex. 6 | Muñoz-Garcia | p. 292–293 | Grim trigger in a public-good game | Exam |
| 12 | Ex. 9 | Muñoz-Garcia | p. 305 | Feasible and individually rational payoffs | Exam |
| 13 | 7.8 | Cabral | p. 180 | Two stage equilibria, two periods (in words) | Foundations |
| 14 | 7.12 | Cabral | p. 181 | Best symmetric equilibrium at given $\delta$ | Exam |
| 15 | 7.13 | Cabral | p. 182 | Finitely repeated PD unravels | Foundations |
| 16 | 12.AA.1 | MWG | p. 420 | Limits of Nash reversion | Advanced |
| 17 | 12.AA.2 | MWG | p. 435 | Punishments harsher than Nash reversion | Advanced |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Finite repetition | Tadelis §10.1 p. 190–192; Gibbons §2.3.A p. 82–88 | Gibbons 2.12, 2.10, 2.11; Cabral 7.8, 7.13 | 2 h |
| 2 | Grim trigger and the critical discount factor | Tadelis §10.2–10.3 p. 192–201; Gibbons §2.3.B p. 88–96 | Tadelis 10.2, 10.3, 10.9; Muñoz-Garcia Ex. 1 | 2–2.5 h |
| 3 | Continuous stage games | Tadelis §10.3 p. 196–201 | Tadelis 10.5; Muñoz-Garcia Ex. 6; Cabral 7.12 | 1.5–2 h |
| 4 | Folk theorem | Tadelis §10.6 p. 209–214; Gibbons p. 96–102 | Muñoz-Garcia Ex. 9 | 1 h |
| 4 | Both horizons in one model | Tadelis §10.1–10.3 | Tadelis 10.7 | 1 h |
| 5 | Advanced | MWG App. A to Ch. 12 p. 417–422 | Gibbons 2.16; MWG 12.AA.1, 12.AA.2 | 2 h |
