---
quiz: "Lecture 8 · Quiz 2 of 3 — Signaling games, the MBA game and Spence (estimated unit, written before the lecture from Tadelis Ch. 16 and Gibbons §4.2)"
tags:
  sig: "Signaling games: pooling, separating, hybrid"
  mba: "The MBA game"
  spence: "Spence's job-market signaling"
---

## sig

Q: A high-quality type wants the receiver to believe "I am the high type", and so does the low-quality type. Why can a costless claim not separate the two types?
- Because the receiver ignores any message that is not observed by both players, so a private claim never enters its best reply at all
- Because both types want the reply reserved for the high type, so any costless message the high type sends, the low type sends as well
- Because a costless claim reaches an off-path information set, where Bayes' rule is undefined and the receiver must keep the prior
- Because the sender moves before the receiver, so the receiver cannot condition its reply on a claim that was made at an earlier stage
<!-- YW5zOjE= -->
> A signal works only if it is an action that costs the types differently (Tadelis's second component of a signaling game; Spence's insight). If the message is free and both types prefer the reply the high type gets, the low type copies whatever the high type does, so no message can be sent by one type only. Costless messages are cheap talk, which is outside this course's scope; the receiver does condition on observed earlier moves, which is what makes the game a signaling game.
> Ref: Tadelis (2013), Ch. 16 opening (pp. 318–319); Gibbons (1992), §4.2.A (p. 183)
> Similar: Tadelis (2013), Exercise 16.5, p. 337

Q: A receiver who sees an unused message $R$ earns $x_1 > 0$ from reply $u$ against type $t_1$ and 0 against $t_2$, and earns 0 from reply $d$ against $t_1$ and $x_2 > 0$ against $t_2$. A pooling candidate needs the reply $d$ after $R$. Which beliefs $q = \mu(t_1 \mid R)$ support it?
- $q \ge x_2/(x_1 + x_2)$, since $d$ must beat $u$ once the receiver believes $t_1$ is likely enough to have sent the message $R$
- $q \le x_1/(x_1 + x_2)$, since $d$ beats $u$ when the belief on $t_1$ is below the weight of $t_1$'s payoff in the total payoff
- $q = 1/2$ only, since the off-path belief must make the receiver indifferent so that either reply can be prescribed after $R$
- $q \le x_2/(x_1 + x_2)$, since $d$ beats $u$ exactly when $(1-q)x_2 \ge q\,x_1$, a belief that $t_2$ is likely enough to send $R$
<!-- YW5zOjM= -->
> $E[u] = q x_1$ and $E[d] = (1-q)x_2$, so $d$ is a best reply iff $q \le x_2/(x_1+x_2)$. In Gibbons's Fig. 4.2.2, $x_1 = 1$ and $x_2 = 2$, which gives his $q \le 2/3$ for the pooling equilibrium on $L$. Off-path beliefs are free, but only those that make the prescribed reply optimal are admissible; indifference is not required.
> Ref: Gibbons (1992), §4.2.A, Fig. 4.2.2 (pp. 188–190); Tadelis (2013), Requirement 15.4 (p. 310)
> Similar: Gibbons (1992), Problem 4.3, pp. 246–247; Gibbons (1992), Problem 4.4, p. 248

Q: In a separating PBE of a signaling game with two types and two messages, which statement about the receiver's beliefs is correct?
- Both messages are on the path, so both beliefs are pinned at 0 or 1 by Bayes' rule; free beliefs appear only with more messages than types
- One message is off the path for each type, so each type faces a free belief, chosen to make mimicking the other type unattractive to it
- Both beliefs equal the prior, since each message is sent by exactly one type and each type carries the same prior weight as its message
- Beliefs are pinned after the high type's message only, while the belief after the low type's message is free and must be pessimistic
<!-- YW5zOjA= -->
> Each message is sent by one type with positive probability, so Bayes' rule applies at both of the receiver's information sets and gives beliefs 1 and 0: full revelation. What holds a separating equilibrium together is then each type's incentive compatibility, not off-path beliefs. With a continuum of messages (Spence, limit pricing) most messages are unused, and there the beliefs are free again.
> Ref: Tadelis (2013), Ch. 16 opening (pp. 318–319); Gibbons (1992), §4.2.A (pp. 186–188)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 1, pp. 376–377

