---
quiz: "Lecture 4 · Quiz 3 of 3 — Rubinstein bargaining, patience and legislative bargaining (estimated unit, written before the lecture)"
tags:
  rub: "Rubinstein's infinite horizon: stationarity and uniqueness"
  pat: "Different discount factors: patience as bargaining power"
  leg: "Legislative bargaining: closed and open rules"
  inf: "Bargaining under private information"
---

## rub

P: Two players split a pie of size 1 by alternating offers with no deadline: player 1 proposes in odd rounds, player 2 in even rounds, a rejection moves the game to the next round, and both discount at $\delta \in (0,1)$ per round. Perpetual disagreement gives both 0.

Q: Without a last round, backward induction has nowhere to start. How does the Shaked–Sutton argument still pin down a unique subgame-perfect payoff $v$ for the first proposer?
- By truncating the game at a large round $T$ and taking $T \to \infty$ in eq. (11.1), since the infinite game is defined as the limit of the finite games
- By the equations $\underline v = 1 - \delta\underline v$ and $\bar v = 1 - \delta\bar v$, each bound solving its own stationarity condition separately
- By the equations $\underline v = \delta\bar v$ and $\bar v = \delta\underline v$, since the proposer keeps what the responder could get one round later
- By the equations $\underline v = 1 - \delta\bar v$ and $\bar v = 1 - \delta\underline v$, whose difference forces $(1 - \delta)(\bar v - \underline v) = 0$
<!-- YW5zOjM= -->
> The subgame after two rejections is the original game, so the highest and lowest SPE payoffs $\bar v$, $\underline v$ of a proposer are the same in every odd round and, for player 2, in every even round. In the worst SPE for player 1, player 2 can secure $\delta\bar v$ by rejecting, so $\underline v = 1 - \delta\bar v$ (11.4); symmetrically $\bar v = 1 - \delta\underline v$ (11.5). Subtracting gives $\bar v = \underline v$, and then $v = 1 - \delta v$, so $v = 1/(1 + \delta)$. The match with the finite limit is a result, not a definition.
> Ref: Tadelis (2013), §11.3, eqs. (11.4)–(11.5) (pp. 228–229); MWG (1995), Example 9.AA.2 (pp. 297–298)
> Similar: Tadelis (2013), Exercise 11.6, p. 237

Q: Gibbons solves this game with the map $f(s) = 1 - \delta + \delta^2 s$, player 1's round-1 share when the continuation from round 3 gives him $s$. Why does $f$ have exactly one fixed point, and what is it?
- $f$ is decreasing with slope $-\delta^2$, so it crosses the diagonal once, at $s^* = 1/(1 + \delta^2)$, the share once both rounds are discounted
- $f$ is increasing with slope $\delta^2 < 1$, a contraction, so it crosses the diagonal once, at $s^* = 1/(1 + \delta)$, the Rubinstein share
- $f$ is increasing with slope $\delta < 1$, a contraction, so it crosses the diagonal once, at $s^* = 1/(1 - \delta)$, the discounted sum of pies
- $f$ is increasing with slope $\delta^2 < 1$, so the highest and lowest payoffs are its two fixed points, $s_L = 1 - \delta$ and $s_H = 1$
<!-- YW5zOjE= -->
> Using the highest backward-induction payoff $s_H$ as the round-3 continuation gives the highest round-1 payoff because $f$ is increasing, and that is $s_H$ again: $f(s_H) = s_H$, likewise $f(s_L) = s_L$. A line with slope $\delta^2 < 1$ meets the diagonal once: $s(1 - \delta^2) = 1 - \delta$, so $s^* = 1/(1 + \delta)$ and $s_H = s_L$. Iterating $f$ from $s = 1$ reproduces the odd-$T$ shares.
> Ref: Gibbons (1992), §2.1.D (pp. 70–71)
> Similar: Gibbons (1992), Problem 2.19, p. 137

