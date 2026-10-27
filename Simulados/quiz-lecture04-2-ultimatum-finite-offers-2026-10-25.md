---
quiz: "Lecture 4 · Quiz 2 of 3 — The ultimatum game and finite alternating offers (estimated unit, written before the lecture)"
tags:
  ult: "The ultimatum game: Nash versus subgame perfection"
  fin: "Finite alternating offers: backward induction to round 1"
  lim: "Last-mover and first-mover advantage, and the order of limits"
---

## ult

Q: In a one-round bargaining game player 1 proposes a split $(x, 1 - x)$ of a pie of size 1 and player 2 accepts or rejects; rejection gives both 0. Why can every $x^* \in [0,1]$ be a Nash equilibrium outcome?
- Because player 2 is indifferent between all offers when the pie is small, so any acceptance rule is a best response and any $x^*$ can be the offer
- Because player 1 can commit to $x^*$ in advance, and once the commitment is common knowledge player 2 has no choice except to accept it
- Because the rule "accept iff $x \le x^*$" makes $x^*$ player 1's best offer, and its rejections are never tested on the equilibrium path
- Because every split is Pareto optimal, and Nash equilibrium selects among Pareto optimal outcomes according to which one the players expect
<!-- YW5zOjI= -->
> Against "accept iff $x \le x^*$", any $x > x^*$ yields 0 and any $x < x^*$ yields less than $x^*$, so $x^*$ is optimal for player 1. Given $x^*$ is offered, accepting yields $1 - x^* \ge 0$, so the rule is a best response; its rejections of larger $x$ are off the path and cost nothing. Nash equilibrium "has no bite" here: it never asks whether rejecting a positive offer would be rational if it were tested.
> Ref: Tadelis (2013), Prop. 11.1 (p. 223)
> Similar: Tadelis (2013), Exercise 11.1, p. 236

