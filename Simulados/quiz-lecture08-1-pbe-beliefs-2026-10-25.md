---
quiz: "Lecture 8 · Quiz 1 of 3 — Beliefs, perfect Bayesian and sequential equilibrium (estimated unit, written before the lecture from Tadelis Ch. 15 and Gibbons §4.1)"
tags:
  sp: "Why subgame perfection fails with private types"
  beliefs: "Systems of beliefs and Bayes' rule"
  pbe: "Sequential rationality and perfect Bayesian equilibrium"
  se: "Consistency and sequential equilibrium"
---

## sp

Q: An entrant privately learns whether it is competitive or weak and chooses Out or Enter; after entry the incumbent chooses Fight or Accommodate without seeing the type. Why does subgame perfection fail to remove the Bayesian Nash equilibrium in which both types stay out and the incumbent would fight?
- Because each entrant type's decision node starts a proper subgame, and in each of those subgames staying out is a Nash equilibrium against fighting
- Because fighting is a best reply after entry whenever the incumbent believes the entrant is competitive with probability above one half, so the threat is credible
- Because the incumbent's post-entry nodes form one information set and the entrant's nodes follow Nature's move, so the only proper subgame is the whole game
- Because that equilibrium is in mixed strategies, and subgame perfection only restricts pure strategies at nodes reached with positive probability
<!-- YW5zOjI= -->
> A proper subgame must start at a singleton information set and cut no information set. The incumbent's nodes after entry are joined in one information set, and each entrant node follows Nature's move, so no proper subgame starts below the root: subgame perfection is then just Bayesian Nash equilibrium. Fighting is never a best reply after entry in this game (accommodating pays 1 against either type, fighting pays −1 or 0), which is exactly why the equilibrium is unreasonable; and the equilibrium is in pure strategies.
> Ref: Tadelis (2013), §15.1 (pp. 303–307), Fig. 15.2 (p. 305); Gibbons (1992), §4.1 (pp. 175–177)
> Similar: Tadelis (2013), Exercise 15.1, p. 314; Gibbons (1992), Problem 4.1, p. 245

Q: In Gibbons's game without Nature, player 1 chooses L, M or R; R ends the game, and after L or M player 2 knows only that R was not chosen. Two Nash equilibria exist and both are subgame perfect. What is the source of the problem that perfect Bayesian equilibrium fixes?
- A non-singleton information set: with no proper subgame, subgame perfection is silent on player 2's reply, which a belief at that set disciplines
- Nature's move: once a chance node precedes player 2, player 2 cannot compute expected payoffs, so the game must first be turned into a Bayesian normal form
- Weakly dominated strategies: one of the two equilibria uses a weakly dominated strategy for player 1, which iterated weak elimination removes at once
- Simultaneous moves: player 2 moves at the same time as player 1 in the normal form, so backward induction cannot be applied to the reply at all
<!-- YW5zOjA= -->
> There is no Nature in this game; what matters is that player 2's two nodes form one information set, so the whole game is the only proper subgame and both Nash equilibria are subgame perfect. Requiring a belief $p$ at that set and a best reply to it kills the equilibrium in which player 2 plays $R'$, because $L'$ pays $2-p$ and $R'$ pays $1-p$ at every $p$. The point is about information sets, not about chance moves or weak dominance.
> Ref: Gibbons (1992), §4.1, Figs. 4.1.1–4.1.2 (pp. 175–177); Tadelis (2013), §15.1 (p. 307)
> Similar: Gibbons (1992), Problem 4.1, p. 245

## beliefs

