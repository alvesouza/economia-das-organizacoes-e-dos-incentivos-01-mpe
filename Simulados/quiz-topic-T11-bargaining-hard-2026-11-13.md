---
quiz: "Topic T11 · Hard conceptual quiz — Strategic bargaining"
tags:
  horizon: "Deadlines, patience and the first-mover advantage"
  options: "Outside options, inside options and delay costs"
  apps: "Delay, multiplicity, legislatures and holdup"
---

## horizon

Q: Two players split a pie of size 1 by alternating offers, player 1 first, before a hard deadline at calendar time $\tau$: an offer is made every $\Delta$ units of time, so there are $T = \tau/\Delta$ rounds, and both discount at rate $r$, so that $\delta = e^{-r\Delta}$. Hold $\tau$ fixed and let $\Delta \to 0$. What happens to player 1's share $(1-(-\delta)^T)/(1+\delta)$?
- It tends to $1/2$ for either parity of $T$, since frequent offers remove the first-mover edge and the deadline edge together, as in Rubinstein's limit
- It tends to $(1 \pm e^{-r\tau})/2$, the sign set by who makes the last offer, since $\delta^T = e^{-r\tau}$ stays fixed while the rounds multiply
- It tends to $1/(1+e^{-r\tau})$, the Rubinstein share computed at the discount factor of the whole bargaining window, for either parity of $T$
- It tends to $1$ for odd $T$ and to $0$ for even $T$, since with $\delta \to 1$ only the last word matters and waiting costs nothing at all
<!-- YW5zOjE= -->
> Right: $\delta^T = e^{-r\Delta\cdot\tau/\Delta} = e^{-r\tau}$ does not move as $\Delta \to 0$, while $1+\delta \to 2$. So the share tends to $(1+e^{-r\tau})/2$ when player 1 has the last offer (odd $T$) and to $(1-e^{-r\tau})/2$ when player 2 has it; with $r = 1$, $\tau = 2$ the two limits are $0.568$ and $0.432$ (checked numerically). The first-mover edge vanishes, but the last-mover edge survives with weight $e^{-r\tau}$, the present value of the final ultimatum. Wrong: the equal split needs the horizon to go to infinity first, which here means $r\tau \to \infty$; the "$1$ or $0$" answer takes $\delta \to 1$ at fixed $T$ (Tadelis's footnote 2), but here $T$ grows with $\delta$; the third option plugs the wrong object into the infinite-horizon formula.
> Ref: Tadelis (2013), §11.2, eqs. (11.1)–(11.3) and footnote 2 (pp. 226–227); MWG (1995), Example 9.AA.1 (p. 297)
> Similar: Tadelis (2013), Exercise 11.3, p. 236

Q: In Rubinstein's infinite-horizon game over a pie of size 1, both players discount at $\delta \in (0,1)$ per round and the first proposer keeps $1/(1+\delta)$, so her advantage over the responder is $(1-\delta)/(1+\delta)$. What is the right reading of this advantage?
- It is the value of the last word: the first proposer is also the one who would make the final offer if bargaining went on, and that is worth $(1-\delta)/(1+\delta)$
- It is a commitment advantage: moving first lets her commit to a demand, so it persists as $\delta \to 1$ and disappears only in the limit $\delta \to 0$
- It is half of the pie destroyed by discounting, $(1-\delta)$ per round, which the two players share equally in every round in which they bargain
- It is the responder's cost of waiting one round to propose: she gets $\delta$ times the proposer's share, so the edge is $(1-\delta)$ times that share
<!-- YW5zOjM= -->
> Right: the responder accepts exactly $\delta x^*$, the discounted value of proposing next round, so the edge is $x^* - \delta x^* = (1-\delta)x^* = (1-\delta)/(1+\delta)$. It is the price of one round of delay to the responder, which is why it vanishes as $\delta \to 1$ and becomes the whole pie (the ultimatum game) as $\delta \to 0$. Wrong: there is no last round in the infinite game, so no last-word edge; the commitment reading gets both limits backwards; and nothing is destroyed on the path, since agreement is immediate.
> Ref: Tadelis (2013), §11.3, eqs. (11.4)–(11.5) and the equilibrium strategies (pp. 228–229); Gibbons (1992), §2.1.D (pp. 70–71)
> Similar: Tadelis (2013), Exercise 11.6, p. 237

Q: Two players alternate offers over a pie of size 1 with no deadline and no discounting at all, $\delta = 1$. In the discounted game, the Shaked–Sutton argument ties the first proposer's best and worst subgame-perfect payoffs by $\underline v = 1 - \delta\bar v$ and $\bar v = 1 - \delta\underline v$. What does the argument deliver at $\delta = 1$?
- Nothing: both equations become $\bar v + \underline v = 1$, and indeed every split of the pie is a subgame-perfect outcome when waiting costs nothing
- The equal split: the equations give $\bar v = \underline v = 1/2$, the limit of $1/(1+\delta)$, so patience alone pins down a fair division of the whole pie
- The whole pie to the first proposer: with no cost of delay the responder gains nothing by rejecting, so she accepts any offer in round 1
- No equilibrium at all: with $\delta = 1$ some player always gains by rejecting, so perpetual disagreement is the only outcome the equations allow
<!-- YW5zOjA= -->
> Right: uniqueness comes from subtracting the equations, $(1-\delta)(\bar v - \underline v) = 0$, which forces $\bar v = \underline v$ only if $\delta < 1$. At $\delta = 1$ the two equations are the same line, and any split $x$ is supported by "always demand $x$, accept iff offered at least your $x$-share": a rejection costs nothing and wins nothing, so no deviation pays. Wrong: $1/2$ is the limit of the unique discounted outcome, not a solution at $\delta = 1$; the proposer taking the whole pie is only one of these many outcomes, since a responder who loses nothing by waiting can equally well hold out for any other share; and agreement-in-round-1 equilibria exist, so disagreement is not forced.
> Ref: Tadelis (2013), §11.3, eqs. (11.4)–(11.5) (pp. 228–229); MWG (1995), Example 9.AA.2 and the remark on sensitivity to preferences (pp. 297–298)
> Similar: MWG (1995), Exercise 9.B.13, pp. 302–303

## options

Q: In Rubinstein's game with common discount factor $\delta$, player 1 proposes first, and player 2, after rejecting any offer, may quit for good and take an outside option worth $w$ instead of making a counteroffer. Without the option she would get $\delta/(1+\delta)$. How does $w$ affect the equilibrium split?
- Player 2's share rises one for one with $w$ at every level, to $\delta/(1+\delta) + w$, since the option adds to what she secures by rejecting
- Player 2 gets the Nash split with threat point $w$, namely $w + (1-w)/2$, since a credible outside option sets the disagreement point of the bargaining
- The option is irrelevant while $w \le \delta/(1+\delta)$; above that she gets exactly $w$, since quitting binds only when it beats bargaining on
- The option always lowers player 1's share, to $(1-w)/(1+\delta)$, since every offer must now leave player 2 a fixed fraction of her option value
<!-- YW5zOjI= -->
> Right (the outside option principle): player 1 must give player 2 the larger of $w$ and $\delta$ times what she gets as next proposer. If $w \le \delta/(1+\delta)$, the threat to quit is worth less than the threat to counteroffer and the Rubinstein split stands; if $w$ is larger, player 1 pays exactly $w$ and keeps $1-w$ (checked by iterating the stationary equations at $\delta = 0.9$: $w = 0.3$ leaves $0.526$ to player 1, $w = 0.7$ leaves $0.3$). Wrong: the option is not added to the bargaining payoff, because she cannot both quit and counteroffer; treating it as a Nash threat point overstates its effect; and the formula $(1-w)/(1+\delta)$ has no basis in the acceptance condition.
> Ref: Tadelis (2013), §11.3 and the Remark on outside options (p. 229); `Aula/aula-02-notes.md` §5.1 for threat points. The principle is due to Binmore, Shaked and Sutton (1989), cited from memory, not from the course books

Q: A union and a firm bargain over a surplus of size 1 by alternating offers, with a common discount factor $\delta$ close to 1. Compare two gains for the union, each worth $b$ in present value if disagreement lasted forever: (i) strike pay received in every round without agreement; (ii) a job offer elsewhere that the workers can take by walking away for good. Which statement is correct?
- Strike pay raises the union's share for any $b > 0$, by about $b/2$; the job offer changes nothing unless $b$ exceeds the union's half of the surplus
- Both raise the union's share by about $b/2$, since in the limit $\delta \to 1$ each acts as a disagreement payoff entering the Nash product the same way
- The job offer raises the union's share for any $b > 0$, by about $b/2$; strike pay changes nothing, since it is paid only while no agreement is in place
- Neither changes the split as $\delta \to 1$, since agreement is immediate in equilibrium, so payoffs that accrue only off the path cannot matter
<!-- YW5zOjA= -->
> Right: strike pay is an inside option, received while bargaining continues; it lowers the union's cost of rejecting in every round, and the stationary equations give the union, as proposer, $(1 + \delta b)/(1+\delta)$, which tends to $(1+b)/2 = 1/2 + b/2$ as $\delta \to 1$ (checked numerically). The job offer is an outside option: it is a constraint, binding only if $b > 1/2$. Wrong: only the inside option acts like a threat point in the Nash product; the third option swaps the two; and off-path payoffs matter precisely because they price the offer accepted on the path.
> Ref: Tadelis (2013), Remark on outside options and Muthoo (1999) (p. 229); §11.3 (pp. 228–229); `Aula/aula-02-notes.md` §5.1–5.2 (Nash solution and its strategic foundation). Inside and outside options are not worked in the course books; the stationary equations were checked in Python

Q: Two players alternate offers over a pie of size 1, player 1 first, over a very long horizon, but instead of discounting, player $i$ pays a fixed cost $c_i > 0$ for each round of delay, with $c_1 < c_2$. How does the split compare with the discounted game, where shares move smoothly with the two discount factors?
- The shares move smoothly with the costs, player 1 getting about $c_2/(c_1 + c_2)$, the analogue of the frequent-offer split set by relative impatience
- The split is equal whatever the two costs are, since fixed costs do not depend on the size of the pie and so cancel out of every acceptance condition
- Player 1 takes (almost) the whole pie however small $c_2 - c_1$ is; were $c_1 > c_2$ he would get only $c_2$, so power jumps to the cheaper waiter
- Player 1 gets exactly $1 - c_2$, the pie minus the responder's one-round cost, whichever cost is larger, as the analogue of the share $1 - \delta_2$
<!-- YW5zOjI= -->
> Right: with fixed costs a responder accepts any offer within one round's cost of her continuation, and those cost gaps accumulate in favour of the cheaper waiter. Backward induction over 200 rounds with $(c_1, c_2) = (0.1, 0.2)$ gives player 1 the whole pie; with $(0.2, 0.1)$ it gives him $0.1 = c_2$ (checked numerically; the infinite-horizon result is Rubinstein's 1982 paper). With two rounds the share is $c_2$ (Tadelis Exercise 11.4a), so "$1 - c_2$" fails already there. Wrong: unlike discounting, there is no smooth trade-off, so the $c_2/(c_1+c_2)$ formula and the equal split are both wrong; equal costs give many equilibria instead.
> Ref: Tadelis (2013), Exercise 11.4 (p. 236); MWG (1995), remark that the outcome is sensitive to preferences, with Exercises 9.B.7 and 9.B.13 (pp. 298, 302–303)
> Similar: MWG (1995), Exercise 9.B.13 (with 9.B.7, which it builds on), pp. 302–303

