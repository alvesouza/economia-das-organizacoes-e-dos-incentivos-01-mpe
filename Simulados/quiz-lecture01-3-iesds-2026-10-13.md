---
quiz: "Lecture 1 · Quiz 3 of 3 — Iterated elimination, Cournot and spatial competition"
tags:
  props: "Properties of IESDS"
  ck: "Common knowledge of rationality"
  cournot: "Cournot by iterated elimination"
  space: "Spatial competition"
---

## props

Q: In a finite game, how does the set of surviving profiles depend on the order in which dominated strategies are removed?
- It never depends on the order, for strict or weak dominance alike, since each removed strategy is worse than another against every remaining profile
- Under strict dominance it does not depend on the order or speed of removal; under weak dominance it can, so the result may hinge on the procedure
- Under strict dominance it can depend on the order, since removing one player's strategy first may save another's; under weak dominance it cannot
- It depends on the order under both, so IESDS fixes a canonical order, removing every dominated strategy of every player in each round
<!-- YW5zOjE= -->
> A strictly dominated strategy stays strictly dominated when opponents' strategies are removed (fewer profiles to check), so delaying a removal never saves it: the final set is order-independent. A weakly dominated strategy can lose its dominator's strict advantage once the one profile where it was strict is removed, so different orders can leave different survivors. The slides' recursion removes everything at once each round, a convenience that matters only for weak dominance.
> Ref: Lecture 1 slides 28–29; Tadelis (2013), §4.2 (pp. 63–69); MWG §8.B (pp. 238–241)
> Similar: MWG 8.B.4, p. 262; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 16–17, pp. 31–33

Q: Why is a strict dominant-strategy equilibrium $s^D$ the unique profile that survives IESDS?
- Because IESDS selects Pareto optimal profiles, and a strict dominant-strategy equilibrium is always Pareto optimal
- Because $S^\infty$ is a single profile in every finite game, and a dominant-strategy profile is never removed
- Because a dominant strategy is a best response to every profile, so it survives, while other survivors are tie-broken away
- Because in round one each $s_i^D$ strictly dominates every other strategy of player $i$, so only $s^D$ remains
<!-- YW5zOjM= -->
> Strict dominance of $s_i^D$ over every alternative means all of player $i$'s other strategies are removed in the first round, simultaneously for every player, leaving $\{s^D\}$. The prisoner's dilemma shows that the survivor need not be Pareto optimal, and many games keep several survivors, so $S^\infty$ is not a singleton in general.
> Ref: Lecture 1 slides 25, 29; Tadelis (2013), Prop. 4.2 (p. 68)
> Similar: Tadelis (2013), Exercise 4.5, p. 77

Q: For a finite game, how do existence and uniqueness look for the set $S^\infty$ of profiles that survive IESDS?
- Nonempty in every finite game, since a best reply to some surviving profile is never strictly dominated, but often large, as in coordination games
- Nonempty and a single profile in every finite game, since each round removes at least one strategy until one profile remains for all players
- Possibly empty, since a round can remove every strategy of a player whose strategies all dominate one another in a cycle
- Nonempty only when some player has a dominant strategy, since otherwise the first round has nothing to remove and the procedure fails at once
<!-- YW5zOjA= -->
> At each round, each player's best reply to any surviving opponent profile maximizes payoff against it, so no surviving strategy strictly beats it there: it is never removed, and $S^\infty \neq \emptyset$ (existence). Strict dominance is a strict order and cannot cycle. But uniqueness often fails: in a pure coordination game no strategy is dominated and nothing is removed, so all profiles survive. A first round with nothing to remove ends the procedure at $S$, not in failure.
> Ref: Lecture 1 slides 22, 29; Tadelis (2013), §4.2.3 (pp. 67–68)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 9, p. 17

## ck

