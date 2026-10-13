---
quiz: "Aula 1 · Quiz 2 of 3 — Complementarities: definition, statics, multiplier"
tags:
  def: "Definition and increasing differences"
  statics: "Monotone comparative statics"
  systems: "Two choices: the multiplier"
  design: "Substitutes, strong complementarity, design"
---

## def

Q: Why do Milgrom and Roberts replace the market definition of complements (a fall in one input's price raises demand for the other) with a "more inclusive" one?
- The market definition is wrong even for traded inputs, since a price fall raises demand for another input only when the two are perfect substitutes in production
- The inclusive definition adds the requirement that each activity be profitable on its own, which the market definition never checks for traded inputs
- Internal activities like delegation or inventory policy have no market price, so complementarity is defined through marginal profitability instead
- The market definition applies only to consumers, so for firms complementarity must be redefined through the sign of total profit rather than through margins
<!-- YW5zOjI= -->
> M&R p. 108: to study "levels of various internal activities as well as levels of input purchases", activities are complementary if doing more of one "increases (or at least does not decrease) the marginal profitability of each other activity". Many of the choices in Aula 1 (decision rights, inventories, supplier relations) have no price at all. The inclusive definition says nothing about each activity being profitable alone.
> Ref: Milgrom & Roberts (1992), Ch. 4 "Complementarities and Design Decisions", p. 108 and footnote 8; Aula 1 notes §6.1
> Similar: M&R FFT 4.3, p. 119

Q: Two yes-or-no practices have profit $f(x,y)$ with $f(1,0) < f(0,0)$, $f(0,1) < f(0,0)$ and $f(1,1) > f(0,0)$. Which conclusion follows?
- Increasing differences hold, and a firm that tests each practice alone against the status quo rejects both, although adopting the pair raises profit
- Increasing differences may fail, because both practices lower profit alone, and complementarity requires each to be profitable on its own first
- The practices must be substitutes, since each lowers profit alone, and the gain from the pair must come from some omitted third practice
- A firm that tests each practice alone adopts both, because the joint gain shows up in each separate test once the other practice is held fixed
<!-- YW5zOjA= -->
> The gain from $x$ with $y = 1$ is $f(1,1) - f(0,1) > 0$ (since $f(1,1) > f(0,0) > f(0,1)$), while the gain with $y = 0$ is $f(1,0) - f(0,0) < 0$: increasing differences hold, equivalently $f(1,1) + f(0,0) \ge f(1,0) + f(0,1)$. Yet each separate test from $(0,0)$ shows a loss. Complementarity says each practice is better where the other is present, not that it is good alone.
> Ref: Milgrom & Roberts (1992), Ch. 4, p. 108; Aula 1 notes §6.1 (the 2×2 example), §9
> Similar: Companion "The Valley Between Systems", preset "No interactions"

## statics

Q: Profit $f(x,t)$ is twice differentiable and strictly concave in the choice $x$, and $x^*(t)$ is the interior optimum given the parameter $t$. Differentiating the first-order condition, what is $dx^*/dt$ and when is it nonnegative?
- $f_{xt}/f_{xx}$, nonnegative whenever $f_{xt} \ge 0$, because both derivatives share the sign of the marginal profit
- $-f_{xx}/f_{xt}$, nonnegative whenever $f_{xt} \ge 0$, because the ratio of curvatures is negative under concavity
- $-f_{t}/f_{x}$, nonnegative whenever $f_{xt} \ge 0$, because it is the slope of a level curve of $f$ in the $(x,t)$ plane
- $-f_{xt}/f_{xx}$, nonnegative whenever $f_{xt} \ge 0$, because strict concavity makes $f_{xx}$ negative
<!-- YW5zOjM= -->
> From $f_x(x^*(t), t) = 0$: $f_{xx}\,x^{*\prime} + f_{xt} = 0$, so $x^{*\prime} = -f_{xt}/f_{xx}$. With $f_{xx} < 0$, the sign is the sign of $f_{xt}$: when the environment raises the marginal return to $x$, the optimal $x$ rises. The level-curve slope is wrong because $f_x = 0$ at the optimum, so that ratio is not even defined.
> Ref: Aula 1 notes §6.2; Milgrom & Roberts (1992), Ch. 4, p. 108 footnote 8
> Similar: Practice plan Aula 1, companion task C4

Q: Topkis' theorem reaches the same monotonicity conclusion as differentiating the first-order condition. What does it need, and why does that matter for the practices in Aula 1?
- Strict concavity in the choice, so it extends the derivative argument only to cases where the optimum is unique, interior and smooth in the parameter
- Only increasing differences in the choice and the parameter, so it holds without derivatives or concavity, as yes-or-no practices require
- An additive parameter, so it covers a cube of yes-or-no practices only when every interaction term between the practices is set equal to zero
- Each activity profitable on its own, so it predicts that practices move together only when each would have been adopted even in isolation
<!-- YW5zOjE= -->
> Topkis: if $f$ has increasing differences in $(x, t)$, the optimal $x$ is non-decreasing in $t$ (with several optima, the largest and smallest ones are). No differentiability, concavity or uniqueness is needed, which is why Milgrom & Roberts (1990, AER 80(3), 511–528) could apply it to discrete manufacturing choices. The course states the theorem without the lattice proof.
> Ref: Aula 1 notes §6.2; Milgrom & Roberts (1990), AER 80(3), 511–528
> Similar: Practice plan Aula 1, item 13 (M&R FFT 4.3, p. 119)

## systems

P: A firm chooses delegated authority $x$ and incentive intensity $y$ to maximize $\pi(x,y) = tx + sy + bxy - \tfrac{c}{2}x^2 - \tfrac{c}{2}y^2$, where $t$ is the value of local information, $s$ how well results can be measured, $b$ the cross effect $\partial^2\pi/\partial x\,\partial y$, and $c > |b|$ measures diminishing returns.

Q: What is the optimal delegation $x^*$?
- $x^* = (ct - bs)/(c^2 - b^2)$, from solving $t - by = cx$ and $s - bx = cy$ together
- $x^* = (ct + bs)/(c^2 - b^2)$, from solving $t + by = cx$ and $s + bx = cy$ together
- $x^* = (t + bs)/(c - b)$, from substituting $y = s/c$ into the condition $t + by = cx$
- $x^* = (ct + bs)/(c^2 + b^2)$, from solving $t + by = cx$ and $s + bx = cy$ together
<!-- YW5zOjE= -->
> The first-order conditions are $t + by = cx$ and $s + bx = cy$. Substituting $y = (s + bx)/c$ into the first: $ct + bs + b^2x = c^2x$, so $x^* = (ct + bs)/(c^2 - b^2)$; symmetrically $y^* = (cs + bt)/(c^2 - b^2)$. Plugging in $y = s/c$ ignores that $y$ responds to $x$; the $c^2 + b^2$ denominator is an algebra slip that would make the second-order condition $c > |b|$ irrelevant.
> Ref: Aula 1 notes §6.2; Milgrom & Roberts (1992), Ch. 1, p. 17 (incentives and delegated authority as complements)
> Similar: Companion "The Complementarity Multiplier"

Q: How does $x^*$ respond to the value of local information $t$, and how should the response be read?
- $1/(c - b) = (1/c)[1 + b/c + (b/c)^2 + \dots]$: the stand-alone response plus rounds of feedback through $y$
- $1/c$: the stand-alone response only, since $t$ does not enter the condition for $y$, so no feedback runs through it
- $b/(c^2 - b^2)$: the feedback through $y$ only, since the direct effect of $t$ on $x$ is already in the stand-alone level
- $c/(c^2 - b^2) = (1/c)[1 + (b/c)^2 + (b/c)^4 + \dots]$: the stand-alone response plus rounds of feedback through $y$
<!-- YW5zOjM= -->
> $\partial x^*/\partial t = c/(c^2 - b^2) = (1/c)\cdot 1/(1 - (b/c)^2)$, a geometric series in $(b/c)^2$: $1/c$ is the response with $y$ fixed, and each further term is a round in which $x$ raises the return to $y$ and $y$ raises the return to $x$, M&R's "another round of increases" (footnote 8, p. 108). $t$ does not enter the $y$ condition, but $y$ still moves because $x$ does: $\partial y^*/\partial t = b/(c^2 - b^2)$.
> Ref: Milgrom & Roberts (1992), Ch. 4, p. 108 footnote 8; Aula 1 notes §6.2
> Similar: Practice plan Aula 1, companion tasks C2 and C6

Q: Suppose instead that the two choices are substitutes, $b < 0$, still with $c > |b|$. What happens to the responses to $t$?
- $\partial x^*/\partial t$ still exceeds $1/c$, since it depends on $b^2$, while $\partial y^*/\partial t = b/(c^2 - b^2)$ turns negative
- $\partial x^*/\partial t$ falls below $1/c$, since negative feedback dampens it, while $\partial y^*/\partial t = b/(c^2 - b^2)$ stays positive
- $\partial x^*/\partial t$ equals $1/c$ exactly, since the feedback terms cancel, while $\partial y^*/\partial t = b/(c^2 - b^2)$ turns negative
- $\partial x^*/\partial t$ falls below $1/c$, since it depends on $b$ linearly, while $\partial y^*/\partial t$ is zero when the two are substitutes
<!-- YW5zOjA= -->
> $c/(c^2 - b^2)$ depends on $b$ only through $b^2$, so the multiplier $1/(1 - (b/c)^2)$ exceeds one for either sign. With substitutes, a rise in $x$ lowers $y$, and a lower $y$ raises the return to $x$ again: the feedback still amplifies $x$. Only the direction of $y$ changes, since $\partial y^*/\partial t$ has the sign of $b$.
> Ref: Aula 1 notes §6.2, §9 (the substitutes mistake)
> Similar: Companion "The Complementarity Multiplier", preset "Substitutes"

## design

P:

Q: Buffer inventories $x$ and floor-level problem solving $y$ are substitutes in profit $f(x,y)$: $\partial^2 f/\partial x\,\partial y \le 0$. What does redefining $z = -y$ establish?
- $g(x,z) = f(x,-z)$ has $g_{xz} = f_{xy} \le 0$, so substitutes stay substitutes and no coherent pole exists for either variable
- $g(x,z) = -f(x,z)$ has $g_{xz} = -f_{xy} \ge 0$, so minimizing $g$ instead of maximizing $f$ recovers a problem in complements
- $g(x,z) = f(x,-z)$ has $g_{xz} = -f_{xy} \ge 0$, so "many buffers, little problem solving" and its opposite are both coherent poles
- $g(x,z) = f(x,-z)$ has $g_{xz} = -f_{xy} \ge 0$, so the firm should choose intermediate levels of buffers and of problem solving
<!-- YW5zOjI= -->
> By the chain rule $g_{xz} = -f_{xy} \ge 0$, so every result for complements applies to $(x, z)$: $x$ and $z$ move together, so buffers and problem solving move in opposite directions. Ford's pole (many buffers, narrow jobs) and Toyota's (no buffers, problem solvers) are both coherent; the mixtures are not. Nothing in the transformation recommends intermediate levels; complementarity pushes toward the corners.
> Ref: Aula 1 notes §6.3; Milgrom & Roberts (1992), Ch. 1, p. 17
> Similar: Companion "Two Coherent Systems" (variety and small batches)

Q: How do Milgrom and Roberts distinguish complementarity from strong complementarity, and what does the distinction explain?
- Strong complementarity means every pair of activities is complementary, while plain complementarity needs it only for adjacent stages of production
- Strong complementarity means the activities are also complements in the market sense, so a fall in one input's price raises demand for all others
- Complementarity alone implies a high cost of misfit, so strong complementarity adds only that the activities must also be profitable separately
- Complementarity makes high levels go together; strong complementarity adds a high cost of failing to fit, which is what makes a choice a design decision
<!-- YW5zOjM= -->
> M&R p. 109: predictability is one defining feature of design attributes; the high cost of failure to match "is a separate aspect of the problem that is not logically implied by the conditions of complementarity alone". A group is strongly complementary when raising some activities "greatly increases the returns" to raising the others, and then "design attributes are always present". This is why such choices are coordinated centrally (Aula 7).
> Ref: Milgrom & Roberts (1992), Ch. 4, pp. 108–109; Ch. 4 "The Variety of Coordination Problems and Solutions", pp. 90–93
> Similar: M&R Math. Ex. 4.2, p. 120

Q: Which statement is consistent with M&R's box "Modern Manufacturing Strategy"?
- Short runs and frequent changeovers make dedicated equipment pay, since each machine then runs one product, and piece rates keep each stage at full speed
- Short runs and frequent changeovers make flexible equipment and multi-skilled workers pay, and keeping every stage in balance argues against piece rates
- Low inventories make piece rates more valuable, since each worker's output is then measured exactly, and skill-based pay would slow the line down
- Frequent redesign lowers the value of cost information, since designs change too fast to cost, so machine costs are allocated by direct labour hours
<!-- YW5zOjE= -->
> M&R pp. 109–110: small demand per product, no finished-goods stocks, short runs, frequent changeovers, flexible equipment; multi-skilled workers paid for skills; with just-in-time "the rate of work at each step of the process must be in constant balance", so systems "tend to avoid piece-rate compensation"; and accurate design costing, with machine costs assigned by machine time. Every link raises the value of the next one.
> Ref: Milgrom & Roberts (1992), Ch. 4, box "Modern Manufacturing Strategy", pp. 109–110
> Similar: M&R FFT 4.2, p. 119
