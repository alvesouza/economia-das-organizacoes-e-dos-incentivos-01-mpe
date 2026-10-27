---
quiz: "Lecture 8 · Quiz 3 of 3 — Limit pricing and the intuitive criterion (estimated unit, written before the lecture from Tadelis §16.2–16.3 and Gibbons §4.4)"
tags:
  lp: "Limit pricing and entry deterrence"
  ic: "The intuitive criterion"
  ref: "Equilibrium dominance and refinements"
---

## lp

P: Two periods, no discounting, inverse demand $P = a - q$ in each. The incumbent's marginal cost is $c_L$ or $c_H > c_L$, known only to itself. Let $M_\theta$ be type $\theta$'s one-period monopoly profit, $D_H$ the high type's Cournot profit against an entrant that knows its cost is $c_H$, and $R_L$ the low type's best one-period profit when the entrant enters believing the cost is $c_H$. In a candidate separating PBE the high type produces its monopoly output and faces entry, the low type produces $q$ in period 1 and deters entry, and any output other than $q$ is read as high cost.

Q: Which inequality stops the high type from mimicking the output $q$?
- $(a - c_L - q)q \le D_H$, so the low type's period-1 profit at $q$ must not exceed the high type's Cournot profit
- $(a - c_H - q)q \le M_H$, so the high type compares its period-1 sacrifice at $q$ with its own monopoly profit
- $(a - c_H - q)q + M_H \le M_H + D_H$, that is, $(a - c_H - q)q \le D_H$, so $q$ must be far from H's monopoly output
- $(a - c_H - q)q \le M_H - D_H$, so the period-1 profit at $q$ must not exceed what deterring entry is worth later
<!-- YW5zOjI= -->
> Mimicking earns $(a-c_H-q)q$ now and, with no entry, $M_H$ next period; staying put earns $M_H + D_H$. So the constraint is $(a-c_H-q)q \le D_H$. With Tadelis's numbers ($a=5$, $c_H=2$, $D_H=1$) it is $(3-q)q \le 1$, i.e. $q \ge (3+\sqrt5)/2 \approx 2.62$; the low type's monopoly output 2 fails it, since mimicking 2 gives the high type $4.25 > 3.25$.
> Ref: Tadelis (2013), §16.2.1, Steps 1–5 (pp. 324–329)
> Similar: Tadelis (2013), Exercise 16.3, pp. 335–336; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 11 Ex. 5, p. 505

Q: Which inequality stops the low type from deviating from $q$, and so bounds $q$ from above?
- $(a - c_L - q)q + M_L \ge M_L + R_L$, that is, $(a - c_L - q)q \ge R_L$: L's best deviation is its monopoly output, then entry
- $(a - c_L - q)q \ge M_L$, that is, L must earn at least its monopoly profit in period 1 at the output that deters entry
- $(a - c_L - q)q + M_L \ge M_L + D_H$, that is, $(a - c_L - q)q \ge D_H$: L's deviation payoff mirrors H's Cournot profit
- $(a - c_H - q)q + M_L \ge M_L + R_L$, that is, $(a - c_H - q)q \ge R_L$: L's output is valued at the cost the entrant believes
<!-- YW5zOjA= -->
> Any output other than $q$ is read as high cost and triggers entry, so the low type's best deviation is its monopoly output now ($M_L$) and its best reply to an entrant who thinks it faces $c_H$ next period ($R_L$). Staying at $q$ earns $(a-c_L-q)q$ now and $M_L$ later. With Tadelis's numbers, $(4-q)q \ge 2.25$, so $q \le 2 + \sqrt{1.75} \approx 3.32$: the separating set is $[2.62, 3.32]$. Requiring the monopoly profit at $q$ would allow only $q = 2$.
> Ref: Tadelis (2013), §16.2.1 (pp. 328–329)
> Similar: Tadelis (2013), Exercise 16.3, pp. 335–336; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 11 Ex. 5, p. 505

P:

