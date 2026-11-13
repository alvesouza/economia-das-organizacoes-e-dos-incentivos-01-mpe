---
tags: [lista, pratica, lecture-07, topic/bayesian-games, topic/adverse-selection, topic/auctions]
date: 2026-11-12
status: estimated
---

# Practice plan — Lecture 7 (Bayesian games, adverse selection and auctions)

24 existing book exercises in one sequence of rising complexity, each reproduced verbatim under
its tier table (transcribed from the PDF text layers and checked against the rendered page
images on 2026-10-25). Sources: Tadelis (2013) Ch. 12–13, the book the lectures follow;
Gibbons (1992) Ch. 3; Muñoz-Garcia & Toro-Gonzalez (2019) Ch. 7–8, worked answers after every
exercise; MWG (1995) §13.B. Class plan: [[Map/study-guide|study guide]]; book map:
[[Map/books-index|books-index]]; notes: [[Notas/L07/L07-00-map|Lecture 7 notes]].

**Re-checked on 2026-11-12** when the lists were re-aligned to the real Lectures 1–5. The real
lectures run about half a lecture behind the estimate, so this unit may shift once its slides
arrive. The 24 items, their order and the three tiers were re-checked and kept unchanged (moved
here from the old Lecture 7 list: items 1–24, same numbers). Worked solutions to all 24 items:
`Listas/pratica-lecture-07-solutions.pdf` (sources in `Listas/pratica-lecture-07-solutions/`).

**Estimated unit.** There are no Lecture 7 slides yet (the lecture is on Tue Nov 17 2026). The
selection follows the study guide's Lecture 7 block and the estimated notes in `Notas/L07/`;
every reference points to the books, not to slides. Re-check the weighting when
`Aula/Lecture07.pdf` arrives.

**Answers in the books.** Muñoz-Garcia: a worked answer follows each exercise. MWG 13.B.1: in
the MWG solutions manual (`Livros/`, Figures 13.B.1(a)–(c)); 13.B.2 was not found in the
manual's OCR text. Gibbons: no official answers. Tadelis: none in the book; the preface (p. xiii)
says about half are solved on Princeton UP's website (not checked). No solutions file for this
list yet.

**Verification.** Printed pages, with the PDF viewer page (1-based) in brackets, from `Livros/book-registry.json` (Tadelis offset 18; Gibbons Ch. 3–4
offset 5; Muñoz-Garcia Ch. 6–7 offset 10, Ch. 8 offset 9; MWG 2-up, `(printed + 20) // 2`).
Every statement below was read off the rendered page: Tadelis pp. 266–269 and 285–287; Gibbons
pp. 169–172; Muñoz-Garcia pp. 318–319, 350, 362; MWG p. 473.

**Not here on purpose.** Mechanism design is out of scope (CLAUDE.md): Gibbons §3.3 (the
Revelation Principle) has no problems of its own, and Tadelis Ch. 14 is skipped. Signaling and
perfect Bayesian equilibrium are Lecture 8 (Muñoz-Garcia Ch. 9–11, MWG 13.C). Tadelis 13.4
(optimal reserve price, continuous types) and 13.7 (risk-averse bidders) are left as optional
extras: the first is the mechanism-design result in disguise, the second needs more calculus
than the lecture uses.

## Weighting

| Block | Subtopic | Items | Weight | Why |
|---|---|---|---|---|
| B1 | Bayesian games: types, the Bayesian normal form, BNE in finite games | 5 | 21% | the machinery every later item uses; Tadelis §12.1–12.2.1 and Gibbons §3.1 |
| B2 | BNE with continuous actions or types: Cournot, Bertrand, thresholds, purification | 3 | 12% | the FOC and cutoff versions of the same condition (Gibbons §3.1.A, Tadelis §12.2.2, §12.5) |
| B3 | Adverse selection and inefficient trade: lemons, unravelling, double auction | 6 | 25% | the lecture's economic core (Tadelis §12.3, MWG §13.B, Gibbons §3.2.C) and the M&R applications |
| B4 | Auctions with independent private values: second-price, first-price, revenue | 8 | 34% | the lecture's second half (Tadelis §13.1, Gibbons §3.2.B); densest in all four books |
| B5 | Common values: swing voter's curse, winner's curse | 2 | 8% | the lecture's closing idea (Tadelis §12.4, §13.2); few clean book exercises |

