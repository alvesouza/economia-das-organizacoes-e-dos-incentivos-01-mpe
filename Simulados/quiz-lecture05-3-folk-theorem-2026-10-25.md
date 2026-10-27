---
quiz: "Lecture 5 · Quiz 3 of 3 — Feasible payoffs and the folk theorem"
tags:
  feas: "Feasible payoffs: convex combinations and the convex hull"
  folk: "The folk theorem and its thresholds"
  alt: "Alternating paths and the binding constraint"
  select: "Almost anything goes: what the folk theorem predicts"
---

## feas

Q: In a finite two-player stage game, which statement about the set of feasible payoffs used by the folk theorem is correct?
- It is the set of payoff vectors of the pure-strategy profiles, since only those can be repeated period after period
- It is the set of payoff vectors that give every player more than a stage Nash payoff, so feasibility already means rationality
- It is the convex hull of the payoff vectors of the Nash equilibria, since only stage equilibria can be played forever
- It is the convex hull of the payoff vectors of the pure profiles, so it holds points that no single cell pays
<!-- YW5zOjM= -->
> Repeating a pure profile forever gives its stage payoff as the average payoff, so pure-profile payoffs are achievable, and weighting them over time (alternating) or with a public randomizing device reaches any convex combination. The feasible set is therefore the convex hull of the pure-profile payoffs. In Tadelis's prisoner's dilemma $(2,2)$ and $(4.4, 2)$ are feasible though no cell pays them. Being above the Nash payoff is the second, separate condition of the theorem.
> Ref: Tadelis (2013), Defs. 10.6–10.7 (pp. 209–210), Figure 10.4 (p. 211); Gibbons (1992), §2.3.B (p. 96)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

Q: Two pure profiles pay $v = (v_1, v_2)$ and $v' = (v_1', v_2')$, with $v_2 > e_2 > v_2'$, where $e_2$ is player 2's stage Nash payoff. For which weight $\alpha \in [0,1]$ does the convex combination $\alpha v + (1-\alpha)v'$ give player 2 exactly $e_2$?
- $\alpha = (v_2 - e_2)/(v_2 - v_2')$, the share of the gap between the two payoffs that lies above player 2's Nash payoff
- $\alpha = (e_2 - v_2')/(v_2 - v_2')$, the share of the gap between the two payoffs that lies below player 2's Nash payoff
- $\alpha = (e_2 - v_2')/(v_2 + v_2')$, the distance from the low payoff to player 2's Nash payoff over the payoffs' sum
- $\alpha = e_2/(v_2 + v_2')$, player 2's Nash payoff divided by the sum of the payoffs she gets in the two profiles
<!-- YW5zOjE= -->
> Solve $\alpha v_2 + (1-\alpha)v_2' = e_2$: $\alpha(v_2 - v_2') = e_2 - v_2'$. At this weight the combination sits on the edge of the folk-theorem region, where player 2 is exactly at her punishment payoff; larger $\alpha$ moves it inside. The first option is $1-\alpha$, the weight on $v'$. Applied to Tadelis's Figure 10.3, the weight $0.6$ on $(4,4)$ and $0.4$ on $(5,-1)$ gives $(4.4, 2)$, inside the region.
> Ref: Tadelis (2013), Def. 10.6 and Figure 10.3 (pp. 209–210), Theorem 10.1 (p. 211)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

## folk

Q: Let $G$ be a finite simultaneous-move game with a stage Nash equilibrium paying $v^* = (v_1^*, \dots, v_n^*)$, and let $v$ be a feasible payoff vector. What does the folk theorem for $G(\delta)$ assert?
- If $v_i > v_i^*$ for every $i$ and $\delta$ is close enough to 1, some SPE has average payoff arbitrarily close to $v$
- If $v$ is feasible and $\delta$ is close enough to 1, some SPE has an average payoff arbitrarily close to $v$
- If $v_i > v_i^*$ for every $i$, then for every $\delta \in (0,1)$ some SPE has an average payoff exactly equal to $v$
- If $v_i > v_i^*$ for at least one $i$ and $\delta$ is close enough to 1, some SPE has average payoff close to $v$
<!-- YW5zOjA= -->
> Theorem 10.1 needs both conditions: feasibility, and every player strictly above a stage Nash payoff, so that Nash reversion punishes everyone. Then for $\delta$ close to 1 an SPE gets arbitrarily close to $v$. A feasible point that leaves some player below $v_i^*$, such as $(0.5, 3)$ in Tadelis's prisoner's dilemma, is not covered: that player would rather defect and take the Nash payoff. Patience is essential; at small $\delta$ only stage Nash play may survive.
> Ref: Tadelis (2013), Theorem 10.1 (p. 211); Gibbons (1992), Friedman's Theorem (p. 97)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305; MWG (1995), Exercise 12.AA.1, p. 420

Q: Under Nash reversion, a path can be sustained as a subgame-perfect equilibrium at some discount factor $\delta$. What can be said about higher discount factors $\delta' > \delta$?
- Nothing in general, since a higher $\delta'$ raises the value of the deviation's continuation as much as the path's
- The path fails at high enough $\delta'$, since very patient players weigh the punishment phase's length more
- The path can still be sustained at every $\delta' \ge \delta$, so the set of sustainable paths only grows with patience
- The path can be sustained at $\delta'$ only if it is stationary, since alternating paths move their bad periods
<!-- YW5zOjI= -->
> The no-deviation condition compares a one-period gain with the discounted future loss from reversion. Raising $\delta$ leaves the gain unchanged and raises the weight on the loss, so a condition that holds at $\delta$ holds at any higher $\delta'$; MWG's Prop. 12.AA.2 states this for every path. That is why the critical discount factor is a cutoff, not a window, and why the folk theorem is stated for $\delta$ close enough to 1.
> Ref: MWG (1995), Def. 12.AA.1 and Lemma 12.AA.1 (p. 418), Prop. 12.AA.2 (p. 420); Tadelis (2013), (10.5) (p. 202)
> Similar: MWG (1995), Exercise 12.AA.1, p. 420

Q: Tadelis's folk theorem uses stage Nash payoffs $e_i$ as its threshold. Gibbons defines the reservation payoff $r_i$, the most player $i$ can guarantee whatever the others do. How do the two compare, and what does Fudenberg and Maskin's result add?
- $r_i \ge e_i$ always, and for two players Fudenberg–Maskin shrink the region to payoffs above $r_i$, the stricter bound
- $r_i \le e_i$ always, and for two players Fudenberg–Maskin show that payoffs above $r_i$ can be supported as $\delta \to 1$
- $r_i = e_i$ always, and Fudenberg–Maskin show the region is the same for any number of players once $\delta \to 1$
- $r_i \le e_i$ always, but Fudenberg–Maskin show that payoffs between $r_i$ and $e_i$ can never be SPE averages
<!-- YW5zOjE= -->
> In a Nash equilibrium each player best-responds, so she gets at least what she can guarantee: $r_i \le e_i$. In the prisoner's dilemma they coincide ($r_i = e_i = 1$ in Tadelis's numbers); in Cournot $r_i = 0 < e_i$. Fudenberg and Maskin (1986) show that for two players any feasible payoff with $x_i > r_i$ is an SPE average for $\delta$ near 1, using punishments harsher than Nash reversion. MWG's minimax folk theorem is the general form; both are named, not examinable.
> Ref: Gibbons (1992), §2.3.B (pp. 98–99); MWG (1995), Props. 12.AA.3 and 12.AA.5 (pp. 420–422)
> Similar: MWG (1995), Exercise 12.AA.2, p. 435

