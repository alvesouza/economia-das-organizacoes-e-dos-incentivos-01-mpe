---
quiz: "Lecture 3 · Quiz 2 of 3 — Backward induction, subgames and subgame-perfect equilibrium (estimated before the lecture: no slides yet, follows Tadelis Ch. 8)"
tags:
  bi: "Sequential rationality and backward induction"
  subg: "Proper subgames"
  spe: "Subgame-perfect equilibrium: branching, multiplicity, outcome vs equilibrium"
---

## bi

Q: A finite game of perfect information has two terminal nodes that give player 1 the same payoff, and no other ties. What can be said about its backward-induction solution?
- It is never unique, since an indifferent mover can pick either action and either pick changes what the earlier movers choose
- It may still be unique, since the tie matters only if player 1 must compare exactly those two payoffs at one of her nodes
- It may fail to exist, since backward induction needs a strict best action at every node and the tie leaves one node open
- It is unique, since Zermelo's theorem needs only finiteness and perfect information, and ties affect only mixed equilibria
<!-- YW5zOjE= -->
> Proposition 8.1 gives existence for every finite game of perfect information, and uniqueness when no player has equal payoffs at two terminal nodes. That condition is sufficient, not necessary: if the tied payoffs are never the deciding comparison at any of player 1's nodes (for instance, both lie below a node of player 2, or one is dominated earlier), the solution is still unique. Existence never fails, since an indifferent mover can simply pick either action; ties only open the door to several solutions.
> Ref: Tadelis (2013), Prop. 8.1 and Cor. 8.1, footnote 1 (p. 153); MWG Prop. 9.B.1 (§9.B, pp. 272–273)
> Similar: MWG Exercise 9.B.4, p. 302; Tadelis (2013), Exercise 8.11, pp. 172–173

Q: Player 1 stops, giving $(s, s)$, or continues; player 2 then stops, giving $(s-\ell, s+h)$, or continues, giving $(s+g, s+g)$, with $s, g, h, \ell > 0$ and player 1's payoff first. When does backward induction reach $(s+g, s+g)$?
- Iff $g > h + \ell$, since player 2's gain from going on must cover her own temptation and player 1's loss
- Iff $g > \ell$, since player 1 goes on only when the end pays more than she loses if player 2 stops
- Iff $h < \ell$, since player 2 goes on when her gain from stopping is below the loss it imposes on player 1
- Iff $g > h$, since player 2 then goes on and player 1 gets $s+g > s$; the size of $\ell$ plays no role at all
<!-- YW5zOjM= -->
> Start at the last node: player 2 compares $s+h$ from stopping with $s+g$ from continuing, so she continues iff $g > h$. If she continues, player 1 compares $s$ with $s+g$ and continues. If she would stop, player 1 compares $s$ with $s-\ell$ and stops, whatever $\ell > 0$ is. So $\ell$ never decides anything; only the last mover's comparison does. The Centipede game makes $h > g$ at every node, which is why it unravels to the first stop.
> Ref: Tadelis (2013), §8.1 (pp. 152–153), the Centipede Game §8.3.1 (pp. 159–160); Gibbons (1992), §2.1.A (pp. 57–58)
> Similar: Tadelis (2013), Exercise 7.4, p. 148; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 9, pp. 176–177