Q: In the stationary equilibrium, player 1 offers $x = 1/(1 + \delta)$ in odd rounds and player 2 offers $x = \delta/(1 + \delta)$ in even rounds, $x$ being player 1's share. Which one-stage deviation check shows that player 2 should accept exactly the offers $x \le 1/(1 + \delta)$?
- Rejecting and then proposing in round 2 lets her keep $1/(1 + \delta)$, worth $\delta/(1 + \delta)$ today, so she accepts iff $1 - x \ge \delta/(1 + \delta)$
- Rejecting and then proposing in round 2 lets her keep $\delta/(1 + \delta)$, worth $\delta^2/(1 + \delta)$ today, so she accepts iff $1 - x \ge \delta^2/(1 + \delta)$
- Rejecting and then rejecting forever gives her 0, so she accepts any offer at all, and the rule $x \le 1/(1 + \delta)$ only reflects player 1's choice
- Rejecting and then proposing in round 2 lets her keep the whole pie, worth $\delta$ today, so she accepts iff $1 - x \ge \delta$, as in two rounds
<!-- YW5zOjA= -->
> A one-stage deviation changes one action and then follows the strategy. If player 2 rejects, she proposes $x = \delta/(1 + \delta)$ next round, which player 1 accepts, so she keeps $1 - \delta/(1 + \delta) = 1/(1 + \delta)$, worth $\delta/(1 + \delta)$ today. Accepting is optimal iff $1 - x \ge \delta/(1 + \delta)$, that is $x \le 1/(1 + \delta)$. The whole-pie continuation belongs to a game with a deadline, not to the stationary one.
> Ref: Tadelis (2013), §11.3, equilibrium strategies (p. 229), §9.5 (pp. 184–186)
> Similar: Gibbons (1992), Problem 2.20, pp. 137–138

Q: Rubinstein's infinite-horizon share $1/(1 + \delta)$ equals the limit of the finite-horizon shares as $T \to \infty$. How should this coincidence be read?
- As true by construction, because an infinite game is defined as the limit of its truncations, so its equilibria are the limits of theirs in every game
- As an accident of the linear pie, since with a pie of size $v$ instead of 1 the infinite-horizon share and the finite limit no longer agree
- As a result proved here by stationarity, not a general fact, since an infinitely repeated game can sustain play that every finite version rules out
- As a consequence of immediate agreement, since any game in which the first offer is accepted has the same equilibrium for every horizon length
<!-- YW5zOjI= -->
> The infinite game has no terminal node to fold back from, so its solution needs its own argument, here stationarity. That the answers match is a theorem, and MWG stress it is not a general property of infinite games; repeated games are the counterexample, where cooperation is sustainable forever but unravels in every finite repetition with a unique stage equilibrium. Scaling the pie scales payoffs, not shares.
> Ref: Tadelis (2013), §11.3 (p. 228); Gibbons (1992), §2.1.D (p. 70); MWG (1995), p. 298
> Similar: MWG (1995), Exercise 9.B.13, p. 303

## pat

P: Two players split a pie of size 1 by alternating offers with no deadline, player 1 proposing first; player $i$ discounts at $\delta_i \in (0,1)$ per round. Let $x$ be player 1's share when he proposes and $y$ player 2's own share when she proposes.

Q: What is player 1's subgame-perfect share $x^*$?
- $x^* = (1 - \delta_1)/(1 - \delta_1\delta_2)$, from $x = 1 - \delta_1 y$ and $y = 1 - \delta_2 x$, each proposer paying his own discounted share
- $x^* = (1 - \delta_2)/(1 - \delta_1\delta_2)$, from $x = 1 - \delta_2 y$ and $y = 1 - \delta_1 x$, each responder paid her discounted proposer share
- $x^* = \delta_2(1 - \delta_1)/(1 - \delta_1\delta_2)$, from $x = \delta_2 y$ and $y = 1 - \delta_1 x$, each responder paid her discounted proposer share
- $x^* = (1 - \delta_2)/(1 + \delta_1\delta_2)$, from $x = 1 - \delta_2 y$ and $y = 1 + \delta_1 x$, each responder paid her discounted proposer share
<!-- YW5zOjE= -->
> Player 1 must give player 2 what she gets by rejecting, $\delta_2 y$, so $x = 1 - \delta_2 y$; symmetrically $y = 1 - \delta_1 x$. Substituting, $x(1 - \delta_1\delta_2) = 1 - \delta_2$. The responder's own factor goes in the numerator; the swapped formula is the standard error. The third expression is player 2's share $1 - x^*$, and with $\delta_1 = \delta_2 = \delta$ the correct one gives $1/(1 + \delta)$.
> Ref: Tadelis (2013), §11.3 (pp. 228–229); Gibbons (1992), §2.1.D (pp. 70–71)
> Similar: Tadelis (2013), Exercise 11.6, p. 237; MWG (1995), Exercise 9.B.12, p. 303

