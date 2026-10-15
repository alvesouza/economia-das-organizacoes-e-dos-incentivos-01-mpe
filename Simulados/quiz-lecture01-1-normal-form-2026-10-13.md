---
quiz: "Lecture 1 · Quiz 1 of 3 — Normal form, strategies and common knowledge"
tags:
  nf: "Normal-form games and solution concepts"
  strategy: "Strategies as complete contingent plans"
  ck: "Complete information and common knowledge"
  payoffs: "From outcomes to payoffs: the grade game"
---

## nf

Q: In an $n$-player normal-form game every player has $m \ge 2$ pure strategies. To verify that $s_i$ is strictly dominated by $s_i'$, and to verify that $s_i$ is strictly dominant, how many strict payoff inequalities must be checked?
- $m^{n}$ to show $s_i$ is dominated by $s_i'$, and $(m-1)\,m^{n}$ to show $s_i$ is dominant, one per full profile and rival strategy
- $(n-1)\,m$ to show $s_i$ is dominated by $s_i'$, and $(m-1)(n-1)\,m$ to show $s_i$ is dominant, one per opponent and strategy
- $m^{n-1}$ to show $s_i$ is dominated by $s_i'$, and $(m-1)\,m^{n-1}$ to show $s_i$ is dominant, one per opponent profile and rival
- $m^{n-1}$ to show $s_i$ is dominated by $s_i'$, and $m^{n-1}$ to show $s_i$ is dominant, since one rival strategy is enough to check
<!-- YW5zOjI= -->
> Dominance compares $u_i(s_i, s_{-i})$ with $u_i(s_i', s_{-i})$ for every $s_{-i} \in S_{-i}$, and $|S_{-i}| = m^{n-1}$: player $i$'s own strategy is fixed by the comparison, so it is not counted. A dominant strategy must strictly dominate each of the other $m - 1$ strategies, giving $(m-1)m^{n-1}$ inequalities. Counting full profiles ($m^n$) double-counts $i$'s own choice; counting opponents one at a time ignores that dominance must hold against every joint profile.
> Ref: Lecture 1 slides 14, 23; Tadelis (2013), §3.2 (pp. 47–48), §4.1.1 (pp. 60–61)
> Similar: Tadelis (2013), Exercise 4.1, p. 76; MWG 8.B.1, p. 262

Q: Judge the strict dominant-strategy equilibrium against the three criteria for a solution concept: existence, uniqueness, and invariance to payoff changes of size $\varepsilon$.
- It exists in every finite game, is unique when payoffs are generic, and is fragile, since any $\varepsilon$ change can break a dominance relation
- It often fails to exist, is unique whenever it exists, and is invariant, since strict inequalities survive any small enough $\varepsilon$ change
- It often fails to exist, can select several profiles when it exists, and is invariant, since strict inequalities survive small $\varepsilon$ changes
- It often fails to exist, is unique whenever it exists, and is fragile, since an $\varepsilon$ change can turn a strict inequality into a tie
<!-- YW5zOjE= -->
> Most games have no strictly dominant strategy for some player, so existence is the concept's weakness. When it exists it is unique (two strictly dominant strategies would each have to beat the other). Strict inequalities hold with slack, so a perturbation smaller than the smallest slack leaves every comparison intact: the prediction is invariant. Ties are a knife-edge case that the strict concept excludes by definition.
> Ref: Lecture 1 slides 22, 25; Tadelis (2013), §3.3.2 (pp. 55–56), §4.1.3 (p. 62)
> Similar: Tadelis (2013), Exercise 4.2, p. 76

Q: Player 1 chooses one of $m$ actions; player 2 observes the choice and then chooses one of $k$ actions. In the normal form of this game, how many pure strategies does player 2 have, and how large is the payoff matrix?
- $k^{m}$ strategies, one action for each of player 1's $m$ choices, so the matrix is $m \times k^{m}$
- $m\,k$ strategies, one pair of observed and chosen actions each, so the matrix is $m \times m\,k$
- $k$ strategies, since player 2 picks an action after observing, so the matrix is $m \times k$
- $m^{k}$ strategies, one choice of player 1 per action of player 2, so the matrix is $m \times m^{k}$
<!-- YW5zOjA= -->
> A strategy for player 2 is a complete contingent plan: a function from the $m$ observed actions to the $k$ available replies, and there are $k^m$ such functions. Player 1 moves once with nothing to condition on, so has $m$ strategies, and the matrix is $m \times k^m$. This is how any dynamic game becomes a normal-form game, at the price of a much larger matrix.
> Ref: Lecture 1 slides 15, 17; Tadelis (2013), Ch. 7 (pp. 129–150); MWG §7.D (p. 228)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 2, p. 4

## strategy

Q: A strategy must specify an action at every contingency, including contingencies that the player's own earlier actions rule out. Why does the definition require that?
- Because a player who leaves a contingency open can be exploited by opponents, so complete plans are what a rational player would choose anyway
- Because payoffs are defined over terminal histories, so every action at every contingency changes the payoff of the plan taken as a whole
- Because common knowledge requires that each player know the others' actions at every contingency, including those never reached
- Because the normal form asks each player for one choice made before play, and that choice must fix behaviour wherever the game could go
<!-- YW5zOjM= -->
> The normal form collapses play into a single simultaneous choice of plans. For the profile of plans to determine an outcome against any opponent behaviour, and for opponents to evaluate deviations, each plan must say what happens at every contingency. Actions at unreached contingencies do not change the payoff of the realised path, which is why the second option fails; the requirement is definitional, not about exploitation.
> Ref: Lecture 1 slide 17; Tadelis (2013), Ch. 7 (pp. 129–150); MWG §7.D (p. 228)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 3, p. 5

## ck

Q: Two players each receive a private letter, unseen by the other, that describes the game's payoffs exactly. Which statement about the payoffs is correct?
- They are common knowledge, since each player knows the payoffs and both are rational, which makes higher-order knowledge follow automatically
- They are known to each player but not common knowledge, since neither knows the other got a letter; a public announcement fixes that
- They are not known to either player, since knowledge requires that the information be verified by the other player before the game starts
- They are common knowledge once both letters are read, since the same text was sent to both, and what is sent identically is known to be known
<!-- YW5zOjE= -->
> Each player knows the payoffs (first-order knowledge), but neither knows that the other knows, so the second level of the infinite hierarchy already fails. A public announcement, made in front of both, gives every level at once: each hears it, knows the other heard it, and so on. Rationality does not generate knowledge of what others were told.
> Ref: Lecture 1 slide 16; Tadelis (2013), Def. 3.1 (p. 45), §4.2 (pp. 63–65)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 12, p. 23

Q: Two firms choose outputs simultaneously; each knows the demand curve and both cost functions, and all of this is common knowledge. How should the game be classified?
- Static with incomplete information, since neither firm observes the other's output before choosing its own output
- Dynamic with complete information, since the firms interact in a market that clears after both of them have chosen
- Static with complete information, since choices are simultaneous and the game itself is common knowledge to both firms
- Static with complete information only if outputs are observed afterwards, since otherwise payoffs stay private to each
<!-- YW5zOjI= -->
> Static versus dynamic is about whether a player observes others' moves before choosing; complete versus incomplete is about whether the game (players, actions, payoffs) is common knowledge. Not observing the rival's output makes the game static, not incomplete: that is imperfect, not incomplete, information. Incomplete information, where a firm does not know the rival's cost, is the subject of Bayesian games (Lecture 7).
> Ref: Lecture 1 slides 15–16; Tadelis (2013), §3.1 (pp. 43–47); Gibbons (1992), §1.1.A (pp. 2–4)
> Similar: Tadelis (2013), Exercise 3.6, p. 58

## payoffs

Q: The grade game's outcome matrix lists grades, not payoffs. Why does the analysis need payoffs before it can predict anything?
- Because one outcome matrix gives different games depending on how players value own and other's grades, so predictions differ
- Because grades are ordinal while dominance needs cardinal payoffs, so outcomes must first be converted into expected utilities
- Because the grades are shared between the two players, so the outcome matrix double-counts each grade unless it is converted
- Because outcome matrices cannot represent simultaneous moves, so converting grades into payoffs is what makes the game static
<!-- YW5zOjA= -->
> A game is defined by preferences over outcomes, $u_i: S \to \mathbb{R}$. A selfish player and one who cares about the pair's grade face the same outcomes but different games: the first may have a dominant strategy that the second lacks. Dominance itself is ordinal (it compares payoffs strategy by strategy), so cardinal utility is not what the conversion is for; expected utility enters only with mixed strategies.
> Ref: Lecture 1 slides 10–12, 18; Tadelis (2013), §3.2 (pp. 47–52)
> Similar: Tadelis (2013), Exercises 3.2 and 3.4, p. 58

P: In the grade game each player writes $\alpha$ or $\beta$. Both $\alpha$ gives each a B−; both $\beta$ gives each a B+; one $\alpha$ and one $\beta$ gives an A to the $\alpha$ writer and a C to the $\beta$ writer. A player's payoff is $g(\text{own grade}) + \lambda\, g(\text{other's grade})$, where $\lambda \ge 0$ weights the other's grade and the grade values satisfy $g_A > g_{B+} > g_{B-} > g_C$.

