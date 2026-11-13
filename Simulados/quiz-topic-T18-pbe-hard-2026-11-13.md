---
quiz: "Topic T18 · Perfect Bayesian equilibrium — hard conceptual quiz (10 questions; estimated unit, no slides: Tadelis Ch. 15, Gibbons §4.1, MWG §9.C)"
tags:
  sp: "Why subgame perfection is not enough"
  beliefs: "Beliefs on and off the path"
  pbe: "Sequential rationality and what a PBE is"
  se: "Consistency and sequential equilibrium"
---

## sp

Q: Player 1 moves first; player 2 then moves at an information set with two nodes, one for each of player 1's possible earlier actions, and player 2's best action depends on which node he is at. Why can neither backward induction nor a belief computed in advance settle player 2's choice on its own?
- Because player 2 must take the same action at both nodes of the set, so his best action is undefined until a tie-breaking rule is added to the game
- Because the information set starts a proper subgame of its own, whose Nash equilibria can be found only once player 1's payoffs at the root are fixed
- Because his best action depends on his belief, the belief depends on player 1's strategy through Bayes' rule, and that strategy depends on his reply
- Because the belief at a two-node information set equals the prior over player 1's actions, which the game does not specify, so the analyst must assume one
<!-- YW5zOjI= -->
> Backward induction needs to know what player 2 does at each node, but player 2 cannot tell the nodes apart, so his choice must be optimal against a belief. On the path that belief is pinned by Bayes' rule from player 1's strategy, and player 1's strategy is a best reply to player 2's action: strategies and beliefs are determined jointly, as a fixed point, which is what a PBE is. Taking one action at both nodes is a constraint, not a source of indeterminacy. A non-singleton information set cannot start a proper subgame, which is exactly why subgame perfection is silent here. There is no exogenous prior over player 1's actions: the belief is endogenous.
> Ref: Tadelis (2013), §15.1 (pp. 303–307) and §15.2, Requirements 15.1–15.4 (pp. 307–310); Gibbons (1992), §4.1 (pp. 175–179)
> Similar: Gibbons (1992), Problem 4.1, p. 245

Q: In a finite game of perfect information, how are perfect Bayesian equilibrium and subgame perfect equilibrium related?
- They coincide: every information set is a singleton, so beliefs are trivial and sequential rationality at every node is exactly backward induction
- PBE is stricter: it adds the requirement that each player's beliefs follow Bayes' rule, which removes some subgame perfect equilibria of such games
- PBE is weaker: with no move by Nature it reduces to Nash equilibrium, since Bayes' rule has nothing to update and off-path play is unrestricted
- They are unrelated: PBE is defined only for games whose types are drawn by Nature, so it does not apply to games of perfect information at all
<!-- YW5zOjA= -->
> With singleton information sets each belief puts probability one on the only node, so Bayes' rule has no work to do, and sequential rationality asks for optimal play at every node, on or off the path: that is subgame perfection, found by backward induction. Bayes' rule cannot remove anything when beliefs are degenerate. Sequential rationality off the path is exactly what Nash equilibrium lacks, so PBE does not collapse to it. PBE is defined for any extensive form; Nature is not required (Gibbons's first example has none).
> Ref: Tadelis (2013), §15.2, Requirement 15.4 (p. 310); Gibbons (1992), §4.1 (pp. 177–182); MWG (1995), §9.C, Defs. 9.C.1–9.C.3 (pp. 283–285)
> Similar: Gibbons (1992), Problem 4.1, p. 245

Q: In a three-player game, player 1 ends the game with $A$ or plays $D$; after $D$, player 2 chooses $L$ or $R$, and player 3, who does not see that choice, picks $L'$ or $R'$. The unique Nash equilibrium of the subgame after $D$ is $(L, R')$, yet $(A, L, L')$, with player 3 believing $R$ was played, is a Nash equilibrium meeting Bayes' rule on the path and sequential rationality given beliefs. What is wrong with it?
- Player 1's action $A$ is strictly dominated, so any profile in which player 1 ends the game at once fails to be a Nash equilibrium of the whole game
- Player 3's action $L'$ is not a best reply to any belief, so the profile breaks sequential rationality at player 3's information set
- Player 3's information set is on the path, so the belief must follow Bayes' rule from player 1's strategy, which forces it to equal the prior
- Player 3's belief contradicts player 2's strategy $L$ in the part of the tree off the path; Bayes' rule where possible forces belief on $L$, then $R'$
<!-- YW5zOjM= -->
> This is Gibbons's Fig. 4.1.4. Player 3's information set is reached only if player 1 deviates, so Bayes' rule on the path does not constrain the belief; but once there, player 2's strategy $L$ still gives the odds, and Gibbons's Requirement 4 (Bayes' rule "where possible" off the path) forces the belief to put probability one on $L$, under which player 3 must play $R'$. Without it the profile satisfies Requirements 1–3 and is not even subgame perfect. $A$ is not dominated (it is a best reply to $(L, L')$); $L'$ is a best reply to the belief on $R$, which is how the profile passes sequential rationality; and the set is off the path, not on it.
> Ref: Gibbons (1992), §4.1, Requirement 4 and Fig. 4.1.4 (pp. 180–181); Tadelis (2013), Remark and Fig. 15.3 (pp. 311–312); MWG (1995), Prop. 9.C.2 (p. 291)
> Similar: Gibbons (1992), Problem 4.2, pp. 245–246

