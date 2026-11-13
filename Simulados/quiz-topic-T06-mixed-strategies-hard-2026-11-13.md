---
quiz: "Topic T6 · Mixed strategies and existence — hard conceptual quiz (10 questions; Lectures 2–3, Tadelis Ch. 6 and §12.5)"
tags:
  indiff: "The indifference principle and what pins each mix"
  interp: "Interpreting mixed equilibria: beliefs, security, purification"
  exist: "Existence: fixed points, finiteness and the count of equilibria"
---

## indiff

Q: A $2\times2$ game has a unique Nash equilibrium, in which both players mix. The row player's two payoffs in the left column are both raised by the same amount $k>0$, and every other payoff stays as it was. What happens to the equilibrium?
- The row player's mix shifts, since her own payoffs changed and a player's mix is the one that makes her own expected payoffs from each row equal
- Neither mix changes, since the gap between the row player's two rows is the same for every column mix, and only that gap pins the column player's mix
- The column player's mix shifts toward the right column, since a larger left-column payoff for the row player must be offset to keep her indifferent
- Both mixes shift, since any change in one player's payoffs moves both best-response curves and so moves the point where the two curves intersect
<!-- YW5zOjE= -->
> Write the row player's payoffs as $a, b$ (top row, left and right) and $c, d$ (bottom row). Her gain from the top row against a column mix $q$ is $q(a-c)+(1-q)(b-d)$; adding $k$ to both $a$ and $c$ leaves it unchanged for every $q$, so her best-response correspondence is identical. The column player's equilibrium mix is the one that makes the row player indifferent, so it does not move; the row player's mix is pinned by the column player's payoffs, which did not change either. Only the row player's equilibrium payoff rises, by $kq^*$. The first option is the classic slip of reading a player's mix off her own indifference; the third forgets that the gap, not the level, matters; the fourth forgets that the column player's best-response curve depends only on the column player's payoffs.
> Ref: Tadelis (2013), §6.2 (pp. 107–114); Lecture 3 slides 10–16 (principle of indifference, Battle of the Sexes)
> Similar: Listas/pratica-lecture-03 #1 (Tadelis 6.5); Listas/pratica-lecture-02 #16 (Tadelis 6.8)

Q: In the Lecture 3 mini case a remote employee works or shirks while the manager monitors or not, and the only equilibrium is fully mixed. A regulator adds a fine, paid to the state, on a shirker who is caught; nothing else changes. What happens in the new equilibrium?
- Shirking falls and monitoring is unchanged, since a harsher penalty deters the employee directly while the manager's costs and gains stay where they were
- Shirking and monitoring both fall, since a deterred employee shirks less often and the manager then needs to monitor less to keep her working
- Shirking falls and monitoring rises, since catching a shirker becomes more valuable once a fine is collected, and the manager responds to that value
- Shirking is unchanged and monitoring falls, since the fine enters only the employee's payoffs, which pin down the manager's mix and not her own
<!-- YW5zOjM= -->
> With wage $w$, effort cost $g$ and monitoring cost $h$, the manager is indifferent between monitoring and not when the shirking probability is $h/w$, a condition that uses only the manager's payoffs. A fine $F$ on a caught shirker changes the employee's payoff from shirking under monitoring from $0$ to $-F$, so the employee is indifferent when the monitoring probability is $g/(w+F)$. With the slide values $w=10$, $g=2$, $h=1$, monitoring falls from $1/5$ (at $F=0$) to $2/15$ (at $F=5$), while shirking stays at $1/10$. Each distractor lets the fine act on the employee's own mix, which is pinned by the other player's payoffs; the fine paid to the state never enters the manager's payoffs, so it cannot raise the value of monitoring to her.
> Ref: Lecture 3 slides 41–42 (mini case "work or shirk?"); Tadelis (2013), §6.2 (pp. 107–114)
> Similar: Resolucao/mini-case-lecture-03.pdf, parts (c)–(e)

