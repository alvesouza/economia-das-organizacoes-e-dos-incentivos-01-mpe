---
quiz: "Topic T8 · Backward induction and subgame perfection — hard conceptual quiz (10 questions; Lectures 3–4, Tadelis Ch. 8, Brexit case)"
tags:
  count: "Counting proper subgames"
  nash: "Why Nash equilibrium is not enough"
  spe: "Subgame perfection: construction, existence and limits"
---

## count

Q: In the Lecture 4 Brexit game, with Parliament's vote replaced by expected payoffs, the UK prepares or not, the EU makes one of three offers, and the UK accepts or rejects. The game has 9 proper subgames when the EU sees whether the UK prepared. How many does it have if the EU cannot see it?
- Nine still, since what the EU can see changes its information but not the nodes of the tree, and every decision node still starts a subgame
- Three, the whole game and one at each of the EU's two offer nodes, since the UK's reply nodes now share information sets across branches
- One, the whole game, since once a single information set joins nodes from both branches, no node below the root can start a subgame
- Seven, the whole game and one at each of the UK's six reply nodes, since the EU's two offer nodes now share an information set and start none
<!-- YW5zOjM= -->
> A proper subgame starts at a node whose information set is a singleton and must not cut any information set. Hiding preparation merges the EU's two offer nodes into one information set, so neither starts a subgame. The UK still knows whether it prepared and sees the offer, so each of its six reply nodes is a singleton whose successors are terminal: six subgames, plus the whole game, makes seven, the count the case uses for this variant. The third option over-applies the "no cutting" rule, which only bars subgames whose successors share a set with nodes outside them; the second gets the merge the wrong way round.
> Ref: Lecture 4 slides 14–18; Cases/Brexit/brexit-game.pdf, "The unobservable variant: commitment must be seen"; Tadelis (2013), Def. 8.2 (pp. 154–155)
> Similar: Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25, section subg

Q: A finite game of perfect information without moves of Nature has $n$ decision nodes. How many proper subgames does it have, and what follows for subgame perfection?
- $n$ plus the number of terminal nodes, since every node starts a subgame, so subgame perfection adds conditions at terminal nodes that backward induction ignores
- Exactly $n$, one at each decision node, so a Nash equilibrium in every subgame means optimal play at every node, which is what backward induction does
- Only one, the whole game, since a subgame must contain every successor of its root, so subgame perfection adds nothing to Nash in such games
- Exactly $n$, but subgame perfection can still differ from backward induction, since a subgame's own equilibria may rest on threats at its later nodes
<!-- YW5zOjE= -->
> With perfect information every decision node is a singleton information set, and no information set can be cut, so each decision node starts a proper subgame: $n$ of them, the whole game included, as in the slides' counts. Requiring a Nash equilibrium in the subgame that starts at a node where only one player moves means her action there is optimal given what follows; doing this at every node is backward induction, hence the Fact that the two coincide. Terminal nodes involve no choices (first option). The fourth option fails because each later node is itself a subgame, so a threat there is already tested.
> Ref: Tadelis (2013), Def. 8.2 (pp. 154–155) and the Fact (p. 157); Lecture 3 slides 32–35; Lecture 4 slides 16–17
> Similar: Listas/pratica-lecture-03 #8 (Tadelis 7.4, Centipedes)

## nash

Q: A Nash equilibrium strategy of a finite extensive-form game prescribes, at one of the player's information sets, an action that is not optimal there given the others' strategies. What must be true of that information set?
- It is reached with probability zero under the equilibrium profile, since at a set reached with positive probability a better action raises her payoff
- It is reached with positive probability, but the loss there is offset by gains elsewhere in the tree, since Nash asks only for overall optimality
- It does not start a proper subgame, since at sets that start subgames a Nash equilibrium already requires optimal play by its very definition
- It belongs to the last mover, since earlier movers are disciplined by the replies their actions trigger, while the last mover faces no reply at all
<!-- YW5zOjA= -->
> If the set is reached with positive probability, switching to a better action there, and keeping everything else fixed, raises the player's expected payoff by that probability times the gain, contradicting Nash. If it is reached with probability zero, the switch changes nothing, so Nash cannot rule the suboptimal action out: "Nash equilibrium only requires optimal behavior on the equilibrium path." Continuations after different actions at a set are disjoint, so no offsetting is possible (second option). The entry game's (Out, Fight) shows a suboptimal action at a node that starts a subgame (third option), and in a longer tree the culprit can be an early mover off the path (fourth option).
> Ref: Lecture 4 slide 13; Tadelis (2013), §7.3 (pp. 145–146) and §8.1 (pp. 152–153)
> Similar: Listas/pratica-lecture-04 #1 (Tadelis 8.8)

