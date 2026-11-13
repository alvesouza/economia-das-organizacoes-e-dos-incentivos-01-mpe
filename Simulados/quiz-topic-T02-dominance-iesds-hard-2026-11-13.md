---
quiz: "Topic T2 · Hard conceptual quiz — Dominance and IESDS"
tags:
  dom: "Strict and weak dominance"
  iesds: "Iterated elimination of strictly dominated strategies"
  ck: "IESDS and common knowledge of rationality"
  space: "Dominance in the location game"
---

## dom

Q: Player 1 has rows T, M and B against player 2's columns L and R. Player 1's payoffs: T pays 3 against L and 0 against R, M pays 1 and 1, B pays 0 and 3. Against each column some row pays more than M. Which statement is correct?
- M is strictly dominated: in each column some other row pays more than M, so a rational player 1 never plays M against either column
- M is strictly dominated by T: T beats M by 2 against L and loses only by 1 against R, so T pays more than M on balance across columns
- No row strictly dominates M: T pays less than M against R, B less against L, and dominance needs one row winning in both columns
- M is weakly dominated by both T and B: each of them pays at least as much as M in one column and strictly more in the other column
<!-- YW5zOjI= -->
> Strict dominance asks for one alternative that wins against every $s_{-i}$: a single row must beat M in every column. T loses to M against R and B loses to M against L, so no pure row dominates M; 'for each column some row is better' is the wrong order of quantifiers.
> Comparing net gains across columns is not dominance. Weak dominance still needs at least as much in every column, which T and B each fail in one column. (The 50-50 mix of T and B pays 1.5 in each column, so M is dominated by a mixed strategy; the pure IESDS of the slides does not use that.)
> Ref: Lecture 1 slide 23; Tadelis (2013), Def. 4.1 (p. 60), §6.3 (pp. 114–115); Gibbons (1992), §1.3.A, Fig. 1.3.1 (p. 32)

Q: In a finite game, which property is equivalent to $s_i$ being a strictly dominant strategy for player $i$?
- $s_i$ is the unique best response to every pure profile $s_{-i}$, so it beats each alternative at each one
- $s_i$ is a best response to every profile $s_{-i}$, though it may tie with other strategies of $i$ at some of them
- $s_i$ is the unique best response to the profile $s_{-i}^*$ that the opponents play in some Nash equilibrium
- $s_i$ is the only strategy of player $i$ left by IESDS, every other strategy of player $i$ being removed
<!-- YW5zOjA= -->
> Being the unique best response at a given $s_{-i}$ means paying strictly more than every other strategy there; holding at every $s_{-i}$, that is exactly strict dominance of every alternative.
> Allowing ties gives a strategy that is a best response to everything, which is weak dominance in the sense of Tadelis's remark ($\ge$ everywhere), not strict. Uniqueness against one equilibrium profile says nothing about other profiles. A unique IESDS survivor need not be dominant: it can be beaten against a column that IESDS removed later.
> Ref: Lecture 1 slide 23; Lecture 2 slide 10; Tadelis (2013), Defs. 4.1–4.2 (pp. 60–61), Remark (p. 63)

Q: Which statement about strict dominance and Pareto optimality is correct in general?
- A profile using a strictly dominated strategy is always Pareto dominated, namely by the profile where that player switches to its dominator
- A profile of strictly dominant strategies is always Pareto optimal, since each player then does as well as she can given the others
- A profile using a strictly dominated strategy can be Pareto optimal, but only in games in which no player has a dominant strategy
- A profile using a strictly dominated strategy can be Pareto optimal, and a profile of strictly dominant strategies can be Pareto dominated
<!-- YW5zOjM= -->
> The prisoner's dilemma shows both halves: (M, F) is Pareto optimal although M is strictly dominated, and the strict dominant-strategy equilibrium (F, F) is Pareto dominated by (M, M).
> Switching to the dominator helps the switcher but can hurt the others, so it need not be a Pareto improvement: from (M, F), player 1's switch to F lowers player 2 from −1 to −4. Being a best reply 'given the others' is an individual statement, not a Pareto one. The prisoner's dilemma has dominant strategies for both players, and (M, F) is still Pareto optimal.
> Ref: Lecture 1 slides 24–26; Tadelis (2013), Def. 3.5 (p. 57), §4.1.3 (p. 62)

## iesds

