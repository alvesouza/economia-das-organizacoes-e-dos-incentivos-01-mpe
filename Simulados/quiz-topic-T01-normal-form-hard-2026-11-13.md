---
quiz: "Topic T1 · Hard conceptual quiz — Normal-form games and solution concepts"
tags:
  nf: "Normal form, strategies and information"
  concepts: "Solution concepts and their criteria"
  pareto: "Pareto optimality"
  payoffs: "Payoffs and their transformations"
---

## nf

Q: Which change to a two-player game turns it from a static game into a game that is not static?
- Player 2 chooses a week after player 1, but nobody tells her what player 1 chose before she commits to her choice
- Player 1's choice is shown to player 2 before she chooses, even though both choices are made within the same hour
- Payoffs depend on a coin tossed after both have chosen, and the odds of the coin are known to both of the players
- Player 2 learns player 1's choice only after both choices are locked in, on the day that the payoffs are paid out
<!-- YW5zOjE= -->
> A game is static when each player chooses without observing what the others chose; the calendar plays no role. Showing player 1's choice to player 2 before she commits lets her condition on it, so the situation becomes dynamic even if both choices fall within one hour.
> Choosing a week later without being told is still static. A coin with commonly known odds tossed after play only turns payoffs into expected payoffs. Learning player 1's choice once both are locked in cannot affect any decision.
> Ref: Lecture 1 slide 15; Tadelis (2013), Ch. 3 opening (pp. 43–44); Gibbons (1992), §1.1.A (p. 4)

Q: Player 1 picks Up or Down; player 2 sees the pick and then picks Left or Right. An analyst writes the game as a 2×2 matrix whose columns are Left and Right. What goes wrong?
- Nothing essential: player 2 best-responds to what she sees, so her two actions already describe everything that she is able to do
- Only the order of moves is lost: the matrix is right as long as it is read with player 2 as the player who moves second in time
- The matrix has too few rows: player 1 needs four strategies, one for each pair of actions that player 2 could take after his pick
- Its columns are actions, not strategies: it is the game in which player 2 cannot see the pick, so plans like 'copy him' are lost
<!-- YW5zOjM= -->
> A strategy is a complete contingent plan. Player 2 moves after seeing Up or Down, so a strategy assigns her an action to each, giving four strategies (Left after both, Right after both, copy, oppose). A 2×2 matrix with columns Left and Right is the normal form of the simultaneous game, a different game.
> Her conditioning is exactly what 'everything she can do' includes, so the claim that nothing is lost fails, and reading the same matrix in a different order does not restore the missing plans. Player 1 moves once without information, so he has two strategies, not four; it is player 2's strategy set that grows.
> Ref: Lecture 1 slides 15, 17; Tadelis (2013), Def. 3.2 (p. 46), §7.2.3 (p. 143); Notas/L01/L01-10-pitfalls.md, item 6

Q: In a two-player game every player knows every player's payoff function. Which further fact still leaves the game short of complete information in the sense used in the course?
- Player 1 knows player 2's payoffs, but she is not sure whether player 2 knows that player 1 knows them
- Player 2 does not observe player 1's choice before making her own, and both of the players know this
- Payoffs depend on a random state drawn after play from a distribution that both of the players know
- Neither player knows which strategy the other player will actually choose once the game is played
<!-- YW5zOjA= -->
> Complete information requires the game to be common knowledge: everyone knows it, everyone knows that everyone knows it, and so on. Knowing the payoffs is only the first level; doubt about whether the other knows that you know breaks the chain at a higher level.
> Not observing the other's choice makes the game static (imperfect information), not incomplete. A random state with a commonly known distribution gives commonly known expected payoffs. Not knowing the other's actual choice is strategic uncertainty, present in every game and handled by beliefs, not a failure of complete information.
> Ref: Lecture 1 slide 16; Tadelis (2013), Def. 3.1 (p. 45); Notas/L01/L01-10-pitfalls.md, item 5

## concepts