Q: For which $\lambda$ is $\alpha$ strictly dominant?
- $\lambda < \max\{(g_{B-} - g_C)/(g_A - g_{B-}),\ (g_A - g_{B+})/(g_{B+} - g_C)\}$, so that $\alpha$ wins against at least one of the pair's choices
- $\lambda < \min\{(g_A - g_{B-})/(g_{B-} - g_C),\ (g_{B+} - g_C)/(g_A - g_{B+})\}$, so that $\alpha$ wins against both of the pair's choices
- $\lambda < 1$, so that each player weighs the own grade more than the pair's grade, whatever the four grade values happen to be
- $\lambda < \min\{(g_{B-} - g_C)/(g_A - g_{B-}),\ (g_A - g_{B+})/(g_{B+} - g_C)\}$, so that $\alpha$ wins against both of the pair's choices
<!-- YW5zOjM= -->
> Against $\alpha$: writing $\alpha$ gives $(1+\lambda)g_{B-}$, writing $\beta$ gives $g_C + \lambda g_A$; $\alpha$ is better iff $\lambda < (g_{B-} - g_C)/(g_A - g_{B-})$. Against $\beta$: $\alpha$ gives $g_A + \lambda g_C$, $\beta$ gives $(1+\lambda)g_{B+}$; $\alpha$ is better iff $\lambda < (g_A - g_{B+})/(g_{B+} - g_C)$. Strict dominance needs both, hence the minimum. The "max" option is the condition for $\alpha$ not to be strictly dominated by $\beta$, which is weaker.
> Ref: Lecture 1 slides 10–12, 23; Tadelis (2013), §4.1 (pp. 59–63)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 13, p. 26

