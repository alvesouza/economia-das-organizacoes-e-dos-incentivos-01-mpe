---
quiz: "Topic T3 · Hard conceptual quiz — Best responses and rationalizability"
tags:
  nbr: "Never-best-responses and dominance"
  br: "Best responses and beliefs"
  rat: "Rationalizability"
---

## nbr

Q: Player 1's rows against player 2's columns L and R pay: T gives 4 against L and 0 against R, M gives 1 and 2, B gives 0 and 4. Which statement about M is correct?
- M is a best response when player 1 thinks L and R are equally likely, since it is the only row that never pays 0 under either column
- M is never a best response though no pure row dominates it; a mix such as 0.4T + 0.6B beats it in both columns, but the 50-50 mix does not
- M is never a best response, and the 50-50 mix of T and B strictly dominates it, since that mix pays 2 against each of the two columns
- M is a best response to some mixed belief, since a strategy that no pure row strictly dominates always survives rationalizability
<!-- YW5zOjE= -->
> With belief $q$ on L, T pays $4q$, B pays $4-4q$ and M pays $2-q$. M beats T only if $q\le 0.4$ and beats B only if $q\ge 2/3$, which never happen together, so M is never a best response. With two players this is equivalent to strict dominance by some mixture: 0.4T + 0.6B pays 1.6 and 2.4 against M's 1 and 2.
> At the 50-50 belief T and B pay 2 each while M pays 1.5. The 50-50 mix pays 2 against R, exactly M's payoff there, so it only weakly dominates M; the mixing weight matters. Not being dominated by a pure row is not enough to survive, since rationalizability also catches strategies dominated by mixtures.
> Ref: Lecture 2 slides 10–12; Tadelis (2013), §6.3 (pp. 114–116), Prop. 6.2 (p. 116); Gibbons (1992), §1.3.A (p. 32)

Q: Player 1's rows against player 2's columns L and R pay: T gives 3 and 0, M gives 0 and 3, B gives 2 and 2. B is a best response neither to L nor to R. Does B survive the first round of rationalizability?
- No: a strategy that is a best response to no pure strategy of the opponent is never a best response, so B goes in round one
- Yes, but only as a tie: at the 50-50 belief B pays exactly as much as T and M, so it is never the unique best response
- No: B is strictly dominated by the mix with two thirds on T and one third on M, which pays 2 against L and 1 against R
- Yes: B is the unique best response to every belief that puts probability strictly between one third and two thirds on L
<!-- YW5zOjM= -->
> With belief $q$ on L, T pays $3q$, M pays $3-3q$ and B pays 2. B beats T when $q<2/3$ and beats M when $q>1/3$, so it is the unique best response on that interval. Beliefs must be allowed to be mixed, or B would be wrongly deleted.
> At the 50-50 belief T and M pay 1.5 each, less than B's 2. The mix with two thirds on T pays 2 against L and 1 against R: it ties with B against L and loses against R. No mixture of T and M beats B in both columns, since that would need a weight on T above two thirds and below one third at once.
> Ref: Lecture 2 slides 10–12; Gibbons (1992), §1.3.A, Fig. 1.3.2 (p. 33); Tadelis (2013), §6.3 (pp. 114–116)

Q: With two players, a strategy is never a best response exactly when some pure or mixed strategy strictly dominates it. Why can this equivalence fail with three or more players?
- Independently mixing opponents cannot express every correlated belief about their joint play, and a strategy may be best only against such a belief
- With three or more players a strategy can be strictly dominated and still be a best response, since the opponents' mixtures can offset each other
- With three or more players best responses may fail to exist in a finite game, so some strategies are never best responses for that reason alone
- With three or more players mixed strategies are not defined for every player, so dominance can be tested only against pure strategies of the others
<!-- YW5zOjA= -->
> If the opponents randomize independently, a belief about them is a product of mixtures, a strict subset of all distributions over $S_{-i}$. Example: player 3 picks one of four matrices against players 1 (U or D) and 2 (L or R); the first pays her 8 at (U, L), the second 4 at (U, L) and 4 at (D, R), the third 8 at (D, R), the fourth 3 everywhere, all other cells 0. The second is the average of the first and third, so against independent beliefs it is best only when those two tie, and then it pays at most 2 < 3. Against the correlated belief with one half on (U, L) and one half on (D, R) it pays 4, as much as any matrix, so nothing strictly dominates it.
> A strictly dominated strategy is never a best response in any game, so the first distractor reverses the direction that fails. Finite games always have best responses. Mixed strategies exist for any number of players; once correlated beliefs are allowed, the equivalence returns.
> Ref: MWG (1995), §8.C (pp. 244–245) and Exercise 8.C.4; Gibbons (1992), §1.3.A (pp. 32–33); Tadelis (2013), Prop. 6.2 (p. 116)

