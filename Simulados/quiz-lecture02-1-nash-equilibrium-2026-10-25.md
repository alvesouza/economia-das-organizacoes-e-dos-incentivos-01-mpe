---
quiz: "Lecture 2 · Quiz 1 of 3 — Best responses, rationalizability and Nash equilibrium"
tags:
  br: "Best responses and rationalizability"
  ne: "Nash equilibrium: definition and interpretations"
  iesds: "Nash equilibrium and IESDS"
  matrix: "Pure equilibria in matrix games"
---

## br

Q: Which statement is exactly the lecture's definition of a strategy $s_i$ that is never a best response (NBR)?
- Some other strategy $s_i'$ gives player $i$ a strictly higher payoff than $s_i$ against every profile $s_{-i}\in S_{-i}$ of the opponents
- Strategy $s_i$ is not a best response to $s_{-i}^*$, the profile the opponents actually play in some Nash equilibrium of the game
- There is no belief $s_{-i}\in S_{-i}$ about the opponents for which $s_i$ belongs to the best-response set $BR_i(s_{-i})$ of player $i$
- Strategy $s_i$ is a best response to no profile $s_{-i}$ built only from strategies that survive the iterated removal of NBR strategies
<!-- YW5zOjI= -->
> The NBR definition quantifies over every belief $s_{-i}\in S_{-i}$. The first option is strict dominance, which implies NBR (a strictly dominated strategy is never a best response) but is a different property. The second ties the definition to one equilibrium profile: a strategy can fail there and still be a best response to another belief. The fourth describes a later round of rationalizability, not the definition itself.
> Ref: Lecture 2 slides 10–11; Tadelis (2013), Defs. 4.5–4.8 (pp. 70–73), Prop. 4.3 (p. 70)
> Similar: Tadelis (2013), Exercise 5.5, p. 96; MWG 8.C.1, p. 262

Q: In a finite game the profile $s^*$ is the unique survivor of IESDS. What does the lecture's proposition on best responses conclude about $s^*$, and which step of its proof uses finiteness?
- Each $s_i^*$ is a best response to $s_{-i}^*$; finiteness ends the chain of eliminating strategies at one that is never eliminated, which must be $s_i^*$
- Each $s_i^*$ is strictly dominant for player $i$; finiteness guarantees that the elimination stops after at most $|S_i|-1$ rounds for every player
- Each $s_i^*$ is a best response to every belief $s_{-i}$; finiteness ensures that a maximum of $u_i(\cdot,s_{-i})$ exists for each of those beliefs
- The profile $s^*$ is Pareto optimal; finiteness ensures that only finitely many profiles have to be compared with $s^*$ in the Pareto ranking
<!-- YW5zOjA= -->
> The proposition says $s_i^*\in BR_i(s_{-i}^*)$ for every $i$. The proof supposes a better reply $s_i'$, notes that it was eliminated by some $s_i''$ that does even better against the never-eliminated $s_{-i}^*$, and repeats; finiteness ends that chain at a survivor, which can only be $s_i^*$, a contradiction. A unique survivor need not be dominant (Cournot) nor a best reply to every belief, and the prisoner's dilemma shows it need not be Pareto optimal.
> Ref: Lecture 2 slide 12; Tadelis (2013), Prop. 4.4 (pp. 70–71)
> Similar: Tadelis (2013), Exercise 5.1, p. 95; MWG 8.D.2, p. 263

Q: Battle of the Sexes: Alex and Chris each choose opera (O) or football (F); Alex gets 2 and Chris 1 at (O, O), Alex gets 1 and Chris 2 at (F, F), and both get 0 when apart. What do rationalizability and Nash equilibrium say about the profile (O, F), Alex at the opera and Chris at football?
- Neither allows it: O is never a best response for Chris and F is never a best response for Alex, so both concepts eliminate the profile in round one
- Both allow it: each strategy is a best response to some belief, and Nash equilibrium only asks that beliefs be justified, not that they be correct
- Rationalizability excludes it but Nash equilibrium allows it: IESDS removes F for Alex, while the profile still survives the underline method
- Rationalizability allows it but Nash equilibrium does not: each choice is a best response to some belief, but the two beliefs cannot both be correct
<!-- YW5zOjM= -->
> O is Alex's best response to the belief that Chris plays O, and F is Chris's best response to the belief that Alex plays F, so every strategy is rationalizable and (O, F) survives. At (O, F) each player would switch given what the other actually does: Nash equilibrium adds the requirement that beliefs be correct, and only (O, O), (F, F) and a mixed profile pass it. Nothing is dominated in this game, so IESDS removes nothing.
> Ref: Lecture 2 slides 9–11, 14–15; Tadelis (2013), §4.3.6 (p. 76), §5.1 (pp. 79–81)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 2 Ex. 2, p. 41; Tadelis (2013), Exercise 6.1, p. 123

## ne