Q: How does $x^* = (1 - \delta_2)/(1 - \delta_1\delta_2)$ respond to each player's patience?
- $\partial x^*/\partial\delta_1 = -\delta_2(1 - \delta_2)/(1 - \delta_1\delta_2)^2 < 0$ and $\partial x^*/\partial\delta_2 = (1 - \delta_1)/(1 - \delta_1\delta_2)^2 > 0$: patience is costly
- $\partial x^*/\partial\delta_1 = \delta_2(1 - \delta_2)/(1 - \delta_1\delta_2)^2 > 0$ and $\partial x^*/\partial\delta_2 = (1 - \delta_1)/(1 - \delta_1\delta_2)^2 > 0$: all patience helps
- $\partial x^*/\partial\delta_1 = (1 - \delta_2)/(1 - \delta_1\delta_2)^2 > 0$ and $\partial x^*/\partial\delta_2 = -\delta_1(1 - \delta_1)/(1 - \delta_1\delta_2)^2 < 0$: patience is power
- $\partial x^*/\partial\delta_1 = \delta_2(1 - \delta_2)/(1 - \delta_1\delta_2)^2 > 0$ and $\partial x^*/\partial\delta_2 = -(1 - \delta_1)/(1 - \delta_1\delta_2)^2 < 0$: patience is power
<!-- YW5zOjM= -->
> By the quotient rule, $\partial x^*/\partial\delta_1 = (1 - \delta_2)\delta_2/(1 - \delta_1\delta_2)^2 > 0$, and $\partial x^*/\partial\delta_2 = [-(1 - \delta_1\delta_2) + (1 - \delta_2)\delta_1]/(1 - \delta_1\delta_2)^2 = -(1 - \delta_1)/(1 - \delta_1\delta_2)^2 < 0$. Your own patience raises your share, your opponent's lowers it: a patient responder is expensive to buy off because waiting costs her little. The third option has the right signs but drops a factor in each numerator.
> Ref: Tadelis (2013), §11.3 (p. 229); Gibbons (1992), §2.1.D (p. 71)
> Similar: Tadelis (2013), Exercise 11.6, p. 237; MWG (1995), Exercise 9.B.12, p. 303

## leg

P: Baron–Ferejohn legislative bargaining: $N$ legislators, $N$ odd, split a budget of size 1; each period every legislator is the proposer with probability $1/N$; $(N+1)/2$ votes pass a proposal; payoffs are discounted at $\delta \in (0,1)$ per period. Look at the symmetric stationary equilibrium, in which each legislator's expected value at the start of a period is $v = 1/N$.

Q: Under the closed rule (no amendments), how much does the proposer keep?
- $k = 1 - \delta(N - 1)/(2N)$, since she buys $(N - 1)/2$ partners at $\delta/N$ each, their discounted value of continuing
- $k = 1 - (N - 1)/(2N)$, since she buys $(N - 1)/2$ partners at $1/N$ each, their undiscounted value of continuing
- $k = 1 - \delta(N - 1)/N$, since she must pay all $N - 1$ other legislators $\delta/N$ each, their discounted value of continuing
- $k = 1/N$, since by symmetry and immediate agreement each legislator, including the proposer, receives the value $v$
<!-- YW5zOjA= -->
> A responder accepts iff offered at least $\delta v = \delta/N$, her discounted continuation. The proposer needs her own vote plus $(N - 1)/2$ others, pays each exactly $\delta/N$ and gives the rest 0, so $k = 1 - \frac{N-1}{2}\cdot\frac{\delta}{N}$, eqs. (11.6)–(11.8). $v = 1/N$ is the ex ante value, not the proposer's share; buying everyone wastes money on votes she does not need.
> Ref: Tadelis (2013), §11.4.1, eqs. (11.6)–(11.8) (pp. 230–231)
> Similar: Tadelis (2013), Exercise 11.7, p. 237

