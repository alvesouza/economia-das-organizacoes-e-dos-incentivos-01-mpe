---
quiz: "Lecture 3 · Quiz 1 of 3 — Extensive form, strategies and the threats behind Nash equilibria (estimated before the lecture: no slides yet, follows Tadelis Ch. 7)"
tags:
  tree: "Game trees, information sets and perfect information"
  strat: "Strategies as complete plans: pure, mixed and behavioral"
  nfpath: "Normal form of a tree, Nash equilibria and off-path threats"
---

## tree

Q: Player 1 chooses one of $m$ actions; player 2 observes it and chooses one of $k$ actions; player 1 then observes both moves, chooses one of $r$ actions, and the game ends. How many pure strategies does player 1 have?
- $m\,r^{k}$, one first action and one final action per reply of player 2, since player 1 already knows her own first move
- $m + r^{mk}$, the first-stage actions plus one final action per history, since the two stages are planned separately
- $m\,r^{mk}$, one first action and one final action at each of the $mk$ histories, even those her first move rules out
- $(m\,r)^{k}$, one pair of first and final actions per reply of player 2, since player 2's move is what she conditions on
<!-- YW5zOjI= -->
> Player 1 has $1 + mk$ information sets: the root, with $m$ actions, and one singleton after each pair $(a_1, a_2)$, with $r$ actions each. A pure strategy picks one action at every information set independently, so $\lvert S_1\rvert = m \cdot r^{mk}$. The count $m\,r^{k}$ is the number of reduced plans: it drops the actions at histories that the plan's own first move makes unreachable, which a strategy in Tadelis's sense must still specify. Sums never appear, because the choices at different information sets multiply.
> Ref: Tadelis (2013), Def. 7.4 and the counting rule, §7.2.1 (pp. 138–139); Gibbons (1992), §2.4.A (pp. 117–118); MWG §7.D (p. 228)
> Similar: Tadelis (2013), Exercise 7.1, p. 147; MWG Exercise 9.B.5(a), p. 302

Q: Nature draws one of two states with known probabilities; both players observe the draw; then player 1 moves, player 2 observes player 1's move and moves, and every information set is a singleton. How does Tadelis's Definition 7.3 classify this game?
- As a game of perfect information, since every information set is a singleton and nobody is uncertain about any earlier move
- As a game of incomplete information, since payoffs depend on a random state and so are not common knowledge before Nature moves
- As a game of perfect information only after Nature's draw is replaced by its expected payoffs, which removes the random move
- As a game of imperfect information, since the definition of perfect information also excludes moves of Nature, observed or not
<!-- YW5zOjM= -->
> Tadelis's Definition 7.3 asks for two things: every information set a singleton, and no moves of Nature. The second fails, so the game is one of imperfect information in his terms, although nobody is ever unsure where they are in the tree. MWG's Definition 7.C.1 asks only for singleton information sets, so they would call it perfect information: check which convention a question uses. The information is still complete, because the structure, including Nature's probabilities, is common knowledge; replacing the draw by expected payoffs would change the game, since players condition on the state.
> Ref: Tadelis (2013), Def. 7.3 (p. 136), the card game (pp. 136–137); MWG §7.C (pp. 221–225)
> Similar: Tadelis (2013), Exercise 7.9, pp. 149–150

Q: An information set may contain several nodes of the same player only if the same set of actions is available at each of them. What is the reason for this requirement?
- If the action sets differed, the player could tell the nodes apart by looking at her menu, which contradicts their being in one information set
- If the action sets differed, the payoffs at the successors would differ too, and payoffs must be equal across the nodes of one information set
- If the action sets differed, the player would forget which actions she had available before, which violates the assumption of perfect recall
- If the action sets differed, the count of pure strategies would no longer be a product, so the normal form of the tree could not be written
<!-- YW5zOjA= -->
> An information set represents what the player knows: she cannot distinguish its nodes. A different menu at one node would itself be information that tells her where she is, so the nodes could not belong to one set. It is a consistency requirement on the representation, not an assumption about payoffs (which can differ freely across the successors), nor about memory: perfect recall concerns forgetting earlier knowledge or moves.
> Ref: Tadelis (2013), Def. 7.2 (p. 135); Gibbons (1992), §2.4.A (p. 119)
> Similar: Tadelis (2013), Exercise 7.2, p. 147