## mba

Q: An employer earns $\pi_{HM}$ or $\pi_{HB}$ from putting a high-skill worker in the manager or blue-collar job, and $\pi_{LM}$ or $\pi_{LB}$ for a low-skill worker, with $\pi_{HM} > \pi_{HB}$ and $\pi_{LB} > \pi_{LM}$. Above which belief $\mu$ that the worker is high-skill does the employer prefer the manager job?
- $\mu^* = (\pi_{HM} - \pi_{HB})/[(\pi_{HM} - \pi_{HB}) + (\pi_{LB} - \pi_{LM})]$, the high type's gain from M over the sum of both gaps
- $\mu^* = (\pi_{LB} - \pi_{LM})/(\pi_{HM} - \pi_{LM})$, the low type's loss from M over the spread of manager profits across types
- $\mu^* = (\pi_{LB} - \pi_{LM})/[(\pi_{HM} - \pi_{HB}) + (\pi_{LB} - \pi_{LM})]$, the low type's loss from M over the sum of both gaps
- $\mu^* = \pi_{LB}/(\pi_{HM} + \pi_{LB})$, the low type's blue-collar profit over the sum of the profits each job earns at its best
<!-- YW5zOjI= -->
> The manager job is better iff $\mu\pi_{HM} + (1-\mu)\pi_{LM} \ge \mu\pi_{HB} + (1-\mu)\pi_{LB}$, i.e. $\mu(\pi_{HM}-\pi_{HB}) \ge (1-\mu)(\pi_{LB}-\pi_{LM})$. With Tadelis's numbers ($10, 5, 0, 3$) this is $3/(5+3) = 3/8$. The first option inverts the weights: a larger gain from promoting the high type should lower the threshold, not raise it.
> Ref: Tadelis (2013), §16.1 (pp. 319–323)
> Similar: Tadelis (2013), Exercise 16.4, pp. 336–337; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 2, pp. 385–386

Q: An MBA adds nothing to productivity and costs the high type $c_H$ and the low type $c_L$; the manager job pays $w_M$ and the blue-collar job $w_B < w_M$. When is there a separating PBE in which only the high type studies and is promoted?
- Iff $c_H \le w_M - w_B \le c_L$, whatever the prior, since beliefs are 0 and 1 and only the two types' incentive constraints bind
- Iff $c_L \le w_M - w_B \le c_H$, whatever the prior, since the type with the higher cost is the one that gains most from promotion
- Iff $c_H \le w_M - w_B$ and the prior is above the employer's threshold, since promotion after a degree must be backed by the prior
- Iff $c_H \le w_M \le c_L$, whatever the prior, since each type compares the manager wage with its own study cost when it chooses
<!-- YW5zOjA= -->
> In the separating profile the employer sees the type: belief 1 after the degree (promote) and 0 without it (blue-collar). The high type must prefer $w_M - c_H$ to $w_B$, and the low type must prefer $w_B$ to $w_M - c_L$. Together: $c_H \le w_M - w_B \le c_L$, Tadelis's $2 \le 4 \le 5$. The prior never enters, so the equilibrium exists for every $p$; the comparison is with the wage premium, not the wage level.
> Ref: Tadelis (2013), §16.1 (pp. 321–323)
> Similar: Tadelis (2013), Exercise 16.4, pp. 336–337; MWG (1995), Exercise 13.C.5, p. 475