## alt

P: In the infinitely repeated prisoner's dilemma with discount factor $\delta \in (0,1)$, mutual cooperation pays $R$ to each, mutual defection $P$ to each, and a defector facing a cooperator gets $T$ while the cooperator gets $S$, with $T > R > P > S$ and $T + S > 2P$. The prescribed path alternates: in odd periods player 1 defects and player 2 cooperates, in even periods the reverse. Any departure from the pattern triggers mutual defection forever.

Q: What is player 1's average payoff on the alternating path, starting in period 1?
- $(T + \delta S)/(1 + \delta)$, which tends to $(T+S)/2$ as $\delta \to 1$, the midpoint of the two off-diagonal payoffs
- $(S + \delta T)/(1 + \delta)$, which tends to $(T+S)/2$ as $\delta \to 1$, the midpoint of the two off-diagonal payoffs
- $(T + S)/2$ for every $\delta$, since player 1 receives $T$ in exactly half of the periods and $S$ in the other half
- $(T + \delta S)/(1 - \delta^{2})$, which grows without bound as $\delta \to 1$, since it adds up both payoff streams
<!-- YW5zOjA= -->
> Player 1's stream is $T, S, T, S, \dots$: $(1-\delta)[T(1+\delta^2+\dots) + S(\delta+\delta^3+\dots)] = (1-\delta)(T+\delta S)/(1-\delta^2) = (T+\delta S)/(1+\delta)$. The second option is player 2's average, who starts with $S$. The fourth is the present value, not the average. With Tadelis's numbers ($T=5$, $S=-1$) it is $(5-\delta)/(1+\delta)$, which tends to $2$.
> Ref: Tadelis (2013), §10.6 alternating path (pp. 212–213)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