## apps

Q: Strikes and long delays before agreement are common, yet in alternating-offer bargaining with complete information every subgame-perfect equilibrium agrees in round 1, whatever the horizon and the two discount factors. Which change to the model can make costly delay happen on the equilibrium path?
- Letting the two players discount at different rates, since the more patient side then gains by holding out until the impatient side gives in
- Giving one side private information about its own valuation, since delay then lets a strong type show it can wait, which a weak type finds too costly
- Lengthening the horizon, since with more rounds left the responder's continuation value rises and she can profitably reject the first offer and wait
- Letting offers be made more often, since with $\delta$ close to 1 waiting costs almost nothing, so both sides are willing to reject for many rounds
<!-- YW5zOjE= -->
> Right: with complete information, any delayed agreement wastes pie that a slightly better round-1 offer could share, so both prefer to skip it (Proposition 11.3). Once a player's value is private, delay becomes a costly signal or a screening device: rejecting shows the player can afford to wait, so wasting time is part of the equilibrium. Wrong: different discount factors change the split, $x^* = (1-\delta_2)/(1-\delta_1\delta_2)$, but it is still accepted at once; a longer horizon changes the offer, not its acceptance; frequent offers make waiting cheap but do not make it useful.
> Ref: Tadelis (2013), Proposition 11.3 (p. 226); Gibbons (1992), §2.1.D opening (p. 68) and §4.3.B (p. 218); Milgrom & Roberts (1992), "Bargaining over a sale" (pp. 140–142)
> Similar: Gibbons (1992), Problem 4.13, p. 251