Q: Every payoff of a finite game is changed by at most ε, with ε > 0 as small as one likes. Which prediction is guaranteed to stay exactly the same?
- The set of profiles that survive IESDS, because every elimination rests on strict inequalities that a small change can never reverse
- The set of pure-strategy Nash equilibria, because each equilibrium condition is a weak inequality that tolerates small payoff changes
- A strict dominant-strategy equilibrium, since it rests on finitely many strict inequalities, each with slack that ε cannot use up
- The set of Pareto-optimal profiles, because Pareto comparisons rank whole payoff vectors and a small change cannot reorder them
<!-- YW5zOjI= -->
> Take ε smaller than half the smallest gap in the strict inequalities that make each $s_i^D$ strictly dominant; they all still hold, so $s^D$ remains the (unique) strict dominant-strategy equilibrium. This is why the dominant-strategy concept passes the invariance test.
> IESDS keeps its old eliminations, but a tie can break into a new strict dominance: if D pays (1, 0) and U pays (1, 1) against two columns, D survives, while D paying (1 − ε, 0) is eliminated, so the surviving set can shrink. A Nash equilibrium resting on a tie can vanish when the tie breaks. Two profiles that both give (1, 1) are both Pareto optimal; raise one by ε and the other is Pareto dominated.
> Ref: Lecture 1 slide 22; Tadelis (2013), §3.3.2 (pp. 55–56), §4.1.3 (p. 62)

Q: The invariance criterion asks a solution concept's prediction to survive small changes to a game. Which change counts as small for that criterion?
- Adding a player whose choices barely matter, since her arrival leaves the original players' payoff functions as they were
- Moving every payoff of every player by no more than ε, while the players and their strategy sets stay exactly as they were
- Deleting a strategy that no player uses in equilibrium, since a strategy never played cannot change what the others do
- Adding a strategy that copies the payoffs of an existing one, since the copy gives the player no outcome she lacked before
<!-- YW5zOjE= -->
> Tadelis restricts 'small changes' to the payoff functions: alter every payoff of every outcome by at most ε and keep the players and strategy sets fixed. Adding or removing players or strategies is ruled out, because it can change what players can guarantee themselves.
> A new player can change outcomes wildly even if her own choices look minor. Deleting a strategy used in no equilibrium can create equilibria, because it may have been the only profitable deviation from some profile. Copying a strategy is still a change to a strategy set, which the criterion excludes by construction.
> Ref: Lecture 1 slide 22; Tadelis (2013), §3.3.2.3 (p. 56)

Q: In the Battle of the Sexes, Alex and Chris each pick opera or football; both prefer being together to being apart, Alex prefers opera together and Chris football together. How do three solution concepts fare on existence and uniqueness?
- Strict dominance fails existence; IESDS exists but keeps all four profiles; pure Nash equilibrium exists but is not unique
- Strict dominance gives a unique prediction; IESDS removes each player's less-liked venue; pure Nash equilibrium does not exist
- Strict dominance fails existence; IESDS keeps only the two matched profiles; pure Nash equilibrium exists and is unique
- All three exist and keep the same two matched profiles, so the game tells none of them apart on either of the criteria
<!-- YW5zOjA= -->
> Each player's best choice depends on the other's, so neither has a dominant strategy and the dominant-strategy concept predicts nothing. No strategy is strictly dominated either, so IESDS can only say 'anything can happen', keeping all four profiles. Nash equilibrium selects (opera, opera) and (football, football): it exists, but it is not unique.
> A less-liked venue is not dominated, since each venue is the best reply to the other being there. IESDS cannot discard the mismatched profiles, because doing so would require correct beliefs, which is what Nash equilibrium adds. Pure equilibria do exist here, two of them.
> Ref: Lecture 1 slide 22; Lecture 2 slides 9, 14; Tadelis (2013), §4.1.3 (p. 62), §4.2.3 (p. 68), §5.1.2 (p. 83)

## pareto

Q: In the prisoner's dilemma of the slides, both staying mum gives −2 each, both finking gives −4 each, and a lone finker gets −1 while the mum partner gets −5. Which statement about Pareto optimality is correct?
- Only (M, M) is Pareto optimal; the lopsided profiles are not, since each one leaves a partner with the worst payoff
- No profile is Pareto optimal, since from each one some player can raise his payoff by changing his own strategy
- All four profiles are Pareto optimal, since from each one some player would lose by a move to any other profile
- Three of the four profiles are Pareto optimal, the two lopsided ones included; only the equilibrium (F, F) is not
<!-- YW5zOjM= -->
> (M, F) is the only profile that gives player 2 as much as −1, so no other profile keeps player 2 at least as well off: nothing Pareto dominates it, and likewise for (F, M). (M, M) is Pareto optimal too. (F, F) is Pareto dominated by (M, M).
> Pareto optimality means 'no waste', not fairness, so the unequal profiles qualify. A unilateral gain is the Nash test, not the Pareto test. From (F, F) the move to (M, M) makes both strictly better off, so it is not true that some player loses from every move.
> Ref: Lecture 1 slides 24, 26; Tadelis (2013), Def. 3.5 (p. 57); Notas/L01/L01-10-pitfalls.md, item 4