Q: In Gibbons's three-move game, player 1 can end the game at once with $L$; backward induction says she does. What does the argument assume about how player 2 would read a move $R$ that, by the argument itself, should never happen?
- That player 2 still expects player 1 to act rationally at the last stage, though $R$ shows rationality is not common knowledge
- That player 2 treats $R$ as a pure mistake and so expects player 1 to randomize evenly between her two actions at the last stage
- That player 2 reads $R$ as a sign that player 1 will play $R''$ at the last stage, so she moves to the end of the tree herself
- Nothing at all, since backward induction compares only the payoffs at nodes after $R$ and never needs a belief about the mover
<!-- YW5zOjA= -->
> Player 2 chooses $L'$ because she expects player 1 to take $L''$ at the last node. If player 1 has just played $R$, that expectation requires player 2 to keep believing player 1 is rational at stage 3, although $R$ shows that common knowledge of rationality has failed. Gibbons's point is that the argument assumes deviations are explained in a way consistent with later rationality (for instance, player 1 doubting player 2's rationality); where a deviator is more plausibly irrational, backward induction loses appeal.
> Ref: Gibbons (1992), §2.1.A (pp. 59–61); Tadelis (2013), Remark on the Centipede evidence (p. 160)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 9, pp. 176–177

Q: Player 1 trusts ($T$) or not ($N$, payoffs $(0,0)$). After $T$, player 2 cooperates, giving $(r, r)$, or defects, giving $(-s, r+t)$, with $r, s, t > 0$ and player 1's payoff first; defecting also costs player 2 a guilt term $\gamma \ge 0$. For which $\gamma$ does the subgame-perfect equilibrium have player 1 trusting?
- $\gamma > t + s$, since player 2's guilt must offset both her own gain from defecting and the loss she imposes on player 1
- $\gamma > r + t$, since player 2's guilt must offset the whole payoff she would collect by defecting after she is trusted
- $\gamma > t$, since player 2 then cooperates after trust, and player 1, anticipating $r > 0$, prefers trusting to $N$
- $\gamma > s$, since player 1 trusts only when player 2's guilt is at least as large as the loss she would suffer
<!-- YW5zOjI= -->
> After $T$, player 2 compares $r$ from cooperating with $r + t - \gamma$ from defecting, so she cooperates iff $\gamma > t$. Player 1 then compares $r > 0$ from $T$ with $0$ from $N$ and trusts. Player 1's loss $s$ enters only player 1's payoff, which player 2 does not weigh; and only the gain $t$ over cooperation matters to player 2, not the level $r + t$. With $\gamma = 0$, the trust game unravels to $(0, 0)$ although both prefer $(r, r)$.
> Ref: Tadelis (2013), trust game Fig. 7.1 (p. 132), §8.1 (pp. 152–153)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 4 Ex. 10, p. 177

## subg

Q: A decision node $x$ is a singleton information set. What else must hold for $x$ to start a proper subgame?
- $x$ must be on the equilibrium path, since a subgame that is never reached imposes no restriction on the strategies
- Every information set containing a successor of $x$ must lie entirely among the successors of $x$, so no set is cut
- Every successor of $x$ must also be a singleton information set, so that the subgame is one of perfect information
- $x$ must belong to the player who moves at the root, so the subgame starts with the same mover as the whole game
<!-- YW5zOjE= -->
> Definition 8.2: a proper subgame is a node and all its successors, closed under information sets: if $x' \in G$ and $x'' \in h(x')$ then $x'' \in G$. In the card game, player 1's nodes are singletons, but each subtree contains one of player 2's nodes whose information set also contains a node in the other subtree, so neither starts a subgame. Successors may share information sets (the simultaneous war stage of mutually assured destruction is a subgame), and subgames off the path are exactly the ones subgame perfection is designed to test.
> Ref: Tadelis (2013), Def. 8.2 (pp. 154–155), card game Fig. 8.5 (p. 156); Gibbons (1992), §2.4.B (pp. 122–124)
> Similar: Tadelis (2013), Exercise 8.5, p. 170

Q: Player 1 chooses one of $m \ge 2$ actions; player 2 observes it and chooses one of $k$ actions; player 3 then observes player 2's action but not player 1's, and moves. Counting the whole game, how many proper subgames are there?
- $1$, since any subgame below the root would cut one of player 3's information sets, which span all of player 1's branches
- $1 + m$, the whole game plus one subgame at each of player 2's nodes, which are singletons that have seen player 1's move
- $1 + m + mk$, the whole game plus one subgame at each decision node, since every later player observes someone's move
- $1 + mk$, the whole game plus one subgame at each of player 3's nodes, which follow a fully observed move of player 2
<!-- YW5zOjA= -->
> Player 3's information set after action $a_2$ contains the $m$ nodes $(a_1, a_2)$, one in each of player 1's branches. A subgame at player 2's node after $a_1$ would contain $(a_1, a_2)$ but not $(a_1', a_2)$, which is in the same information set, so it cuts that set and is not a subgame. Player 3's nodes are not singletons, so they cannot be roots either. Only the whole game remains, and subgame perfection reduces to Nash equilibrium here. If player 3 observed both earlier moves the count would be $1 + m + mk$.
> Ref: Tadelis (2013), Def. 8.2 (pp. 154–156); MWG Def. 9.B.1 (§9.B, pp. 274–275)
> Similar: Tadelis (2013), Exercise 8.4, p. 170; MWG Exercise 9.B.5, p. 302

## spe

Q: Player 1 chooses $N$, ending the game with payoff $w$ to her, or $Y$, after which both play the simultaneous Battle of the Sexes: $(O, o)$ pays $(a, b)$, $(F, f)$ pays $(b, a)$, mismatches pay $(0, 0)$, player 1's payoff first and $a > b > 0$. Player 1's strategy lists her action at the root, then in the subgame. If $w > a$, what are the pure-strategy SPE?
- $(NO, o)$, $(NO, f)$, $(NF, o)$ and $(NF, f)$, since $Y$ is never chosen and so the plan after $Y$ is never put to a test
- $(NF, f)$ only, since player 1 opts out and the subgame equilibrium player 2 prefers is the one carried up the tree
- $(NO, f)$ and $(NF, o)$, since player 1 opts out and a mismatch inside the unreached subgame is what keeps her out
- $(NO, o)$ and $(NF, f)$, since $N$ beats either equilibrium of the subgame and the plan after $Y$ must be one of them
<!-- YW5zOjM= -->
> The subgame after $Y$ has two pure equilibria, $(O, o)$ worth $a$ to player 1 and $(F, f)$ worth $b$. Branch: in both, $w > a > b$, so player 1 chooses $N$ at the root. Subgame perfection still requires the restriction to the subgame to be a Nash equilibrium of it, so the plans after $Y$ must be $(O, o)$ or $(F, f)$, never a mismatch. With $b < w < a$, as in Tadelis's $w = 1.5$, $a = 2$, $b = 1$, the SPE become $(YO, o)$ and $(NF, f)$.
> Ref: Tadelis (2013), voluntary Battle of the Sexes, §8.2 (pp. 154–159), Def. 8.3 (p. 157)
> Similar: Tadelis (2013), Exercise 8.1, p. 170; Exercise 8.10, p. 172