Q: In a mixed-strategy Nash equilibrium, player 1 is indifferent among the pure strategies in her support. What, then, requires her to use exactly her equilibrium probabilities?
- Nothing in her own payoffs: any mix over her support is a best reply, and the exact weights are needed only to keep player 2 indifferent
- Her own expected payoff, which is highest only at the equilibrium weights, since any other mix over the support lowers it below the value
- The strict concavity of expected payoffs in her own probabilities, which makes her best reply unique once the opponent's mix is held fixed
- The support condition, since weights that drift from equilibrium put probability on strategies that earn less than the equilibrium value
<!-- YW5zOjA= -->
> Expected payoff is linear in a player's own probabilities, so once the pure strategies in the support tie, every mix over them earns the same; nothing in her own incentives selects the equilibrium weights. They are required because player 2 must be indifferent too, and player 2's indifference depends on player 1's weights. This is the discomfort Tadelis names before presenting Harsanyi's purification: "Does it make sense to expect such precision when a player is indifferent?" The second and third options would need strict concavity, which linear expected payoffs never have; the fourth confuses the support (which strategies get weight) with the weights placed on them.
> Ref: Tadelis (2013), §6.2, Prop. 6.1 (pp. 107–114), §12.5 (p. 264); Lecture 3 slides 10–12
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 3, Exercises 1–4

Q: Against the opponents' equilibrium strategies, player 1 earns the same expected payoff from three pure strategies, but her equilibrium mix uses only two of them. If she moved some weight onto the third, what would happen?
- Nothing at all, since her payoff is unchanged, and an equilibrium only requires that no player can gain by changing her own strategy alone
- She would lose, since a strategy outside the support must earn strictly less than the equilibrium value under the principle of indifference
- Her payoff stays the same, but the profile may stop being an equilibrium, since the other players' indifference can depend on her weights
- The profile stays an equilibrium but becomes a different one, since any convex combination of best replies is itself an equilibrium strategy
<!-- YW5zOjI= -->
> Condition (2) of the principle of indifference asks only that strategies outside the support earn no more than the equilibrium value, so a tie is allowed and moving weight there leaves player 1's payoff unchanged. The new profile is an equilibrium only if every other player is still best-replying, and their indifference conditions were computed against her old weights. The first option checks only player 1; the second turns "no more" into "strictly less"; the fourth is true for player 1's own best-reply set but not for the profile, whose equilibrium status depends on everyone.
> Ref: Lecture 3 slide 10 (conditions 1 and 2); Tadelis (2013), §6.2 (pp. 107–114); MWG §8.D, Prop. 8.D.1
> Similar: Listas/pratica-lecture-03 #15 (Tadelis 6.3); Listas/pratica-lecture-02 #21 (MWG 8.D.6)

## interp

Q: In Tadelis's perturbed Matching Pennies, each player privately draws a bonus, uniform on a small interval centred at zero, that is added to her payoffs whenever she plays H. Which statement describes the Bayesian Nash equilibrium?
- Each type mixes evenly between H and T, as in the original game, since a bonus that small cannot break the indifference of a player who faces an even opponent
- Each type plays a pure action, but the share of types playing H differs from one half for every positive bound and reaches it only as the bound shrinks
- No pure-strategy equilibrium exists, since the perturbed game keeps the cyclical best responses of Matching Pennies and so its types must still randomize
- Each type plays H if her bonus is nonnegative and T otherwise, so every type is pure, yet each player faces H from her opponent with probability one half
<!-- YW5zOjM= -->
> Claim 12.3: the unique Bayesian Nash equilibrium has $s_i(\varepsilon_i)=H$ iff $\varepsilon_i \ge 0$. Because the bonus is symmetric around zero, half of each player's types play H, so each player believes she faces H with probability exactly one half, and against that belief her own threshold at zero is a best reply. Every type has a strict best response (only the measure-zero type $\varepsilon_i=0$ is indifferent), which is Harsanyi's answer to the precision problem: the mixed equilibrium describes beliefs about types, not randomization. In this symmetric example the share is one half for every bound, not only in the limit; what converges as the bound shrinks is the payoffs. The first option needs every type to be indifferent, which a nonzero bonus rules out.
> Ref: Tadelis (2013), §12.5, Claim 12.3 (pp. 264–266)
> Similar: Tadelis (2013), Exercise 12.10, p. 269; Listas/pratica-lecture-07 #12 (Tadelis 12.9)

