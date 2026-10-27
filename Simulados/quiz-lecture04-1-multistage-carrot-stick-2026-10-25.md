---
quiz: "Lecture 4 · Quiz 1 of 3 — Multistage games, the carrot and the stick (estimated unit, written before the lecture)"
tags:
  msg: "Multistage games: payoffs, histories and strategies"
  cs: "Subgame perfection across stages: the carrot and the stick"
  osd: "The one-stage deviation principle"
  app: "Two-stage applications: bank runs and tariffs"
---

## msg

Q: Two players play a two-stage game. In stage 1 each chooses simultaneously among $m$ actions; the stage-1 outcome is observed by both; in stage 2 each chooses simultaneously among $k$ actions. How many pure strategies does each player have?
- $m\,k^{m}$, one stage-2 action for each of the $m$ actions that the player could have chosen in stage 1
- $m\,k^{m^2}$, one stage-2 action for each of the $m^2$ stage-1 outcomes that the player could observe
- $m + k\,m^{2}$, one stage-1 action plus one stage-2 action for each of the $m^2$ stage-1 outcomes
- $(m\,k)^{m^2}$, one pair of stage-1 and stage-2 actions for each of the $m^2$ possible stage-1 outcomes
<!-- YW5zOjE= -->
> A strategy names a stage-1 action ($m$ choices) and, for each of the $m^2$ observable stage-1 outcomes, a stage-2 action ($k$ choices each), so $|S_i| = m \cdot k^{m^2}$. With $m = k = 2$ this is $2 \cdot 2^4 = 32$, Tadelis's count for the Prisoner-Revenge Game. Conditioning only on one's own stage-1 action forgets that the opponent's action is observed too; adding instead of multiplying confuses the number of entries in the plan with the number of plans.
> Ref: Tadelis (2013), §9.3 (pp. 178–180); Gibbons (1992), §2.2.A (pp. 71–73)
> Similar: Tadelis (2013), Exercise 9.1, pp. 186–187

Q: In a multistage game whose stage outcomes are publicly observed, how many information sets does a player have at stage $t$, and why does each of them contain more than one decision node?
- One per action the player took in earlier stages, since a player only conditions on what she did; each set has several nodes because others moved too
- One per action profile of stage $t$ itself, since the player must plan for every profile; each set has several nodes because the past is forgotten
- Exactly one, since all players move simultaneously at stage $t$; the set has several nodes because every earlier history leads into it
- One per possible outcome of stages $1$ to $t-1$, since all of that is observed; each set has several nodes because stage-$t$ moves are simultaneous
<!-- YW5zOjM= -->
> Public observation of each stage means the player knows the whole history $h_{t-1}$, so there is one information set per history in $H_{t-1}$. Inside stage $t$ the players still move without seeing each other's current choice, so each set pools the nodes that differ only in the others' stage-$t$ moves. Collapsing all histories into one set would describe a game in which earlier outcomes are never revealed, which is outside Tadelis's definition.
> Ref: Tadelis (2013), §9.1 (p. 176), §9.3 (p. 178)
> Similar: Tadelis (2013), Exercise 9.2, p. 187

## cs

Q: Players use "unconditional" strategies: at every stage $t$ each plays a fixed Nash equilibrium of the stage-$t$ game, whatever happened before. Why is this a subgame-perfect equilibrium for every discount factor $\delta \in [0,1]$?
- Because later play ignores earlier outcomes, it adds the same constant to every cell of each earlier stage, and a constant changes no best response
- Because a low enough $\delta$ makes the future negligible, and Proposition 9.1 is stated for the case in which only the current stage carries any weight
- Because Proposition 9.2 requires a stage-game equilibrium in every stage, and any profile that meets that requirement is subgame perfect automatically
- Because one-stage deviations at stage 1 are unprofitable once $\delta$ exceeds the ratio of the one-shot gain to the gap between the stage-2 equilibria
<!-- YW5zOjA= -->
> Fix any subgame starting at stage $t$. Sunk payoffs are constants, and the discounted payoff of stages after $t$ is also a constant because unconditional play does not react to the stage-$t$ outcome. Adding constants leaves best responses unchanged, so the stage-$t$ equilibrium remains a best response; induct back to $t = 1$. Proposition 9.2 restricts only the last stage, and the threshold in the last option belongs to history-dependent strategies.
> Ref: Tadelis (2013), Prop. 9.1 (p. 180), footnote 3 (p. 181)
> Similar: Tadelis (2013), Exercise 9.1, pp. 186–187

P: In stage 1 of a two-stage game the target profile $a^*$ is not a stage Nash equilibrium: a tempted player gains $g > 0$ by deviating unilaterally. Stage 2 has two Nash equilibria that pay this player $c$ (the carrot) and $s$ (the stick), with $c > s$. Players use the strategies "carrot after $a^*$, stick after any other stage-1 outcome", and payoffs are $v_{i1} + \delta v_{i2}$ with $\delta \in [0,1]$.