Q: In the Brexit strategic form, (DF, FF) is a Nash equilibrium: the UK does not prepare and accepts only a favourable deal, and the EU always offers the favourable deal. Which statement about it is correct?
- It is subgame perfect, since the UK never faces an unfavourable offer, and a threat that is never tested places no constraint on play in any subgame
- It is not a Nash equilibrium, since the EU would rather offer the unfavourable deal to an unprepared UK, which then accepts it with probability one
- Its threat is never tested, so DF and DU tie in that column; DU weakly dominates DF, and the threat fails in the subgame after an unfavourable offer
- It gives the UK less than the subgame-perfect equilibrium does, which is why the UK prefers to prepare and so leaves this equilibrium in the end
<!-- YW5zOjI= -->
> Against FF the unfavourable offer is never made, so the UK's rule "accept only F" (DF) and "accept anything" (DU) earn the same, and Nash cannot tell them apart. Row by row, DU is never worse than DF and is strictly better in every column where the EU offers U or N to an unprepared UK, so DF is weakly dominated. In the subgame after "no preparation, unfavourable offer", accepting gives $-28.6$ against $-35$ for rejecting, so (DF, FF) is not subgame perfect. Given DF, offering U to an unprepared UK gets it rejected ($-18$ for the EU against $-14$ from F), so the EU's FF is a best reply (second option). The UK gets $-22.2$ here, more than $-24.7$ in the SPE, so the fourth option has the comparison backwards.
> Ref: Lecture 4 slides 7–8 and 18; Cases/Brexit/brexit-game.pdf, "A Nash equilibrium that is not subgame perfect"
> Similar: Listas/pratica-lecture-04 #10 (Tadelis 8.7)

Q: A Nash equilibrium of a finite game fails to be subgame perfect. Must its path of play differ from the path of every subgame-perfect equilibrium?
- Yes, since a strategy that is not sequentially rational somewhere must change the actions that are taken along the path of play of the game
- No, since its faulty plan may sit off the path and deter no one, so its path and payoffs can match those of a subgame-perfect equilibrium
- Yes, since subgame perfection selects paths rather than strategies, so two profiles with the same path are either both perfect or neither is
- No, but only in games with payoff ties, since with generic payoffs a non-credible plan always changes what some earlier mover chooses
<!-- YW5zOjE= -->
> Take player 1 choosing L, which ends the game with payoffs $(3,1)$, or R, after which player 2 chooses x, giving $(0,0)$, or y, giving $(2,2)$. Both (L, x) and (L, y) are Nash equilibria with the path L; only (L, y) is subgame perfect, because x is not optimal in the subgame after R. Player 2's bad plan deters nothing, since player 1 prefers L anyway. The payoffs are generic, so the fourth option fails, and subgame perfection is a property of whole strategy profiles, not of paths, so the first and third fail.
> Ref: Tadelis (2013), §8.2 (pp. 153–159); Lecture 4 slides 13 and 17
> Similar: Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25, section spe

## spe

Q: Player 1 can take Out, ending the game with payoff $c$ to her, $0<c<1$, or In, after which both play Matching Pennies with payoffs 1 and $-1$, player 1 winning on a match. Which profile is a subgame-perfect equilibrium?
- In, followed by player 1 matching player 2's more likely action, since a first mover who enters can secure more than $c$ by best-replying to it
- Out, with no play specified after In, since that subgame is never reached and so the strategies there do not enter any payoff of the game
- Out, with player 2 playing Heads for sure after In, since that threat makes In unattractive and player 2 loses nothing by carrying it out
- Out, with each player mixing evenly after In, since the only equilibrium of that subgame gives player 1 an expected payoff of 0, below $c$
<!-- YW5zOjM= -->
> Subgame perfection requires a Nash equilibrium in the subgame after In even though it is off the path, and Matching Pennies has only the even mix, worth 0 to player 1. Since $c>0$, she takes Out. A strategy must state play after In (second option); player 2 playing Heads for sure is not an equilibrium of that subgame, since player 1 would match and player 2 would then switch (third option); and entering earns 0 in equilibrium, not more than $c$ (first option). This is why the definition of subgame perfection uses behavioral strategies: the off-path subgame may need mixing.
> Ref: Tadelis (2013), Def. 8.3 (p. 157), §6.2.1 (pp. 108–111); Lecture 3 slide 34
> Similar: Simulados/quiz-lecture03-2-backward-induction-spe-2026-10-25, section spe

Q: A game ends with a simultaneous-move subgame after each first-stage outcome, and each of these subgames has several Nash equilibria. How does backward induction over subgames proceed?
- It branches: any selection of one equilibrium per subgame, which may differ across first-stage outcomes, gives an SPE once stage 1 best-responds
- It must select the same equilibrium in every subgame, since a subgame-perfect profile cannot let its choice of equilibrium depend on what happened before
- It stops, since backward induction needs a unique optimal choice at every step and has no way to continue once a subgame has several equilibria
- It keeps only the Pareto-efficient equilibrium of each subgame, since rational players who reach a subgame coordinate on the one that is best for both
<!-- YW5zOjA= -->
> MWG's generalized backward induction: replace each final subgame by the payoffs of one of its Nash equilibria, solve the reduced game, and repeat; the set of all SPE comes from running this for every possible selection. The selection may differ across histories, and that dependence is exactly what a carrot and a stick exploit: a good equilibrium after the target outcome and a bad one after a deviation. Nothing forces the same selection (second option) or Pareto efficiency (fourth option), and multiplicity makes the procedure branch rather than stop (third option).
> Ref: MWG §9.B, Prop. 9.B.3 (pp. 274–277); Tadelis (2013), §9.4 (pp. 180–184); Lecture 5 slides 11–13
> Similar: Listas/pratica-lecture-05 #17 (Tadelis 9.1)