Q: The competitive type ($C$, prior probability $p \in (0,1)$) enters with probability $\sigma_C$ and the weak type ($W$) with probability $\sigma_W$. What belief $\mu = \Pr\{C \mid \text{entry}\}$ does Bayes' rule assign, and when is it pinned down?
- $\mu = \sigma_C/(\sigma_C + \sigma_W)$, pinned down whenever $\sigma_C + \sigma_W > 0$, since the prior cancels once both types are allowed to enter
- $\mu = p\,\sigma_C/[p\,\sigma_C + (1-p)(1-\sigma_W)]$, pinned down whenever $\sigma_W < 1$, the case where the weak type sometimes stays out
- $\mu = p\,\sigma_C + (1-p)\,\sigma_W$, pinned down for every strategy profile, since it is the total probability with which entry occurs
- $\mu = p\,\sigma_C/[p\,\sigma_C + (1-p)\,\sigma_W]$, pinned down whenever $p\,\sigma_C + (1-p)\,\sigma_W > 0$, that is, when entry is on the path
<!-- YW5zOjM= -->
> $\Pr\{C \mid E\} = \Pr\{C\}\Pr\{E \mid C\}/\Pr\{E\}$ with $\Pr\{E\} = p\sigma_C + (1-p)\sigma_W$. The formula needs both the exogenous prior and the endogenous strategy; it is defined only when the denominator is positive, i.e. when entry is reached with positive probability. When both types stay out it reads $0/0$ and Requirement 15.3 leaves the belief free. The third option is the denominator, not the posterior; the first drops the prior.
> Ref: Tadelis (2013), §15.2, Requirement 15.2 (pp. 308–309); Gibbons (1992), §4.1 (pp. 178–179)
> Similar: Tadelis (2013), Exercise 15.3, pp. 315–316; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 1, pp. 376–377