Q: An MBA adds nothing to productivity and costs the high type $c_H < w_M - w_B$, where $w_M > w_B$ are the manager and blue-collar wages; the employer promotes iff its belief that the worker is high-skill is at least $\mu^*$, and the prior $p$ is below $\mu^*$. Nobody studies and everyone gets blue-collar work. Which beliefs $\mu_U$ (no degree) and $\mu_D$ (degree) make this a PBE?
- Only $\mu_U = \mu_D = p$, since Bayes' rule must hold at both information sets, and a degree nobody takes leaves the belief at the prior
- $\mu_U = p$ and any $\mu_D \ge \mu^*$, since the employer must reward the degree for the low type to be deterred from deviating to it
- $\mu_U = 0$ and $\mu_D = 1$, since a pooling equilibrium is held up by the beliefs that would hold if the two types were separating
- $\mu_U = p$ and any $\mu_D \le \mu^*$, since the unused degree must be met with blue-collar work, or the high type would study
<!-- YW5zOjM= -->
> No degree is on the path: Bayes gives $\mu_U = p < \mu^*$, so blue-collar work is the best reply. The degree is off the path, so $\mu_D$ is free, but blue-collar work after it must be optimal, which needs $\mu_D \le \mu^*$. If the degree were met with promotion, the high type would earn $w_M - c_H > w_B$ and deviate. With Tadelis's numbers, $\mu_D \in [0, 3/8]$; the belief equal to the prior is one admissible value, not the only one.
> Ref: Tadelis (2013), §16.1 (pp. 322–323)
> Similar: Tadelis (2013), Exercise 16.5, p. 337; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 5, pp. 422–423

## spence

Q: In Spence's model with unproductive education, productivity is $\theta_H$ or $\theta_L < \theta_H$, a share $p$ of workers is high-ability, a unit of education costs $c_H$ to the high type and $c_L > c_H$ to the low type, and firms pay expected productivity. Which levels $e_H$ are supported in a separating PBE with $e_L = 0$?
- $e_H \in [(\theta_H - \theta_L)/c_H,\ (\theta_H - \theta_L)/c_L]$, from the high type's constraint below and the low type's above
- $e_H \in [(\theta_H - \theta_L)/c_L,\ (\theta_H - \theta_L)/c_H]$, from the low type's no-mimic constraint below and the high type's above
- $e_H \in [(\theta_H - \theta_L)/(c_L - c_H),\ (\theta_H - \theta_L)/c_H]$, since only the cost gap can deter the low type from mimicking
- $e_H \in [p(\theta_H - \theta_L)/c_L,\ (\theta_H - \theta_L)/c_H]$, since the low type compares mimicking with the pooled wage at $p$
<!-- YW5zOjE= -->
> The low type must not mimic: $\theta_H - c_L e_H \le \theta_L$, i.e. $e_H \ge (\theta_H-\theta_L)/c_L$. The high type must prefer signaling: $\theta_H - c_H e_H \ge \theta_L$, i.e. $e_H \le (\theta_H-\theta_L)/c_H$. The interval is non-empty because $c_H < c_L$; with M&R's numbers it is $[1.5, 3]$. In a separating equilibrium the low type's alternative is $\theta_L$, not the pooled wage.
> Ref: Gibbons (1992), §4.2.B (pp. 199–202); Milgrom & Roberts (1992), Ch. 5 (pp. 155–156); MWG (1995), §13.C (pp. 453–455)
> Similar: MWG (1995), Exercise 13.C.1, p. 474; Gibbons (1992), Problem 4.7, p. 249

