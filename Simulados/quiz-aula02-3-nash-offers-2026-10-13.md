---
quiz: "Aula 2 · Quiz 3 of 3 — Threat points, alternating offers and objectives"
tags:
  nash: "Threat points and the Nash solution"
  offers: "Alternating offers and patience"
  objectives: "Organizational objectives"
  aula1: "Back to Aula 1"
---

## nash

P: Two parties choose a decision $y$ and utilities $u_1, u_2$ with $u_1 + u_2 = W(y)$, where $W(y)$ is their total value (no wealth effects, free transfers) and $y^*$ maximizes it. Party $i$'s threat point (payoff if no agreement is reached) is $d_i$, and the outcome maximizes the weighted Nash product $(u_1 - d_1)^{\beta}(u_2 - d_2)^{1 - \beta}$ over $y$, $u_1$ and $u_2$, with $\beta \in (0, 1)$.

Q: Suppose $W(y^*) > d_1 + d_2$. For a fixed $y$, what is the largest value the Nash product can reach, and what does it imply for the choice of $y$?
- $\beta(1 - \beta)[W(y) - d_1 - d_2]^2$, increasing in $W(y)$ only when $\beta = \tfrac12$, so $y^*$ is chosen only under symmetric bargaining
- $\beta^{\beta}(1 - \beta)^{1 - \beta}[W(y) - d_1 - d_2]$, increasing in $W(y)$ for every $\beta$, so $y^*$ is chosen whatever the weights
- $\beta^{\beta}(1 - \beta)^{1 - \beta}[W(y) - d_1 - d_2]$, increasing in $\beta$ for every $W(y)$, so the stronger party's preferred $y$ is chosen
- $[\beta W(y) - d_1]^{\beta}[(1 - \beta)W(y) - d_2]^{1 - \beta}$, peaking where $\beta W'(y) = 0$, so $y^*$ is chosen only if $d_1 = d_2$
<!-- YW5zOjE= -->
> With $S(y) = W(y) - d_1 - d_2$ and gain $g$ to party 1, maximize $g^{\beta}(S - g)^{1-\beta}$: the first-order condition gives $g = \beta S$, and the maximum is $\beta^{\beta}(1-\beta)^{1-\beta}S(y)$, linear and increasing in $W(y)$. So the Nash solution picks $y^*$ by itself: the Coase theorem holds inside it, and the weights move only the split. The symmetric case gives $(S/2)^2$, also increasing in $W$.
> Ref: Aula 2 notes §5.1; Varian (2014), §30.7, p. 581
> Similar: M&R Mathematical Exercise 2.1, p. 53

Q: Suppose $W(y^*) > d_1 + d_2$. What is party 1's payoff, and how does it respond to the two threat points?
- $u_1 = d_1 + \beta[W(y^*) - d_1 - d_2]$, with $\partial u_1/\partial d_1 = 1 - \beta$ and $\partial u_1/\partial d_2 = -\beta$
- $u_1 = d_1 + \beta[W(y^*) - d_1 - d_2]$, with $\partial u_1/\partial d_1 = 1$ and $\partial u_1/\partial d_2 = -\beta$
- $u_1 = \beta W(y^*)$, with $\partial u_1/\partial d_1 = 0$ and $\partial u_1/\partial d_2 = 0$ at every threat point
- $u_1 = d_1 + (1 - \beta)[W(y^*) - d_1 - d_2]$, with $\partial u_1/\partial d_1 = \beta$ and $\partial u_1/\partial d_2 = \beta - 1$
<!-- YW5zOjA= -->
> Party 1 gets its threat point plus share $\beta$ of the surplus $S = W(y^*) - d_1 - d_2$. Raising $d_1$ adds one unit directly but shrinks the surplus by one, of which party 1 had share $\beta$: net $1 - \beta$. Raising $d_2$ shrinks the surplus and costs party 1 $\beta$. A better outside option helps, but by less than one for one. The fourth option swaps the weights.
> Ref: Aula 2 notes §5.1
> Similar: M&R Mathematical Exercise 2.1, p. 53

Q: Party 2's outside option improves to $d_2'$, so that now $d_1 + d_2' > W(y^*)$. What happens?
- The parties still agree on $y^*$, with party 2 taking the whole of $W(y^*)$ and party 1 receiving a negative transfer
- No agreement is reached, and value is lost, since $W(y^*)$ was the most the parties could create and it now goes unused
- The parties agree on a decision other than $y^*$ that raises $W$ above $d_1 + d_2'$, so the surplus becomes positive again
- No agreement is reached, and that is efficient, since outside uses worth $d_1 + d_2'$ beat anything the parties create together
<!-- YW5zOjM= -->
> Agreement requires a positive surplus, $W(y^*) > d_1 + d_2$. If the threat points sum to more, any deal leaves someone below their outside option, so none is signed; and since outside uses are worth $d_1 + d_2' > W(y^*)$, not trading maximizes total value. No $y$ can beat $y^*$, by definition. A negative transfer below $d_1$ would be refused.
> Ref: Aula 2 notes §5.1
> Similar: Cabral (2017), §6.4 "Negotiations", p. 143