Q: The lecture contrasts IESDS and rationalizability with Nash equilibrium. Which statement matches that contrast?
- IESDS and rationalizability describe stable conventions, while Nash equilibrium is derived from common knowledge of rationality and nothing else
- IESDS and rationalizability follow from common knowledge of rationality, while Nash equilibrium is strategic stability with correct beliefs
- IESDS and rationalizability require correct beliefs about play, while Nash equilibrium requires only that each player be individually rational
- All three follow from common knowledge of rationality alone; Nash equilibrium is the sharpest because it also uses each player's own payoffs
<!-- YW5zOjE= -->
> IESDS and rationalizability are epistemic: they are derived from common knowledge of rationality. Nash equilibrium is a notion of strategic stability in which beliefs are correct, read as self-fulfilling expectations, self-enforcing agreements or social conventions. Common knowledge of rationality does not imply Nash play: in the Battle of the Sexes it allows (O, F), which is not an equilibrium.
> Ref: Lecture 2 slide 15; Tadelis (2013), §5.1 (pp. 79–81); Gibbons (1992), §1.1.C (pp. 8–9); MWG §8.D (pp. 248–249)
> Similar: Tadelis (2013), Exercise 5.3, p. 95

Q: Two drivers each choose a side of the road, L or R. Both get $\alpha$ at (L, L), $\beta$ at (R, R) and $0$ when they choose differently, with $\alpha>\beta>0$. Which statement about the pure Nash equilibria and IESDS is correct?
- (L, L) and (R, R) are both Nash equilibria although (R, R) is Pareto dominated, and IESDS removes nothing since each side is best against itself
- Only (L, L) is a Nash equilibrium, because $\alpha>\beta$ makes L a strictly dominant strategy, and IESDS also selects it after a single round
- (L, L) and (R, R) are both Nash equilibria, and IESDS removes R in the first round because it is weakly dominated by L when $\alpha>\beta$
- No pure profile is a Nash equilibrium, since at (R, R) each driver gains by switching to L, and at (L, L) a driver gains by matching the other
<!-- YW5zOjA= -->
> Against L a driver's best reply is L ($\alpha>0$); against R it is R ($\beta>0$). Both diagonal cells are mutual best replies, and the Pareto ranking does not remove (R, R): no single driver gains by switching alone. L does not dominate R even weakly, since it pays $0<\beta$ against R, so IESDS has nothing to remove: in coordination games the equilibrium concept, not elimination, does the selecting.
> Ref: Lecture 2 slide 18; Tadelis (2013), §5.1.1 (pp. 81–82), §5.2.1 (pp. 83–84)
> Similar: Tadelis (2013), Exercise 5.6, p. 96; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 2 Ex. 2, p. 41

## iesds

Q: The proof that every Nash equilibrium $s^*$ survives IESDS looks at the first round $k$ in which some component $s_i^*$ is eliminated. Why the first round?
- Because IESDS removes at most one strategy per round, so the first round is the only one in which a component of $s^*$ can possibly be eliminated
- Because after round $k$ the game is smaller, so $s_{-i}^*$ is no longer a profile of the original game and the equilibrium condition stops applying
- Because no component of $s^*$ is gone before round $k$, so $s_{-i}^*\in S_{-i}^{k-1}$ and the dominance inequality can be evaluated at $s_{-i}^*$
- Because the strategy that eliminates $s_i^*$ in a later round could itself be eliminated, so only round-one dominators are sure to survive
<!-- YW5zOjI= -->
> In round $k$, $s_i^*$ is strictly dominated by some $s_i'$ against every surviving $s_{-i}\in S_{-i}^{k-1}$. Taking the first such round guarantees that $s_{-i}^*$ is still among the survivors, so $u_i(s_i',s_{-i}^*)>u_i(s_i^*,s_{-i}^*)$, which contradicts $s_i^*\in BR_i(s_{-i}^*)$. IESDS may remove many strategies per round, and the reduced game keeps $s_{-i}^*$ as long as none of its components was removed.
> Ref: Lecture 2 slide 16; Gibbons (1992), App. 1.1.C (pp. 12–14); Tadelis (2013), Prop. 5.1 (pp. 80–81)
> Similar: Tadelis (2013), Exercise 5.1, p. 95; Gibbons (1992), Problem 1.14, p. 51

Q: The converse result says: in a finite game, if $s^*$ is the unique profile surviving IESDS, it is a Nash equilibrium. Where does its proof use finiteness?
- To ensure each player has a best response to $s_{-i}^*$, since with infinitely many strategies the supremum of $u_i(\cdot,s_{-i}^*)$ may never be attained
- To ensure the chain of strategies, each eliminating the previous one and paying more against $s_{-i}^*$, ends at a never-eliminated strategy, $s_i^*$
- To ensure that IESDS ends after finitely many rounds, since an infinite elimination process could remove every strategy of some player in the limit
- To ensure every strictly dominated strategy is dominated by a pure strategy, since with infinite sets the dominating strategy $s_i'$ may be mixed
<!-- YW5zOjE= -->
> Suppose $u_i(s_i,s_{-i}^*)>u_i(s_i^*,s_{-i}^*)$. Then $s_i$ was eliminated by some $s_i'$ with $u_i(s_i',s_{-i}^*)>u_i(s_i,s_{-i}^*)$; if $s_i'$ was eliminated later, repeat. Payoffs against $s_{-i}^*$ rise along the chain, and finiteness makes it stop at a strategy that is never eliminated, which is $s_i^*$, so $u_i(s_i^*,s_{-i}^*)>u_i(s_i,s_{-i}^*)$: a contradiction. The other options name real issues with infinite games, but not the step this proof uses.
> Ref: Lecture 2 slide 17; Tadelis (2013), Prop. 4.4 (pp. 70–71); Gibbons (1992), App. 1.1.C (pp. 12–14)
> Similar: MWG 8.D.2, p. 263; Tadelis (2013), Exercise 5.1, p. 95