Q: Player 1 chooses T, M or B, player 2 chooses L or R. Payoffs (player 1, player 2): (T, L) = (1, 1), (T, R) = (0, 0), (M, L) = (1, 1), (M, R) = (2, 1), (B, L) = (0, 0), (B, R) = (2, 1). M weakly dominates both T and B. What happens if weakly dominated strategies are removed iteratively?
- The order is irrelevant: every sequence ends at M against R with payoffs (2, 1), because M weakly dominates both T and B at the start
- The result depends on the order: removing T first ends at payoffs (2, 1), removing B first at (1, 1), so there is no unique answer
- The order is irrelevant: every sequence ends at M against L with payoffs (1, 1), because L is a best reply to every row of player 1
- The order is irrelevant here, since order dependence of weak elimination needs at least three strategies for each of the two players
<!-- YW5zOjE= -->
> Remove T first: on rows M and B, R pays player 2 at least as much as L and strictly more against B, so L goes, leaving M or B against R, payoffs (2, 1). Remove B first: on rows T and M, L pays at least as much as R and strictly more against T, so R goes, leaving T or M against L, payoffs (1, 1). Removing T and B together leaves M with L and R tied. Three orders, three answers.
> No strategy here is strictly dominated, so IESDS removes nothing and is order-free, which is why the course uses strict dominance. L is not a best reply to B (0 < 1), and order dependence already appears with three strategies against two.
> Ref: Lecture 1 slides 23, 29; Tadelis (2013), Remark (p. 63); MWG (1995), §8.B (pp. 238–240)

Q: Why does the order in which strictly dominated strategies are removed not affect what survives in a finite game?
- A strategy dominated against some opponent profiles stays dominated against any subset, and if its dominator falls later, a survivor dominates it too
- Each strictly dominated strategy has exactly one dominator, so whatever the order, every strategy is removed by the same strategy and in the same round
- Strict dominance is checked only against the original strategy sets, so removing strategies earlier or later never changes any of the comparisons
- Payoffs in a finite game are bounded, so every order of removal reaches the same set after at most $|S_1|+\dots+|S_n|$ rounds of elimination
<!-- YW5zOjA= -->
> Shrinking the opponents' sets only removes conditions, so a dominated strategy stays dominated. If its dominator $s_i'$ is itself eliminated later by $s_i''$ on a smaller set, then $s_i''$ beats $s_i$ on that set as well; finiteness ends the chain at a surviving strategy, so $s_i$ is eliminated in every order.
> A strategy can have several dominators and be removed in different rounds under different orders; only the final set is order-free. Dominance is checked against the surviving sets $S_{-i}^{k-1}$, not the original ones. Bounded payoffs play no role in the argument; finiteness of the strategy sets does.
> Ref: Lecture 1 slide 29; Tadelis (2013), §4.2.1 (p. 65); MWG (1995), §8.B (pp. 239–240) and Exercise 8.B.4

Q: In a finite two-player game, player 1 has a strictly dominant strategy $s_1^D$ and player 2 has none. What survives IESDS?
- Exactly $\{s_1^D\}\times S_2$: player 1's other strategies go first, but player 2 has no dominated strategy, so all of hers survive
- Exactly $\{s_1^D\}\times BR_2(s_1^D)$ if player 2's best reply is unique; if it is not, the elimination stops after the first round
- Exactly $\{s_1^D\}\times BR_2(s_1^D)$: player 1's other strategies go first, then each of player 2's that is not a best reply to $s_1^D$
- Possibly more than $s_1^D$ for player 1, since dominance is checked only against strategies of player 2 that are still standing
<!-- YW5zOjI= -->
> Every other strategy of player 1 is strictly dominated by $s_1^D$ and goes in round 1. Against the single surviving row, any $s_2$ that is not a best reply to $s_1^D$ pays strictly less than a best reply, so it is now strictly dominated and goes in round 2; all best replies tie and survive.
> Dominance is relative to the opponents' surviving strategies, so player 2's strategies become dominated once player 1's set shrinks. Ties among best replies do not stop the elimination of the non-best replies. A strategy that is strictly dominant against all of $S_2$ remains so against any subset, so none of player 1's other strategies survive.
> Ref: Lecture 1 slides 25, 29; Tadelis (2013), §4.2.1 (p. 65), Prop. 4.2 (p. 68)

Q: In a finite game IESDS always leaves each player at least one strategy. Which example shows that this can fail once strategy sets are infinite?
- Each player names $x_i\in[0,1]$ and earns $x_i$: every number below 1 goes in round 1, so in the end not even the number 1 is left
- Each player names $x_i\in[0,1)$ and earns $x_i$: every number is strictly dominated by a larger one, so no strategy survives at all
- The linear Cournot duopoly: no output survives every round, since the interval of surviving outputs keeps shrinking after each round
- The Bertrand duopoly: $p_i=c$ is weakly dominated, so IESDS removes it first and then removes each of the remaining prices in turn
<!-- YW5zOjE= -->
> On $[0,1)$ there is no largest number, so every strategy is strictly dominated in round 1 and the surviving set is empty. In a finite game a best reply to a surviving profile always exists and cannot be strictly dominated, so each $S_i^k$ stays nonempty.
> On the closed interval $[0,1]$ the number 1 is a best reply and survives. In Cournot the nested intervals shrink to the single output 30 in Tadelis's example, which survives every round. IESDS uses strict dominance, and a weakly dominated price such as $p_i=c$ is not removed by it.
> Ref: Lecture 1 slide 29; Tadelis (2013), §4.2.2 (pp. 65–67), §4.2.3 (p. 67); Notas/L01/L01-10-pitfalls.md, True/False item 13