Q: Which implication holds in every normal-form game, finite or infinite, with any number of players?
- If $s_i$ is a best response to no belief, then some pure strategy of player $i$ strictly dominates $s_i$
- If $s_i$ is a best response to no pure profile $s_{-i}$, then it is a best response to no mixed belief
- If some pure strategy strictly dominates $s_i$, then $s_i$ is a best response to no belief about the opponents
- If $s_i$ is a best response to some belief, then $s_i$ survives every round of rationalizability
<!-- YW5zOjI= -->
> If $s_i'$ pays more than $s_i$ against every $s_{-i}$, it also pays more against any average of them, so no belief makes $s_i$ optimal; neither finiteness nor the number of players enters the argument.
> The converse fails: M = (1, 2) against T = (4, 0) and B = (0, 4) is never a best response yet no pure row dominates it, and with three or more players even mixed dominators may not exist. B = (2, 2) against T = (3, 0) and M = (0, 3) is a best response to no pure profile but to mixed beliefs. A strategy justified only by beliefs that weight an opponent's never-best-response goes in round two.
> Ref: Lecture 2 slides 10–12; Tadelis (2013), Prop. 4.3 (p. 70), §6.3 (pp. 114–116); MWG (1995), §8.C (pp. 242–245)

## br

Q: Which statement about player $i$'s best-response correspondence $BR_i(s_{-i})$ is correct?
- It is never empty in any game, since a rational player always has an optimal strategy against any belief she holds
- It is a single strategy in every game with continuous payoffs, which is why it is usually written as a function
- In a finite game it is always a single strategy, since finitely many payoffs against a fixed $s_{-i}$ have one maximum
- In a finite game it is never empty, but with infinite strategy sets it can be, as in Bertrand when $c<p_j\le p^m$
<!-- YW5zOjM= -->
> Finitely many payoffs always have a maximum, possibly attained by several strategies, so $BR_i$ is nonempty in finite games. In the homogeneous Bertrand duopoly with continuous prices and $c<p_j\le p^m$, any price below $p_j$ can be raised a little and still undercut, so no best price exists and $BR_i(p_j)=\emptyset$.
> Rationality presupposes that an optimum exists; it cannot create one. Ties make the correspondence set-valued even with smooth payoffs, for instance when a payoff is flat over a range of one's own strategies, and in finite games: in the Battle of the Sexes, Alex is indifferent between the venues when he puts one third on Chris going to the opera. A finite maximum can be attained more than once.
> Ref: Lecture 2 slides 10, 32–34, 48; Tadelis (2013), §4.3.2 (pp. 71–72), §5.2.4 (pp. 91–93)