Q: In a one-round game where player 1 proposes $(x, 1 - x)$ of a pie of size 1 and player 2 accepts or rejects, with rejection giving both 0, the unique subgame-perfect equilibrium has player 1 offer $x = 1$ and player 2 accept it, although she is indifferent. Why must she accept at indifference?
- Because if she rejected $x = 1$ and accepted every $x < 1$, player 1 would have no best response, since any offer below 1 is beaten by one closer to 1
- Because ties are broken in favour of acceptance by assumption in Tadelis's protocol, and a different tie-breaking rule would leave the equilibrium unchanged
- Because rejecting $x = 1$ is weakly dominated by accepting it, and subgame perfection eliminates every weakly dominated action at each decision node
- Because if she rejected $x = 1$, player 1 would offer a little less instead, and the equilibrium would then give player 2 a small but positive share
<!-- YW5zOjA= -->
> Any $x < 1$ gives player 2 a positive amount, so sequential rationality makes her accept it. At $x = 1$ she is indifferent; if she rejected, player 1's payoff $\sup_{x<1} x = 1$ would not be attained, since $x'' = x' + (1 - x')/2$ beats any $x' < 1$. A strategy that leaves the proposer without a best response cannot be part of an equilibrium, so acceptance at indifference is forced, not assumed. MWG's penny grid gives the same limit.
> Ref: Tadelis (2013), Prop. 11.2 and footnote 1 (p. 223); MWG (1995), footnote 16 (p. 297)
> Similar: Tadelis (2013), Exercise 11.2, p. 236; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 1, p. 154

Q: In laboratory ultimatum games proposers typically offer 25–50 per cent of the pie and responders usually reject offers below about 20–25 per cent. What does this imply for the subgame-perfect prediction?
- That subgame perfection is the wrong concept for bargaining, since real responders do not act sequentially rationally once they see the offer on the table
- That Nash equilibrium is the right concept for bargaining, since the observed rejections are exactly the off-path threats of its acceptance rules
- That players cannot do backward induction in one round, since a single round already demands too many levels of reasoning about the other player
- That payoffs are not money alone: if a responder's utility falls with the proposer's advantage, rejecting a small offer is sequentially rational
<!-- YW5zOjM= -->
> The prediction $(1, 0)$ assumed utility equals money. If the responder dislikes unequal splits, rejecting a low offer can be her best action at that node, and the subgame-perfect equilibrium of that game gives her a positive share. The experiments refute the payoff specification, not subgame perfection. The magnitudes are Camerer's (2003) as reported by Tadelis; they are quoted, not derived.
> Ref: Tadelis (2013), Remark (pp. 223–224)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 1, p. 154; Milgrom & Roberts (1992), Food for Thought 5.1, pp. 163–164

## fin

P: Two players split a pie of size 1. Player 1 proposes in odd rounds and player 2 in even rounds; $x$ always denotes player 1's share; a rejected offer moves the game to the next round, and both discount at $\delta \in (0,1)$ per round. If no offer is accepted by round $T$, both get 0.

Q: What is player 1's share in the unique subgame-perfect equilibrium, for any horizon $T \ge 1$?
- $x_1(T) = (1 - \delta^T)/(1 - \delta)$, the sum of the discounted pies over the $T$ rounds in which the game can still be played
- $x_1(T) = (1 - (-\delta)^T)/(1 + \delta)$, the alternating sum $1 - \delta + \delta^2 - \dots$ with $T$ terms from backward induction
- $x_1(T) = (1 + \delta^T)/(1 + \delta)$, the value of the odd-horizon game, which holds for even $T$ as well by the same induction
- $x_1(T) = (1 - (-\delta)^{T-1})/(1 + \delta)$, the alternating sum with $T - 1$ terms since the last round is an ultimatum game
<!-- YW5zOjE= -->
> The last proposer takes the pie; each step back, the proposer offers the responder exactly the discounted value of rejecting. That builds $x_1 = 1 - \delta + \delta^2 - \dots + (-\delta)^{T-1} = \sum_{k=0}^{T-1}(-\delta)^k = (1 - (-\delta)^T)/(1 + \delta)$. For odd $T$ it equals $(1 + \delta^T)/(1 + \delta)$, eq. (11.1); for even $T$ it is $(1 - \delta^T)/(1 + \delta)$, so the odd-$T$ formula fails there. With $T = 1$ the correct expression gives 1, the ultimatum game; the $T - 1$ version gives 0.
> Ref: Tadelis (2013), §11.2, eq. (11.1) (pp. 225–226); MWG (1995), Example 9.AA.1 (pp. 296–297)
> Similar: Tadelis (2013), Exercise 11.3, p. 236; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 16, pp. 198–199

Q: Why does every subgame-perfect equilibrium of this game reach agreement in round 1?
- Because the responder in round 1 is always offered at least what she could get by waiting, so a rejection would never raise her payoff in any subgame
- Because the deadline makes the last round an ultimatum game, and backward induction rules out any rejection in a game that has a last round
- Because a strategy that delays agreement violates the one-stage deviation principle at the round in which the accepted offer is finally made
- Because delay shrinks the pie, so player 1 could offer player 2 a bit more than her continuation value now and keep more than he gets by waiting
<!-- YW5zOjM= -->
> Suppose agreement came later with payoffs $(v_1, v_2)$. Discounting wastes pie, so $v_1 + v_2 < 1$. Player 1 can offer $x = 1 - v_2 - \varepsilon$ in round 1; player 2 gets $v_2 + \varepsilon$ now, more than by continuing, so she accepts, and for small $\varepsilon$ player 1 gets $1 - v_2 - \varepsilon > v_1$. The argument uses discounting, not the deadline, which is why it carries over to the infinite game.
> Ref: Tadelis (2013), Prop. 11.3 (p. 226)
> Similar: Tadelis (2013), Exercise 11.4, p. 236

Q: Set $T = 3$. What does player 2 receive in round 1, and how is it computed?
- $\delta(1 - \delta)$, since rejecting leads to round 2, where as proposer she keeps $1 - \delta$, worth $\delta(1 - \delta)$ in round 1
- $\delta$, since a rejection costs her one round of discounting, so player 1 must give her the discounted value $\delta$ of the whole pie
- $\delta^2$, since her rejection leads to the final round two rounds later, where player 1 makes an ultimatum offer and the pie is worth $\delta^2$
- $1 - \delta + \delta^2$, since she is offered the alternating sum of the discounted pies in the three rounds in which the game can be played
<!-- YW5zOjA= -->
> Round 3: player 1 takes everything. Round 2: player 1 accepts $x \ge \delta$, so player 2 proposes $x = \delta$ and keeps $1 - \delta$. Round 1: player 2 accepts iff $1 - x \ge \delta(1 - \delta)$, so she gets $\delta(1 - \delta)$ and player 1 keeps $1 - \delta + \delta^2$. The responder is paid her discounted continuation as next proposer, not the discounted pie; the two coincide only with two rounds. The last option is player 1's share, not player 2's.
> Ref: Tadelis (2013), §11.2 table (pp. 225–226); Gibbons (1992), §2.1.D (pp. 68–70)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 17, pp. 199–200

P:

Q: Three rounds of alternating offers over a pie of size 1: player 1 proposes in rounds 1 and 3, player 2 in round 2, rejection after round 3 gives both 0, and player $i$ discounts at $\delta_i \in (0,1)$. What is player 1's subgame-perfect share in round 1?
- $s_1 = 1 - \delta_1(1 - \delta_2)$, since player 2's round-2 share must be discounted at player 1's own rate before player 1 can offer it
- $s_1 = \delta_1(1 - \delta_2)$, since player 1 keeps what player 2 would leave him as proposer in round 2, discounted at his own rate
- $s_1 = 1 - \delta_2(1 - \delta_1)$, since player 2 keeps $1 - \delta_1$ as round-2 proposer, which she discounts at her own rate
- $s_1 = 1 - \delta_2 + \delta_2^2$, since the responder's discount factor is the one that matters at both of the steps of the induction
<!-- YW5zOjI= -->
> Round 3: player 1 takes the pie. Round 2: player 1 accepts $s_2 \ge \delta_1$, so player 2 offers $\delta_1$ and keeps $1 - \delta_1$. Round 1: player 2 accepts iff $1 - s_1 \ge \delta_2(1 - \delta_1)$, so $s_1 = 1 - \delta_2(1 - \delta_1)$. Each responder discounts her continuation at her own rate; swapping the factors is the standard error. With $\delta_1 = \delta_2 = \delta$ this is $1 - \delta + \delta^2$.
> Ref: Gibbons (1992), §2.1.D (pp. 68–70); Tadelis (2013), §11.2 (pp. 224–227)
> Similar: Tadelis (2013), Exercise 11.5, pp. 236–237

Q: In Gibbons's three-period model, player 1 proposes in round 1, player 2 in round 2, and if both are rejected the settlement $(s, 1 - s)$ is imposed in round 3; both discount at $\delta \in (0,1)$. What does player 1 offer to keep in round 1?
- $s_1^* = 1 - \delta(1 - s)$, since player 2 rejects only if she expects the imposed settlement to give her more than her round-1 share
- $s_1^* = 1 - \delta + \delta^2 s$, since player 2 as round-2 proposer keeps $1 - \delta s$, worth $\delta(1 - \delta s)$ in round 1
- $s_1^* = 1 - \delta + \delta s$, since player 2 as round-2 proposer keeps $1 - s$, which is worth $\delta(1 - s)$ to her in round 1
- $s_1^* = \delta^2 s$, since player 1 can secure the settlement $s$ two rounds later and must be offered its discounted value now
<!-- YW5zOjE= -->
> Round 2: player 1 accepts $s_2 \ge \delta s$, so player 2 offers $s_2^* = \delta s$ and keeps $1 - \delta s$, more than the $\delta(1 - s)$ she would get by waiting. Round 1: player 2 accepts iff $1 - s_1 \ge \delta(1 - \delta s)$, so $s_1^* = 1 - \delta + \delta^2 s$. With $s = 1$ this is the $T = 3$ share; the map $f(s) = 1 - \delta + \delta^2 s$ is what Gibbons iterates to solve the infinite game.
> Ref: Gibbons (1992), §2.1.D (pp. 68–70)
> Similar: Gibbons (1992), Problem 2.19, p. 137

## lim

Q: In alternating-offer bargaining over a pie of size 1, player 1 proposes first, both discount at $\delta \in (0,1)$, and the game ends after $T$ rounds; for odd $T$ player 1's share is $(1 + \delta^T)/(1 + \delta)$. What do the two iterated limits of this share give, and why do they differ?
- $\lim_{\delta \to 1}\lim_{T \to \infty}$ gives $1/2$ and $\lim_{T \to \infty}\lim_{\delta \to 1}$ gives $1$: patience first keeps the last proposer's take-it-or-leave-it edge
- $\lim_{\delta \to 1}\lim_{T \to \infty}$ gives $1$ and $\lim_{T \to \infty}\lim_{\delta \to 1}$ gives $1/2$: a long horizon first keeps the last proposer's take-it-or-leave-it edge
- Both give $1/2$: the share is continuous in $(\delta, T)$, so taking the limits in either order removes both the first-mover and the last-mover edge
- Both give $1/(1 + \delta)$ evaluated at $\delta = 1$: the order is irrelevant because the deadline effect $\delta^T$ vanishes under either one
<!-- YW5zOjA= -->
> With $T \to \infty$ first, $\delta^T \to 0$ and the share is $1/(1 + \delta)$, which tends to $1/2$ as $\delta \to 1$, eqs. (11.2)–(11.3). With $\delta \to 1$ first at fixed odd $T$, the share is $(1 + 1)/(1 + 1) = 1$, and lengthening the game keeps it at 1: without a cost of waiting only the last word matters. "Patient players split equally" needs the horizon to go first.
> Ref: Tadelis (2013), eqs. (11.2)–(11.3) and footnote 2 (pp. 226–227)
> Similar: Tadelis (2013), Exercise 11.3, p. 236

Q: In alternating-offer bargaining over a pie of size 1 with player 1 proposing first, common discount factor $\delta \in (0,1)$ and deadline $T$, player 1's share is $(1 - (-\delta)^T)/(1 + \delta)$. How does the gap between this share and $1/(1 + \delta)$ behave?
- It equals $\delta/(1 + \delta)$ in absolute value for every $T$, so the last mover's edge is a fixed premium that a longer deadline cannot erode
- It equals $\delta^{T}/(1 - \delta)$ in absolute value, so it vanishes as $T$ grows and vanishes faster the more patient the two players are
- It equals $\delta^{T}/(1 + \delta)$ in absolute value, so it decays geometrically in $T$ and decays more slowly the more patient the players are
- It equals $(1 - \delta^{T})/(1 + \delta)$ in absolute value, so it grows with $T$ and converges to the first-mover share as the deadline recedes
<!-- YW5zOjI= -->
> Subtracting, $x_1(T) - 1/(1 + \delta) = -(-\delta)^T/(1 + \delta)$: positive for odd $T$ (player 1 has the last word), negative for even $T$, with absolute value $\delta^T/(1 + \delta)$. It decays like $\delta^T$, so the last-mover advantage survives longer when $\delta$ is close to 1. What remains in the limit, $1/(1 + \delta) > 1/2$, is the first-mover advantage created by discounting, not by the deadline.
> Ref: Tadelis (2013), eqs. (11.1)–(11.2) (pp. 226–227); MWG (1995), Example 9.AA.1 (p. 297)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 16, pp. 198–199