Q: Let $N = 3$ under an open rule: after a proposal, one of the other two is drawn as amender and can second it or offer an amendment. If the proposer offers each of the others enough that whoever is drawn seconds, how much does she keep?
- $k = 1/(1 + \delta)$, since the amender can reject and become proposer in a two-player Rubinstein game worth $\delta k$ to her
- $k = 1 - 2\delta/3$, since she must pay each of the two others the closed-rule partner price $\delta/3$ to secure their votes
- $k = 1/(1 + 2\delta)$, since each of the two others must get $(1 - k)/2 = \delta k$, the amender's value of proposing next period
- $k = (1 - \delta)/(1 + 2\delta)$, since each of the two others must get $(1 - k)/2 = \delta k$ plus the value of continuing as responder
<!-- YW5zOjI= -->
> Either of the two could be drawn as amender, and an amender's alternative is to propose herself next period, worth $\delta k$ by symmetry. Giving each $(1 - k)/2$ and setting it equal to $\delta k$ gives $1 - k = 2\delta k$, so $k = 1/(1 + 2\delta)$, eq. (11.9). This is below the closed-rule $1 - \delta/3$, since their difference is $\delta(5 - 2\delta)/[3(1 + 2\delta)] > 0$: amendments stop the proposer from playing legislators against each other.
> Ref: Tadelis (2013), §11.4.2.1, eq. (11.9) and footnote 7 (pp. 232–233)
> Similar: Tadelis (2013), Exercise 11.7, p. 237

Q: Let $N = 3$ under an open rule, where one of the two non-proposers is drawn as amender and can second the proposal or amend it. The proposer can instead buy only one partner and risk the excluded player being drawn as amender, for an expected payoff $2/(4 + 2\delta - \delta^2)$. When does this beat paying both, which yields $1/(1 + 2\delta)$?
- When $\delta < \sqrt{3} - 1$, since impatient legislators accept little, so a single cheap partner is enough and the risk of an amendment costs little
- When $\delta > \sqrt{3} - 1$, since the comparison reduces to $\delta^2 + 2\delta - 2 > 0$: patient amenders make buying off both too expensive
- When $\delta > 1/2$, since the comparison reduces to $2\delta - 1 > 0$: once half the budget is lost to delay, buying both stops being worth it
- For every $\delta$, since the risky payoff exceeds the guaranteed one at $\delta = 0$ and both fall at the same rate as $\delta$ rises
<!-- YW5zOjE= -->
> $2/(4 + 2\delta - \delta^2) > 1/(1 + 2\delta)$ iff $2 + 4\delta > 4 + 2\delta - \delta^2$ iff $\delta^2 + 2\delta - 2 > 0$, whose positive root is $\sqrt{3} - 1$. Patient legislators make the guaranteed strategy expensive, so the proposer caters to one and accepts a one-half chance of failure; delay then happens in equilibrium, unlike in Rubinstein's game. At $\delta = 0$ both payoffs equal $1/2$ and $1$, so the risky one does not win everywhere.
> Ref: Tadelis (2013), §11.4.2.2, eqs. (11.10)–(11.13) (pp. 233–235)
> Similar: Tadelis (2013), Exercise 11.7, p. 237

## inf

Q: In Milgrom and Roberts's example a seller has a low or a high private value and a buyer has a low or a high private value, and trade is efficient unless a high-value seller meets a low-value buyer. Why can no price rule make both report truthfully and trade exactly when trade is efficient?
- Because honesty by the low-value seller needs a high price when a low seller meets a high buyer, and honesty by the high-value buyer needs a low one
- Because the high-value seller and the low-value buyer never trade, so a price for that pair of reports cannot be set and the rule is left incomplete
- Because efficient trade requires the price to equal the buyer's value in every trade, and a buyer who expects that has no reason to report truthfully
- Because private values make delay inevitable, and any delay destroys surplus, so immediate efficient agreement is ruled out by Proposition 11.3 itself
<!-- YW5zOjA= -->
> With a low seller and a high buyer the price $p$ is free. A low seller who could claim a high value trades only with high buyers at the high price, so honesty needs $p$ high enough, $p \ge 1.75$ in M&R's numbers; a high buyer who could claim a low value trades only with low sellers at the low price, so honesty needs $p$ low enough, $p \le 1.25$. Both cannot hold. Proposition 11.3's immediate efficient agreement relies on complete information; the general mechanism-design theory behind the result is outside this course.
> Ref: Milgrom & Roberts (1992), Ch. 5, "Bargaining over a Sale", Tables 5.2–5.3 (pp. 140–142)
> Similar: Milgrom & Roberts (1992), Ch. 5, Food for Thought 5.1, pp. 163–164