Q: In a two-player game the payoffs satisfy $u_1(s)+u_2(s)=k$ for every profile $s$, with $k$ a constant (the pharmacy location game, where the chains split the customers, is one). What does the Pareto criterion say about its profiles?
- Only profiles in which each player gets $k/2$ are Pareto optimal, since any unequal split wastes part of the total $k$
- Only Nash equilibria are Pareto optimal, since at any other profile some player gains by changing her own strategy
- Every profile is Pareto optimal, so the criterion cannot rank the equilibrium against any other profile of the game
- No profile is Pareto optimal, since from every profile either player can gain at the expense of the other player
<!-- YW5zOjI= -->
> A Pareto improvement needs one player strictly better off and nobody worse off; with a constant sum, any gain for one player is a loss for the other, so no profile Pareto dominates another and all are Pareto optimal.
> No split wastes anything, since every split adds up to $k$; equal division is a fairness notion, not a Pareto one. The Nash test (unilateral deviations) has nothing to do with Pareto rankings. A gain at the other's expense is not a Pareto improvement, so it cannot make a profile Pareto dominated.
> Ref: Lecture 1 slides 26, 32; Tadelis (2013), Def. 3.5 (p. 57); Notas/L01/L01-10-pitfalls.md, True/False item 21

## payoffs

Q: Player 1's payoff $u_1$ is replaced by $\tilde u_1(s)=u_1(s)+h(s_{-1})$, where $h$ is any real function of the opponents' strategies alone. Which conclusion holds?
- Player 1's best responses to every belief, pure or mixed, are unchanged, so dominance, IESDS and all Nash equilibria stay the same
- Player 1's best responses to pure beliefs are unchanged, but against mixed beliefs the term $h$ re-weights payoffs and can change them
- Player 1's best responses are unchanged only if $h$ is constant, since otherwise player 1 now cares about what the opponents choose
- Player 1's best responses are unchanged, but the Pareto ranking can change, and with it the set of Nash equilibria of the game
<!-- YW5zOjA= -->
> For any belief $\sigma_{-1}$, the expected value of $\tilde u_1(s_1,\cdot)$ equals that of $u_1(s_1,\cdot)$ plus the expected value of $h$, a term that is the same for every $s_1$. Every comparison between player 1's strategies is unchanged, so best responses, dominance, IESDS and Nash equilibria are all unchanged.
> The added term does not depend on $s_1$, so mixing cannot re-weight it differently across player 1's options. Player 1 already cared about the opponents' choices through $u_1$; what matters is whether the change varies with her own choice. The Pareto ranking can indeed change, since it compares payoffs across profiles, but Nash equilibria depend only on best responses.
> Ref: Lecture 1 slides 18, 23; Lecture 2 slides 10, 43; Tadelis (2013), §6.1.4 (pp. 105–106)

Q: Player 1's payoffs are all cubed, $\tilde u_1=u_1^3$, a strictly increasing transformation; player 2's payoffs are unchanged. Which prediction can change?
- Which of player 1's strategies are strictly dominated by her other pure strategies, since the gaps change
- The set of pure-strategy Nash equilibria, since cubing stretches the payoff gaps between player 1's options
- The profiles that survive IESDS, since cubing alters which of player 1's payoff comparisons are strict ones
- The probabilities of a mixed equilibrium, since player 1's indifference condition is what fixes player 2's mix
<!-- YW5zOjM= -->
> Pure-strategy concepts compare player 1's payoffs at a fixed $s_{-1}$, and a strictly increasing transformation preserves every such comparison, so dominance, IESDS and pure equilibria are unchanged. Mixed-strategy analysis uses expected payoffs, which are preserved only by positive affine transformations.
> In the Battle of the Sexes with Alex's payoffs 2 and 1, Chris's equilibrium probability $q$ of opera solves $2q=1-q$, so $q=1/3$; with cubed payoffs it solves $8q=1-q$, so $q=1/9$. Alex's own mix is fixed by Chris's payoffs and does not move. Strictness of a comparison and the set of pure equilibria are ordinal and survive the cube.
> Ref: Lecture 1 slide 18; Lecture 2 slides 44, 47–50; Tadelis (2013), §6.1.4 (pp. 105–106), §6.2 (pp. 107–113)