Q: In Tadelis's two-period limit-pricing game, an incumbent of low or high cost (prior one half each) moves first and an entrant who sees first-period output decides whether to enter. Which statement about the pooling PBE is correct?
- The entrant stays out after the pooled output, since with a belief equal to the prior its expected Cournot profit after entry is negative
- Every pooled output must exceed the low type's monopoly output, since only an output above it is costly enough to deter the high type
- The pooled output is pinned to one value, since both types must be exactly indifferent between it and their best deviation at once
- The entrant enters after the pooled output, since at the prior its Bayesian Cournot profit is positive, so pooling deters no entry
<!-- YW5zOjM= -->
> With belief one half, the second period is a Cournot game with incomplete information: $q_2 = 5/6$, $q_1^L = 19/12$, $q_1^H = 13/12$, and the entrant nets $25/36 - 1/2 = 7/36 > 0$ (the book prints $7/18$; positive either way). So it enters. The pooling outputs form an interval, $[1.493, 1.917]$, below the low type's monopoly output 2, which is why Tadelis calls pooling "somewhat artificial".
> Ref: Tadelis (2013), §16.2.2 (pp. 330–332)
> Similar: Tadelis (2013), Exercise 16.7, p. 338

## ic

Q: A PBE of a signaling game fails the intuitive criterion when there are an unused action $a_1$, a set of types $\Theta'$ and a type $\theta' \notin \Theta'$ satisfying two conditions, each stated relative to the type's equilibrium payoff. Which two?
- Every type in $\Theta'$ gains from $a_1$ under some reply, and $\theta'$ loses from $a_1$ under every reply to beliefs on $\Theta'$ alone
- Every type in $\Theta'$ loses from $a_1$ under every reply, and $\theta'$ gains from $a_1$ under every reply to beliefs outside $\Theta'$
- Every type in $\Theta'$ loses from $a_1$ under some reply, and $\theta'$ gains from $a_1$ under some reply to beliefs outside $\Theta'$
- Every type in $\Theta'$ is dominated at $a_1$ by another action, and $\theta'$ prefers $a_1$ to every other action it could take
<!-- YW5zOjE= -->
> Condition 1: $a_1$ is equilibrium-dominated for $\Theta'$, so even the best reply to $a_1$, under any belief, leaves those types below their equilibrium payoffs. Condition 2: once the receiver puts no weight on $\Theta'$, even the worst reply it might then choose gives $\theta'$ more than its equilibrium payoff. "Some reply" in either condition would make the test too weak to be convincing. (Tadelis prints $v_2$ in condition 2; the sender's $v_1$ is meant.)
> Ref: Tadelis (2013), §16.3, Def. 16.1 (pp. 333–334); Gibbons (1992), §4.4, Signaling Requirement 6 (p. 239)
> Similar: Tadelis (2013), Exercise 16.7, p. 338; Tadelis (2013), Exercise 16.8, p. 338

Q: An MBA adds nothing to productivity, costs $c_H$ to the high type and $c_L$ to the low type, and the jobs pay $w_M > w_B$. Nobody studies, everyone gets $w_B$, and the unused degree is met with blue-collar work. When does this pooling PBE fail the intuitive criterion?
- If $w_M - c_L < w_B < w_M - c_H$: the degree is equilibrium-dominated for the low type, and the high type, once believed, gains for sure
- If $w_B - c_L < w_B < w_M - c_H$: the degree met by blue-collar work hurts the low type, and the high type gains if believed to be high
- If $w_M - c_H < w_B < w_M - c_L$: the degree is equilibrium-dominated for the high type, and the low type, once believed, gains for sure
- If $c_H < c_L$ alone: any cost gap makes the degree cheaper for the high type, which suffices for the employer to read it as high skill
<!-- YW5zOjA= -->
> The low type's best payoff from the degree is $w_M - c_L$; if it is below $w_B$, the degree is equilibrium-dominated for him. Believing the degree comes from the high type, the employer promotes, and the high type gets $w_M - c_H > w_B$. With Tadelis's numbers, $5 < 6 < 8$: the pooling PBE $(UU, BB)$ fails and only the separating $(DU, BM)$ survives. The second option uses the low type's worst payoff from the degree, which is a far weaker test.
> Ref: Tadelis (2013), §16.3 (pp. 333–334)
> Similar: Tadelis (2013), Exercise 16.5, p. 337; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 2, pp. 385–386