Q: In Spence's model with unproductive education, productivity is $\theta_H > \theta_L$, a share $p$ of workers is high-ability, and a unit of education costs $c_H$ to the high type and $c_L > c_H$ to the low type. When does the high type prefer the least-cost separating equilibrium to a world where signaling is impossible and everyone is paid expected productivity?
- Iff $p \le c_H/c_L$, because the pooled wage falls with $p$ and the high type is the one who subsidizes the low types when they are few
- Iff $p \ge 1 - c_H/c_L$, because the more high types there are, the cheaper it becomes for each of them to separate from the rest
- Iff $p \le 1 - c_H/c_L$, because the pooled wage rises with $p$ while the least-cost separating payoff of the high type does not
- Iff $p \le (c_L - c_H)/(c_L + c_H)$, because the high type weighs the cost gap against total costs when choosing to separate
<!-- YW5zOjI= -->
> Least-cost separation gives the high type $\theta_H - c_H(\theta_H-\theta_L)/c_L$, which does not involve $p$; no signaling gives $p\theta_H + (1-p)\theta_L$. The first is at least the second iff $(1-p)(\theta_H-\theta_L) \ge (c_H/c_L)(\theta_H-\theta_L)$, i.e. $p \le 1 - c_H/c_L$. With M&R's costs the cut-off is $0.5$: at 30% high types signaling helps them ($35 > 29$), at 70% it hurts. The low type is always worse off.
> Ref: MWG (1995), §13.C, Fig. 13.C.8 (pp. 456–457); Milgrom & Roberts (1992), Ch. 5 (p. 156)
> Similar: MWG (1995), Exercise 13.C.2, p. 475

Q: In Spence's model with unproductive education, productivity is $\theta_H > \theta_L$, a share $p$ of workers is high-ability, and education costs $c_H$ per unit to the high type and $c_L > c_H$ to the low type. Both types choose $e_p$, and any other level is read as low ability. What is the largest $e_p$ a pooling PBE can sustain?
- $e_p = p(\theta_H - \theta_L)/c_L$, where the low type is just indifferent between the pooled wage and $\theta_L$ at zero education
- $e_p = p(\theta_H - \theta_L)/c_H$, where the high type is just indifferent between the pooled wage and $\theta_L$ at zero education
- $e_p = (1-p)(\theta_H - \theta_L)/c_L$, where the low type is just indifferent between the pooled wage and $\theta_L$ at zero
- $e_p = (\theta_H - \theta_L)/c_L$, where the low type is just indifferent between the wage $\theta_H$ and $\theta_L$ at zero education
<!-- YW5zOjA= -->
> With the pessimistic off-path belief, a deviating worker is paid $\theta_L$ and chooses $e = 0$. Type $\theta$ pools iff $p\theta_H + (1-p)\theta_L - c_\theta e_p \ge \theta_L$, i.e. $e_p \le p(\theta_H-\theta_L)/c_\theta$. The low type has the larger cost, so his constraint binds: $e_p \le p(\theta_H-\theta_L)/c_L$, which is $0.45$ with M&R's numbers. The last option is the least-cost separating level, not a pooling bound.
> Ref: Gibbons (1992), §4.2.B, eqs. (4.2.2)–(4.2.5) (pp. 196–199); MWG (1995), §13.C (pp. 457–459)
> Similar: MWG (1995), Exercise 13.C.1, p. 474; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 11 Ex. 4, p. 500

Q: In the two-type Spence model with unproductive education and single crossing, which statement about the separating equilibria is correct?
- The high type chooses its full-information education and the low type over-invests, since the low type must prove it is not mimicking
- Both types choose positive education, and the set of separating levels shrinks as the share of high-ability workers in the market rises
- The low type chooses zero education, and the least-cost separating level rises with the share of high-ability workers in the market
- The low type chooses zero education and the high type over-invests, and the set of separating levels does not depend on the prior
<!-- YW5zOjM= -->
> In a separating equilibrium each type is paid its own productivity (MWG Lemma 13.C.1), so the low type gains nothing from education and picks $e = 0$ (Lemma 13.C.2). The high type must go beyond his full-information choice of zero to deter mimicking. Both constraints involve only $\theta_H$, $\theta_L$, $c_H$ and $c_L$, so the separating set is "completely unaffected" by the share of high types (MWG p. 456). Wages rise with education here although output does not.
> Ref: MWG (1995), §13.C, Lemmas 13.C.1–13.C.2 (pp. 453–456); Gibbons (1992), §4.2.B (pp. 199–202)
> Similar: MWG (1995), Exercise 13.C.4, p. 475; Gibbons (1992), Problem 4.16, p. 253