Q: In a signaling game every type sends message $m$ in a candidate equilibrium, and message $m'$ is sent by no type. What do the PBE requirements say about the receiver's beliefs after $m$ and after $m'$?
- After $m$ the belief is the prior; after $m'$ it must also equal the prior, because with no new information the receiver has no reason to revise what it believed
- After $m$ the belief is the prior; after $m'$ Bayes' rule reads $0/0$, so any belief is allowed, provided it makes the receiver's reply to $m'$ optimal
- After $m$ the belief puts probability one on the most likely type; after $m'$ it puts probability one on the other type, the only one left to deviate
- After $m$ the belief is free, since pooling reveals nothing; after $m'$ it is pinned by Bayes' rule applied to the equilibrium probability of a deviation
<!-- YW5zOjE= -->
> When all types send $m$, Bayes' rule gives $\mu(t \mid m) = p(t)$: pooling teaches nothing. At the unused $m'$ the denominator is zero, so Requirement 15.3 (Gibbons's Requirement 4 is vacuous in a signaling game) leaves the belief free; the only restriction is Requirement 15.4, that the reply to $m'$ be a best reply to it. Confusing "on path, equal to the prior" with "off path, equal to the prior" is the standard error.
> Ref: Tadelis (2013), Ch. 16 opening (pp. 318–319), Requirements 15.2–15.3 (pp. 309–310); Gibbons (1992), §4.2.A (pp. 186–188)
> Similar: Gibbons (1992), Problem 4.3, pp. 246–247; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 9 Ex. 2, pp. 385–386

Q: Type $t_1$ (prior $p \in (0,1)$) always sends message $m$; type $t_2$ sends $m$ with probability $\pi \in (0,1)$ and another message otherwise. What is the receiver's posterior $\mu(t_1 \mid m)$, and where does it lie?
- $\mu = p/[p + (1-p)\pi]$, which lies strictly between $p$ and 1, so $m$ is informative about $t_1$ without being conclusive
- $\mu = p\pi/[p\pi + (1-p)]$, which lies strictly between 0 and $p$, so $m$ makes $t_1$ less likely than it was before the message
- $\mu = p/[p + (1-p)(1-\pi)]$, which lies strictly between $p$ and 1, so $m$ is informative about $t_1$ without being conclusive
- $\mu = p$, whatever the value of $\pi$, because one of the types sends $m$ for sure and so the message cannot change the receiver's belief
<!-- YW5zOjA= -->
> $\Pr\{m \mid t_1\} = 1$ and $\Pr\{m \mid t_2\} = \pi$, so $\mu = p/[p + (1-p)\pi]$. At $\pi = 1$ it is the prior (pooling); as $\pi \to 0$ it tends to 1 (separating); for $\pi \in (0,1)$ it is strictly inside $(p, 1)$: a hybrid equilibrium's message is informative but not conclusive. The third option uses the probability that $t_2$ sends the other message; the second swaps the roles of the types.
> Ref: Gibbons (1992), §4.2.B, eq. (4.2.8) (pp. 202–203); Tadelis (2013), Remark (p. 319)
> Similar: Gibbons (1992), Problem 4.7, p. 249

## pbe

Q: After entry the incumbent earns $a_C$ (competitive entrant) or $a_W$ (weak entrant) by accommodating, and $f_C$ or $f_W$ by fighting; entry is off the equilibrium path, so the belief $\mu = \Pr\{C \mid \text{entry}\}$ is free. When does some belief make fighting sequentially rational?
- Iff $\min\{f_C - a_C,\ f_W - a_W\} \ge 0$, so a belief supports fighting only when fighting beats accommodating against both types at once
- Iff $p f_C + (1-p) f_W \ge p a_C + (1-p) a_W$, with $p$ the prior, since an off-path belief has to coincide with the prior distribution
- Iff $f_C + f_W \ge a_C + a_W$, since the belief that matters off the path is the uniform one, $\mu = 1/2$, which treats both types equally
- Iff $\max\{f_C - a_C,\ f_W - a_W\} \ge 0$, so no belief supports fighting exactly when accommodating beats fighting against both types
<!-- YW5zOjM= -->
> The gain from fighting, $\mu(f_C - a_C) + (1-\mu)(f_W - a_W)$, is linear in $\mu$, so its maximum over $\mu \in [0,1]$ is at an endpoint: some belief supports fighting iff one of the two differences is non-negative. In Tadelis's entry game $a_C = a_W = 1$, $f_C = -1$, $f_W = 0$: both differences are negative, so no belief supports the threat and the pooling BNE is not a PBE. Off-path beliefs need not equal the prior, nor any particular value.
> Ref: Tadelis (2013), §15.2, Requirements 15.3–15.4 and the entry game (pp. 310–311)
> Similar: Tadelis (2013), Exercise 15.1, p. 314; Gibbons (1992), Problem 4.2, pp. 245–246

Q: A Bayesian Nash equilibrium reaches every information set with positive probability. Why is it then a PBE once beliefs are computed by Bayes' rule?
- Because a suboptimal action at a reached set $h$ would cost $\Pr\{h\}$ times the gain ex ante, a profitable deviation no BNE can contain
- Because Bayes' rule then pins every belief, and a belief pinned by Bayes' rule makes every action prescribed by the equilibrium a best reply to it
- Because every information set then starts a proper subgame, so subgame perfection, which a BNE of such a game satisfies, delivers sequential rationality
- Because beliefs at reached sets are then degenerate on one node, so the expected payoff at each set $h$ equals the payoff at a single node
<!-- YW5zOjA= -->
> Requirements 15.1–15.3 hold by construction, so only sequential rationality could fail. If player $i$ were not best-responding at a reached set $h$, switching there would raise $i$'s ex-ante expected payoff by $\Pr\{h\} \times (\text{gain at } h) > 0$, contradicting BNE. Off-path information sets are the only place where BNE and PBE can differ. Pinned beliefs do not by themselves make actions optimal; reached sets need not start subgames or carry degenerate beliefs.
> Ref: Tadelis (2013), Prop. 15.1 (p. 311); MWG (1995), §9.C (pp. 282–285)
> Similar: Tadelis (2013), Exercise 15.3, pp. 315–316

Q: Tadelis's PBE leaves off-path beliefs unrestricted, whereas Gibbons asks for Bayes' rule "where possible" off the path as well. Why does the difference not matter in a two-stage signaling game?
- Because in a signaling game the receiver moves only once, so sequential rationality off the path reduces to Nash equilibrium of the whole game and any belief does
- Because an unused message is reached under no type's strategy, so the denominator of Bayes' rule is zero at every off-path information set of the receiver
- Because the sender's information sets are singletons, so Bayes' rule is never needed for the sender and only on-path beliefs of the receiver matter
- Because in a signaling game the off-path beliefs are always set equal to the prior by the requirement, so both definitions pin them to the same value
<!-- YW5zOjE= -->
> Bayes' rule "where possible" off the path bites when an information set is unreached because of one player's deviation but other players' strategies still give conditional probabilities (Tadelis's Fig. 15.3, Gibbons's Fig. 4.1.4). In a signaling game an unused message is reached by no type, so there is nothing to condition on: Gibbons notes his Requirement 4 is vacuous there. Sender sets being singletons is true but is not why the receiver's off-path beliefs are unconstrained.
> Ref: Tadelis (2013), Remark and Fig. 15.3 (pp. 311–312); Gibbons (1992), §4.1 Requirement 4 (p. 180), §4.2.A (p. 186)
> Similar: Gibbons (1992), Problem 4.2, pp. 245–246

## se

Q: Nature selects node $x_1$ with probability $\lambda \in (0,1)$ and $x_2$ otherwise; player 1, who does not see the draw, plays $U$ (ending the game) or $D$; after $D$ player 2 moves at the information set $\{x_1, x_2\}$ and strictly prefers $R$ iff its belief on $x_1$ exceeds $\bar\mu$. The equilibrium has player 1 play $U$ and player 2 play $R$. When is it a sequential equilibrium?
- Only if $\bar\mu < 1/2$, because trembles are symmetric across nodes, so every consistent belief puts probability one half on $x_1$
- For any $\bar\mu < 1$, because a suitable sequence of trembles can make the limiting belief on $x_1$ any number in the unit interval
- Only if $\bar\mu < \lambda$, since player 1's tremble cannot depend on the draw, so each consistent belief on $x_1$ is $\lambda$
- Never, because $D$ is played with probability zero, so the belief on $x_1$ is undefined and no consistent belief system can exist
<!-- YW5zOjI= -->
> In any totally mixed profile player 1 plays $D$ with some $\varepsilon_k$ at both nodes (he cannot condition on Nature), so Bayes gives $\lambda\varepsilon_k/[\lambda\varepsilon_k + (1-\lambda)\varepsilon_k] = \lambda$ for every $k$, and the limit is $\lambda$. $R$ is then sequentially rational iff $\lambda > \bar\mu$. In Tadelis's Fig. 15.4, $\lambda = 1/2$ and $R$ needs a belief above $2/3$, so $(U, R)$ is a PBE but not a sequential equilibrium.
> Ref: Tadelis (2013), §15.3, Fig. 15.4, Defs. 15.4–15.5 (pp. 312–313)
> Similar: Tadelis (2013), Exercise 15.6, p. 317

Q: Which statement about consistency and sequential equilibrium is correct?
- Consistency asks that off-path beliefs equal the prior over Nature's moves, which is why the beliefs of a sequential equilibrium never depend on strategies
- Consistency asks that off-path beliefs be limits of Bayes' rule under totally mixed profiles, so a sequential equilibrium is a PBE and is subgame perfect
- Consistency asks that off-path beliefs be the ones the deviating type would want the receiver to hold, which is how it selects least-cost separation
- Consistency asks that off-path beliefs follow Bayes' rule where possible, so it coincides with the weak PBE in every finite extensive-form game
<!-- YW5zOjE= -->
> Kreps and Wilson's consistency takes beliefs to be limits of Bayes' rule along totally mixed profiles converging to the equilibrium. Every sequential equilibrium is a PBE (Def. 15.5) and is subgame perfect (MWG Prop. 9.C.2), while a weak PBE need not be (Gibbons Fig. 4.1.4). The limit equals the prior only when the trembling player cannot condition on Nature; trembles by an informed player can shift the odds. Reading deviations as coming from the type that gains is the intuitive criterion, a different refinement.
> Ref: Tadelis (2013), Defs. 15.4–15.5 (p. 313); MWG (1995), Def. 9.C.4 and Prop. 9.C.2 (pp. 290–291); Gibbons (1992), §4.1 (pp. 179–181)
> Similar: Tadelis (2013), Exercise 15.6, p. 317