Q: In the two-type Spence model with unproductive education, productivity is $\theta_H > \theta_L$ and a unit of education costs $c_H < c_L$; both types pool at $e_p$ and earn $u_H^*$ and $u_L^*$. Which deviations $e$ break the pooling PBE under the intuitive criterion?
- $e \in ((\theta_H - u_H^*)/c_H,\ (\theta_H - u_L^*)/c_L)$, levels the high type would refuse even at $\theta_H$ but the low type would take
- $e \in ((\theta_L - u_L^*)/c_L,\ (\theta_L - u_H^*)/c_H)$, levels the low type would refuse even at $\theta_L$ but the high type would take
- $e \in (e_p,\ (\theta_H - u_H^*)/c_H)$, every level above the pooling one that the high type would take if it were paid $\theta_H$ for it
- $e \in ((\theta_H - u_L^*)/c_L,\ (\theta_H - u_H^*)/c_H)$, levels the low type would refuse even at $\theta_H$ but the high type would take
<!-- YW5zOjM= -->
> The low type is excluded at $e$ if even the best wage, $\theta_H$, leaves him below $u_L^*$: $e > (\theta_H - u_L^*)/c_L$. The high type, believed, gains if $\theta_H - c_H e > u_H^*$: $e < (\theta_H - u_H^*)/c_H$. Single crossing makes the interval non-empty at every pooling point; with M&R's numbers at $e_p = 0.3$ it is $(1.35, 2.4)$. So no pooling PBE survives.
> Ref: Gibbons (1992), §4.4 (pp. 239–244); MWG (1995), Appendix 13.AA, Fig. 13.AA.2 (pp. 469–471)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 11 Ex. 4, p. 500; MWG (1995), Exercise 13.C.1, p. 474