Q: In Baron–Ferejohn closed-rule bargaining, $N$ legislators ($N$ odd) split a budget of 1; each period one is drawn as proposer with probability $1/N$, $(N+1)/2$ votes pass a proposal, and payoffs are discounted at $\delta$. The proposer keeps $1 - \delta(N-1)/(2N)$. For $N = 3$, why does she keep about $2/3$ as $\delta \to 1$, although Rubinstein's first-mover edge vanishes in that limit?
- Because the closed rule lets her make one take-it-or-leave-it offer to all legislators together, which alternating offers never allow, so the limit is an ultimatum share
- Because the excluded legislator holds a veto under the closed rule, so she must pay her partner the full value of that veto, a value that falls as $\delta$ rises
- Because each legislator's continuation value is $1/2$ in a two-member coalition, and she needs only one partner, whom she pays $\delta/2$, keeping the rest of the budget
- Because she needs one partner, priced at $\delta$ times a continuation value of $1/3$, and both others compete for that role, so patience cannot erode her share
<!-- YW5zOjM= -->
> Right: a legislator's value before the draw is $1/N = 1/3$, since anyone may be the proposer and the budget is always fully shared; the proposer buys the $(N-1)/2 = 1$ cheapest vote at $\delta/3$ and keeps $1 - \delta/3 \to 2/3$. The excluded legislator gets nothing, and competition to be included keeps the price at the continuation value. In Rubinstein's game the single responder's continuation is the proposer's own share, which is why the edge vanishes there. Wrong: she needs a majority, not unanimity, and there is no veto; the continuation value is $1/3$, not $1/2$.
> Ref: Tadelis (2013), §11.4.1, eq. (11.8) (pp. 230–231); §11.3 (pp. 228–229)
> Similar: Tadelis (2013), Exercise 11.7, p. 237