Q: Player 1 ignores ($I$, payoffs $(0,0)$) or escalates ($E$). After $E$, player 2 backs down ($B$, payoffs $(\beta, -\beta)$) or goes nuclear ($N$), and then both choose at once: mutual retreat $(R, r)$ pays $(-\omega, -\omega)$, and any profile with Doomsday ($D$ or $d$) pays $(-M, -M)$, with $\beta, \omega > 0$ and $M > \max\{\omega, \beta\}$. If $\omega > \beta$, which are the pure SPE?
- $(IR, Nr)$ and $(ED, Bd)$, since the war stage has two equilibria and each one carried up gives a different reduced game
- $(ED, Bd)$ only, since $(D, d)$ is the only equilibrium of the war stage once Doomsday costs more than backing down
- $(ER, Br)$ and $(ED, Bd)$, since player 2 backs down whichever war-stage equilibrium is expected, so player 1 escalates
- $(IR, Br)$ and $(ED, Bd)$, since player 2 backs down but player 1 fears the war stage and ignores in one of the branches
<!-- YW5zOjI= -->
> The war stage has two pure equilibria, $(R, r)$ worth $-\omega$ each and $(D, d)$ worth $-M$ each. If $(R, r)$ is expected, player 2 compares $-\omega$ with $-\beta$ and, since $\omega > \beta$, backs down; player 1 then gets $\beta > 0$ from escalating. If $(D, d)$ is expected, $-M < -\beta$, so player 2 again backs down and player 1 escalates. Both branches give escalation. In Tadelis's numbers $\omega = 5 < \beta = 10$, so the first branch flips to $(IR, Nr)$; the first option is that case.
> Ref: Tadelis (2013), mutually assured destruction, §8.3.3 (pp. 163–166)
> Similar: Tadelis (2013), Exercise 8.2, p. 170

Q: Players 1 and 2 move simultaneously; players 3 and 4 observe $(a_1, a_2)$ and then move simultaneously, and each second-stage game has a unique Nash equilibrium $(a_3^*(a_1,a_2), a_4^*(a_1,a_2))$. If $(a_1^*, a_2^*)$ is the unique equilibrium of the induced first stage, what is the subgame-perfect equilibrium?
- $(a_1^*, a_2^*, a_3^*(\cdot,\cdot), a_4^*(\cdot,\cdot))$, with a reply of players 3 and 4 for every first-stage pair
- $(a_1^*, a_2^*, a_3^*(a_1^*,a_2^*), a_4^*(a_1^*,a_2^*))$, the four actions played along the equilibrium path
- $(a_1^*, a_2^*)$ together with any replies of players 3 and 4 that are best responses on the equilibrium path
- $(a_3^*(\cdot,\cdot), a_4^*(\cdot,\cdot))$ alone, since the first-stage choices follow from the replies of the later movers
<!-- YW5zOjA= -->
> An equilibrium is a profile of complete strategies, and the strategies of players 3 and 4 are functions of the observed first-stage pair. The second option is the subgame-perfect outcome, the path; writing it when the equilibrium is asked for is the most common error on this topic. Best responses on the path only, the third option, are what Nash equilibrium requires; subgame perfection asks for the equilibrium reply in every second-stage subgame. The first-stage actions are part of the profile, not implied by it.
> Ref: Gibbons (1992), §2.2.A (pp. 71–73), outcome vs equilibrium (pp. 125–126); Tadelis (2013), §8.3.2 (p. 161)
> Similar: Tadelis (2013), Exercise 8.4, p. 170; Exercise 8.6, pp. 170–171

Q: In a game whose only proper subgame is the whole game, how does the set of subgame-perfect equilibria compare with the set of Nash equilibria?
- SPE is a strict subset, since sequential rationality still rules out actions that are not best replies at unreached nodes
- SPE is empty unless the game has perfect information, since backward induction then has no last subgame to start from
- SPE is a strict superset, since without proper subgames below the root the refinement admits mixed profiles as well
- They coincide, since the definition then asks only for a Nash equilibrium of the whole game, as in any simultaneous game
<!-- YW5zOjM= -->
> Definition 8.3 requires a Nash equilibrium in every proper subgame; if the whole game is the only one, that is exactly the Nash condition. Every simultaneous game, and the card game, are of this kind. Sequential rationality at non-singleton information sets would need beliefs, which subgame perfection does not use; that gap is what perfect Bayesian equilibrium fills in Lecture 8. Every SPE is always a Nash equilibrium, so SPE can never be a superset.
> Ref: Tadelis (2013), Def. 8.3 (p. 157), card game (p. 156); MWG §9.B (pp. 274–275)
> Similar: Tadelis (2013), Exercise 8.5, p. 170
