---
quiz: "Topic T4 · Hard conceptual quiz — Nash equilibrium"
tags:
  def: "Definition and interpretations"
  iesds: "Nash equilibrium and iterated elimination"
  robust: "Adding and deleting strategies"
  eff: "Multiplicity, symmetry and efficiency"
---

## def

Q: Let $BR(s)=BR_1(s_{-1})\times\dots\times BR_n(s_{-n})$ be the joint best-response correspondence of a game. Which condition is equivalent to $s^*$ being a Nash equilibrium?
- $s_i^*\in BR_i(s_{-i})$ for every $s_{-i}$ and every $i$, so that each component is optimal whatever the others do
- $s_i^*\in BR_i(\sigma_{-i})$ for some belief $\sigma_{-i}$ over rationalizable profiles, for every player $i$
- $BR(s^*)=\{s^*\}$: each component $s_i^*$ is the unique best response to the components $s_{-i}^*$ of the profile
- $s^*\in BR(s^*)$: each component $s_i^*$ is a best response to the components $s_{-i}^*$ of the same profile
<!-- YW5zOjM= -->
> A Nash equilibrium is a profile of mutual best responses, that is, a fixed point of the joint best-response correspondence.
> Optimality against every $s_{-i}$ is dominance, far stronger. Best responses to some belief over rationalizable profiles define rationalizability, which allows wrong beliefs. A unique best response defines a strict equilibrium: sufficient, not necessary, since Bertrand's $(c,c)$ and many other equilibria involve ties.
> Ref: Lecture 2 slides 10, 14; Tadelis (2013), Def. 5.1 (p. 80), §6.4 (p. 120)

Q: Suppose the players of a one-shot game have agreed to play the profile $s$, and no contract, court or outside enforcer exists. For which profiles is such an agreement self-enforcing?
- For Pareto-optimal profiles, since no player breaks an agreement that cannot be improved upon for everybody
- For Nash equilibria, since each player keeps her part only if it is a best response when the others keep theirs
- For profiles that survive IESDS, since those are the strategies consistent with common knowledge of rationality
- For profiles in which each player uses a strategy that is a best response to some belief about the others
<!-- YW5zOjE= -->
> Without enforcement each player sticks to her part only if it is in her interest given that the others stick to theirs, which is the Nash condition; self-enforcement is one of the lecture's interpretations of Nash equilibrium.
> In the prisoner's dilemma (M, M) is Pareto optimal, yet each suspect gains by finking on the agreement. In the Battle of the Sexes the profile (opera, football) survives IESDS and each strategy in it is a best response to some belief, but each player would break that agreement given that the other keeps it.
> Ref: Lecture 2 slide 15; Tadelis (2013), §3.3.1 (pp. 54–55), §5.1 (p. 80)

Q: Three voters choose between A and B by majority, voting simultaneously; each voter gets 1 if A wins and 0 if B wins. Is the profile in which all three vote for B a Nash equilibrium?
- Yes: no single voter can change the outcome by switching, though each one uses the weakly dominated choice of voting for B
- No: every voter strictly prefers A, so each one gains by switching her vote to A whatever the other two voters do
- No: voting for B is strictly dominated by voting for A, and a Nash equilibrium never uses a strictly dominated strategy
- Yes, and it is the unique equilibrium, since with three voters any profile in which B wins by two or more votes is stable
<!-- YW5zOjA= -->
> If one voter switches to A, B still wins two to one, so her payoff stays 0: no unilateral deviation is profitable and all-B is a Nash equilibrium. Voting B is weakly dominated by voting A, which does strictly better when the other two split.
> A voter gains from switching only when she is pivotal, and she is not when both others vote B; that is why voting B is weakly, not strictly, dominated, and the slides' note warns that equilibria in weakly dominated strategies are less plausible. All-A is an equilibrium too, so all-B is not unique.
> Ref: Lecture 2 slides 14, 16 (note); Tadelis (2013), §3.1.3 (p. 49), Def. 5.1 (p. 80)