Q: Nature makes an entrant competitive or weak; the entrant, who knows its type, enters or stays out; the incumbent sees entry but not the type, and accommodating beats fighting at both of its nodes. Why is "both types stay out, the incumbent fights" subgame perfect?
- Because fighting becomes a credible threat once the incumbent weighs the two types by the prior, and against a weak entrant fighting earns it more
- Because subgame perfection asks each player to best-respond only at sets reached with positive probability, and here entry never happens
- Because the only proper subgame is the whole game, as the incumbent's information set spans both types, so subgame perfection reduces to Nash
- Because the incumbent's two nodes become singletons once entry is observed, so each starts a subgame in which fighting is a best reply
<!-- YW5zOjI= -->
> In Tadelis's example the incumbent gets 1 from accommodating and $-1$ from fighting a competitive entrant, and 1 against 0 against a weak one, so fighting is worse at both nodes, whatever the incumbent believes. Yet its information set after entry contains a node of each type, so no node below Nature's root starts a subgame, and the only restriction is Nash in the whole game: with both types out, the incumbent's set is never reached and fighting deters entry. The second option is the definition of Nash, not of subgame perfection; the fourth misreads the information set. This failure is the motivation for perfect Bayesian equilibrium.
> Ref: Tadelis (2013), §15.1, Figs. 15.1–15.2 (pp. 303–306); Lecture 4 slide 15
> Similar: Listas/pratica-lecture-08 #2 (Gibbons 4.1)

Q: Why does every finite extensive-form game have a subgame-perfect equilibrium, possibly in behavioral strategies that mix?
- Each minimal subgame is a finite game and so has a Nash equilibrium by Nash's theorem; replace it by those payoffs and repeat until the root
- Zermelo's theorem extends to every finite game, so backward induction always gives a pure profile that is optimal at every information set
- Every Nash equilibrium of a finite game is subgame perfect once mixed strategies are allowed, so existence follows at once from Nash's theorem
- The subgame-perfect profiles are the intersection of finitely many nonempty sets of Nash equilibria, which is nonempty by compactness alone
<!-- YW5zOjA= -->
> A minimal subgame contains no smaller one, and as a finite game it has a Nash equilibrium, possibly mixed. Replacing it by that equilibrium's payoffs gives a smaller finite game; repeating reaches the root after finitely many steps, and the pieces form a behavioral profile that is a Nash equilibrium in every subgame. A pure SPE need not exist, since a Matching Pennies subgame has no pure equilibrium (second option); the entry game's (Out, Fight) is a Nash equilibrium that is not subgame perfect (third option); and an intersection of nonempty sets can be empty, so compactness alone proves nothing (fourth option).
> Ref: Tadelis (2013), §8.2 (pp. 157–159) and §6.4 (p. 117); MWG §9.B, Prop. 9.B.3 (pp. 274–277)
> Similar: Listas/pratica-lecture-03 #16 (MWG 9.B.4)

Q: In the Brexit SPE the UK prepares, yet its strategy also says what it would do had it not prepared: accept any deal. Why must the equilibrium specify this plan for a node that is never reached?
- Because the EU needs it to choose its offer after preparation, since the EU compares the deal it offers with what an unprepared UK would accept
- Because Nash equilibrium requires a best reply at every node, and the UK's plan at unreached nodes enters its payoff through the chance of an error
- Because Parliament's vote may fail, so the node after no preparation is reached with positive probability and the plan there affects the payoffs
- Because the value of not preparing, which the UK compares with preparing at the first node, is computed from that plan and the EU's reply to it
<!-- YW5zOjM= -->
> At the root the UK compares $-24.7$ from preparing with $-28.6$ from not preparing, and the second number is built from the off-path plan: an unprepared UK accepts any deal, so the EU offers the unfavourable one. Without that plan the choice to prepare cannot be justified, and subgame perfection requires the plan to be optimal in the subgames it covers. The EU's offer after preparation depends on what a prepared UK would accept (first option); Nash does not require optimality off the path (second option); and Parliament votes after a deal is accepted, so it cannot reach the no-preparation branch (third option).
> Ref: Lecture 4 slides 9–10; Cases/Brexit/brexit-game.pdf, section (vi), backward induction in three steps
> Similar: Cases/Brexit/brexit-game.pdf, "Sensitivity"