Q: Player 1 chooses at 9 a.m.; player 2 chooses at 5 p.m. and learns nothing about player 1's choice before then. Payoffs are those of the Battle of the Sexes. What is the right model of this game?
- A sequential game in which player 2 is the follower, since she moves later and so best-responds to whatever player 1 has already done
- A simultaneous game, written as a tree with player 2's two nodes in one information set, so she has two pure strategies and not four
- A sequential game with four pure strategies for player 2, since a strategy for a later mover must list a reply to each earlier action
- A game of incomplete information, since player 2 does not know player 1's choice and so does not know which payoff she will receive
<!-- YW5zOjE= -->
> What makes a game sequential is what the later mover knows when she moves, not the clock (element 5 of the extensive form). Player 2 cannot condition on player 1's choice, so both of her nodes lie in one information set and her strategies are just $o$ and $f$: the tree is the simultaneous Battle of the Sexes. Not observing a move is imperfect information; incomplete information is about not knowing the game itself.
> Ref: Tadelis (2013), §7.1 (pp. 130–131, 135–136); Gibbons (1992), §2.4.A (pp. 115–119)
> Similar: Tadelis (2013), Exercise 7.2, p. 147; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 3, p. 160

## strat

Q: In the sequential Battle of the Sexes, player 2's pure strategies are $oo$, $of$, $fo$, $ff$ (first letter: reply to $O$; second: reply to $F$), and she uses the mixed strategy $(p_{oo}, p_{of}, p_{fo}, p_{ff})$. What is the equivalent behavioral probability of playing $o$ after $F$?
- $p_{oo} + p_{of}$, the total weight of the plans whose first letter is $o$, since those are the plans that play $o$ at a node
- $p_{oo} + p_{fo}$, the total weight of the plans whose second letter is $o$, since those are the plans that play $o$ after $F$
- $p_{fo} + p_{ff}$, the total weight of the plans whose first letter is $f$, since after $F$ the first letter is the one used
- $p_{oo}\,p_{fo}$, the product of the weights of the plans with $o$ after $F$, since the two information sets are independent
<!-- YW5zOjE= -->
> Conditional on reaching the information set after $F$, the probability of $o$ is the total probability of the plans that prescribe $o$ there: those with second letter $o$, $oo$ and $fo$. The first option is $\Pr\{o \mid O\}$; the third is $\Pr\{f \mid O\}$. A product would be right only for the probability of a joint event across information sets, not for a single conditional choice.
> Ref: Tadelis (2013), Defs. 7.5–7.6 and the worked conversion, §7.2.2 (pp. 139–141)
> Similar: Tadelis (2013), Exercise 7.10, p. 150

Q: In the sequential Battle of the Sexes, player 2 uses the behavioral strategy $\sigma_2(o \mid O) = \alpha$, $\sigma_2(o \mid F) = \gamma$, with $\alpha, \gamma \in (0,1)$. Which mixed strategies $(p_{oo}, p_{of}, p_{fo}, p_{ff})$ generate it?
- Exactly one, $(\alpha\gamma,\ \alpha(1-\gamma),\ (1-\alpha)\gamma,\ (1-\alpha)(1-\gamma))$, since the two information sets randomize independently
- A two-parameter family, since there are four unknowns and only the two conditional probabilities $\alpha$ and $\gamma$ to match
- None in general, since a behavioral strategy randomizes at each node and a mixed strategy only once, before the game starts
- A one-parameter family, $(t,\ \alpha - t,\ \gamma - t,\ 1 - \alpha - \gamma + t)$ for each $t$ keeping all four weights nonnegative
<!-- YW5zOjM= -->
> Matching requires $p_{oo}+p_{of}=\alpha$, $p_{fo}+p_{ff}=1-\alpha$, $p_{oo}+p_{fo}=\gamma$, $p_{of}+p_{ff}=1-\gamma$, together with the four weights summing to 1. Given the sum, the second equation follows from the first and the fourth from the third, so there are three independent equations in four unknowns: one free parameter $t = p_{oo}$, constrained by nonnegativity of all four weights: $\max\{0, \alpha+\gamma-1\} \le t \le \min\{\alpha, \gamma\}$. The product strategy in the first option is the member with $t = \alpha\gamma$, one of many. At $\alpha = 1/3$, $\gamma = 1/2$ this is the family behind Tadelis's two examples.
> Ref: Tadelis (2013), §7.2.2 (pp. 140–142), footnote 4 (p. 142)
> Similar: Tadelis (2013), Exercise 7.10, p. 150

Q: Which statement about mixed and behavioral strategies in extensive-form games is correct?
- Under perfect recall the two are equivalent: against given opponents, any outcome distribution one generates the other can generate
- Under perfect recall the two are equivalent only in games of perfect information, since information sets with several nodes break the mapping
- The two are always equivalent, since a behavioral strategy is just a mixed strategy that happens to randomize separately at each node
- The two are never equivalent, since a mixed strategy commits to one plan before the game while a behavioral one decides during play
<!-- YW5zOjA= -->
> Every mixed strategy has a behavioral equivalent obtained by conditioning, and Kuhn's theorem gives the converse when no player forgets what she knew, whether or not information sets are singletons. Without perfect recall the equivalence can fail: in the absent-minded driver (named only, not examinable) randomizing at the single information set beats every pure plan. The timing of the randomization differs, but timing alone does not change the outcome distribution under perfect recall.
> Ref: Tadelis (2013), Def. 7.7 and Kuhn's theorem (p. 142), Remark (pp. 142–143)
> Similar: Tadelis (2013), Exercise 7.10, p. 150