Q: Set $\lambda = 0$. What is the prediction, and how does it rank by Pareto optimality?
- Both write $\beta$, a strict dominant-strategy equilibrium that is also the unique Pareto optimal profile of the game
- Both write $\alpha$, a strict dominant-strategy equilibrium that is Pareto dominated by the profile where both write $\beta$
- Both write $\alpha$, a strict dominant-strategy equilibrium that is Pareto optimal, since no profile raises both payoffs
- No prediction, since with $\lambda = 0$ each player's best choice depends on what the pair writes
<!-- YW5zOjE= -->
> With $\lambda = 0$, $\alpha$ beats $\beta$ against $\alpha$ ($g_{B-} > g_C$) and against $\beta$ ($g_A > g_{B+}$): strictly dominant for both, so the prediction is ($\alpha$, $\alpha$) with B− each. Both writing $\beta$ gives B+ each, which is better for both: a prisoner's dilemma. Individually rational choices lead to a socially undesirable outcome (Lesson 2).
> Ref: Lecture 1 slides 24–26; Tadelis (2013), §3.2.1 (pp. 51–52), Def. 3.5 (p. 57), §4.1 (pp. 59–63)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 1 Ex. 5, p. 8

Q: For which $\lambda$ is $\beta$ strictly dominant?
- $\lambda > \min\{(g_{B-} - g_C)/(g_A - g_{B-}),\ (g_A - g_{B+})/(g_{B+} - g_C)\}$, so that $\beta$ wins against at least one of the pair's choices
- $\lambda > 1$, so that each player weighs the pair's grade more than the own grade, whatever the four grade values happen to be
- $\lambda > \max\{(g_{B-} - g_C)/(g_A - g_{B-}),\ (g_A - g_{B+})/(g_{B+} - g_C)\}$, so that $\beta$ wins against both of the pair's choices
- No $\lambda$, since against a pair who writes $\beta$, writing $\alpha$ always earns an A, which no weight on the pair's grade can offset
<!-- YW5zOjI= -->
> $\beta$ beats $\alpha$ against $\alpha$ iff $\lambda > (g_{B-} - g_C)/(g_A - g_{B-})$ and against $\beta$ iff $\lambda > (g_A - g_{B+})/(g_{B+} - g_C)$, so strict dominance needs $\lambda$ above the maximum. The last option forgets that writing $\alpha$ against $\beta$ hands the pair a C, which costs $\lambda(g_{B+} - g_C)$. Between the minimum and the maximum neither strategy dominates, and the prediction depends on beliefs about the pair.
> Ref: Lecture 1 slides 10–12, 23; Tadelis (2013), §4.1 (pp. 59–63)
> Similar: Tadelis (2013), Exercise 3.4, p. 58