## beliefs

Q: Type $t_1$, with prior 1/2, never sends message $m$, while type $t_2$, with prior 1/2, sends $m$ with probability 1/10. What do the PBE requirements say about the receiver's belief after $m$?
- $m$ is reached with probability only 1/20, which counts as off the path, so the belief after $m$ is free and can be chosen to support any reply
- $m$ is on the path, reached with probability 1/20, so Bayes' rule applies and puts probability 1 on $t_2$, however rarely $m$ is sent
- $m$ is on the path, so Bayes' rule applies, but since $t_2$ sends it only one time in ten, the belief on $t_2$ after $m$ is 1/10
- $m$ is on the path, so Bayes' rule applies, and as the two types are equally likely a priori, the belief on $t_2$ after $m$ stays 1/2
<!-- YW5zOjE= -->
> An information set is on the path if it is reached with positive probability, however small: here $\Pr\{m\} = \tfrac12 \cdot 0 + \tfrac12 \cdot \tfrac1{10} = \tfrac1{20} > 0$. Bayes' rule then gives $\mu(t_2 \mid m) = (1/20)/(1/20) = 1$: only $t_2$ ever sends $m$. Freedom of beliefs arises only at probability zero. The value 1/10 confuses the likelihood $\Pr\{m \mid t_2\}$ with the posterior, and 1/2 is the prior, which would be the posterior only if both types sent $m$ equally often.
> Ref: Tadelis (2013), §15.2, Def. 15.1 (p. 307) and Requirement 15.2 (p. 309)
> Similar: Tadelis (2013), Exercise 15.3, pp. 315–316