Q: In the Battle of the Sexes, Alex gets 2 at (O, O) and 1 at (F, F), Chris gets 1 and 2, and both get 0 apart. In the mixed equilibrium Alex plays O with probability 2/3 and expects 2/3. Which statement is correct?
- Alex's equilibrium mix guarantees her 2/3 whatever Chris does, since an equilibrium mix makes the opponent's choice irrelevant to one's own payoff
- Alex can guarantee 2/3 whatever Chris does by playing O with probability 1/3, while her equilibrium mix guarantees her only 1/3 if Chris deviates
- Alex cannot guarantee more than 1/3 against every choice of Chris, since a security level always lies below the payoff of the worst Nash equilibrium
- Alex's 2/3 is also her security level, and her equilibrium mix is the strategy that secures it, since in equilibrium she best-replies to the worst case
<!-- YW5zOjE= -->
> If Alex plays O with probability $p$, she gets $2p$ when Chris plays O and $1-p$ when Chris plays F. Her security level is $\max_p \min\{2p, 1-p\}$, reached at $p=1/3$, where both equal $2/3$. Her equilibrium mix $p=2/3$ gives $4/3$ against O but only $1/3$ against F. An equilibrium mix makes the *opponent* indifferent; it is not chosen to protect oneself, so in a game that is not zero-sum it need not be a security strategy. Here the two values happen to coincide at $2/3$, but the strategies differ, which is exactly what the fourth option misses. The first option inverts whose payoff is made flat; the third has the inequality backwards, since a Nash payoff is always at least the security level.
> Ref: Lecture 3 slides 13–16; Tadelis (2013), §6.2 (pp. 107–114)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 3, Exercise 18 "Maxmin Strategies", p. 145

Q: Under the beliefs interpretation of a mixed-strategy Nash equilibrium in a two-player game, what does player 1's equilibrium mix describe?
- Player 2's conjecture about player 1, which must make player 2 willing to play her own part, while player 1 herself may well choose a pure action
- Player 1's own deliberate randomization, which she must carry out with a device so that player 2 can check the probabilities she has announced
- The long-run frequency of player 1's actions over many plays, which player 2 learns over time and which therefore requires a repeated game
- The share of a population of player-1 types using each action, which needs a continuum of players on each side for the equilibrium to exist
<!-- YW5zOjA= -->
> Slide 17 lists three readings. Under the beliefs reading, $\sigma_{-i}$ is what player $i$ believes the others will do; so player 1's mix is player 2's belief about player 1, and the equilibrium requires this belief to make each action in player 2's support a best reply (and symmetrically). Player 1 need not physically randomize; she only must not have a strictly better action than those player 2 expects. The second option is the literal reading, which needs no verification device in any case; the third and fourth describe the empirical-frequency and population readings, which are different interpretations, not the beliefs one.
> Ref: Lecture 3 slide 17; Tadelis (2013), §6.1.3 (p. 105)
> Similar: Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25, section exist

## exist