Q: In a finite game, player $i$'s security level is $\max_{s_i}\min_{s_{-i}}u_i(s_i,s_{-i})$, the most she can guarantee with a pure strategy. In any pure-strategy Nash equilibrium $s^*$, how does $u_i(s^*)$ compare with it?
- It equals the security level, since in equilibrium each player chooses the strategy that maximizes her worst-case payoff
- It can fall short of the security level, since the opponents' equilibrium strategies may be the ones that hurt $i$ most
- It is at least the security level, since $u_i(s^*)$ is her best payoff against $s_{-i}^*$, above any strategy's worst case
- It is at least the security level only in zero-sum games, where each player's gain is exactly the other player's loss
<!-- YW5zOjI= -->
> Let $\hat s_i$ attain the security level. Then $u_i(s^*)\ge u_i(\hat s_i,s_{-i}^*)\ge\min_{s_{-i}}u_i(\hat s_i,s_{-i})$: the first inequality is the equilibrium condition, the second holds because $s_{-i}^*$ is one of the profiles in the minimum.
> In the stag hunt, (S, S) pays 5 while hare guarantees only 3, so equilibrium payoffs can exceed the security level and need not come from maximin strategies. Falling short is ruled out by the chain of inequalities, and nothing in that chain uses zero-sum payoffs.
> Ref: Lecture 2 slide 14; Tadelis (2013), Def. 5.1 (p. 80), §5.2.1 (pp. 83–84)

## iesds

Q: Player 1 chooses U or D, player 2 chooses L or R. Payoffs (player 1, player 2): (U, L) = (1, 1), (U, R) = (1, 0), (D, L) = (1, 0), (D, R) = (0, 1). (U, L) is the only pure-strategy Nash equilibrium. What does IESDS do in this game?
- It removes nothing: U only weakly dominates D and no strategy of player 2 is dominated, so (U, L) is not singled out
- It removes D in round one, since U pays at least as much as D in both columns, and then removes R, leaving only (U, L)
- It removes R in round one, since L pays more than R against U, and then removes D, leaving the equilibrium (U, L) alone
- It must leave only (U, L), since in a finite game a unique pure Nash equilibrium is always the unique survivor of IESDS
<!-- YW5zOjA= -->
> U pays 1 against both columns and D pays 1 and 0: a tie against L, so U only weakly dominates D. For player 2, L is better against U and R against D. Nothing is strictly dominated, so all four profiles survive, although (U, L) is the unique pure equilibrium.
> The converse of the slides' Proposition 2 fails when payoffs tie: a unique Nash equilibrium need not be the unique IESDS survivor. Removing D needs strict dominance, and R is not dominated, since it beats L against D. The game is 2×2, so it also shows that Tadelis's Exercise 5.3(a) holds only for games without payoff ties.
> Ref: Lecture 2 slides 16–17; Tadelis (2013), Prop. 5.1 (pp. 80–81), §5.3 (p. 95), Exercise 5.3 (p. 95)

Q: IESDS reduces a finite game $G$ to a smaller game $G'$ without reaching a single profile. How do the pure-strategy Nash equilibria of $G$ and of $G'$ compare?
- $G$ can have extra equilibria, since IESDS may delete a strategy that is part of an equilibrium in which some player is indifferent
- $G'$ can have extra equilibria, since a profile stable in $G'$ may be upset by a deviation to a strategy that IESDS removed
- They coincide only when $G'$ has a unique equilibrium, since with several equilibria removed strategies can restore deviations
- They coincide: each equilibrium of $G$ survives into $G'$, and no removed strategy is a profitable deviation from a profile of $G'$
<!-- YW5zOjM= -->
> By the slides' Proposition 1 no equilibrium component is ever removed, so each equilibrium of $G$ lies in $G'$ and is still one there. Conversely, take an equilibrium $s$ of $G'$ and a removed strategy $t_i$: it was strictly dominated against a set containing $s_{-i}$, and following the chain of dominators ends, by finiteness, at a surviving $t_i''$ with $u_i(t_i'',s_{-i})>u_i(t_i,s_{-i})$. Since $s_i$ is a best response in $G'$, $u_i(s)\ge u_i(t_i'',s_{-i})$, so the deviation to $t_i$ does not pay.
> Indifference never exposes an equilibrium strategy to strict dominance, which would contradict its being a best response to $s_{-i}^*$. The argument uses no uniqueness, which is why IESDS is a safe first step before searching for equilibria.
> Ref: Lecture 2 slides 16–17; Tadelis (2013), Prop. 5.1 (pp. 80–81), §5.3 (p. 95)

## robust

Q: Player 1 is given an extra strategy $x$ that is strictly dominated by one of her existing strategies. How can the set of pure-strategy Nash equilibria change?
- It can lose equilibria: $x$ gives player 1 a new deviation, which may be profitable against the opponents' equilibrium play
- It cannot change: $x$ is never a best response, and a deviation to $x$ pays less than one to the strategy dominating it
- It can gain equilibria: the opponents may now best-respond to the threat of $x$ by moving to profiles that were unstable
- It can gain and lose equilibria, since the invariance criterion treats any change to a strategy set as a large change
<!-- YW5zOjE= -->
> Let $y$ strictly dominate $x$. At an old equilibrium $s^*$, $u_1(x,s_{-1}^*)<u_1(y,s_{-1}^*)\le u_1(s^*)$, so $x$ is not a profitable deviation; no profile using $x$ is an equilibrium, since $y$ beats $x$ there; and the opponents' comparisons at profiles without $x$ are untouched.
> A deviation to $x$ is always beaten by the deviation to $y$, which was already available. In a simultaneous game there are no threats: the opponents respond to what player 1 plays, and in equilibrium she never plays $x$. The invariance criterion excludes changes to strategy sets from what it calls small, but that does not make every such change matter.
> Ref: Lecture 2 slides 14, 16; Tadelis (2013), §3.3.2.3 (p. 56), Def. 5.1 (p. 80)