Q: In a two-player finite game, IESDS removes strategies in rounds $1$ to $K$ and then stops. What is the least assumption about rationality that justifies predicting a profile in $S^\infty$?
- Each player is rational, and nothing about knowledge is needed, since each round only asks a player to avoid own strictly dominated strategies
- Common knowledge of rationality and nothing less, since any finite level of mutual knowledge leaves some round of removal unjustified
- Rationality plus $K - 1$ levels of mutual knowledge of rationality; common knowledge is sufficient but asks more than this game needs
- Rationality plus $K$ levels of mutual knowledge of rationality, one level for each round, counting the first round of removal as well
<!-- YW5zOjI= -->
> Round 1 needs only rationality. Removing a strategy in round 2 relies on knowing that the opponent is rational (one level of knowledge); round $k$ relies on $k - 1$ levels ("I know that you know that …"). A procedure that stops at round $K$ therefore needs $K - 1$ levels. Common knowledge, the infinite hierarchy, covers every finite game at once, which is why the slides invoke it.
> Ref: Lecture 1 slides 16, 28; Tadelis (2013), §4.2 (pp. 63–65)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 12, p. 23

## cournot

P: Two firms choose outputs $q_1, q_2 \ge 0$ simultaneously. Inverse demand is $P = a - b(q_1 + q_2)$ and each firm has constant marginal cost $c$, with $a > c \ge 0$ and $b > 0$, so firm $i$'s profit is $q_i(a - c - bq_i - bq_j)$. Let $q^M = (a - c)/(2b)$ denote the monopoly output.

Q: Which outputs are strictly dominated in the first round?
- Every $q_i > (a-c)/(2b)$, each strictly dominated by $q^M$, since output past $q^M$ lowers profit at every $q_j$
- Every $q_i > (a-c)/b$, each strictly dominated by $q^M$, since only outputs that push the price below $c$ lose money
- Every $q_i > (a-c)/(3b)$, each strictly dominated by $(a-c)/(3b)$, since that output is the best reply to itself
- No output, since each $q_i \ge 0$ is a best reply to some $q_j \ge 0$, so the first round has nothing to act on
<!-- YW5zOjA= -->
> For $q_i > q^M$: $\pi_i(q_i) - \pi_i(q^M) = (q_i - q^M)[a - c - bq_j - b(q_i + q^M)]$, and since $q_i + q^M > (a-c)/b$ the bracket is below $-bq_j \le 0$: strictly negative for every $q_j$. Best replies $\max\{(a - c - bq_j)/(2b), 0\}$ never exceed $q^M$, so outputs above it are best replies to nothing. Outputs that lose money are only part of the dominated set.
> Ref: Lecture 1 slides 4, 29; Tadelis (2013), §4.2 (Cournot, p. 65); Gibbons (1992), §1.1.B and §1.2.A
> Similar: Tadelis (2013), Exercise 4.6, p. 77

Q: Once the first round has removed every output above $q^M$ for both firms, which outputs survive the second round?
- $[0, (a-c)/(2b)]$, since every output in that range is a best reply to some rival output that still survives the first round
- $[(a-c)/(3b), (a-c)/(2b)]$, since outputs below the best reply to itself are now strictly dominated
- $[(a-c)/(4b), (a-c)/b]$, since a rival producing up to $q^M$ pushes each best reply up to $(a-c)/b$
- $[(a-c)/(4b), (a-c)/(2b)]$, since the best reply to the largest surviving rival output, $q^M$, is $(a-c)/(4b)$
<!-- YW5zOjM= -->
> With $q_j \le q^M$, every best reply is at least $(a - c - bq^M)/(2b) = (a-c)/(4b)$. Profit is concave in $q_i$ with its peak at or above $(a-c)/(4b)$, so any smaller output earns strictly less than $(a-c)/(4b)$ against every surviving $q_j$: strictly dominated. Outputs in $[(a-c)/(4b), q^M]$ are best replies to surviving rival outputs and stay.
> Ref: Tadelis (2013), §4.2 (Cournot, p. 65); Gibbons (1992), §1.2.A; Lecture 1 slide 29
> Similar: Tadelis (2013), Exercise 4.6, p. 77

Q: Where does the elimination end?
- At the interval $[(a-c)/(4b), (a-c)/(2b)]$, since after two rounds no remaining output is dominated
- At the single output $(a-c)/(3b)$ for each firm, since the bounds alternate and converge to the fixed point
- At the single output $(a-c)/(4b)$ for each firm, since each round lowers the upper bound to a best reply of the rival
- At the single output $(a-c)/(2b)$ for each firm, since the monopoly output is the only one never dominated
<!-- YW5zOjE= -->
> Each round replaces the bounds by best replies to the opposite bound: $\overline{q}_{k+1} = (a - c - b\underline{q}_k)/(2b)$ and $\underline{q}_{k+1} = (a - c - b\overline{q}_k)/(2b)$. The map has slope $-\tfrac12$, so both bounds converge to its fixed point $q = (a - c - bq)/(2b)$, i.e. $q = (a-c)/(3b)$. The unique survivor coincides with the Cournot equilibrium of Lecture 2.
> Ref: Tadelis (2013), §4.2 (Cournot, p. 65); Gibbons (1992), §1.2.A
> Similar: MWG 8.B.5, p. 262