## offers

P: Two players alternate offers over the division of a surplus of size 1, player 1 proposing first, with discount factors $\delta_1, \delta_2 \in (0, 1)$, full information and an infinite horizon (Rubinstein's game).

Q: What is player 1's share in the subgame-perfect equilibrium, and how does it respond to the two discount factors?
- $(1 - \delta_1)/(1 - \delta_1\delta_2)$, falling in $\delta_1$ and rising in $\delta_2$
- $(1 - \delta_2)/(1 - \delta_1\delta_2)$, falling in $\delta_1$ and rising in $\delta_2$
- $(1 - \delta_2)/(1 - \delta_1\delta_2)$, rising in $\delta_1$ and falling in $\delta_2$
- $\delta_2/(1 + \delta_1\delta_2)$, rising in both $\delta_1$ and $\delta_2$
<!-- YW5zOjI= -->
> Player 1 offers player 2 exactly what player 2 would get by waiting and proposing: $x_1 = 1 - \delta_2(1 - \delta_1 x_1)$, so $x_1 = (1 - \delta_2)/(1 - \delta_1\delta_2)$. Differentiating, $\partial x_1/\partial \delta_1 = \delta_2(1 - \delta_2)/(1 - \delta_1\delta_2)^2 > 0$ and $\partial x_1/\partial \delta_2 = -(1 - \delta_1)/(1 - \delta_1\delta_2)^2 < 0$. Own patience helps; the opponent's patience hurts. With equal $\delta$ the share is $1/(1 + \delta)$.
> Ref: Mas-Colell, Whinston & Green (1995), Example 9.AA.2, pp. 297–298; Varian (2014), §30.7, pp. 581–582; Aula 2 notes §5.2
> Similar: MWG 9.AA (finite horizon, Example 9.AA.1), p. 296

Q: Let $\delta_i = e^{-r_i\Delta}$, where $r_i > 0$ is player $i$'s rate of time preference and $\Delta$ the time between offers. What is the limit of player 1's share as $\Delta \to 0$, and how does it relate to the Nash solution?
- $r_2/(r_1 + r_2)$, the Nash split with weight $\beta = r_2/(r_1 + r_2)$, so the more patient player gets more
- $r_1/(r_1 + r_2)$, the Nash split with weight $\beta = r_1/(r_1 + r_2)$, so the more impatient player gets more
- $\tfrac12$, the symmetric Nash split, since the first-mover advantage vanishes and patience stops mattering
- $1 - r_2$, the Nash split with weight $\beta = 1 - r_2$, so the share depends only on the opponent's patience
<!-- YW5zOjA= -->
> For small $\Delta$, $1 - e^{-r\Delta} \approx r\Delta$, so the share $\to r_2\Delta/[(r_1 + r_2)\Delta] = r_2/(r_1 + r_2)$. The first-mover advantage does vanish, but patience does not stop mattering: a low $r_1$ (patient player 1) raises the share. That is the Nash split with weight $\beta = r_2/(r_1 + r_2)$, giving the axiomatic weights a strategic foundation.
> Ref: Aula 2 notes §5.2; Mas-Colell, Whinston & Green (1995), Appendix 9.AA, pp. 296–298
> Similar: MWG 9.AA, p. 296

Q: In the equilibrium of this game, what does the timing of agreement imply for the Coase theorem's hypothesis of efficient bargaining?
- Agreement comes only after a delay that shrinks the surplus, so even under full information the game breaks the efficient bargaining Coase assumes
- Agreement comes at once, but the more patient player picks the project, so patience decides what is produced as well as who gets the surplus
- Agreement comes at once only when the discount factors are equal, so with unequal patience the bargaining game falls short of what Coase assumes
- Agreement comes at once and the whole surplus is divided, so under full information the game itself delivers the efficient bargaining Coase assumes
<!-- YW5zOjM= -->
> In the unique subgame-perfect equilibrium the first offer is accepted, whatever $\delta_1$ and $\delta_2$ are, so nothing is lost to delay. Patience moves only the division, just as the Coase theorem says bargaining power should. Delay and failed deals need something the model leaves out, such as private information or haggling costs, which is where Aula 3 starts.
> Ref: Aula 2 notes §5.2; Milgrom & Roberts (1992), Ch. 2, p. 38; Ch. 5, pp. 140–149
> Similar: MWG 9.AA, p. 296

## objectives

Q: A dairy cooperative is owned by the farmers who sell it their milk. Why might its owners not want it to maximize its own profit, and what objective does the value maximization principle give it instead?
- Profit ignores the farmers' labour, which owners supply for free; with no wealth effects, the objective is the farmers' total income from milk sales alone
- Profit counts the milk price as a cost, while owners also receive it as revenue; with no wealth effects, the objective is total value of all affected parties
- Profit is taxed while milk payments are not; with no wealth effects, the objective is to minimize the cooperative's measured profit through the milk price
- Profit belongs to outside lenders, who own the cooperative's debt; with no wealth effects, the objective is to maximize the lenders' expected repayment
<!-- YW5zOjE= -->
> An owner who is also a supplier gains from a higher milk price what the cooperative loses in profit, so profit is not the owners' objective (M&R p. 40; FFT 2.2). Only when the value maximization principle applies is there an objective implied by efficiency alone: the total value of the affected parties, here members, buyers and anyone else whose payoff the decisions change. Farmers' income alone leaves out the other parties.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 39–40; Aula 2 notes §6
> Similar: M&R FFT 2.2, p. 52

## aula1

Q: In Aula 1, every comparison of organizational systems maximized a single profit function $\pi(x, y)$ over practices. What licenses treating the organization as having that one objective?
- The firm's legal owners are residual claimants, so whatever maximizes their profit is efficient for every party, whatever transfers are feasible
- With complementary practices, the profit function is supermodular, which guarantees a unique maximum that all of the parties agree to choose
- With no wealth effects and free transfers, efficiency requires maximizing total value; transfers settle who gets what separately
- With efficient bargaining, the parties' bargaining power determines the system, and the strongest party's profit is the function maximized
<!-- YW5zOjI= -->
> One objective is legitimate only under the value maximization principle: then efficiency picks the system by total value, and the division is a separate matter settled by money. Supermodularity orders choices but does not guarantee a unique maximum (Aula 1's two coherent systems), and bargaining power moves only the split.
> Ref: Milgrom & Roberts (1992), Ch. 2, pp. 36–39; Aula 2 notes §7; Aula 1 notes §6–§7
> Similar: M&R FFT 2.2, p. 52

Q: When a party's pay is a fixed share of the value it helps create and side payments cannot be renegotiated freely, what changes relative to the value maximization principle, and which Aula 1 case illustrates it?
- Each party's action tracks its own share rather than the total, so the split shapes the size of the pie, as in Salomon's individual trading bonuses
- Each party still chooses the value-maximizing action, since shares only redistribute the total, as in GM's divisions under Sloan's financial controls
- Each party's action tracks the total once shares are equal, so equal splits restore efficiency, as in Toyota's long-term relations with its suppliers
- Each party's action tracks its bargaining power rather than the total, so the stronger side picks the system, as in Ford's moving assembly line
<!-- YW5zOjA= -->
> With fixed shares each party maximizes its own share minus its own cost, not total value, so incentives and the size of the pie stop being separable. Salomon's near piece-rate bonuses rewarded each trader's own profit and discouraged sharing information across departments; HBC's flat salaries are the opposite failure. Equal shares restore efficiency only by coincidence of costs. Aulas 13–16 study this case as moral hazard.
> Ref: Aula 2 notes §3.2, §7; Aula 1 notes §4; Milgrom & Roberts (1992), Ch. 1, pp. 9–12
> Similar: M&R FFT 1.3, p. 18

Q: The Coase theorem says efficient bargainers reach the value-maximizing decision. What does Aula 1's valley between coherent systems add to that claim?
- Nothing new: bargainers who adjust one practice at a time climb to the best system, since every step that raises total value is agreed
- With complementary practices, total value has no maximum, so the theorem's prediction is undefined until the practices become substitutes
- With complementary practices, wealth effects necessarily appear, so the efficient system depends on who held the assets at the start
- With complementary practices, one-step adjustments can stall at a lower coherent system; reaching the best one needs a coordinated jump
<!-- YW5zOjM= -->
> Coase assumes the bargain reaches the maximum of total value. With complementarities there can be two coherent systems, each a local peak, separated by a valley: every single step from the lower peak loses value, so step-by-step agreement stops there. Reaching the higher peak needs a whole-system change, which is what organization (and central choice among systems) is for. Complementarity says nothing about wealth effects.
> Ref: Aula 2 notes §7; Aula 1 notes §7–§8; Milgrom & Roberts (1992), Ch. 4, pp. 111–113
> Similar: Companion "The Valley Between Systems"
