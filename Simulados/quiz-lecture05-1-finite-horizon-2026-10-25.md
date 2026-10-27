---
quiz: "Lecture 5 · Quiz 1 of 3 — Finite repetition, carrot and stick, renegotiation"
tags:
  unravel: "A unique stage equilibrium unravels"
  carrot: "Two stage equilibria: carrot and stick"
  reneg: "Renegotiation of punishments"
---

## unravel

Q: A stage game $G$ has a unique Nash equilibrium $a^*$. It is repeated a known number $T \ge 2$ of times with common discount factor $\delta \in (0,1]$. Which statement describes the subgame-perfect equilibria of $G(T,\delta)$?
- There are many, since for $\delta$ near 1 and $T$ large the players can cooperate in every period except the last few
- There is one in outcomes, $a^*$ every period on the path, but off-path play after a deviation can be any stage profile
- There is exactly one: $a^*$ in every period after every history, whatever the values of $T$ and $\delta$ happen to be
- There is exactly one only when $\delta < 1$, since with $\delta = 1$ summed payoffs leave every first-period profile tied
<!-- YW5zOjI= -->
> In the last period no future depends on the action, so play is a stage equilibrium after every history, and only $a^*$ exists. One period earlier the continuation is the same constant in every cell, so the stage game is strategically $G$ again, and induction reaches period 1. Off-path play is pinned down too, because the argument holds after every history. Neither $T$ nor $\delta$ enters: Gibbons states the result with summed payoffs ($\delta = 1$).
> Ref: Tadelis (2013), Def. 10.1 (p. 190), Prop. 10.1 (p. 192), Prop. 9.3 (p. 181); Gibbons (1992), §2.3.A (pp. 82–84)
> Similar: Cabral (2017), Exercise 7.13, p. 182; Gibbons (1992), Exercise 2.12, p. 135

Q: In the proof that a unique stage equilibrium $a^*$ unravels $G(T,\delta)$, suppose $a^*$ is played from stage $t+1$ on after every history. What is player $i$'s payoff from a stage-$t$ profile $a$, and why does it settle play at $t$?
- $u_i(a) + \sum_{s=t+1}^{T}\delta^{s-t}u_i(a^*)$, where the sum is the same in every cell, so stage-$t$ best responses are those of $G$
- $u_i(a) + \sum_{s=t+1}^{T}\delta^{s-t}u_i(a)$, where the sum scales each cell by its own payoff, so the ranking of cells in $G$ is kept
- $u_i(a)\,\big(1 + \sum_{s=t+1}^{T}\delta^{s-t}\big)$, where the factor multiplies all cells equally, so stage-$t$ best responses are those of $G$
- $u_i(a) + \delta^{T-t}u_i(a^*)$, where only the final stage carries a payoff that can depend on history, so stage $t$ acts as the last
<!-- YW5zOjA= -->
> From $t+1$ on, $a^*$ is played whatever happens at $t$, so the continuation is $\sum_{s=t+1}^{T}\delta^{s-t}u_i(a^*)$, a constant added to every cell. Adding a constant changes no best response, so the unique equilibrium at $t$ is $a^*$. The second and third options wrongly assume that today's profile is repeated tomorrow; the fourth forgets the intermediate stages. A continuation that does not depend on today's action can neither reward nor punish.
> Ref: Tadelis (2013), Prop. 10.1 (p. 192), fn. 3 (p. 181); Gibbons (1992), Figure 2.3.2 (p. 83)
> Similar: Tadelis (2013), Exercise 10.7(b), pp. 217–218

Q: The 500-round prisoner's dilemma has finking in every round as its only subgame-perfect equilibrium. Which change to the setting could make cooperation in the early rounds subgame-perfect?
- Raising the discount factor close to one, so that the later rounds weigh far more than any one-round gain from finking
- Lengthening the game to many thousands of rounds, so that the end is too distant to affect what players do at the start
- Letting each player see the full history of play, so that a fink in one round can be answered by a fink in the next one
- Adding a second stage equilibrium that both prefer, or removing the known last round, so tomorrow can depend on today
<!-- YW5zOjM= -->
> The unraveling uses only a known last period and a unique stage equilibrium. Patience and length do not enter the induction, and perfect monitoring is already assumed. A second, Pareto-better stage equilibrium gives the last rounds a carrot and a stick; an uncertain end (no last period) lets the repeated game create its own carrot. Either breaks the constant continuation that drives the proof.
> Ref: Tadelis (2013), §10.1 (pp. 190–192), §10.2.1 (pp. 193–194); Gibbons (1992), §2.3.A (pp. 84–88)
> Similar: Cabral (2017), Exercise 7.8, p. 180

## carrot