## nfpath

P: Player 1 chooses $O$ or $F$; player 2 observes the choice and chooses $o$ or $f$. Matching on $O$ pays $(a, b)$, matching on $F$ pays $(b, a)$, any mismatch pays $(0,0)$, where the first number is player 1's payoff and $a > b > 0$. Player 2's strategies are written as (reply to $O$, reply to $F$): $oo$, $of$, $fo$, $ff$.

Q: Which are the pure-strategy Nash equilibria of this game?
- $(O, oo)$, $(O, of)$, $(F, ff)$ and $(F, fo)$, since in every column player 1 has a best reply and player 2 is indifferent in some rows
- $(O, oo)$, $(O, of)$ and $(F, ff)$, since only these cells are mutual best replies once the matrix is built from the tree's paths
- $(O, of)$ only, since player 2 follows player 1 in every subgame and player 1, anticipating it, picks the option that pays her $a$
- $(O, oo)$ and $(F, ff)$, since a Nash equilibrium of the sequential game must be one of the two pure equilibria of the simultaneous game
<!-- YW5zOjE= -->
> Row $O$ pays $(a,b)$ against $oo$ and $of$ and $(0,0)$ against $fo$ and $ff$; row $F$ pays $(b,a)$ against $of$ and $ff$ and $(0,0)$ against $oo$ and $fo$. Player 1's best reply is $O$ against $oo$ and $of$ (because $a > b$ and $a > 0$) and $F$ against $ff$. Player 2's best replies are $oo, of$ to $O$ and $of, ff$ to $F$. The cells where both hold are the three listed; $(F, fo)$ fails because $fo$ gives player 2 zero after $F$. The third option is the subgame-perfect equilibrium, a subset of the Nash set.
> Ref: Tadelis (2013), §7.2.3 and §7.3 (pp. 143–145)
> Similar: Tadelis (2013), Exercise 7.2(d), p. 147; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 4, p. 163

Q: In the equilibrium $(F, ff)$, which information set is off the equilibrium path, and what keeps player 1 at $F$?
- Player 2's node after $F$ is off the path, and player 1 stays at $F$ because she expects $f$ there, which gives her $b > 0$
- Player 2's node after $O$ is off the path, and player 1 stays at $F$ because $b > a$ makes football her better outcome
- Player 2's node after $O$ is off the path, and player 1 stays at $F$ because the plan $f$ there would leave her with $0 < b$
- No information set is off the path, since in a game of perfect information every node is reached with positive probability
<!-- YW5zOjI= -->
> Under $(F, ff)$ play goes $F \to f$, so the node after $O$ is reached with probability 0. Player 2's plan there, $f$, would give player 1 a payoff of 0 if she switched to $O$, less than the $b$ she gets at $F$: an off-path plan acts as a threat. The threat is empty, since at that node player 2 would get $b$ from $o$ against $0$ from $f$, but Nash equilibrium never tests it because the node is not reached. Note that $a > b$, not $b > a$.
> Ref: Tadelis (2013), Def. 7.8 and §7.3 (pp. 145–146); Gibbons (1992), §2.4.B (pp. 126–128)
> Similar: Tadelis (2013), Exercise 7.6, pp. 148–149; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 4, p. 163

P:

Q: Every extensive-form game has a unique normal form. Why can't the normal form alone be used to decide which Nash equilibria rest on empty threats?
- Because one normal form can come from several trees, so it has lost the order of moves and what each player knew when moving
- Because the normal form only lists pure strategies, and empty threats can only be detected once mixed strategies are allowed
- Because the normal form repeats each terminal payoff several times, which hides the best replies of players who move later on
- Because the normal form is defined only for simultaneous games, so writing a tree as a matrix changes the game being analysed
<!-- YW5zOjA= -->
> The map from trees to matrices is many-to-one: Tadelis's Fig. 7.12 gives a perfect-information tree and an imperfect-information tree with the same matrix. Whether a plan is a best reply at an unreached node depends on the timing and information that the matrix discards, so the matrix cannot tell a credible plan from an empty one. Repeated payoffs are a symptom of this loss, not the cause, and any tree can be written as a matrix without changing its Nash equilibria.
> Ref: Tadelis (2013), Remark and Fig. 7.12 (p. 144), §7.3 (p. 146)
> Similar: Tadelis (2013), Exercise 7.9, pp. 149–150