Q: In a period where a player is prescribed to cooperate while the other defects, what condition on $\delta$ keeps that player on the path?
- $\delta \ge (T-R)/(T-P)$, the grim-trigger threshold, since the deviation gain and the punishment are the same
- $\delta \ge (P-S)/(T-S)$, the loss from being the sucker over the full spread of the stage-game payoffs
- $\delta \ge (T-P)/(P-S)$, the gain in the next good period over the loss from being the sucker today
- $\delta \ge (P-S)/(T-P)$, the loss from being the sucker today over the gain in the next good period
<!-- YW5zOjM= -->
> In the bad period the continuation average is $(S + \delta T)/(1+\delta)$; defecting instead gives $P$ today and $P$ forever, an average of $P$. The condition $(S+\delta T)/(1+\delta) \ge P$ becomes $S + \delta T \ge P + \delta P$, i.e. $\delta(T-P) \ge P - S$. The assumption $T + S > 2P$ makes the ratio below one. With Tadelis's numbers it is $\delta \ge 2/4 = 1/2$, and it is the binding constraint: the good-period check holds for every $\delta$.
> Ref: Tadelis (2013), §10.6 (pp. 212–214), Prop. 10.3 (p. 198)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

Q: Compare the sucker payoff's role on the alternating path with its role under grim trigger on permanent mutual cooperation. Which statement is correct?
- It matters in both, since every incentive constraint in the repeated game compares a deviation with the worst stage payoff
- It matters in neither, since the punishment after any departure is mutual defection, which pays $P$ to both players
- It matters on the alternating path, where each player takes $S$ on the path, but not under grim trigger, where no one does
- It matters under grim trigger, where cooperating risks $S$ each period, but not on the alternating path, where $S$ is offset
<!-- YW5zOjI= -->
> Under grim trigger both cooperate on the path and both defect in punishment, so $S$ never enters $\delta^* = (T-R)/(T-P)$. On the alternating path each player is the sucker in every other period, so $S$ enters the average payoff and the bad-period threshold $(P-S)/(T-P)$: a lower $S$ makes the path harder to sustain. The punishment is the same in both, which is why the second option is tempting.
> Ref: Tadelis (2013), (10.3) (p. 200), §10.6 (pp. 212–214); Gibbons (1992), §2.3.B (p. 92)
> Similar: Tadelis (2013), Exercise 10.2, p. 215

## select

Q: For patient players in an infinitely repeated prisoner's dilemma, what does the folk theorem imply about predicting their behaviour?
- Cooperation is one of a continuum of SPE outcomes, alongside permanent defection and lopsided paths, so none is singled out
- Cooperation is the predicted outcome, since it is the only SPE outcome that is Pareto efficient once $\delta$ is near one
- Defection is the predicted outcome, since the stage equilibrium is the only one that survives every discount factor
- Cooperation is predicted once $\delta$ exceeds the critical value, since the other equilibria then stop being subgame-perfect
<!-- YW5zOjA= -->
> Theorem 10.1 delivers a whole region of SPE average payoffs: efficient ones, the inefficient $(1,1)$ of defection forever (an SPE for every $\delta$ by Prop. 10.2), and lopsided points near $(4.6, 1)$ in Tadelis's numbers. Many efficient points exist, not one. Repetition explains how cooperation can be self-enforcing, not that it will be: the result moves the question to equilibrium selection, which Tadelis calls "rather disturbing".
> Ref: Tadelis (2013), §10.6 (pp. 209, 211–212), Prop. 10.2 (p. 196); Gibbons (1992), §2.3.B (pp. 97–99)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

Q: In a symmetric prisoner's dilemma with $T > R > P > S$ and $2R > T + S$, the feasible set has corners $(S,T)$, $(R,R)$, $(T,S)$ and $(P,P)$. What is the supremum of player 2's average payoff over the folk-theorem region, where both players get more than $P$?
- $T - (T-R)(R-P)/(R-S)$, found on the edge from $(S,T)$ to $(R,R)$ where it meets the line $v_1 = R$
- $T - (T-R)(P-S)/(R-S)$, found on the edge from $(S,T)$ to $(R,R)$ where it meets the line $v_1 = P$
- $R + (T-R)(P-S)/(R-S)$, found on the edge from $(R,R)$ to $(T,S)$ where it meets the line $v_1 = P$
- $T - (T-R)(P-S)/(T-S)$, found on the edge from $(S,T)$ to $(T,S)$ where it meets the line $v_1 = P$
<!-- YW5zOjE= -->
> The upper-left frontier runs from $(S,T)$ to $(R,R)$: $v_2 = T - (T-R)(v_1 - S)/(R-S)$, decreasing in $v_1$. The region requires $v_1 > P$, so player 2's payoff is highest as $v_1 \to P$, giving $T - (T-R)(P-S)/(R-S)$. With Tadelis's numbers this is $5 - 1 \cdot 2/5 = 4.6$, the corner $(1, 4.6)$ of Figure 10.4's region. Such a lopsided split is as much an equilibrium as mutual cooperation.
> Ref: Tadelis (2013), Figures 10.4–10.5 (pp. 211–212), Theorem 10.1 (p. 211)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305