Q: Player 1 has rows U, D and X and player 2 has columns L and R. Payoffs (player 1, player 2): (U, L) = (1, 1), (U, R) = (0, 0), (D, L) = (0, 0), (D, R) = (1, 1), (X, L) = (0, 1), (X, R) = (2, 0). The only pure Nash equilibrium is (U, L). What happens if row X, which no pure equilibrium uses, is deleted?
- Nothing changes, since a strategy that no equilibrium uses cannot matter for which profiles are stable ones
- (U, L) stops being an equilibrium, since X was what kept player 2 on L, and (D, R) takes its place
- (D, R) becomes a second equilibrium, since X was the only profitable deviation from it, and (U, L) stays one
- (D, R) becomes an equilibrium, but (U, L) stops being one, so the game still has a unique equilibrium
<!-- YW5zOjI= -->
> At (D, R) player 1 gets 1 but X would give 2, so (D, R) fails only because of X; once X is gone, D is a best response to R and R to D. Deleting strategies only removes deviations, so (U, L) remains an equilibrium.
> An unused strategy can still be the profitable deviation that destabilizes a profile, which is why deleting strategies is not a small change of the game. Player 2's incentives at (U, L) do not involve X at all.
> Ref: Lecture 2 slide 14; Tadelis (2013), §3.3.2.3 (p. 56), Def. 5.1 (p. 80)

## eff

Q: Two hunters each choose stag (S) or hare (H): (S, S) gives 5 each, a lone stag hunter gets 0 while the hare hunter gets 3, and (H, H) gives 3 each. Which statement is correct?
- Only (S, S) is a Nash equilibrium, since at (H, H) each hunter would gain 2 by moving to the profile both prefer
- Both are Nash equilibria, but (H, H) is eliminated by IESDS, since S strictly dominates H against a stag hunter
- Only (H, H) is a Nash equilibrium, since H guarantees 3 whatever the other does, while S risks getting nothing
- Both (S, S) and (H, H) are Nash equilibria, and nothing in the definition selects the Pareto-dominant one
<!-- YW5zOjM= -->
> Against S the best reply is S (5 > 3); against H it is H (3 > 0). Both diagonal profiles are mutual best responses, and the Pareto ranking plays no role in the definition; which one a society reaches depends on self-fulfilling beliefs, norms or history.
> Moving from (H, H) to (S, S) needs both hunters to switch, and a lone switch to S pays 0. Beating H against a stag hunter is not dominance, which must hold against every strategy, and IESDS removes nothing here. Safety does not make S a bad reply to S.
> Ref: Lecture 2 slides 15, 18; Tadelis (2013), §5.1.2 (p. 83), §5.2.1 (pp. 83–84)

Q: Two drivers each choose Swerve or Straight: (Swerve, Swerve) gives 0 each, a lone Straight driver gets 1 while the swerver gets −1, and (Straight, Straight) gives −10 each. Which statement is correct?
- The pure equilibria are (Straight, Swerve) and (Swerve, Straight); a symmetric game can lack a symmetric pure equilibrium
- There is a symmetric pure equilibrium, (Swerve, Swerve), since a symmetric game must have one in which both do the same
- There is no pure equilibrium, since in a symmetric game either player can reverse an asymmetric profile by deviating
- The only pure equilibrium is (Straight, Straight), since going straight is the best reply to a rival who swerves
<!-- YW5zOjA= -->
> Against Swerve the best reply is Straight (1 > 0); against Straight it is Swerve (−1 > −10). The mutual best responses are the two asymmetric profiles; the only symmetric equilibrium is mixed, with each driver swerving with probability 9/10.
> At (Swerve, Swerve) each driver gains by going straight, and at (Straight, Straight) each gains by swerving. Reversing an asymmetric profile would take both drivers to deviate, and a lone deviation from (Straight, Swerve) hurts the deviator. Straight is the best reply to Swerve, not to Straight.
> Ref: Lecture 2 slides 14, 18; Tadelis (2013), §5.1 (pp. 80–83), §6.2.3 (p. 113)