Q: In the two-type Spence model with unproductive education, productivity $\theta_H > \theta_L$ and unit costs $c_H < c_L$, the separating PBE have $e_L = 0$ and $e_H \in [(\theta_H-\theta_L)/c_L,\ (\theta_H-\theta_L)/c_H]$. Which survive the intuitive criterion?
- Only $e_H = (\theta_H-\theta_L)/c_H$, since at the top of the interval the high type is indifferent and has no reason to deviate down
- All of them, since every level in the interval is used by one type, so there is no off-path level at which beliefs could be tested
- Only $e_H = (\theta_H-\theta_L)/c_L$, since above it, levels just below $e_H$ are equilibrium-dominated for L and attractive to H
- None, since a pooling equilibrium always pays the high type more, and the criterion selects the outcome the high type prefers
<!-- YW5zOjI= -->
> For $e_H$ above the least-cost level, any $e$ between $(\theta_H-\theta_L)/c_L$ and $e_H$ gives the low type less than $\theta_L$ even at wage $\theta_H$, while the high type, believed, saves education cost. Only two education levels are used, so the other levels are off the path and their beliefs can be tested. At $e_H = (\theta_H-\theta_L)/c_L$ (1.5 with M&R's numbers) the gap is empty: the low type is exactly indifferent to mimicking.
> Ref: Gibbons (1992), §4.4, Fig. 4.4.4 (pp. 241–242); Tadelis (2013), §16.3 (p. 335)
> Similar: Tadelis (2013), Exercise 16.7, p. 338; MWG (1995), Exercise 13.C.2, p. 475

## ref

Q: A message $m$ is dominated for type $t$ if some other message's worst payoff beats $m$'s best payoff for $t$, and equilibrium-dominated if $t$'s equilibrium payoff beats $m$'s best payoff. Which statement is correct?
- Equilibrium-dominated implies dominated, so the intuitive criterion is weaker than deleting dominated messages and removes fewer equilibria
- Dominated implies equilibrium-dominated but not conversely, so the intuitive criterion is stronger and can remove more equilibria
- The two tests coincide in every two-type signaling game, since the equilibrium payoff is always the worst payoff of some other message
- Neither implies the other, since dominance looks at all replies while equilibrium dominance looks only at beliefs on the path
<!-- YW5zOjE= -->
> The equilibrium payoff is at least what the type gets from any message under the equilibrium replies, hence at least that message's worst payoff; so dominated implies equilibrium-dominated. The converse fails: in Beer–Quiche, Beer is equilibrium-dominated for the wimpy type ($2 < 3$) but not dominated (its best from Beer, 2, beats its worst from Quiche, 1). Gibbons's Requirement 6 is therefore stronger than Requirement 5.
> Ref: Gibbons (1992), §4.4, Signaling Requirements 5–6 (pp. 235–239); MWG (1995), Appendix 13.AA, (13.AA.1)–(13.AA.3) (pp. 468–469)
> Similar: Tadelis (2013), Exercise 16.8, p. 338

Q: In the two-type Spence model with unproductive education, unit costs $c_H < c_L$, and a share $p$ of high types above $1 - c_H/c_L$, which statement about the intuitive criterion is correct?
- It selects the pooling equilibrium at zero education, since above that share the high type prefers pooling and the criterion follows the sender
- It removes every equilibrium, since above that share no separating equilibrium exists and every pooling equilibrium is broken by a deviation
- It selects the least-cost separating equilibrium, but only because above that share the high type prefers it to every pooling outcome too
- It selects the least-cost separating equilibrium, even though above that share the high type would prefer pooling at zero education
<!-- YW5zOjM= -->
> The criterion is a credible-deviation test, not a welfare ranking. It always leaves the least-cost separating equilibrium in the two-type model, and the separating set does not depend on $p$. Above $p^* = 1 - c_H/c_L$ the pooled wage exceeds the high type's least-cost separating payoff, so the high type would prefer the pooling outcome the criterion eliminates.
> Ref: Gibbons (1992), §4.4 (pp. 239–244); MWG (1995), §13.C, Fig. 13.C.8 (p. 456) and Appendix 13.AA (p. 471)
> Similar: MWG (1995), Exercise 13.C.2, p. 475

Q: Each sender type values its preferred breakfast at $b > 0$ (wimpy prefers Quiche, surly prefers Beer) and avoiding a duel at $d > b$; the receiver wants to duel only a wimpy sender. In a pooling PBE everyone eats Quiche, there is no duel after Quiche, and Beer is met with a duel. What does the intuitive criterion conclude?
- Beer gives the wimpy type at most $d < b + d$, its equilibrium payoff, so he is excluded; the surly type, believed and not dueled, gets $b + d > d$
- Beer gives the surly type at most $d$, his equilibrium payoff, so he is excluded; the wimpy type, believed and not dueled, gets $d > b$ and deviates
- Beer gives each type at most $b + d$, no less than the equilibrium payoffs, so no type is excluded and the pooling PBE survives the criterion
- Beer gives the wimpy type at most $d - b$, below his payoff $d$, so he is excluded, but the surly type only ties at $d$, so the pooling survives
<!-- YW5zOjA= -->
> In the pooling equilibrium the wimpy type gets $b + d$ (Quiche, no duel) and the surly type gets $d$. The best Beer can give the wimpy type is $d$ (no duel), below $b + d$: Beer is equilibrium-dominated for him. The surly type's best from Beer is $b + d > d$, so he is not excluded; with the belief on the surly type only, the receiver does not duel, and the surly type gains for sure. With Gibbons's $b = 1$, $d = 2$: 2 < 3 and 3 > 2. The pooling-on-Quiche PBE fails.
> Ref: Gibbons (1992), §4.4, Beer and Quiche, Fig. 4.4.3 (pp. 237–239)
> Similar: Tadelis (2013), Exercise 16.8, p. 338