Q: In a candidate equilibrium player 1 ends the game at once, so the rest of the tree is off the path. Had player 1 continued, player 2 would play $L$ with probability 0.2, $R$ with probability 0.6 and end the game with probability 0.2; player 3, who moves after $L$ or $R$ without seeing which, must hold a belief $p$ that $L$ was played. What does Bayes' rule where possible prescribe?
- $p = 1/4$, the share of $L$ among the moves that reach player 3, because only player 1 deviated and player 2's strategy still gives the odds
- $p = 0.2$, the probability with which player 2 plays $L$, because Bayes' rule uses player 2's strategy as it stands, with no renormalising
- $p$ is free, because player 3's set is off the path and Bayes' rule is never possible at an information set reached with zero probability
- $p = 1/2$, because with player 3's set off the path the only defensible belief treats both moves of player 2 that reach it as equally likely
<!-- YW5zOjA= -->
> Conditional on reaching player 3, player 2 played $L$ or $R$, so $p = 0.2/(0.2+0.6) = 1/4$ (Gibbons's Fig. 4.1.5, $p = q_1/(q_1+q_2)$). Only player 1 has deviated; nothing suggests that player 2 deviated too. Using 0.2 forgets to condition on the event that player 3 moves. Under Tadelis's definition (the "weak" PBE) the belief would indeed be free, but the claim that Bayes' rule is never possible off the path is false: it is possible whenever the moves after the deviation are played with positive probability. Equal weights have no basis in player 2's strategy.
> Ref: Gibbons (1992), §4.1, Requirement 4 and Fig. 4.1.5 (pp. 180–182); Tadelis (2013), Remark and Fig. 15.3 (pp. 311–312)
> Similar: Gibbons (1992), Problem 4.2, pp. 245–246

Q: To test a pooling PBE, a student checks whether the high type gains by switching to an unused message and argues: "only the high type would want this message, so the receiver will believe it comes from the high type, and the deviation pays." Under the PBE definition alone, what is wrong with this step?
- Nothing: PBE requires the receiver to update by Bayes' rule after any message that a type has a reason to send, so the belief after the deviation must be the high type
- The belief after the unused message must equal the prior, since the deviation is a zero-probability event and the receiver has no data on which to update
- The belief after the unused message is part of the candidate equilibrium and stays fixed when a deviation is checked; reasoning about who deviates is a refinement
- The student should instead assume the worst belief for the deviator, because PBE requires off-path beliefs to make every deviation as unattractive as possible
<!-- YW5zOjI= -->
> A PBE is a profile plus a belief system; checking it means asking whether any type gains by a unilateral deviation given the receiver's strategy, which is a best reply to the given beliefs. At an unused message Bayes' rule is silent and any belief is allowed, so the student's belief is one admissible choice among many, not an implication. Arguing that a deviation must come from the type that could gain is forward induction, the intuitive criterion of Cho and Kreps. Equating off-path beliefs with the prior is the classic error. Pessimistic beliefs are a convenient device for constructing equilibria, not a requirement.
> Ref: Tadelis (2013), §15.2, Requirements 15.3–15.4 (p. 310) and §16.3 (pp. 332–334); Gibbons (1992), §4.4 (pp. 233–239)
> Similar: Tadelis (2013), Exercise 16.7, p. 338

## pbe

Q: In a candidate semi-separating PBE of a two-type signaling game, the high type always sends $m$, the low type sends $m$ with probability $\pi \in (0,1)$ and $m'$ otherwise, and the receiver's best reply after $m$ depends on its belief. Which set of conditions pins the equilibrium down?
- The high type must be indifferent between $m$ and $m'$, and the receiver's belief after $m$ must be the prior, since a message both types send is uninformative
- The low type must strictly prefer $m$, and the belief after $m'$ is free, since $m'$ is sent by one type only and so lies off the equilibrium path
- The receiver must play a pure reply after $m$, and $\pi$ is set so that the belief after $m$ is one half, which makes the receiver's two replies equally good
- The low type must be indifferent between $m$ and $m'$, the belief after $m$ must follow Bayes' rule given $\pi$, and the reply, often mixed, is optimal at it
<!-- YW5zOjM= -->
> A type that mixes must be indifferent between the messages it uses, so the condition is on the low type. Both messages are on the path: Bayes' rule gives $\mu(\text{high} \mid m) = p/[p + (1-p)\pi]$ and $\mu(\text{high} \mid m') = 0$. The receiver must best-respond to that belief, and to make the low type indifferent it is often itself mixing, which requires the belief to sit exactly at its indifference threshold, a threshold set by its payoffs and not, in general, at one half. A message sent by both types is informative when they send it with different probabilities; and $m'$ is sent with probability $(1-p)(1-\pi) > 0$, so it is on the path.
> Ref: Gibbons (1992), §4.2.B, hybrid equilibria, eqs. 4.2.8–4.2.10 (pp. 202–205); Tadelis (2013), §15.2 (pp. 308–310)
> Similar: Gibbons (1992), Problem 4.2, pp. 245–246; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 5