P: A stage game has a prisoner's-dilemma block in which $(M,m)$ pays $a$ to each player and the best one-stage deviation from $(M,m)$ pays the deviator $b > a$. It also has two Pareto-ranked Nash equilibria, $(R,r)$ paying $r$ to each and $(F,f)$ paying $p < r$ to each, with $r - p \ge b - a$. The game is repeated with discount factor $\delta \in (0,1)$; after any deviation from the prescribed path, play switches to $(F,f)$ until the end.

Q: The game is played twice: $(M,m)$ in stage 1, then $(R,r)$ if stage 1 was $(M,m)$ and $(F,f)$ otherwise. When is this profile a subgame-perfect equilibrium?
- $\delta \ge (b-a)/(b-p)$, the one-stage gain over the gain the deviator makes when measured against the stick
- $\delta \ge (b-a)/(r-p)$, the one-stage gain over the second-stage gap between the carrot and the stick
- $\delta \ge (b-a)/(b-a+r-p)$, the one-stage gain over the sum of that gain and the carrot-stick gap
- $\delta \ge (r-p)/(b-a)$, the carrot-stick gap over the one-stage gain that the deviator makes today
<!-- YW5zOjE= -->
> Stage 2 prescribes a stage equilibrium after every history, so only stage 1 needs checking: cooperate gives $a + \delta r$, the best deviation $b + \delta p$. Cooperation holds iff $\delta(r-p) \ge b-a$. With Tadelis's numbers ($a=4$, $b=5$, $r=3$, $p=1$) this is $\delta \ge 1/2$. The third option is the limit of a long reward phase, not the two-stage condition; the fourth is the inverse ratio.
> Ref: Tadelis (2013), §10.1, two-stage example and fn. 2 (p. 191); Gibbons (1992), Figures 2.3.3–2.3.4 (pp. 84–86)
> Similar: Gibbons (1992), Exercise 2.10, p. 134; Gibbons (1992), Exercise 2.11, p. 135

Q: The game is now played $T$ rounds: $(M,m)$ in rounds $1,\dots,n$, then $(R,r)$ in the final $k = T-n$ rounds. For the last cooperative round $n$, what is the deviator's discounted loss, and what floor on $\delta$ must hold for some finite $k$ to work?
- Loss $(r-p)\,\delta^{k}/(1-\delta)$; some $k$ works iff $\delta > (b-a)/(r-p)$, which is the two-round threshold
- Loss $(r-p)\,\delta k$; some $k$ works for every $\delta>0$, since $k$ can be made as large as the game allows
- Loss $(a-p)\,\delta(1-\delta^{k})/(1-\delta)$; some $k$ works iff $\delta > (b-a)/(b-p)$, the grim-trigger cutoff
- Loss $(r-p)\,\delta(1-\delta^{k})/(1-\delta)$; some $k$ works iff $\delta > (b-a)/(b-a+r-p)$, a lower floor
<!-- YW5zOjM= -->
> A deviation in round $n$ costs $r-p$ in each of the $k$ reward rounds: $\sum_{j=1}^{k}\delta^{j}(r-p) = (r-p)\delta(1-\delta^k)/(1-\delta)$. As $k \to \infty$ this tends to $(r-p)\delta/(1-\delta)$, so some finite $k$ covers $b-a$ iff $\delta(b-a+r-p) > b-a$. With Tadelis's numbers the floor is $1/3$, below the one-round threshold $1/2$. The loss is discounted, so it is not linear in $k$, and the reward phase pays $r$, not $a$.
> Ref: Tadelis (2013), two-stage example (p. 191), extended to $T$ rounds; Prop. 9.3 (p. 181)
> Similar: Tadelis (2013), Exercise 10.7(b), pp. 217–218

Q: Suppose instead the two stage equilibria pay every player the same, $r = p$. Which first-stage behaviour can a subgame-perfect equilibrium of the finitely repeated game support?
- Only stage Nash play, since a deviator's continuation is the same after every history, so nothing offsets $b-a$
- $(M,m)$ for $\delta$ close to 1, since the two equilibria can still act as a reward and a punishment for deviators
- $(M,m)$ whenever $T$ is large, since the many later rounds add up to a loss of $(T-1)(a-p)$ for any deviator
- Any profile at all, since equal-payoff equilibria let the players coordinate freely on whichever continuation they like
<!-- YW5zOjA= -->
> A carrot and a stick must differ in payoff. With $r = p$ every continuation pays the deviator what conforming would, so the loss from deviating is zero and the one-stage gain $b - a$ is never offset; the game unravels exactly as with a unique stage equilibrium. Multiple equilibria matter only when they are payoff-distinct for the player being disciplined.
> Ref: Tadelis (2013), §10.1 (pp. 191–192); Gibbons (1992), §2.3.A (p. 86)
> Similar: Gibbons (1992), Exercise 2.11, p. 135

P:

Q: In any subgame-perfect equilibrium of a finitely repeated game, what must be true of play in the last period, and why?
- It must be the Pareto-best stage equilibrium, because any other choice could be renegotiated by both players at no cost
- It must be a stage equilibrium only on the path, because off-path histories in the last period are never reached in play
- It must be a stage Nash equilibrium after every history, because no future payoff depends on what is chosen in that period
- It must be the stage equilibrium that was played in the first period, because strategies are stationary in repeated games
<!-- YW5zOjI= -->
> In the last period each subgame is a one-shot play of the stage game, so each player best-responds to the others' current actions: play is a stage Nash equilibrium, after every history, whether the stage equilibrium is unique or not. Subgame perfection constrains off-path histories as well. Which stage equilibrium is played may depend on the history, which is exactly what makes a carrot and a stick possible.
> Ref: Tadelis (2013), Prop. 9.2 (p. 181), §10.1 (p. 191); Gibbons (1992), §2.3.A (p. 84)
> Similar: Cabral (2017), Exercise 7.13, p. 182

Q: A stage game in which player 1 has $n_1$ actions and player 2 has $n_2$ actions is played twice, and the first-stage outcome is observed by both. How many pure strategies does player 1 have in the two-stage game?
- $n_1^{\,2}$, one action in each of the two stages, since the second-stage choice is made once whatever happened
- $n_1^{\,1+n_1n_2}$, one first-stage action plus one second-stage action for each of the $n_1n_2$ outcomes
- $n_1 \cdot n_1n_2$, one first-stage action combined with one of the $n_1n_2$ outcomes observed at stage 2
- $n_1^{\,1+n_2}$, one first-stage action plus one second-stage action for each of the $n_2$ rival actions
<!-- YW5zOjE= -->
> A strategy is a complete contingent plan: one action at stage 1 and one action at each of the $n_1 n_2$ possible first-stage outcomes, including outcomes the player's own stage-1 action rules out. That is $1 + n_1n_2$ instructions, each with $n_1$ choices. In Tadelis's $3 \times 3$ example a strategy has one first-stage action and nine contingent second-stage actions; in the two-stage prisoner's dilemma it has five instructions.
> Ref: Tadelis (2013), fn. 1 (p. 191), Def. 10.4 (p. 196); Gibbons (1992), §2.3.B (p. 93)
> Similar: Gibbons (1992), Exercise 2.12, p. 135

## reneg

Q: A stage game has Nash equilibria worth $(r,r)$ and $(p,p)$ with $r > p$, and in a two-stage game cooperation in stage 1 is supported by punishing any deviation with $(p,p)$ in stage 2. Why may this punishment fail to be credible once renegotiation is allowed?
- After a deviation both players prefer $(r,r)$ to $(p,p)$, so they would agree to skip the stick, and the threat is empty
- After a deviation the punisher earns $p$ instead of $r$, so $(p,p)$ stops being a Nash equilibrium of the second-stage game
- After a deviation the deviator can offer a side payment worth $r-p$, which the punisher accepts once the stage game is over
- After a deviation $(p,p)$ stays credible, since renegotiation only matters when the stage game has three or more equilibria
<!-- YW5zOjA= -->
> The stick hurts the punisher as well. Once the deviation has happened, "bygones are bygones": both players gain by moving from $(p,p)$ to $(r,r)$, so if they can talk they would, and stage 2 would be $(r,r)$ after every history, which removes the incentive to cooperate in stage 1. $(p,p)$ remains a Nash equilibrium of the stage game; the problem is that it is Pareto-dominated by another one.
> Ref: Gibbons (1992), §2.3.A (pp. 86–88)
> Similar: Gibbons (1992), Exercise 2.11, p. 135

Q: To make punishments immune to renegotiation, Gibbons adds two stage equilibria: one that punishes player 1 and one that punishes player 2. Which property of these punishment equilibria removes the renegotiation problem?
- Each one gives the deviator less than $p$, so the stick is harsher than the original one and outweighs any one-stage gain
- Each one is drawn at random after a deviation, so neither player can predict which equilibrium to renegotiate toward
- Each one pays the two players the same total as $(r,r)$, so moving away from it cannot raise the pair's joint payoff
- Each one gives the punisher more than $(r,r)$ would, so no stage equilibrium is better for both, and none gets renegotiated
<!-- YW5zOjM= -->
> In Gibbons's Figure 2.3.5 player 1's deviation is punished with an equilibrium paying $(1/2, 4)$ and player 2's with $(4, 1/2)$, while cooperation is rewarded with $(3,3)$. The punisher earns $4 > 3$, so each punishment is on the Pareto frontier of the stage equilibria: no alternative equilibrium is better for both, and the punisher has nothing to renegotiate toward. Totals differ ($4.5$ against $6$), so the third option is false.
> Ref: Gibbons (1992), §2.3.A, Figure 2.3.5 (pp. 87–88)
> Similar: Gibbons (1992), Exercise 2.10, p. 134