Q: For which discount factors is $a^*$ in stage 1, followed by the carrot, a subgame-perfect path?
- $\delta \ge (c - s)/g$, since the deviation must be worth less than the gap between the two equilibria scaled by $\delta$
- $\delta \ge g/c$, since only the carrot the player gives up by deviating enters the comparison against the one-shot gain $g$
- $\delta \ge g/(c - s)$, since the one-shot gain $g$ must not exceed the discounted gap $\delta(c - s)$ that deviating forfeits
- $\delta \ge g/(g + c - s)$, since the player compares her one-shot gain $g$ with the total of that gain and the gap $c - s$
<!-- YW5zOjI= -->
> Staying gives the target payoff now plus $\delta c$; deviating gives $g$ more now plus $\delta s$, because the deviation triggers the stick. Staying is a best response iff $\delta c \ge g + \delta s$, that is $g \le \delta(c - s)$, so $\delta \ge g/(c - s)$. Stage-2 play is a stage equilibrium after every history, so no subgame needs a further check. The inverted ratio would make sustaining harder as the stick gets harsher, the opposite of the logic.
> Ref: Tadelis (2013), §9.4 (pp. 182–184), the two requirements (p. 183)
> Similar: Tadelis (2013), Exercise 9.3, pp. 187–188

Q: Let stage 1 be a Prisoner's Dilemma with payoffs $R$ (both mum), $T$ (temptation), $S$ (sucker), $P$ (both fink), $T > R > P > S$, and let the stage-2 equilibria pay $0$ (carrot) and $-\gamma$ (stick), $\gamma > 0$. What does it take to sustain $(M,m)$ and the lopsided $(F,m)$ in stage 1?
- $(M,m)$ needs $\delta \ge (T - R)/\gamma$ and $(F,m)$ needs $\delta \ge (P - S)/\gamma$, since player 2 weighs the sucker payoff against mutual fink
- $(M,m)$ needs $\delta \ge (T - R)/\gamma$ and $(F,m)$ needs $\delta \ge (T - S)/\gamma$, since player 2 weighs the sucker payoff against temptation
- $(M,m)$ needs $\delta \ge (R - P)/\gamma$ and $(F,m)$ needs $\delta \ge (P - S)/\gamma$, since each player weighs the target cell against mutual fink
- $(M,m)$ needs $\delta \ge (T - R)/\gamma$ and $(F,m)$ needs no condition, since player 1 plays her dominant action in stage 1 anyway
<!-- YW5zOjA= -->
> On $(M,m)$ each player compares $R + 0$ with $T - \delta\gamma$: $\delta \ge (T - R)/\gamma$. On $(F,m)$ player 1 plays a dominant action and gets the carrot, so only player 2 binds: $S + 0 \ge P - \delta\gamma$, so $\delta \ge (P - S)/\gamma$, because her deviation from $m$ to $f$ against $F$ moves her from $S$ to $P$, not to $T$. With Tadelis's numbers, $T - R = 1$, $P - S = 2$ and $\gamma = 3$, these are $1/3$ and $2/3$.
> Ref: Tadelis (2013), §9.4 (pp. 182–184)
> Similar: Tadelis (2013), Exercise 9.3, pp. 187–188; Exercise 9.1, pp. 186–187

Q: Why must the punishment carried out in stage 2 be a Nash equilibrium of the stage-2 game, even when a harsher non-equilibrium profile is available to punish a deviator?
- Because a harsher profile lowers both players' payoffs on the path itself, so the target outcome in stage 1 would stop being worth sustaining at all
- Because the stick only enters the comparison multiplied by $\delta$, so a harsher profile could never change a stage-1 incentive by enough to matter
- Because a profile that is not a stage equilibrium fails to be a Nash equilibrium of the whole game, even though it is only played off the path
- Because in the subgame after a deviation some player gains by leaving that profile, so the threat is not credible and subgame perfection fails
<!-- YW5zOjM= -->
> Subgame perfection requires a Nash equilibrium in every subgame, including the stage-2 subgames reached only after a deviation; there, a non-equilibrium profile has some player with a profitable deviation, so the threat would not be carried out (Gibbons p. 73). Nash equilibrium of the whole game, by contrast, does not test off-path behaviour, which is exactly why the third option is wrong. Off-path punishments do not touch on-path payoffs.
> Ref: Tadelis (2013), Prop. 9.2 (p. 181), §9.4 (p. 183); Gibbons (1992), §2.2.A (p. 73)
> Similar: Tadelis (2013), Exercise 9.4, p. 188

## osd