Q: Two analysts report the same pooling strategy profile of a signaling game as a PBE. The receiver's prescribed reply to the unused message is optimal only for beliefs on the high type below 0.4. One analyst supports it with the belief 0.2 on the high type, the other with 0.6. Which statement is correct?
- Both are PBE, because the unused message is off the path and any belief is allowed there, so the two analysts just picked different free beliefs
- Only the first is a PBE: a PBE is a profile together with beliefs, and the second pair fails sequential rationality at the unused message
- Neither is a PBE, because at an unused message the belief must equal the prior, and an equilibrium may not rest on a belief chosen freely
- Only the second is a PBE, because the high type is the one with a reason to deviate, so a belief tilted toward it is the one PBE requires
<!-- YW5zOjE= -->
> Off the path the belief is free, but the reply must still be a best reply to it. With belief 0.2 the prescribed reply is optimal; with 0.6 it is not, so the second strategy–belief pair violates sequential rationality and is not a PBE, even though the strategies are the same. That is why stating a PBE means stating the beliefs: in Tadelis's MBA game the same pooling strategies are a PBE with $\mu_D \le 3/8$ and not with $\mu_D = 0.9$. Requiring the prior off the path is the classic error, and tilting the belief toward the type that gains is a refinement, not part of PBE.
> Ref: Tadelis (2013), §15.2, Def. 15.3 and Requirements 15.3–15.4 (pp. 308–310); §16.1, the MBA pooling equilibrium (pp. 321–323)
> Similar: Tadelis (2013), Exercise 15.5, pp. 316–317

Q: Which property does sequential rationality give a perfect Bayesian equilibrium that a Bayesian Nash equilibrium need not have?
- No player uses a weakly dominated strategy, so in a second-price auction PBE leaves bidding one's value as the only equilibrium of the game
- Every player's belief at every information set off the path equals the prior, which rules out the equilibria sustained by pessimistic beliefs
- No player uses a strategy that is strictly dominated from some information set onward, including information sets the equilibrium never reaches
- The equilibrium is unique in every finite signaling game, because sequential rationality leaves the receiver one best reply at each information set
<!-- YW5zOjI= -->
> Gibbons states it directly: Requirements 1–2 are equivalent to insisting that no player's strategy be strictly dominated beginning at any information set. A BNE can prescribe such play at unreached information sets because there it costs nothing ex ante; Tadelis's Prop. 15.1 shows that this is the only place where BNE and PBE can differ. PBE does not remove weakly dominated strategies: in a simultaneous-move auction it adds nothing to BNE, and the low-value bidder's bid of 100 in a complete-information second-price auction survives. Off-path beliefs are free, not the prior, and signaling games typically have continua of PBE.
> Ref: Gibbons (1992), §4.1 (p. 182); Tadelis (2013), §15.2, Prop. 15.1 (p. 311)
> Similar: Tadelis (2013), Exercise 15.1, p. 314

## se

Q: In a two-type signaling game with prior 1/2 on each type, a pooling PBE supports the unused message with the belief 0.9 on the low type. Does Kreps–Wilson consistency rule this belief out?
- No: the two types can tremble toward the unused message at different rates, say the low type nine times as often, so any belief there is a limit of Bayes' rule
- Yes: trembles are mistakes and so must be equally likely for both types, which pins the belief at the unused message to the prior of one half on each type
- Yes: consistency requires beliefs to be limits of totally mixed strategies, and a belief as extreme as 0.9 can only arise if one type sends the message on purpose
- No, but only because the receiver may also tremble, and the receiver's trembles at the unused message can be chosen to justify any belief that it holds there
<!-- YW5zOjA= -->
> Each type is a separate decision point of the sender, so its tremble can differ: if the low type sends the message with probability $9\varepsilon$ and the high type with $\varepsilon$, Bayes' rule gives $\tfrac12 \cdot 9\varepsilon / (\tfrac12 \cdot 9\varepsilon + \tfrac12\varepsilon) = 0.9$ for every $\varepsilon$, and the limit is 0.9. So in a signaling game consistency does not restrict beliefs after unused messages, and PBE and sequential equilibrium coincide. Contrast Tadelis's Fig. 15.4, where one player who does not observe Nature trembles once, so the odds between the nodes cannot move. Trembles need not be equal across types, and the receiver's own trembles occur after the message, so they cannot affect the belief about who sent it.
> Ref: Tadelis (2013), §15.3, Fig. 15.4 and Defs. 15.4–15.5 (pp. 312–313); MWG (1995), §9.C, Def. 9.C.4 (p. 290) and §13.C (pp. 450–452)
> Similar: Tadelis (2013), Exercise 15.6, p. 317