P:

Q: $n \ge 3$ identical firms choose outputs $q_i \ge 0$ simultaneously, with inverse demand $P = a - b\sum_j q_j$, constant marginal cost $c$, $a > c \ge 0$ and $b > 0$. What does IESDS deliver?
- The single output $(a-c)/((n+1)b)$ for each firm, by the same alternating bounds that work with two firms
- The single output $(a-c)/(2nb)$ for each firm, since each round splits the monopoly output among the firms
- The interval $[0, (a-c)/(2b)]$ each, since rivals' total can reach $(a-c)/b$, making 0 a best reply
- No elimination at all, since with three or more firms every output is a best reply to some rival profile
<!-- YW5zOjI= -->
> Round one removes outputs above $q^M = (a-c)/(2b)$, as with two firms. But now the rivals' total can be as large as $(n-1)q^M \ge (a-c)/b$, against which the best reply is 0; every output in $[0, q^M]$ is a best reply to some surviving rival profile and is never strictly dominated. Elimination stops after one round, far from the Cournot output $(a-c)/((n+1)b)$: IESDS has little bite here, one reason Lecture 2 needs Nash equilibrium.
> Ref: Tadelis (2013), §4.2 (Cournot, p. 65); Gibbons (1992), §1.2.A; MWG §8.B (pp. 238–241)
> Similar: MWG 8.B.5, p. 262

## space

P: Two firms each pick a block among $1, \dots, n$ on a street, simultaneously, with $n = 2k + 1$ odd and $k \ge 1$. Each block holds one customer, who buys from the nearest firm and splits evenly when the two are equally distant (including when both pick the same block). Each firm maximizes its number of customers.

Q: How does IESDS proceed, and what survives?
- Round one removes every block except the middle one, since the middle block strictly dominates all the others at once
- Nothing is removed, since each block is a best reply to some location of the rival, so every profile of blocks survives
- Each round removes one end block for each firm, alternating sides, so $2k$ rounds leave the profile ($k + 1$, $k + 1$)
- Each round removes the two outermost surviving blocks, so after $k$ rounds only the median block $k + 1$ survives
<!-- YW5zOjM= -->
> An end block is strictly dominated by its neighbour: moving one block inward gains customers whatever the rival does. Nothing else is dominated in round one (block 2 is the best reply to a rival at block 1, so the middle cannot dominate it). Once the ends are gone for the rival, the next blocks in become dominated, and so on: $k$ rounds, one pair of blocks each, leave ($k + 1$, $k + 1$). Ends are not all best replies, so the second option fails.
> Ref: Lecture 1 slides 29, 31–33; Tadelis (2013), §4.2 (pp. 63–69), §5.2.5 (p. 93)
> Similar: Tadelis (2013), Exercise 4.10, p. 78

Q: Customers dislike walking. How does the IESDS prediction compare with the pair of locations that minimizes customers' total walking distance?
- They coincide, since both firms at the median minimize the total distance, as the median minimizes the sum of distances to points
- They differ: the IESDS pair clusters at the median, while the distance-minimizing pair spreads out, each firm near a quartile
- They differ: the distance-minimizing pair puts the firms at the two ends of the street, so each half is served from its edge
- They coincide only when $n$ is large, since the quartile and median locations converge as the street gets longer and denser
<!-- YW5zOjE= -->
> The median minimizes the sum of distances for one facility; with two, each should sit at the median of the half it serves, near the quartiles, which halves total walking compared with clustering at the centre. Competition for the marginal customer drives both firms to the middle anyway: the private gain from stealing customers ignores the walking cost. With prices also chosen, clustering would trigger price competition, which pushes firms apart.
> Ref: Lecture 1 slides 26, 31–33; Tadelis (2013), §5.2.5 (p. 93); Cabral (2017), §14.2 (pp. 358–360)
> Similar: Tadelis (2013), Exercise 4.10, p. 78; Gibbons (1992), Problem 1.8, p. 50