Q: Which elimination procedure can delete a pure-strategy Nash equilibrium of a finite game?
- Iterated removal of strictly dominated pure strategies, provided the dominated strategies are removed in a particular order
- Iterated removal of strategies that are never a best response, once the beliefs that justify strategies may be mixed
- Removal of strategies strictly dominated by a mixed strategy, since a mixture can beat a pure strategy no pure one beats
- Iterated removal of weakly dominated strategies, since an equilibrium strategy can tie with its dominator at the others' play
<!-- YW5zOjM= -->
> If (U, L) gives (1, 1) and the other three cells give (0, 0), then (D, R) is a Nash equilibrium although D is weakly dominated by U; removing D deletes it. Bertrand's (c, c) is another equilibrium in weakly dominated strategies.
> Every Nash equilibrium survives IESDS whatever the order, by the first-round argument: a strategy removed in the first round in which an equilibrium component falls would be beaten against $s_{-i}^*$. The same argument covers never-best-responses and strategies dominated by mixtures, since an equilibrium strategy is a best response to $s_{-i}^*$.
> Ref: Lecture 2 slide 16 (Prop. 1 and its note), slide 36; Tadelis (2013), §5.3 (p. 95), §6.3 (pp. 114–116)

## ck

Q: Player 1 chooses U or D, player 2 chooses L, C or R. Player 1 gets 3, 2, 0 from U and 1, 1, 5 from D against L, C, R. Player 2 gets 2 from L against U and 0 against D, 1 and 3 from C, 0 and 1 from R. IESDS ends at (U, L) after three rounds. What does the last step, removing C, require?
- That player 2 is rational, knows player 1 is rational, and knows player 1 knows that player 2 is rational
- Only that player 2 is rational, since L strictly dominates C against both of player 1's rows from the start
- That player 2 is rational and knows player 1 is rational, but nothing about what player 1 knows of player 2
- That rationality is common knowledge to every depth, since IESDS cannot remove anything with finite depth
<!-- YW5zOjA= -->
> Round 1: C strictly dominates R, which uses only player 2's rationality. Round 2: once R is gone, U strictly dominates D (3 > 1, 2 > 1), which needs player 1 rational and knowing player 2 is rational. Round 3: against U alone, L beats C (2 > 1); player 2 can use this only if she knows player 1 has dropped D, that is, if she knows player 1 is rational and knows player 2 is rational.
> C beats L against D (3 > 0), so L does not dominate C at the start. Knowing that player 1 is rational is not enough for player 2, because player 1 drops D only if he knows player 2 is rational. Three rounds need two levels of knowledge, not infinitely many.
> Ref: Lecture 1 slide 28; Lecture 2 slide 7; Tadelis (2013), §4.2.1 (pp. 63–65)

## space

Q: Two chains each open one store on an avenue of 8 blocks with one customer per block. They choose blocks simultaneously, customers buy at the nearer store and split evenly when equidistant, and each chain maximizes customers. What does IESDS predict?
- Both chains end on block 4, since block 4 strictly dominates block 5 once blocks 1 to 3 and blocks 6 to 8 have been eliminated
- Each chain ends on some block from 3 to 6, since with an even number of blocks the elimination stops after the first round
- Each chain ends on block 4 or 5, and each of the four resulting profiles is a Nash equilibrium giving each chain 4 customers
- Nothing is eliminated, since with an even number of blocks no block is strictly dominated by another one at the start
<!-- YW5zOjI= -->
> Blocks 1 and 8, then 2 and 7, then 3 and 6 are removed in three rounds, as on the 7-block avenue. Blocks 4 and 5 then tie against a rival on block 4 (4 customers each way), so neither dominates the other and both survive; each of (4, 4), (4, 5), (5, 4) and (5, 5) gives each chain 4 customers and is a Nash equilibrium.
> Block 4 does not beat block 5 against a rival on block 4. The elimination runs three rounds, not one. Block 1 is strictly dominated by block 2 from the start, whatever the parity of the avenue.
> Ref: Lecture 1 slides 32–33; Lecture 2 slide 3; Tadelis (2013), Exercise 4.10 (p. 78)
> Similar: Listas/pratica-lecture-01.md, item 18 (Tadelis 4.10)