Q: Nash's proof applies Kakutani's fixed-point theorem to the best-response correspondence. Why must it be applied to mixed rather than pure strategies in a finite game?
- Because pure best replies can fail to exist in a finite game, while mixed best replies always exist once expected payoffs are made continuous
- Because the pure best-response correspondence has no closed graph, while expected payoffs turn the mixed one into a continuous function
- Because a finite set of pure profiles is not convex and neither are pure best-reply sets, while mixing makes both of them convex sets
- Because Kakutani's theorem needs strictly concave payoffs, which pure strategies lack, while expected payoffs are strictly concave in probabilities
<!-- YW5zOjI= -->
> Kakutani needs (1) a non-empty, compact, convex domain, (2) non-empty values, (3) convex values and (4) a closed graph. A finite set of pure profiles fails (1), and a pure best-reply set with a tie, say $\{U, D\}$, fails (3). With mixing the domain is a product of simplices and each best-reply set is the face spanned by the tied pure strategies, which is convex. Pure best replies always exist in a finite game (a maximum over finitely many numbers), so the first option is wrong; the mixed best reply is a correspondence, not a function, whenever there are ties; and expected payoffs are linear in own probabilities, never strictly concave.
> Ref: Tadelis (2013), §6.4, Theorem 6.1 and the Fact (pp. 117–122); MWG Ch. 8, Appendix A (p. 260)
> Similar: Simulados/quiz-lecture02-3-mixed-strategies-2026-10-25, section exist

Q: In the Lecture 3 price game with capacity constraints, prices are continuous and there is no pure-strategy equilibrium. What does Nash's existence theorem say about this game?
- It guarantees a mixed equilibrium, since every game with compact strategy sets and bounded payoffs is covered by the theorem as it is stated
- Nothing directly, since the strategy sets are infinite; the slides instead construct a mixed equilibrium in which prices follow a continuous distribution
- It rules out any equilibrium, since a game with infinite strategy sets and no pure equilibrium falls outside the theorem and so has none at all
- It guarantees a pure equilibrium once prices are restricted to a fine grid, since a finite game always has an equilibrium of the theorem in pure form
<!-- YW5zOjE= -->
> The theorem covers games with finite strategy sets. In the Edgeworth game prices are continuous and payoffs jump where prices tie, so neither the theorem nor its continuous-game extensions applies as stated. The appendix shows existence directly: by the indifference principle each firm draws its price from $F(p)$ on $[\underline p, 1]$ with every price in the support earning $1-\bar q$. Failing a sufficient condition does not rule out an equilibrium (third option), and a finite grid guarantees a mixed equilibrium, not a pure one (fourth option).
> Ref: Lecture 3 slides 4–6 and appendix slides 45–49; Tadelis (2013), §6.4 (p. 117)
> Similar: Listas/pratica-lecture-02 #20 (Tadelis 5.12, Asymmetric Bertrand)

Q: A $2\times2$ game with generic payoffs, so that no player gets the same payoff at two different cells, has exactly two pure-strategy Nash equilibria. What else can be concluded?
- It also has a third, mixed equilibrium, since generic finite games have an odd number of equilibria, though games with ties can break the rule
- Nothing more, since a game that already has pure equilibria needs no mixed one, and Nash's theorem is silent once a pure equilibrium has been found
- It has infinitely many mixed equilibria, since with generic payoffs any probability mixture of the two pure equilibria is itself an equilibrium
- It has a mixed equilibrium only if the game is symmetric, since asymmetric payoffs keep the two players from being indifferent at the same time
<!-- YW5zOjA= -->
> With two strict pure equilibria on a diagonal, each player strictly prefers to match one action and the other, so each player's indifference point lies strictly inside $(0,1)$ and the best-response curves cross a third time in the interior. Tadelis's footnote: a game "will typically have an odd number of equilibria" (an index theorem). Ties can break this: if both players get 1 at (first, first) and 0 elsewhere, there are two pure equilibria and no profile with a mixing player is an equilibrium. A mixture of two equilibria is not a product of independent mixes, so the third option fails; the Battle of the Sexes is asymmetric and still has its mixed equilibrium, so the fourth fails.
> Ref: Tadelis (2013), §6.2.3 and footnote 6 (p. 113); Lecture 3 slides 13–16
> Similar: Notas/L02/L02-11-pitfalls, self-test item 17