| Level | Items | Count |
|---|---|---|
| Foundations (definitions, a Bayesian normal form, second- and first-price auctions with two bidders) | 1–8 | 8 |
| Exam (FOCs with private costs, threshold equilibria, lemons markets, $n$-bidder and linear bidding, reserve prices, jury voting) | 9–18 | 10 |
| Advanced (MWG's competitive adverse selection, two-sided private information, mixed bids, common-value bidding) | 19–24 | 6 |

---

## Tier 1 — Foundations

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 1 | B1 | Gibbons | §3.5, Problems (Section 3.1) | 3.1 | 169 | The three definitions: static Bayesian game, strategy, Bayesian Nash equilibrium |
| 2 | B1 | Muñoz-Garcia | Ch. 7 | Ex. 1 | 318–319 | Complete-information benchmark, then the Bayesian normal form and its BNE |
| 3 | B1 | Gibbons | §3.5, Problems (Section 3.1) | 3.4 | 169–170 | All pure-strategy BNE when one player knows which game was drawn |
| 4 | B1 | Tadelis | §12.7, Exercises | 12.1 | 266 | Re-solving chicken with private types under two payoff stories |
| 5 | B4 | Tadelis | §13.4, Exercises | 13.1 | 285 | Second-price auction: bidding above value is weakly dominated |
| 6 | B4 | Muñoz-Garcia | Ch. 8 | Ex. 4 | 362 | Truthful bidding in the second-price auction, and what it does not depend on |
| 7 | B4 | Muñoz-Garcia | Ch. 8 | Ex. 1 | 350 | First-price auction, two uniform bidders: the expected-utility problem and the bid $v_i/2$ |
| 8 | B4 | Tadelis | §13.4, Exercises | 13.2 | 285 | Second-price auction under complete information: dominance and other Nash equilibria |

### Statements

#### 1. Gibbons 3.1

<!-- id: Gibbons 3.1 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §3.5 Problems, Section 3.1, Problem 3.1, p. 169 [PDF p. 175]. Reproduced verbatim. **Answer in the source:** no.

> **3.1.** What is a static Bayesian game? What is a (pure) strategy in such a game? What is a (pure-strategy) Bayesian Nash equilibrium in such a game?

#### 2. Muñoz-Garcia Ch. 7 Ex. 1

<!-- id: Muñoz-Garcia Ch. 7 Ex. 1 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 7, Exercise 1 "A Simple Bayesian Game", pp. 318–319 [PDF pp. 329–330]. Reproduced verbatim (statement only; the book's worked answer follows it). **Answer in the source:** yes, the book's worked answer follows the exercise.

> Consider the payoff matrix in Fig. 7.1, where player 1 (in rows) chooses between $A$ and $B$, and player 2 (in columns) selects $C$ or $D$. Player 1 observes the realization of random variable $x$, which takes value $x = 15$ with probability 1/2 or $x = 4$ with probability 1/2. Player 2, however, doesn't observe the realization of $x$, but knows its probability distribution. Therefore, player 1 is perfectly informed about the payoff matrix they face, while player 2 does not know the payoff that player 1 earns in strategy profile $(A, C)$. While this payoff only affects player 1, player 2's behavior is affected by this uncertainty since he could anticipate that player 1 best responds to column $C$ with $A$ when $x = 15$, but player 1 would best respond with $B$ when $x = 4$.
>
> | Player 1 \ Player 2 | *C* | *D* |
> |---|---|---|
> | *A* | $x$, 18 | 6, 7 |
> | *B* | 8, 0 | 8, 11 |
>
> *Fig. 7.1* Simultaneous-move game under asymmetric information about $x$
>
> (a) *Complete information*. As a benchmark, let us assume in this part of the exercise that both players are informed about the realization of $x$. Which are the pure strategy Nash equilibria of the game when $x = 15$? And what are the pure strategy Nash equilibria when $x = 4$?
>
> (b) *Incomplete information*. Let us now return to the game where only player 1 privately observes the realization of $x$. Find the Bayesian Nash Equilibrium of this incomplete information game by following the next three steps:
>
> 1. Identify each player's strategy space in this incomplete information setting,
> 2. Construct the Bayesian normal form representation, and
> 3. Underline each player's best response payoffs to find the BNE of the game.

#### 3. Gibbons 3.4

<!-- id: Gibbons 3.4 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §3.5 Problems, Section 3.1, Problem 3.4, pp. 169–170 [PDF pp. 175–176]. Reproduced verbatim. **Answer in the source:** no.

> **3.4.** Find all the pure-strategy Bayesian Nash equilibria in the following static Bayesian game:
>
> 1. Nature determines whether the payoffs are as in Game 1 or as in Game 2, each game being equally likely.
> 2. Player 1 learns whether nature has drawn Game 1 or Game 2, but player 2 does not.
> 3. Player 1 chooses either $T$ or $B$; player 2 simultaneously chooses either $L$ or $R$.
> 4. Payoffs are given by the game drawn by nature.
>
> | Game 1 | $L$ | $R$ |
> |---|---|---|
> | $T$ | 1, 1 | 0, 0 |
> | $B$ | 0, 0 | 0, 0 |
>
> | Game 2 | $L$ | $R$ |
> |---|---|---|
> | $T$ | 0, 0 | 0, 0 |
> | $B$ | 0, 0 | 2, 2 |

#### 4. Tadelis 12.1

<!-- id: Tadelis 12.1 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.1 "Chicken Revisited", p. 266 [PDF p. 285]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Chicken Revisited:** Consider the game of chicken in Section 12.2.1 with the parameters $R = 8$, $H = 16$, and $L = 0$ as described there. A preacher, who knows some game theory, decides to use this model to claim that moving to a society in which all parents are lenient will have detrimental effects on the behavior of teenagers. Does equilibrium analysis support this claim? What if $R = 8$, $H = 0$, and $L = 16$?

**Referred to in the statement.** The game of chicken of Section 12.2.1 (Tadelis pp. 252–254 [PDF p. 271–273]) (reproduced from the book; Figure 12.3, the game tree, is replaced by the matrix the book derives from it):

> Two teenagers, players 1 and 2, have borrowed their parents' cars and decided to play the game of chicken as follows: They drive toward each other in the middle of a street, and just before impact they must simultaneously choose whether to be chicken and swerve to the right, or continue driving head on. If both are chicken then both gain no respect from their friends but suffer no losses; thus both get a payoff of 0. If $i$ continues to drive while $j \neq i$ plays chicken then $i$ gains all the respect, which is a payoff of $R$, and $j$ gets no respect, which is worth 0. In this case both players suffer no additional losses. Finally if both continue to drive head on then they split the respect (because respect is considered to be relative), but an accident is bound to happen and they will at least be reprimanded by their parents, if not seriously injured. An accident imposes a personal loss of $k$ on each player, so the payoff to each one is $\frac{R}{2} - k$.
>
> There is, however, a potential difference between these two youngsters: The punishment, $k$, depends on the type of parents they have. For each kid, parents can be either harsh ($H$) or lenient ($L$) with equal probability, and the draws from Nature on the types of parents are independently distributed. This means that the likelihood that player $i$'s parents are harsh is equal to $\frac{1}{2}$ and is independent of the type of parents that player $j$ has. If player $i$'s parents are harsh then they will beat the living daylights out of their child, which imposes a high cost of an accident, denoted by $k = H$. If instead the parents are lenient then they will give their child a long lecture on why his behavior is unacceptable, which imposes a lower cost of an accident, denoted by $k = L < H$. Each kid knows the type of his parents but does not know the type of his opponent's parents. The distribution of types is common knowledge (this is the common prior assumption).
>
> […] The action sets of each player are $A_1 = \{C, D\}$ and $A_2 = \{c, d\}$, where $C$ (or $c$) stands for "chicken" and $D$ (or $d$) stands for "drive."
>
> From the extensive form in Figure 12.3 we can derive the matrix form as follows. A strategy for player 1 is denoted by $xy \in S_1 = \{CC, CD, DC, DD\}$, where $x$ is what he does if he is an $L$ type and $y$ is what he does if he is an $H$ type. Similarly $S_2 = \{cc, cd, dc, dd\}$. […] This results in the following matrix-form Bayesian game:
>
> | Player 1 \ Player 2 | $cc$ | $cd$ | $dc$ | $dd$ |
> |---|---|---|---|---|
> | $CC$ | $0, 0$ | $0, \frac{R}{2}$ | $0, \frac{R}{2}$ | $0, R$ |
> | $CD$ | $\frac{R}{2}, 0$ | $\frac{3R}{8} - \frac{H}{4}, \frac{3R}{8} - \frac{H}{4}$ | $\frac{3R}{8} - \frac{H}{4}, \frac{3R}{8} - \frac{L}{4}$ | $\frac{R}{4} - \frac{H}{2}, \frac{3R}{4} - \frac{L}{4} - \frac{H}{4}$ |
> | $DC$ | $\frac{R}{2}, 0$ | $\frac{3R}{8} - \frac{L}{4}, \frac{3R}{8} - \frac{H}{4}$ | $\frac{3R}{8} - \frac{L}{4}, \frac{3R}{8} - \frac{L}{4}$ | $\frac{R}{4} - \frac{L}{2}, \frac{3R}{4} - \frac{L}{4} - \frac{H}{4}$ |
> | $DD$ | $R, 0$ | $\frac{3R}{4} - \frac{L}{4} - \frac{H}{4}, \frac{R}{4} - \frac{H}{2}$ | $\frac{3R}{4} - \frac{L}{4} - \frac{H}{4}, \frac{R}{4} - \frac{L}{2}$ | $\frac{R}{2} - \frac{L}{2} - \frac{H}{2}, \frac{R}{2} - \frac{L}{2} - \frac{H}{2}$ |
>
> To solve for the Bayesian Nash equilibria we need to have more information about the parameters $R$, $H$, and $L$. Assume that $R = 8$, $H = 16$, and $L = 0$, which results in the following matrix-form game:
>
> | Player 1 \ Player 2 | $cc$ | $cd$ | $dc$ | $dd$ |
> |---|---|---|---|---|
> | $CC$ | $0, 0$ | $0, 4$ | $0, 4$ | $0, 8$ |
> | $CD$ | $4, 0$ | $-1, -1$ | $-1, 3$ | $-6, 2$ |
> | $DC$ | $4, 0$ | $3, -1$ | $3, 3$ | $2, 2$ |
> | $DD$ | $8, 0$ | $2, -6$ | $2, 2$ | $-4, -4$ |
>
> A quick analysis reveals that the game has a unique pure-strategy Bayesian Nash equilibrium: $(DC, dc)$.

#### 5. Tadelis 13.1

<!-- id: Tadelis 13.1 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.1 "Second-Price Auctions", p. 285 [PDF p. 304]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Second-Price Auctions:** Show that in a second-price sealed-bid auction bidding your valuation weakly dominates bidding above your valuation.

#### 6. Muñoz-Garcia Ch. 8 Ex. 4

<!-- id: Muñoz-Garcia Ch. 8 Ex. 4 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 8, Exercise 4 "Second Price Auction", p. 362 [PDF p. 372]. Reproduced verbatim (statement only; the book's worked answer follows it). **Answer in the source:** yes, the book's worked answer follows the exercise.

> Consider a setting where every bidder privately observes his/her own valuation for the object. In addition, assume that $N$ bidders interact in an auction in which they simultaneously and independently submit their own bids, the highest bidder wins the object, but he/she pays the second-highest bid (this is the so-called second-price auction, SPA). All other bidders pay zero.
>
> a. Argue that it is a weakly dominant strategy for a bidder to bid her value in the SPA.
>
> b. Are optimal bids affected if the joint distribution of bidders' values exhibits correlation, i.e., if bidder $i$ observes that he has a high valuation for the object he can infer that other bidders must also have a high valuation (in the case of positively correlated values) or that, instead, they must have a low valuation for the object (in the case of negatively correlated values)?
>
> c. Are optimal bids affected by the number of bidders participating in the auction? Are optimal bids affected by bidders' risk aversion?

#### 7. Muñoz-Garcia Ch. 8 Ex. 1

<!-- id: Muñoz-Garcia Ch. 8 Ex. 1 -->
**Source.** Muñoz-Garcia & Toro-Gonzalez (2019), *Strategy and Game Theory: Practice Exercises with Answers*, Ch. 8, Exercise 1 "First Price Auction with Uniformly Distributed Valuations—Two Players", p. 350 [PDF p. 360]. Reproduced verbatim (statement only; the book's worked answer follows it). **Answer in the source:** yes, the book's worked answer follows the exercise.

> Consider a first-price auction with two players, each of them drawing his valuation for the object $v_i$ from a uniform distribution $v_i \sim U[0, 1]$. Every player $i$ simultaneously and independently submits his bid for the object, $b_i$, and the seller chooses the player who submitted the highest bid as the winning bidder, who pays the bid he submitted. The other bidder loses the auction and receives a zero payoff.
>
> (a) Set up every bidder $i$'s expected utility maximization problem. Interpret.
>
> (b) Find the equilibrium bidding function that every bidder $i$ uses in the Bayesian Nash Equilibrium (BNE) of the first-price auction.

#### 8. Tadelis 13.2

<!-- id: Tadelis 13.2 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.2 "Complete Information", p. 285 [PDF p. 304]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Complete Information:** Consider a set of $N$ players participating in a sealed-bid second-price auction, but assume that there is complete information so that each player knows the valuation of every other player.
>
> a. Is it still true that each player bidding his valuation is a weakly dominant strategy?
>
> b. Are there other Nash equilibria of this game?

---

## Tier 2 — Exam level

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 9 | B2 | Tadelis | §12.7, Exercises | 12.2 | 266 | Cournot with privately known costs: three FOCs solved jointly |
| 10 | B2 | Gibbons | §3.5, Problems (Section 3.1) | 3.3 | 169 | Writing out every element of a Bayesian game (Bertrand with private demand sensitivity), then the symmetric BNE |
| 11 | B1 | Tadelis | §12.7, Exercises | 12.3 | 266–267 | All pure BNE of a 2-type, 2-action conflict game, for two parameter cases |
| 12 | B2 | Tadelis | §12.7, Exercises | 12.9 | 269 | Purification: a threshold BNE that converges to the mixed equilibrium |
| 13 | B3 | Tadelis | §12.7, Exercises | 12.5 | 267–268 | Lemons with a continuum of types: a threshold seller and the unique BNE |
| 14 | B3 | Tadelis | §12.7, Exercises | 12.6 | 268 | The same with wages: social surplus, and why cutting outside options can raise it |
| 15 | B4 | Gibbons | §3.5, Problems (Section 3.2) | 3.6 | 170 | Verifying the first-price bid $(n-1)v/n$ with $n$ uniform bidders |
| 16 | B4 | Tadelis | §13.4, Exercises | 13.9 | 287 | Linear first-price bidding when values are $0.5 + \theta_i$ |
| 17 | B4 | Tadelis | §13.4, Exercises | 13.3 | 285–286 | Reserve prices with discrete values: revenue at $r = 0$ and $r = 1$ |
| 18 | B5 | Tadelis | §12.7, Exercises | 12.8 | 268–269 | Jury voting: the pivotal event, one juror vs two, majority of three |

### Statements

#### 9. Tadelis 12.2

<!-- id: Tadelis 12.2 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.2 "Cournot Revisited", p. 266 [PDF p. 285]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Cournot Revisited:** Consider the Cournot duopoly model in which two firms, 1 and 2, simultaneously choose the quantities they supply, $q_1$ and $q_2$. The price each will face is determined by the market demand function $p(q_1, q_2) = a - b(q_1 + q_2)$. Each firm has a probability $\mu$ of having a marginal unit cost of $c_L$ and a probability $1 - \mu$ of having a marginal unit cost of $c_H$. These probabilities are common knowledge, but the true type is revealed only to each firm individually. Solve for the Bayesian Nash equilibrium.

#### 10. Gibbons 3.3

<!-- id: Gibbons 3.3 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §3.5 Problems, Section 3.1, Problem 3.3, p. 169 [PDF p. 175]. Reproduced verbatim. The demand function is printed with a minus sign before $b_i \cdot p_j$; the scanned copy in `Livros/` carries a reader's handwritten mark over that sign. **Answer in the source:** no.

> **3.3.** Consider the following asymmetric-information model of Bertrand duopoly with differentiated products. Demand for firm $i$ is $q_i(p_i, p_j) = a - p_i - b_i \cdot p_j$. Costs are zero for both firms. The sensitivity of firm $i$'s demand to firm $j$'s price is either high or low. That is, $b_i$ is either $b_H$ or $b_L$, where $b_H > b_L > 0$. For each firm, $b_i = b_H$ with probability $\theta$ and $b_i = b_L$ with probability $1 - \theta$, independent of the realization of $b_j$. Each firm knows its own $b_i$ but not its competitor's. All of this is common knowledge. What are the action spaces, type spaces, beliefs, and utility functions in this game? What are the strategy spaces? What conditions define a symmetric pure-strategy Bayesian Nash equilibrium of this game? Solve for such an equilibrium.

#### 11. Tadelis 12.3

<!-- id: Tadelis 12.3 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.3 "Armed Conflict", pp. 266–267 [PDF pp. 285–286]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Armed Conflict:** Consider the following strategic situation: Two rival armies plan to seize a disputed territory. Each army's general can choose either to attack ($A$) or to not attack ($N$). In addition, each army is either strong ($S$) or weak ($W$) with equal probability, and the realizations for each army are *independent*. Furthermore the type of each army is known only to that army's general. An army can capture the territory if either (i) it attacks and its rival does not or (ii) it and its rival attack, but it is strong and the rival is weak. If both attack and are of equal strength then neither captures the territory. As for payoffs, the territory is worth $m$ if captured and each army has a cost of fighting equal to $s$ if it is strong and $w$ if it is weak, where $s < w$. If an army attacks but its rival does not, no costs are borne by either side. Identify all the pure-strategy Bayesian Nash equilibria of this game for the following two cases, and briefly describe the intuition for your results:
>
> a. $m = 3$, $w = 2$, $s = 1$.
>
> b. $m = 3$, $w = 4$, $s = 2$.

#### 12. Tadelis 12.9

<!-- id: Tadelis 12.9 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.9 "Grab the Dollar", p. 269 [PDF p. 288]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Grab the Dollar:** Each of two players has two possible actions: grab the dollar or don't grab the dollar. Player $i$'s payoff is 1 if he is the only one to grab the dollar, and his payoff is 0 if he does not. Each player's payoff is $-1$ if both players grab the dollar.
>
> a. Find the Nash equilibria of this game of complete information.
>
> b. Consider the following perturbation of the game. The payoff structure is the same, with the following addition: When player $i$ is the only one to grab the dollar his payoff is $1 + \theta_i$, where $\theta_i$ is player $i$'s type and it is uniformly distributed over $[-\varepsilon, \varepsilon]$ with $\varepsilon < 1$. Each player knows only his own type, and the distribution of types is common knowledge. Find the pure-strategy Bayesian Nash equilibrium of this game of incomplete information.
>
> c. Show that when $\varepsilon$ converges to 0, the pure-strategy Bayesian Nash equilibrium converges to the mixed-strategy Nash equilibrium of the game with complete information.

#### 13. Tadelis 12.5

<!-- id: Tadelis 12.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.5 "Not All That Glitters", pp. 267–268 [PDF pp. 286–287]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Not All That Glitters:** A prospector owns a gold mine where he can dig to recover gold. His output depends on the amount of gold in the mine, denoted by $x$. The prospector knows the value of $x$, but the rest of the world knows only that the amount of gold is uniformly distributed on the interval $[0, 1]$. Before deciding to mine, the prospector can try to sell his mine to a large mining company, which is much more efficient in its extraction methods. The prospector can ask the company owner for any price $p \ge 0$, and the owner can reject ($R$) or accept ($A$) the offer. If the owner rejects the offer then the prospector is left to mine himself, and his payoff from self-mining is equal to $3x$. If the owner accepts the offer then the prospector's payoff is the price $p$, while the owner's payoff is given by the net value $4x - p$, and this is common knowledge.
>
> a. Show that for a given price $p \ge 0$ there is a threshold type $x(p) \in [0, 1]$ of prospector, such that types below $x(p)$ will prefer to sell the mine, while types above $x(p)$ will prefer to self-mine.
>
> b. Find the pure-strategy Bayesian Nash equilibrium of this game, and show that it is unique. What is the expected payoff of each type of prospector and of the company owner in the equilibrium you derived?

#### 14. Tadelis 12.6

<!-- id: Tadelis 12.6 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.6 "Reap and Weep", p. 268 [PDF p. 287]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Reap and Weep:** A farmer owns some land that he can farm to produce crops. Farming output depends on the talent of the farmer. The farmer knows his talent, but the rest of the world knows only that a farmer's talent is uniformly distributed: $\theta \in [0, 1]$. The farmer's payoff from farming his land is equal to his talent $\theta$. Before setting up his farm, the farmer approaches the local manufacturing plant and offers to work on the production line. The farmer can ask the plant owner for any wage $w \ge 0$, and the owner can reject ($R$) or accept ($A$) the offer. If the owner rejects the offer then the farmer must return home and settle into his farming. If the owner accepts the offer then the farmer's payoff is the wage $w$, while the owner's payoff is given by the net value $\frac{3}{2}\theta - w$, and this is common knowledge.
>
> a. Define the set of pure strategies for each player and find the pure-strategy Bayesian Nash equilibria of this game.
>
> b. Averaging over the type of farmer, what are the possible levels of *social surplus* (sum of expected payoffs of the farmer and the owner in their potential relationship) from the equilibrium you derived in (a)?
>
> c. A local policy maker who is advocating for the increase of social surplus is proposing to cut water subsidies to the farmers, which would imply that a farmer of type $\theta$ would get a payoff of $\frac{1}{2}\theta$ from farming his land. This policy has no effect on the productivity of manufacturing. Using the criterion of social surplus, can you advocate for this policy maker using equilibrium analysis?

#### 15. Gibbons 3.6

<!-- id: Gibbons 3.6 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §3.5 Problems, Section 3.2, Problem 3.6, p. 170 [PDF p. 176]. Reproduced verbatim. **Answer in the source:** no.

> **3.6.** Consider a first-price, sealed-bid auction in which the bidders' valuations are independently and uniformly distributed on $[0,1]$. Show that if there are $n$ bidders, then the strategy of bidding $(n-1)/n$ times one's valuation is a symmetric Bayesian Nash equilibrium of this auction.

#### 16. Tadelis 13.9

<!-- id: Tadelis 13.9 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.9 "Private Value Linear Bidding", p. 287 [PDF p. 306]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Private Value Linear Bidding:** Two players participate in a first-price sealed-bid auction in an IPV setting. The value of the good for each player is given by $0.5 + \theta_i$, where $\theta_i$ is observed only by player $i$ and is uniformly distributed over the interval $[0, 1]$.
>
> a. Show that there is a symmetric Bayesian Nash equilibrium in which each bidder $i$'s bidding strategy is of the form $s_i^*(\theta_i) = a + b\theta_i$.
>
> b. What is the expected payoff of a player if his type is $\theta_i$?

#### 17. Tadelis 13.3

<!-- id: Tadelis 13.3 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.3 "Reserve Prices (Easier)", pp. 285–286 [PDF pp. 304–305]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Reserve Prices (Easier):** Consider a seller who must sell a single private value good. There are two potential buyers, each with a valuation that can take on one of three values, $\theta_i \in \{0, 1, 2\}$, each value occurring with an equal probability of $\frac{1}{3}$. The players' values are independently drawn. The seller will offer the good using a second-price sealed-bid auction, but he can set a "reserve price" of $r \ge 0$ that modifies the rules of the auction as follows. If both bids are below $r$ then neither bidder obtains the good and it is destroyed. If both bids are at or above $r$ then the regular auction rules prevail. If only one bid is at or above $r$ then that bidder obtains the good and pays $r$ to the seller.
>
> a. Is it still a weakly dominant strategy for each player to bid his valuation when $r > 0$?
>
> b. What is the expected revenue of the seller when $r = 0$ (no reserve price)?
>
> c. What is the expected revenue of the seller when $r = 1$?
>
> d. What explains the difference between your answers to (b) and (c)?
>
> e. What is the optimal reserve price $r$ for the seller, and what can you conclude about the value of reserve prices?

#### 18. Tadelis 12.8

<!-- id: Tadelis 12.8 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.8 "Jury Voting", pp. 268–269 [PDF pp. 287–288]. Reproduced verbatim. The game it refers to is Tadelis §12.4 (pp. 261–264), summarized in [[Notas/L07/L07-09-common-values-curses]] §1. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Jury Voting:** Consider the jury voting game in Section 12.4.
>
> a. Show that both players choosing $CC$ is a Bayesian Nash equilibrium of the two-player game.
>
> b. Would it be better for the two players if only one of them decided on the fate of the defendant? Why or why not?
>
> c. Consider a three-player game in which the defendant is convicted if at least two players vote to convict him, and acquitted otherwise (i.e., majority voting determines the defendant's fate). Assume that the informational structure is the same as in the two-player game. Are there conditions in which voting according to one's signal ($C$ if $\theta_i = \theta_G$ and $A$ if $\theta_i = \theta_I$) is a Bayesian Nash equilibrium?

**Referred to in the statement.** The jury voting game of Section 12.4 (Tadelis pp. 261–262 [PDF p. 280–281]) (reproduced from the book):

> As an example, consider a jury made up of two players (jurors) who must collectively decide whether to acquit ($A$) or to convict ($C$) a defendant. The process calls for each player to cast a sealed vote, and the defendant is convicted only if both vote $C$. The problem is that there is uncertainty about whether the defendant is guilty ($G$) or innocent ($I$). The prior probability that the defendant is guilty is given by $q > \frac{1}{2}$ and is common knowledge. Assume that each player cares about making the right decision, so that if the defendant is guilty then each player receives a payoff of 1 from a conviction and 0 from an acquittal. If instead the defendant is innocent then each player receives a payoff of 0 from a conviction and 1 from an acquittal.
>
> […] Now imagine that things are a bit more complex. Each player $i$ has a different expertise and, when observing the evidence, gets a private signal $\theta_i \in \{\theta_G, \theta_I\}$ that contains valuable information. In particular when the defendant is guilty player $i$ is more likely to receive the signal $\theta_i = \theta_G$ than when the defendant is innocent, and vice versa for $\theta_i = \theta_I$. Assume that the signals are independent: the probability of receiving the signal $\theta_G$ when the defendant is guilty is equal to the probability of receiving the signal $\theta_I$ when the defendant is innocent, so that
>
> $$\Pr\{\theta_i = \theta_G \mid G\} = \Pr\{\theta_i = \theta_I \mid I\} = p > \tfrac{1}{2} \quad \text{for } i \in \{1, 2\}$$
>
> and
>
> $$\Pr\{\theta_i = \theta_G \mid I\} = \Pr\{\theta_i = \theta_I \mid G\} = 1 - p < \tfrac{1}{2} \quad \text{for } i \in \{1, 2\}.$$
>
> […] With this information structure in place we have a Bayesian game of incomplete information in which each player $i$ will choose a signal-dependent action to maximize the probability that a guilty defendant is convicted while an innocent one is acquitted. Because each player has two types, given by the signal he observes, each player will have four pure strategies, $s_i \in \{AA, AC, CA, CC\}$, where strategy $xy$ means that he chooses $x$ when his signal is $\theta_G$ and he chooses $y$ when his signal is $\theta_I$.

**Note on the book (item 18).** Part (a) is true only for $p \le q$ (the signal precision does not exceed the
prior): against a juror who always convicts, a juror who sees $\theta_I$ is pivotal and acquits when $p > q$.
The book (p. 264) states $CC$ as an equilibrium without the condition. See the solutions PDF, item 18.

---

## Tier 3 — Advanced

| # | Block | Source | Ch./Sec. | Exercise | Page | What it trains |
|---|---|---|---|---|---|---|
| 19 | B3 | MWG | §13.B, Exercises | 13.B.1 | 473 | The competitive equilibria of the adverse-selection labor market read off one diagram |
| 20 | B3 | MWG | §13.B, Exercises | 13.B.2 | 473 | Proving that the competitive equilibrium with unobservable types is Pareto inefficient |
| 21 | B3 | Tadelis | §12.7, Exercises | 12.7 | 268 | Two-sided private information: house swaps, threshold strategies and why only the worst trade |
| 22 | B3 | Gibbons | §3.5, Problems (Section 3.2) | 3.8 | 171–172 | The double auction as a labor market, against a fixed-wage contract and a wage offer |
| 23 | B4 | Tadelis | §13.4, Exercises | 13.5 | 286 | A first-price auction with two discrete values: the mixed-bid BNE and its revenue |
| 24 | B5 | Tadelis | §13.4, Exercises | 13.10 | 287 | Common-value linear bidding: the winner's curse lowers every bid |

### Statements

#### 19. MWG 13.B.1

<!-- id: MWG 13.B.1 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 13 Exercises, Exercise 13.B.1^A, p. 473 [PDF p. 247]. Reproduced verbatim. Figures 13.B.1–13.B.3 are in the text, pp. 440–443. **Answer in the source:** yes, in the MWG solutions manual (Figures 13.B.1(a)-(c)).

> Consider three functions of $\hat\theta$: $r(\hat\theta)$, $E[\theta \mid \theta \le \hat\theta]$, and $\hat\theta$. Graph these three functions over the domain $[\underline\theta, \bar\theta]$, assuming that the first two functions are continuous in $\hat\theta$ but allowing them to be otherwise quite arbitrary. Identify the competitive equilibria of the adverse selection model of Section 13.B using this diagram. What about the Pareto optimal labor allocation? Now produce a diagram to depict each of the situations in Figures 13.B.1 to 13.B.3.

#### 20. MWG 13.B.2

<!-- id: MWG 13.B.2 -->
**Source.** Mas-Colell, Whinston & Green (1995), *Microeconomic Theory*, Ch. 13 Exercises, Exercise 13.B.2^B, p. 473 [PDF p. 247]. Reproduced verbatim. **Answer in the source:** not found in the solutions manual's OCR text.

> Suppose that $r(\cdot)$ is a continuous and strictly increasing function and that there exists $\hat\theta \in (\underline\theta, \bar\theta)$ such that $r(\theta) > \theta$ for $\theta > \hat\theta$ and $r(\theta) < \theta$ for $\theta < \hat\theta$. Let the density of workers of type $\theta$ be $f(\theta)$, with $f(\theta) > 0$ for all $\theta \in [\underline\theta, \bar\theta]$. Show that a competitive equilibrium with unobservable worker types necessarily involves a Pareto inefficient outcome.

#### 21. Tadelis 12.7

<!-- id: Tadelis 12.7 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 12.7 "Trading Places", p. 268 [PDF p. 287]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Trading Places:** Two players, 1 and 2, each own a house. Each player $i$ values his own house at $v_i$. The value of player $i$'s house to the other player, i.e., to player $j \ne i$, is $\frac{3}{2}v_i$. Each player $i$ knows the value $v_i$ of his own house to himself, but not the value of the other player's house. The values $v_i$ are drawn independently from the interval $[0, 1]$ with uniform distribution.
>
> a. Suppose players announce simultaneously whether they want to exchange their houses. If both players agree to an exchange, the exchange takes place. Otherwise no exchange takes place. Find a Bayesian Nash equilibrium of this game in pure strategies in which each player $i$ accepts an exchange if and only if the value $v_i$ does not exceed some threshold $\theta_i$.
>
> b. How would your answer to (a) change if player $j$'s valuation of player $i$'s house were $\frac{5}{2}v_i$?
>
> c. Try to explain why any Bayesian Nash equilibrium of the game described in (a) must involve threshold strategies of the type postulated in (a).

#### 22. Gibbons 3.8

<!-- id: Gibbons 3.8 -->
**Source.** Gibbons (1992), *Game Theory for Applied Economists*, §3.5 Problems, Section 3.2, Problem 3.8, pp. 171–172 [PDF pp. 177–178]. Reproduced verbatim. Figure 3.2.3 (the double auction's trading region) is in the text, p. 163. **Answer in the source:** no.

> **3.8.** Reinterpret the buyer and seller in the double auction analyzed in Section 3.2.C as a firm that knows a worker's marginal product ($m$) and a worker who knows his or her outside opportunity ($v$), respectively, as in Hall and Lazear (1984). In this context, trade means that the worker is employed by the firm, and the price at which the parties trade is the worker's wage, $w$. If there is trade, then the firm's payoff is $m - w$ and the worker's is $w$; if there is no trade then the firm's payoff is zero and the worker's is $v$.
>
> Suppose that $m$ and $v$ are independent draws from a uniform distribution on $[0, 1]$, as in the text. For purposes of comparison, compute the players' expected payoffs in the linear equilibrium of the double auction. Now consider the following two trading games as alternatives to the double auction.
>
> *Game I*: Before the parties learn their private information, they sign a contract specifying that if the worker is employed by the firm then the worker's wage will be $w$, but also that either side can escape from the employment relationship at no cost. After the parties learn the values of their respective pieces of private information, they simultaneously announce either that they Accept the wage $w$ or that they Reject that wage. If both announce Accept, then trade occurs; otherwise it does not. Given an arbitrary value of $w$ from $[0, 1]$, what is the Bayesian Nash equilibrium of this game? Draw a diagram analogous to Figure 3.2.3 showing the type-pairs that trade. Find the value of $w$ that maximizes the sum of the players' expected payoffs and compute this maximized sum.
>
> *Game II*: Before the parties learn their private information, they sign a contract specifying that the following dynamic game will be used to determine whether the worker joins the firm and if so at what wage. (Strictly speaking, this game belongs in Chapter 4. We will anticipate the spirit of Chapter 4 by arguing that this game can be solved by combining the lessons of this chapter with those of Chapter 2.) After the parties learn the values of their respective pieces of private information, the firm chooses a wage $w$ to offer the worker, which the worker then accepts or rejects. Try to analyze this game using backwards induction, as we did for the analogous complete-information games in Section 2.1.A, as follows. Given $w$ and $v$, what will the worker do? If the firm anticipates what the worker will do, then given $m$ what will the firm do? What is the sum of the players' expected payoffs?

**Referred to in the statement.** The double auction of Section 3.2.C, its linear equilibrium and Figure 3.2.3 (Gibbons pp. 159, 161 and 163 [PDF p. 165, 167 and 169]) (reproduced from the book; the figure is described in words):

> We analyze a trading game called a double auction. The seller names an asking price, $p_s$, and the buyer simultaneously names an offer price, $p_b$. If $p_b \ge p_s$, then trade occurs at price $p = (p_b + p_s)/2$; if $p_b < p_s$, then no trade occurs.
>
> The buyer's valuation for the seller's good is $v_b$, the seller's is $v_s$. These valuations are private information and are drawn from independent uniform distributions on $[0, 1]$. If the buyer gets the good for price $p$, then the buyer's utility is $v_b - p$; if there is no trade, then the buyer's utility is zero. If the seller sells the good for price $p$, then the seller's utility is $p - v_s$; if there is no trade, then the seller's utility is zero. (Each of these utility functions measures the change in the party's utility. If there is no trade, then there is no change in utility. It would make no difference to define, say, the seller's utility to be $p$ if there is trade at price $p$ and $v_s$ if there is no trade.)
>
> […] Therefore, the linear equilibrium strategies are
>
> $$p_b(v_b) = \frac{2}{3}v_b + \frac{1}{12} \tag{3.2.7}$$
>
> and
>
> $$p_s(v_s) = \frac{2}{3}v_s + \frac{1}{4}, \tag{3.2.8}$$
>
> as shown in Figure 3.2.2.
>
> Recall that trade occurs in the double auction if and only if $p_b \ge p_s$. Manipulating (3.2.7) and (3.2.8) shows that trade occurs in the linear equilibrium if and only if $v_b \ge v_s + (1/4)$, as shown in Figure 3.2.3.
>
> *Figure 3.2.3 (described):* the unit square with $v_s$ on the horizontal axis and $v_b$ on the vertical axis; it draws the line $v_b = v_s$ and the line $v_b = v_s + (1/4)$, and labels the region above $v_b = v_s + (1/4)$ "TRADE".

#### 23. Tadelis 13.5

<!-- id: Tadelis 13.5 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.5 "Mixed Strategies", p. 286 [PDF p. 305]. Reproduced verbatim. **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Mixed Strategies:** Consider a seller who offers a single private value good using a first-price sealed-bid auction. There are two potential buyers, each with a valuation that can take on one of two values, $\theta_i \in \{4, 8\}$, each value occurring with an equal probability of $\frac{1}{2}$. The players' values are independently drawn. Call the type with $\theta_i = 4$ the "low" type and $\theta_i = 8$ the "high" type.
>
> a. Show that in a Bayesian Nash equilibrium the low must be using a pure strategy bid $b_L = 4$. (Hint: First show that in a Bayesian Nash equilibrium the low type cannot be using a pure strategy bid $b_L < 4$. Next show that in a Bayesian Nash equilibrium the low type cannot be using a mixed strategy with two different bids.)
>
> b. Show that given the fact described in (a), in any Bayesian Nash equilibrium the high type will never choose a bid $b_H > 6$.
>
> c. Show that the low type choosing $b_L = 4$ and the high type choosing $b_H$ uniformly from the interval $[4, 6]$ together constitute a Bayesian Nash equilibrium.
>
> d. Calculate the expected revenue to the seller given the Bayesian Nash equilibrium in (c). How does it compare to the expected revenue he would obtain from an English auction?

**Note on the book (item 23).** In part (c) the uniform distribution on $[4,6]$ is not an equilibrium strategy of
the high type (the payoff $(8-b)(b-2)/4$ is not constant on $[4,6]$); the indifference condition gives the cdf
$(b-4)/(8-b)$ on $[4,6]$, whose revenue equals the English auction's $5$. See the solutions PDF, item 23.

#### 24. Tadelis 13.10

<!-- id: Tadelis 13.10 -->
**Source.** Tadelis (2013), *Game Theory: An Introduction*, Exercise 13.10 "Common Values Linear Bidding", p. 287 [PDF p. 306]. Reproduced verbatim. "The previous exercise" is item 16 (Tadelis 13.9). **Answer in the source:** no (none in the book; Princeton UP's website has about half, not checked).

> **Common Values Linear Bidding:** Two players participate in a first-price sealed-bid auction in a common-values setting. The value of the good for each player is given by $\theta_1 + \theta_2$, where $\theta_i$ is a signal observed only by player $i$ and is uniformly distributed over the interval $[0, 1]$. Hence if player $i$ observes his signal $\theta_i$ then his expected valuation is equal to $0.5 + \theta_i$ (but unlike the previous exercise, this is a common-values setting).
>
> a. Show that there is a symmetric Bayesian Nash equilibrium in which each bidder $i$'s bidding strategy is of the form $s_i^*(\theta_i) = a + b\theta_i$.
>
> b. What is the expected payoff of a player if his type is $\theta_i$?
>
> c. Show that for each value of $\theta_i$ the equilibrium bid of player $i$ is less than what you found in (a) of the previous exercise.

**Referred to in the statement.** The previous exercise, Exercise 13.9 "Private Value Linear Bidding" (Tadelis p. 287 [PDF p. 306]) (reproduced from the book):

> **Private Value Linear Bidding:** Two players participate in a first-price sealed-bid auction in an IPV setting. The value of the good for each player is given by $0.5 + \theta_i$, where $\theta_i$ is observed only by player $i$ and is uniformly distributed over the interval $[0, 1]$.
>
> a. Show that there is a symmetric Bayesian Nash equilibrium in which each bidder $i$'s bidding strategy is of the form $s_i^*(\theta_i) = a + b\theta_i$.
>
> b. What is the expected payoff of a player if his type is $\theta_i$?


**Optional extras.**
- Tadelis 12.4 "Grade Gambles" (p. 267): a finite Bayesian game where more information hurts; pair it with Muñoz-Garcia Ch. 7 Ex. 4 "More Information Might Hurt" (p. 331).
- Tadelis 12.10 "Purification" (p. 269): uniqueness of the perturbed Matching Pennies BNE, after item 12; Gibbons 3.5 (p. 170) asks for the same construction.
- Gibbons 3.2 (p. 169) and Muñoz-Garcia Ch. 7 Ex. 5 (p. 336): Cournot and differentiated duopoly with private demand information, after item 9.
- Muñoz-Garcia Ch. 7 Ex. 6 (p. 339, public good) and Ex. 7 (p. 343, starting a fight): more threshold BNE, with answers.
- Muñoz-Garcia Ch. 8 Ex. 2–3 (pp. 352, 355): first-price auction with $N$ bidders and general distributions, after item 15; Gibbons 3.7 (pp. 170–171) is the two-bidder general-density case.
- Tadelis 13.6 (pp. 286–287) and Muñoz-Garcia Ch. 8 Ex. 7 (p. 371): the third-price auction and revenue equivalence.
- Tadelis 13.8 (p. 287): the oil-field second-price auction with common values, after item 24.
- Tadelis 13.4 (p. 286) and 13.7 (p. 287); Muñoz-Garcia Ch. 8 Ex. 5–6 (pp. 364–365, all-pay) and Ex. 8 (p. 371, risk-averse bidders): beyond the lecture's core.

---

## Suggested study order

1. **Bayesian games.** Read Tadelis Ch. 12 opening and §12.1 (pp. 241–252) and Gibbons §3.1 (pp. 144–152), then do items **1–4**, then **11**.
2. **Continuous actions and types.** Read Gibbons §3.1.A (pp. 144–146), Tadelis §12.2.2 and §12.5 (pp. 255–258, 264–266), then do **9, 10, 12**.
3. **Adverse selection.** Read Tadelis §12.3 (pp. 258–261) and M&R pp. 149–153, then do **13, 14**; then Gibbons §3.2.C (pp. 158–163) before **21, 22**.
4. **Auctions.** Read Tadelis §13.1 (pp. 270–282) and Gibbons §3.2.B (pp. 155–158), then do **5–8**, then **15–17**, and **23** last.
5. **Common values.** Read Tadelis §12.4 (pp. 261–264) and §13.2 (pp. 282–284), then do **18**, then **24** right after 16.
6. **Advanced.** Read MWG §13.B (pp. 437–449), then do **19** before **20**.

---

## Consolidated Reading by Book

### Tadelis — Tadelis (2013)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Types, Nature, common prior; Bayesian games; BNE | Ch. 12, §12.1 | p. 241–252 | Foundations |
| Examples: chicken; study groups (thresholds) | Ch. 12, §12.2 | p. 252–258 | Foundations |
| Inefficient trade and adverse selection | Ch. 12, §12.3 | p. 258–261 | Exam |
| Committee voting | Ch. 12, §12.4 | p. 261–264 | Exam |
| Mixed strategies revisited: Harsanyi's interpretation | Ch. 12, §12.5 | p. 264–266 | Exam |
| Exercises 12.1–12.3, 12.5–12.9 | Ch. 12, §12.7 | p. 266–269 | Exam |
| Independent private values: second-price, English, first-price, Dutch; revenue equivalence | Ch. 13, §13.1 | p. 270–282 | Foundations |
| Common values and the winner's curse | Ch. 13, §13.2 | p. 282–284 | Exam |
| Exercises 13.1–13.3, 13.5, 13.9, 13.10 | Ch. 13, §13.4 | p. 285–287 | Exam |

### Gibbons — Gibbons (1992)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Static Bayesian games; Cournot with asymmetric information | §3.1 | p. 144–152 | Foundations |
| Mixed strategies revisited; an auction | §3.2.A–B | p. 152–158 | Exam |
| A double auction | §3.2.C | p. 158–163 | Advanced |
| Problems 3.1, 3.3, 3.4, 3.6, 3.8 | §3.5 | p. 169–172 | Exam |

### MWG — Mas-Colell, Whinston & Green (1995)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Bayesian games (formal side) | §8.E | p. 253–257 | Advanced |
| Informational asymmetries and adverse selection | §13.B | p. 437–449 | Advanced |
| Exercises 13.B.1, 13.B.2 | Ch. 13, Exercises | p. 473 | Advanced |

### Muñoz-Garcia — Muñoz-Garcia & Toro-Gonzalez (2019)
| Topic | Chapter / Section | Pages | Priority |
|---|---|---|---|
| Simultaneous-move games with incomplete information: exercises with worked answers | Ch. 7 | p. 317–347 | Foundations |
| Auctions: exercises with worked answers | Ch. 8 | p. 349–373 | Foundations |

## Consolidated Exercises

| # | Exercise | Book | Page | Topic | Level |
|---|---|---|---|---|---|
| 1 | 12.1 | Tadelis | p. 266 | Chicken with private types | Foundations |
| 2 | 12.2 | Tadelis | p. 266 | Cournot with private costs | Exam |
| 3 | 12.3 | Tadelis | p. 266–267 | Armed conflict, all pure BNE | Exam |
| 4 | 12.5 | Tadelis | p. 267–268 | Lemons: the gold mine | Exam |
| 5 | 12.6 | Tadelis | p. 268 | Lemons: wages and social surplus | Exam |
| 6 | 12.7 | Tadelis | p. 268 | Two-sided private information: house swaps | Advanced |
| 7 | 12.8 | Tadelis | p. 268–269 | Jury voting | Exam |
| 8 | 12.9 | Tadelis | p. 269 | Purification: grab the dollar | Exam |
| 9 | 13.1 | Tadelis | p. 285 | Second-price weak dominance | Foundations |
| 10 | 13.2 | Tadelis | p. 285 | Second-price with complete information | Foundations |
| 11 | 13.3 | Tadelis | p. 285–286 | Reserve prices, discrete values | Exam |
| 12 | 13.5 | Tadelis | p. 286 | First-price with mixed bids | Advanced |
| 13 | 13.9 | Tadelis | p. 287 | Linear first-price bidding | Exam |
| 14 | 13.10 | Tadelis | p. 287 | Common-value linear bidding | Advanced |
| 15 | 3.1 | Gibbons | p. 169 | Definitions | Foundations |
| 16 | 3.3 | Gibbons | p. 169 | Bertrand with private demand sensitivity | Exam |
| 17 | 3.4 | Gibbons | p. 169–170 | Pure BNE, one informed player | Foundations |
| 18 | 3.6 | Gibbons | p. 170 | First-price with $n$ bidders | Exam |
| 19 | 3.8 | Gibbons | p. 171–172 | Double auction as a labor market | Advanced |
| 20 | 13.B.1 | MWG | p. 473 | Competitive equilibria by diagram | Advanced |
| 21 | 13.B.2 | MWG | p. 473 | Inefficiency of the competitive equilibrium | Advanced |
| 22 | Ch. 7 Ex. 1 | Muñoz-Garcia | p. 318–319 | Bayesian normal form | Foundations |
| 23 | Ch. 8 Ex. 1 | Muñoz-Garcia | p. 350 | First-price, two bidders | Foundations |
| 24 | Ch. 8 Ex. 4 | Muñoz-Garcia | p. 362 | Second-price auction | Foundations |

## Study roadmap

| Priority | Topic | Reading | Exercises | Suggested time |
|:---:|---|---|---|:---:|
| 1 | Bayesian games and BNE | Tadelis §12.1–12.2.1 p. 241–255; Gibbons §3.1 p. 144–152 | Gibbons 3.1, 3.4; Muñoz-Garcia Ch. 7 Ex. 1; Tadelis 12.1, 12.3 | 2–2.5 h |
| 2 | Continuous actions, thresholds, purification | Gibbons §3.1.A p. 144–146; Tadelis §12.2.2, §12.5 p. 255–258, 264–266 | Tadelis 12.2, 12.9; Gibbons 3.3 | 1.5–2 h |
| 3 | Adverse selection and trade | Tadelis §12.3 p. 258–261; Gibbons §3.2.C p. 158–163; M&R p. 149–153 | Tadelis 12.5, 12.6, 12.7; Gibbons 3.8 | 2.5–3 h |
| 4 | Private-value auctions | Tadelis §13.1 p. 270–282; Gibbons §3.2.B p. 155–158 | Tadelis 13.1, 13.2, 13.3, 13.5, 13.9; Muñoz-Garcia Ch. 8 Ex. 1, 4; Gibbons 3.6 | 2.5–3 h |
| 5 | Common values | Tadelis §12.4 p. 261–264, §13.2 p. 282–284 | Tadelis 12.8, 13.10 | 1–1.5 h |
| 6 | Advanced | MWG §13.B p. 437–449 | MWG 13.B.1, 13.B.2 | 1.5 h |
