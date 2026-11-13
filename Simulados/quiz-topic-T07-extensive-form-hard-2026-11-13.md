---
quiz: "Topic T7 · Extensive form, strategies and information — hard conceptual quiz (10 questions; Lecture 3, Tadelis Ch. 7)"
tags:
  recall: "Perfect recall, mixed and behavioral strategies"
  strat: "Strategies as complete plans"
  info: "What information sets can and cannot model"
  nf: "Normal forms and paths of play"
---

## recall

Q: An absent-minded driver passes two exits he cannot tell apart, so both lie in one information set: leaving at the first exit pays 0, at the second 4, and missing both pays 1. How do his best mixed and best behavioral strategies compare?
- They coincide at a payoff of 1, since with a single information set a behavioral strategy is just a mixed strategy over his two pure plans
- The mixed strategy does better, reaching 4 by drawing once in advance between exiting and continuing and then following the draw at both exits
- The behavioral strategy does better, reaching 4/3 by exiting with probability 1/3 at each pass, while no mixed strategy earns more than 1
- Both reach 4/3, since Kuhn's theorem makes every behavioral strategy equivalent to a mixed one whenever the game has a single player
<!-- YW5zOjI= -->
> His two pure plans are "exit" (he leaves at the first exit: 0) and "continue" (he misses both: 1), so any mixture of them earns at most 1; no pure plan reaches the second exit, since the same action is taken at both nodes. A behavioral strategy exits with probability $p$ at each pass: $0\cdot p + 4p(1-p) + 1\cdot(1-p)^2 = -3p^2+2p+1$, maximized at $p=1/3$ with value $4/3$. Kuhn's equivalence needs perfect recall, which fails here because one node of the information set precedes the other; a single player does not rescue it.
> Ref: Tadelis (2013), §7.2.2, Def. 7.7 and the Remark on the absent-minded driver (pp. 142–143); Lecture 3 slides 27–28
> Similar: Tadelis (2013), Exercise 7.10, p. 150 (Listas/pratica-lecture-03 #10)

Q: Player 1 chooses L or R and then moves again, choosing l or r at one information set holding both of her later nodes, because she forgets her first choice. She wants the outcomes (L, l) and (R, r) to occur with probability 1/2 each. Which statement is correct?
- A mixed strategy can do it by drawing one of the two plans once, but no behavioral strategy can, since it randomizes independently at each set
- A behavioral strategy can do it by playing each action with probability 1/2 at both sets, and a mixed strategy can do the same with the two plans
- Neither can do it, since forgetting the first move means that the second move cannot be made to depend on the first one by any strategy
- Both can do it, since Kuhn's theorem guarantees that mixed and behavioral strategies give the same outcomes in every finite game tree
<!-- YW5zOjA= -->
> The mixed strategy that puts 1/2 on the plan (L, l) and 1/2 on (R, r) delivers the target: the correlation is created by the single draw before the game. A behavioral strategy sets $\Pr(L)=a$ and $\Pr(l)=b$ independently, and the target needs $a(1-b)=0$, $(1-a)b=0$ and $ab=1/2$ at once, which is impossible. Playing 1/2 everywhere yields each of the four outcomes with probability 1/4. This is the other direction in which Kuhn's equivalence fails without perfect recall; the absent-minded driver shows the reverse failure.
> Ref: Tadelis (2013), §7.2.2, Defs. 7.5–7.7 (pp. 139–142); Lecture 3 slides 27–28; MWG §7.E (pp. 231–233)
> Similar: Simulados/quiz-lecture03-1-extensive-form-2026-10-25, section strat

Q: Which statement about perfect information and perfect recall is correct?
- Perfect recall implies perfect information, since a player who forgets nothing always knows exactly which node of the tree she has reached
- Imperfect information implies imperfect recall, since a player who cannot see a rival's earlier move has in effect forgotten part of the history
- Perfect information can coexist with imperfect recall, since a player who moves twice may forget her first move even when every set is a singleton
- Perfect information implies perfect recall, since singleton sets leave nothing to forget, while perfect recall allows sets with several nodes
<!-- YW5zOjM= -->
> Forgetting means an information set lumps together nodes that differ in what the player herself did or saw before; with only singleton sets there is nothing to lump, so perfect information implies perfect recall. The converse fails: the simultaneous Battle of the Sexes drawn as a tree has a two-node information set (imperfect information) and perfect recall, since player 2 never knew player 1's move and so forgets nothing. Not observing a rival is not forgetting (second option), and a singleton set always tells the player where she is (third option).
> Ref: Tadelis (2013), Def. 7.3 (p. 136) and Def. 7.7 (p. 142); Lecture 3 slides 22–24 and 28
> Similar: Listas/pratica-lecture-03 #2 (Tadelis 7.1)

## strat

Q: Player 2 has $k$ information sets with two actions at each, and the game has perfect recall. How do her sets of mixed and behavioral strategies compare?
- Both have dimension $k$, since a mixed strategy is pinned down by the probability of each action at each information set, which is $k$ numbers
- Mixed strategies form a simplex of dimension $2^k-1$ and behavioral ones a cube of dimension $k$, so many mixed ones share one behavioral image
- Mixed strategies have dimension $2k-1$ and behavioral ones $2k$, so every behavioral strategy is generated by a unique mixed strategy of hers
- Behavioral strategies have dimension $2^k$ and mixed ones $k$, since a behavioral strategy must give a probability to every complete plan
<!-- YW5zOjE= -->
> A pure strategy picks one of two actions at each of $k$ sets, so there are $2^k$ pure plans and the mixed strategies form a simplex of dimension $2^k-1$. A behavioral strategy is one probability per set, a point of $[0,1]^k$. Under perfect recall every mixed strategy maps to the behavioral strategy with the same conditional probabilities, and the map is many-to-one: in the sequential Battle of the Sexes ($k=2$) Tadelis shows that both $(1/3, 0, 1/6, 1/2)$ and $(1/6, 1/6, 1/3, 1/3)$ over $(oo, of, fo, ff)$ generate the behavioral strategy $(1/3, 1/2)$.
> Ref: Tadelis (2013), §7.2.2 and footnote 4 (pp. 139–142); Lecture 3 slides 25–28
> Similar: Listas/pratica-lecture-03 #4 (Tadelis 7.2); Listas/pratica-lecture-03 #6 (Tadelis 7.6)

Q: Player 1 moves at the root and again later, but her plan takes an action at the root that never leads to her later information set. Why must her strategy still specify an action there?
- Because subgame perfection checks play after her own deviation, and player 2's best reply there depends on what player 1 would do later
- Because otherwise the normal form would have fewer rows, and Nash's theorem guarantees existence only when every plan is fully written out
- Because the action there changes her payoff on the equilibrium path, since expected payoffs average over every information set of the tree
- Because perfect recall forces each player to choose at every set she owns, whether or not her own earlier choices allow her to reach it
<!-- YW5zOjA= -->
> A pure strategy assigns an action to every information set of the player (Def. 7.4), including sets her own plan precludes. Those actions never change her payoff on the path (third option) and Nash's theorem holds for the reduced normal form too (second option). They matter for subgame perfection: if player 1 deviates at the root, the subgame that follows must be played at a Nash equilibrium, and player 2's best reply there depends on player 1's later action. Perfect recall is about memory, not about what a plan must contain (fourth option).
> Ref: Tadelis (2013), §7.2.1, Def. 7.4 (pp. 137–139), §8.2 (pp. 153–159); Lecture 3 slides 25 and 34
> Similar: Simulados/quiz-lecture03-1-extensive-form-2026-10-25, section strat

Q: Player 1 has perfect recall and moves twice. Her mixed strategy puts zero weight on every pure plan that takes her to her second information set. What behavioral strategy at that set is equivalent to her mixed strategy?
- The uniform one, since the conditional probabilities there are zero over zero, and the convention resolves that ratio by spreading weight evenly
- Only the one that copies her action at the root, since perfect recall requires her later choice to be consistent with the choice she made first
- Any distribution at all, since the set is never reached, and the distribution over outcomes is the same against any strategies of the others
- None, since Kuhn's equivalence breaks down when an information set is reached with zero probability under the mixed strategy being copied
<!-- YW5zOjI= -->
> The equivalent behavioral strategy uses $\Pr(a \mid h)$, the probability of action $a$ given that the mixed strategy reaches $h$. When her own mixed strategy never reaches $h$, this ratio is undefined and any choice there leaves the outcome distribution unchanged, so every distribution is equivalent and Kuhn's theorem holds. There is no uniform convention (first option) and perfect recall does not tie her action to her earlier one (second option). The practical lesson is that a mixed strategy does not pin down behavior off its own path, which is why subgame perfection must state it separately.
> Ref: Tadelis (2013), §7.2.2 (pp. 139–142); Lecture 3 slides 27–28; MWG §7.E (pp. 231–233)
> Similar: Simulados/quiz-lecture03-1-extensive-form-2026-10-25, section strat

## info

Q: Player 2 moves after player 1 and sees a signal that equals player 1's action with probability 0.9 and the other action otherwise. How is this represented in an extensive form?
- As one information set holding both of player 2's nodes, with her payoffs replaced by averages that put weight 0.9 on the action she saw
- As a game of perfect information in which player 2 sees player 1's action, with every payoff scaled by 0.9 to reflect the chance of an error
- As two singleton information sets for player 2, one per action of player 1, with player 2 told to randomize 0.9 and 0.1 between her replies
- As a Nature move after each action of player 1, with one information set of player 2 per signal value, each holding a node from both branches
<!-- YW5zOjM= -->
> Noise is a move of Nature: after each action of player 1, Nature draws the signal with probabilities 0.9 and 0.1. Player 2 knows the signal but not the action, so her information sets are indexed by the signal, each containing one node after each action of player 1. Payoffs stay attached to terminal nodes; they are never averaged or scaled to represent information (first two options), and singleton sets would mean that she sees the action perfectly (third option). A consequence: none of player 2's nodes starts a proper subgame, so subgame perfection adds nothing here, which is the gap that perfect Bayesian equilibrium fills.
> Ref: Tadelis (2013), §7.1 (pp. 130–137), §15.1 (p. 303); Lecture 3 slides 22–24
> Similar: Simulados/quiz-lecture03-1-extensive-form-2026-10-25, section tree

Q: The extensive form is common knowledge among the players. Which kind of uncertainty can an information set capture directly, and which needs more?
- Both kinds fit directly, since an information set can group nodes that differ in a rival's payoffs as easily as nodes that differ in her past moves
- Not knowing a rival's past move fits an information set; not knowing her payoffs needs a move of Nature over types, as in Harsanyi's approach
- Not knowing a rival's payoffs fits an information set; not knowing her past move needs a move of Nature that draws that move with known odds
- Neither fits, since an information set records only a player's own past moves, and any doubt about a rival requires incomplete information
<!-- YW5zOjE= -->
> Information sets partition decision nodes, and payoffs are attached to terminal nodes of a tree that everyone knows; so a player can be unsure which node she is at (a rival's earlier move), but not about what the payoffs at a node are. Uncertainty about a rival's payoffs means the game itself is not common knowledge; Harsanyi's device restores common knowledge by letting Nature draw the rival's type at the root, after which ordinary information sets capture the uncertainty. The third option reverses the roles; the fourth confuses information sets with memory of one's own moves.
> Ref: Lecture 3 slides 21–22; Tadelis (2013), §7.1 (pp. 130–137) and Ch. 12 introduction (pp. 241–245)
> Similar: Listas/pratica-lecture-07 #4 (Tadelis 12.1)

## nf

Q: In tree X player 1 moves first and player 2 moves without seeing her choice; in tree Y player 2 moves first and player 1 moves without seeing his. Each action pair pays the same in both trees. Which is correct?
- Their normal forms differ, since the order of moves fixes which player's strategies are written as rows and which player is the first to act
- They share a normal form, but tree X has a proper subgame at player 2's node, so its subgame-perfect equilibria are a strict subset of tree Y's
- They share a normal form but not their Nash equilibria, since a Nash equilibrium of a tree depends on which of the players moves first
- They share a normal form, and since neither has a proper subgame other than itself, their Nash and subgame-perfect equilibria also coincide
<!-- YW5zOjM= -->
> In both trees each player has a single information set with the same actions, so the strategy sets and the payoff of every strategy pair are identical: one normal form. In each tree the second mover's set holds two nodes, so no node below the root starts a proper subgame; subgame perfection then coincides with Nash, and both coincide across the trees. The order of moves matters only when it is observed. Which player is written as rows is a labeling convention (first option), player 2's node in tree X is not a singleton (second option), and Nash equilibria depend only on strategies and payoffs (third option).
> Ref: Tadelis (2013), §7.2.3, Fig. 7.11 (pp. 143–145); Lecture 3 slides 19–23
> Similar: Listas/pratica-lecture-03 #5 (Muñoz-Garcia Ch. 4 Ex. 4, sequential Battle of the Sexes)

Q: Two different Nash equilibria of a finite extensive-form game induce the same path of play. Which statement is correct?
- They give every player the same payoff and differ only off the path, so one of them can be subgame perfect while the other is not
- They must be the same profile, since a pure strategy is identified by the path it generates against the strategies of the other players
- They are either both subgame perfect or neither is, since subgame perfection is a property of the path of play and of its payoffs alone
- They can give different payoffs, since the plans at information sets off the path enter expected payoffs through the threats that they carry
<!-- YW5zOjA= -->
> Payoffs are determined by the terminal node reached, so the same path means the same payoffs, and the two profiles can differ only where play does not go. For instance, if player 1 strictly prefers to end the game at once, both "end; and player 2 would reply badly after continuing" and "end; and player 2 would reply optimally" are Nash equilibria with the same path, and only the second is subgame perfect. A strategy is a plan for every information set, not a path (second option); subgame perfection is a property of the whole profile, including its off-path plans (third option); off-path plans affect incentives but never the payoffs actually received (fourth option).
> Ref: Tadelis (2013), §7.3 (pp. 145–146) and §8.2 (pp. 153–159); Lecture 4 slide 13
> Similar: Simulados/quiz-lecture03-1-extensive-form-2026-10-25, section nfpath