Q: An analyst sees only player 1's choice in one play of a game and knows nothing about her beliefs. Which observation contradicts the hypothesis that player 1 is rational?
- She chose a strategy that was not a best response to what the opponent actually played in that game
- She chose a strategy that is a best response to no belief at all about the opponent, pure or mixed
- She chose a strategy that IESDS removes only in its second round, after an opponent strategy goes
- She chose a strictly dominant strategy although the outcome is Pareto dominated by another profile
<!-- YW5zOjE= -->
> A rational player chooses a best response to some belief, so only a strategy that no belief justifies is incompatible with rationality (the lecture's Lesson 3).
> Beliefs may be wrong, so failing against actual play says nothing about rationality; that gap is what Nash equilibrium closes by requiring correct beliefs. A strategy removed in round two is a best response to some belief, one that weights a strategy a rational opponent would not use, so it contradicts knowing that the opponent is rational, not rationality itself. Playing a strictly dominant strategy is exactly what rationality demands, as in the prisoner's dilemma.
> Ref: Lecture 2 slides 7, 11–12, 15; Tadelis (2013), §3.3.1 (p. 54), §4.3.1 (pp. 69–70)

Q: Strategy $s_i$ is a best response both to the mixed belief $\sigma_{-i}$ and to the mixed belief $\sigma'_{-i}$. What follows for the belief $\lambda\sigma_{-i}+(1-\lambda)\sigma'_{-i}$, with $0<\lambda<1$?
- $s_i$ is a best response to it too, since expected payoffs are linear in the belief, so the beliefs supporting $s_i$ form a convex set
- $s_i$ need not be a best response to it, since averaging two beliefs can make optimal a third strategy that was optimal at neither
- $s_i$ is a best response to it only if $\sigma_{-i}$ and $\sigma'_{-i}$ have the same support, so that no new profile gets any weight
- $s_i$ is a best response to it only in $2\times2$ games, where each belief about the opponent is described by a single probability
<!-- YW5zOjA= -->
> The expected payoff of any strategy at the mixed belief is $\lambda$ times its payoff at $\sigma_{-i}$ plus $1-\lambda$ times its payoff at $\sigma'_{-i}$. Since $s_i$ does at least as well as every alternative at both beliefs, it does at least as well at the average.
> A third strategy's payoff at the average is the same weighted average of its two payoffs, each no larger than that of $s_i$, so it cannot overtake $s_i$. Supports and the size of the game play no role: linearity in beliefs holds in every finite game.
> Ref: Lecture 2 slide 43; Tadelis (2013), §4.3.2 (pp. 71–72), §6.1.4 (pp. 105–106)

## rat

Q: Each of $n>2$ players picks an integer from 0 to 20; those closest to three quarters of the average split a prize, and everyone else loses an entry fee. What does rationalizability predict, and what does the prediction take?
- Each picks 0, the only number left after 20 rounds of deletion, and getting there takes at least 20 levels of knowledge
- Each picks at most 15, since three quarters of the largest possible average is 15, and rationality alone removes the rest
- Each picks 0 or 1, the numbers left after 19 rounds of deleting the highest survivor; rationality alone deletes only 20
- Each picks at most 1, and rationality alone suffices, since every player can see that 0 and 1 are best replies to anything
<!-- YW5zOjI= -->
> If all others pick 20, picking 19 wins outright, so 20 is never a best response; 19 is a best response to that same belief, so only 20 goes in round one. Each further round deletes the highest survivor, and after 19 rounds {0, 1} remains. With $n>2$, 1 is a best response to the belief that all others pick 1, so it cannot be deleted; only with two players does the prediction shrink to 0.
> Winning requires being closest, not hitting the target, so numbers from 16 to 19 can still be best responses and rationality alone removes only 20. Each round uses one more level of knowledge of rationality, so the full prediction needs 19 rounds of it, not rationality alone. Nor are 0 and 1 best replies to every belief: with four or more players, against all others at 20 both lose, while 15 or 19 wins.
> Ref: Lecture 2 slides 7, 11–12; Tadelis (2013), §4.3.5 (pp. 74–75)
> Similar: Tadelis (2013), Exercises 4.8–4.9 (p. 78)

Q: In a finite two-player game, call a pure strategy an equilibrium strategy if some pure-strategy Nash equilibrium uses it. Which chain of inclusions is correct?
- Rationalizable strategies ⊆ equilibrium strategies ⊆ survivors of IESDS, since a rationalizable strategy answers a correct belief
- Equilibrium strategies ⊆ rationalizable strategies = survivors of IESDS with mixed dominators, and the inclusion can be strict
- Equilibrium strategies = rationalizable strategies ⊆ survivors of IESDS, since every rationalizable strategy is part of an equilibrium
- Survivors of IESDS ⊆ rationalizable strategies ⊆ equilibrium strategies, since each concept adds one more requirement on beliefs
<!-- YW5zOjE= -->
> An equilibrium strategy is a best response to $s_{-i}^*$, whose components are best responses too, so it is never removed in any round: it is rationalizable. With two players, never-best-responses are exactly the strategies strictly dominated by pure or mixed strategies, so rationalizability and IESDS with mixed dominators coincide. In matching pennies every strategy is rationalizable and none is an equilibrium strategy, since there is no pure equilibrium.
> Matching pennies refutes both chains that put the rationalizable strategies inside, or equal to, the equilibrium strategies: rationalizability never asks beliefs to be correct. The reversed chain gets every inclusion backwards: the survivors of IESDS form the largest set and the equilibrium strategies the smallest.
> Ref: Lecture 2 slides 12, 15–17; Tadelis (2013), §5.3 (p. 95), Prop. 6.2 (p. 116)

Q: Player 1's strategy $a$ is a best response to some beliefs, but each of them puts positive probability on player 2's strategy $x$, which is never a best response for player 2. What does rationalizability conclude about $a$?
- $a$ survives, since it is a best response to some belief, and rationalizability only asks each strategy to be justified by a belief
- $a$ goes in round one together with $x$, since both of them rest on the same unreasonable belief about how the game will be played
- $a$ survives unless, once $x$ is deleted, some pure strategy of player 1 strictly dominates $a$ in the game that is left over
- $a$ survives round one but goes in round two, since a belief that gives $x$ weight is inconsistent with player 2 being rational
<!-- YW5zOjM= -->
> Round one deletes $x$ but not $a$, which is a best response to some belief. In round two player 1's beliefs must be over player 2's surviving strategies; every belief that justified $a$ gave weight to $x$, so $a$ is a best response to no admissible belief and goes.
> Rationalizability asks for a belief over rationalizable strategies, a chain of justification, not just any belief. Deletion in round one depends only on $a$'s own status, and $a$ is justified there. Testing only pure dominators in the reduced game is too narrow: with two players the right test is dominance by pure or mixed strategies.
> Ref: Lecture 2 slides 11–12; Tadelis (2013), §4.3.3 (p. 73); MWG (1995), §8.C (pp. 242–244)