Q: To check that "mum in stage 1, carrot after $(M,m)$, stick otherwise" is an SPE with the one-stage deviation principle, how is a player's deviation to fink in stage 1 evaluated?
- With the deviator playing the carrot afterwards, since a one-stage deviation keeps her on-path stage-2 action, so she gets the temptation plus $\delta$ times the carrot
- With the deviator following her own strategy afterwards, which prescribes the stick, so she gets the temptation plus $\delta$ times the stick
- With the deviator best-responding in stage 2 to the punishment, so the check covers only the combined deviation and the single deviation is not tested
- With the deviator choosing the stage-2 action that maximizes her total payoff, since a one-stage deviation lets her re-optimize after any stage-1 change
<!-- YW5zOjE= -->
> A one-stage deviation changes the action at a single information set and keeps the rest of the strategy, and the strategy prescribes the stick action after any outcome other than $(M,m)$. The deviation payoff is therefore the temptation plus $\delta$ times the stick, the $5 - 3\delta$ of Tadelis's example. Combined deviations need no separate test: the stage-2 checks show switching away from a stage equilibrium never pays, so they are covered.
> Ref: Tadelis (2013), §9.5 (pp. 184–186), closing remark of §9.4 (p. 184)
> Similar: Tadelis (2013), Exercise 9.3, pp. 187–188

Q: Theorem 9.1 says that in a finite game a one-stage unimprovable strategy is optimal. Which step carries the proof?
- Take the first profitable change in an improving sequence of changes; since the rest of the plan is unchanged, it alone is a profitable one-stage deviation
- Use discounting to bound the gain from changes far down the tree, so only the changes close to the root of the tree can matter for the comparison
- Take the last profitable change in a finite improving sequence; in its subgame it is a one-stage deviation, so it can be dropped without losing the gain
- Use the convexity of mixed strategies to show that any improving plan is a mixture of one-stage deviations, at least one of which must be profitable
<!-- YW5zOjI= -->
> If $\sigma_i$ is not optimal, finitely many changes along a path beat it. From the information set of the last change onward, the improved plan differs from $\sigma_i$ at one set only, so unimprovability says that change does not help there; removing it keeps the improvement, as in (9.1)–(9.2). Repeating leaves a single profitable one-stage deviation, a contradiction. The first change is followed by other changes, so it is not a one-stage deviation from $\sigma_i$; discounting is needed only for infinite horizons.
> Ref: Tadelis (2013), Def. 9.1 and Thm. 9.1 (p. 185), proof (pp. 185–186)
> Similar: Gibbons (1992), Problem 2.20, pp. 137–138

## app

Q: In Gibbons's tariff game, inverse demand in each country is $P_i = a - Q_i$, marginal cost is $c$, and governments set tariffs $t_1, t_2$ before firms play Cournot in each market. What is government $i$'s optimal tariff, and what kind of game do the governments play?
- $t_i^* = (a - c)/3$, the best reply only when $t_j = (a - c)/3$; the governments face a coordination game with two equilibria
- $t_i^* = (a - c - t_j)/3$, falling in the rival's tariff; the governments play a game of strategic substitutes like a Cournot duopoly
- $t_i^* = (a - c)/2$, a dominant strategy; free trade is jointly better, so the governments face a Prisoners' Dilemma with a unique equilibrium
- $t_i^* = (a - c)/3$, a dominant strategy; free trade is jointly better, so the governments face a Prisoners' Dilemma with a unique equilibrium
<!-- YW5zOjM= -->
> Stage 2 gives $h_i^* = (a - c + t_i)/3$ and $e_j^* = (a - c - 2t_i)/3$. In $W_i^* = \frac12 Q_i^2 + \pi_i + t_i e_j^*$ the rival tariff enters only through firm $i$'s export profit, which does not involve $t_i$, so $\partial W_i^*/\partial t_i = (3(a-c) - 9t_i)/9 = 0$ gives $t_i^* = (a - c)/3$ for every $t_j$: dominant. Both governments are worse off at $(t^*, t^*)$ than under free trade, the Prisoners' Dilemma that motivates trade agreements.
> Ref: Gibbons (1992), §2.2.C (pp. 75–79)
> Similar: Gibbons (1992), Problem 2.6, p. 133

Q: In Gibbons's bank-run game two investors each deposit $D$; early liquidation returns $2r$ and maturity returns $2R$, with $D > r > D/2$ and $R > D$. Which inequalities produce the two subgame-perfect outcomes, a run and no run?
- $R > D$ makes "don't withdraw" dominant at date 2, and $r > D/2$ makes "withdraw" dominant at date 1, so the two dates pull in opposite directions
- $r < D$ makes withdrawing the best reply to a withdrawal at date 1, and $R > D$ makes waiting the best reply to waiting, in the reduced date-1 game
- $r > D/2$ makes withdrawing the best reply to waiting at date 1, and $R > D$ makes waiting the best reply to a withdrawal, in the reduced date-1 game
- $R > D$ makes withdrawing dominant at date 2, and $r < D$ makes withdrawing dominant at date 1, so the run is the unique outcome and waiting is not
<!-- YW5zOjE= -->
> At date 2, $R > D$ gives $2R - D > R$, so withdrawing is dominant and both get $R$. Substituting, date 1 has withdraw against withdraw paying $r > 2r - D$ (because $r < D$), and wait against wait paying $R > D$: two pure equilibria, a run and no run. The inefficiency is a coordination failure, not a dominant-strategy trap; $r > D/2$ only ensures the early withdrawer of a lone run is paid in full.
> Ref: Gibbons (1992), §2.2.B (pp. 73–75), Figure 2.2.1
> Similar: Gibbons (1992), Problem 2.22, p. 138