Q: Before bargaining, a supplier chooses a relationship-specific investment $I$ at cost $C(I)$, increasing and convex, that creates a surplus $S(I)$, increasing and concave; the investment is sunk and cannot be contracted on. The buyer then makes the first offer in Rubinstein bargaining over $S(I)$, both discounting at $\delta$. How does the supplier's investment compare with the efficient level, where $S'(I) = C'(I)$?
- It is too low: the supplier solves $\frac{\delta}{1+\delta}S'(I) = C'(I)$, capturing under half of each marginal unit, though bargaining wastes nothing
- It is efficient: Rubinstein bargaining reaches agreement at once and wastes no surplus, so the supplier's choice takes the full value of the investment into account
- It is zero: once $C(I)$ is sunk the buyer extracts all the surplus by making the first offer, so any positive investment is a pure loss for the supplier
- It is too high: investing more raises the supplier's stake in the bargaining, so she over-invests to shift the split of $S(I)$ in her own favour
<!-- YW5zOjA= -->
> Right: as responder the supplier receives $\delta/(1+\delta)$ of whatever surplus exists, so her marginal return is $\frac{\delta}{1+\delta}S'(I) < S'(I)$ and she stops short of the efficient level; even with $\delta \to 1$ she internalizes only half. This is holdup: ex post efficiency of the bargain does not deliver ex ante efficient investment. Wrong: immediate agreement concerns the split, not the incentive to invest; the buyer gets everything only in an ultimatum game, not with alternating offers; and the investment raises the pie, not her share of it.
> Ref: Tadelis (2013), Exercise 11.2 "Holdup" (p. 236) and §11.3 (pp. 228–229); `Aula/aula-02-notes.md` §5 (value maximization and the split)
> Similar: Tadelis (2013), Exercise 11.2, p. 236

Q: In Rubinstein's infinite-horizon game with discount factor $\delta \in (0,1)$, consider Nash equilibria that need not be subgame perfect. Which outcomes can they produce?
- Only immediate agreement, but on any split, since delay wastes surplus, so every Nash equilibrium admits a profitable switch to an earlier, slightly better offer
- Only the split $1/(1+\delta)$, since the Shaked–Sutton bounds hold in every Nash equilibrium and the stationary structure of the game pins down the payoffs
- Any split, reached in any round, since threats to reject everything off the path are never tested in a Nash equilibrium; subgame perfection removes them
- Any split, but only in round 1 or round 2, since a responder who rejects twice reveals that her threat to keep on rejecting offers is not credible
<!-- YW5zOjI= -->
> Right: fix a split $x$ and a round $t$. Let both reject every offer before $t$, and let the responder in round $t$ accept only $x$, with perpetual disagreement after any other move. On the path each player's best response is to go along, because any deviation meets a rejection that is never tested. Tadelis makes the same point for the finite game: Nash cannot pin down the split or even the timing. Wrong: the profitable earlier offer exists only if the responder would accept it, which a Nash profile need not have; the Shaked–Sutton bounds use subgame perfection; and Nash equilibrium places no credibility test on rejections.
> Ref: Tadelis (2013), Proposition 11.1 (p. 223) and §11.2 (p. 224); §11.3 (pp. 228–229)
> Similar: Tadelis (2013), Exercise 11.1, p. 236