Q: Which statement about Nash equilibria and weakly dominated strategies is correct?
- A Nash equilibrium $s^*$ never uses a weakly dominated strategy, because the dominating strategy is a profitable deviation even when the inequality is weak
- A Nash equilibrium may use a weakly dominated strategy only with infinitely many strategies, as in Bertrand at $(c,c)$, never in finite matrix games
- Iterated removal of weakly dominated strategies keeps every Nash equilibrium $s^*$, because each removal is justified by rationality just as before
- A Nash equilibrium may use a weakly dominated strategy, as in Bertrand at $(c,c)$, because only strict dominance guarantees a profitable deviation
<!-- YW5zOjM= -->
> The proof that Nash equilibria survive IESDS uses strict dominance; a weakly dominating strategy may tie against the equilibrium profile, so no profitable deviation exists. In Bertrand $p_i=c$ is weakly dominated by any higher price with positive demand, yet $(c,c)$ is the unique Nash equilibrium. Finite examples exist too (a row that ties against one column and loses against the other), and removing weakly dominated strategies can delete equilibria; such equilibria are only considered less plausible.
> Ref: Lecture 2 slides 16, 36; Tadelis (2013), §4.1 (p. 63), §5.2.4 (p. 91)
> Similar: Tadelis (2013), Exercise 5.2, p. 95

## matrix

Q: In a symmetric $2\times2$ game, (C, C) gives $r$ to each player, (D, D) gives $p$ to each, and a player who plays D against C gets $t$ while the one playing C gets $s$. Which ordering makes D strictly dominant and the unique Nash equilibrium (D, D) Pareto dominated by (C, C)?
- $t>r>p>s$, so D is better against C ($t>r$) and against D ($p>s$), while $r>p$ makes (C, C) better for both players
- $r>t>p>s$, so D is better against D ($p>s$) and against C ($r>t$), while $r>p$ makes (C, C) better for both players
- $t>r>s>p$, so D is better against C ($t>r$) and against D ($s>p$), while $r>p$ makes (C, C) better for both players
- $t>p>r>s$, so D is better against C ($t>r$) and against D ($p>s$), while $p>r$ makes (C, C) better for both players
<!-- YW5zOjA= -->
> D strictly dominates C iff $t>r$ (against C) and $p>s$ (against D); (D, D) is then the unique Nash equilibrium, and it is Pareto dominated by (C, C) iff $r>p$. Together: $t>r>p>s$, the slides' dilemma ($3>2>0>-1$). With $r>t$ the best reply to C is C (a coordination structure); with $s>p$ the best reply to D is C (a hawk-dove structure with asymmetric equilibria); with $p>r$ the equilibrium is not a social dilemma.
> Ref: Lecture 2 slides 4–6, 18; Tadelis (2013), p. 52 (prisoner's dilemma), §5.1 (pp. 80–81)
> Similar: Tadelis (2013), Exercise 5.6, p. 96

Q: Player 1 chooses U or D, player 2 chooses L or R. Payoffs: (U, L) gives $(x, 1)$, (U, R) gives $(0, 0)$, (D, L) gives $(1, 0)$, (D, R) gives $(1, 2)$, with $x$ a real parameter. For which $x$ is (U, L) a Nash equilibrium, and what happens at $x=1$?
- For $x>1$ only, since at $x=1$ player 1 is indifferent between U and D against L, and a tie fails the best-response inequality
- For $x\ge1$, but at $x=1$ the profile (U, L) is no longer an equilibrium because IESDS removes U before the equilibrium test applies
- For $x\ge1$; at $x=1$ the profile (U, L) is still an equilibrium, although U is then weakly dominated by D for player 1
- For $x\le1$, since player 2 plays L against U only when player 1's payoff there is low enough to keep player 1 from deviating
<!-- YW5zOjI= -->
> Player 2's best reply to U is L ($1>0$) for every $x$. Player 1's best reply to L includes U iff $x\ge1$, because the best-response definition uses a weak inequality. At $x=1$, U ties with D against L and loses against R ($0<1$): it is weakly dominated, yet (U, L) is a Nash equilibrium, the caveat on weakly dominated strategies. Strict IESDS removes nothing at $x=1$. (D, R) is a Nash equilibrium for every $x$.
> Ref: Lecture 2 slides 10, 14, 16; Tadelis (2013), Def. 5.1 (p. 80)
> Similar: Tadelis (2013), Exercise 5.2, p. 95; Tadelis (2013), Exercise 5.3, p. 95
