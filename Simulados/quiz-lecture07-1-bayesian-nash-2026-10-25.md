---
quiz: "Lecture 7 · Quiz 1 of 3 — Bayesian games and Bayesian Nash equilibrium"
tags:
  harsanyi: "Types, Nature and the common prior"
  bne: "Type-contingent strategies and Bayesian Nash equilibrium"
  cournot: "Cournot with a privately known cost"
  threshold: "Threshold strategies and purification"
---

## harsanyi

Q: In a static Bayesian game player $i$ has $m \ge 2$ actions and $k \ge 2$ types. How many pure strategies does $i$ have, and how many single-deviation inequalities must be checked for $i$ to verify a candidate Bayesian Nash equilibrium?
- $k^{m}$ strategies, one type for each action, and $m(k-1)$ inequalities, one per action and alternative type
- $m\,k$ strategies, one action-type pair each, and $(m-1)^{k}$ inequalities, one per profile of alternative actions
- $m^{k}$ strategies, one action for each type, and $k(m-1)$ inequalities, one per type and alternative action
- $m^{k}$ strategies, one action for each type, and $m^{k}-1$ inequalities, one per alternative whole strategy
<!-- YW5zOjI= -->
> A pure strategy is a map $s_i:\Theta_i \to A_i$, and there are $m^k$ such maps. Definition 12.4 asks every type to be unable to gain by switching to any single other action, so the check is type by type: $k$ types times $m-1$ alternatives. Checking against whole alternative strategies is unnecessary, because if no type gains by changing his own action, no rearrangement across types can gain either.
> Ref: Tadelis (2013), Def. 12.3 (p. 249), Def. 12.4 and eq. (12.2) (p. 251); Gibbons (1992), §3.1.C (pp. 149–151)
> Similar: Tadelis (2013), Exercise 12.1, p. 266; Gibbons (1992), Problem 3.1, p. 169

Q: An entrant chooses Out (payoffs entrant 0, incumbent 2) or Enter. After entry the incumbent Accommodates (payoffs 1, 1) or Fights (entrant $-1$; incumbent $-1$ if rational, $2$ if crazy). The incumbent is rational with probability $p$, known only to him. With $AF$ meaning that the rational type accommodates and the crazy type fights, what is the entrant's expected payoff from Enter against $AF$, and when is (Enter, $AF$) a Bayesian Nash equilibrium?
- $2p-1$, so (Enter, $AF$) is a BNE if and only if $p \ge 1/2$, since each incumbent type already best-responds to entry
- $1-2p$, so (Enter, $AF$) is a BNE if and only if $p \le 1/2$, since each incumbent type already best-responds to entry
- $2p-1$, so (Enter, $AF$) is a BNE for every $p$, since the crazy type's fighting is then a credible threat to the entrant
- $p$, so (Enter, $AF$) is a BNE if and only if $p \ge 2/3$, since the entrant must expect accommodation two times in three
<!-- YW5zOjA= -->
> Against $AF$ entry yields $1$ with probability $p$ and $-1$ with probability $1-p$, so $u_1 = 2p-1$, and entering beats the $0$ from Out iff $p \ge 1/2$. Each incumbent type is optimizing at his own node (rational: $1 > -1$; crazy: $2 > 1$), so only the entrant's condition binds. Tadelis's $p = 2/3$ is one value inside this range, not the threshold.
> Ref: Tadelis (2013), Ch. 12 opening, Figs. 12.1–12.2 (pp. 243–245)
> Similar: Tadelis (2013), Exercise 12.1, p. 266; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 1, p. 318

Q: Player 1's type is $a$ or $b$, player 2's is $c$ or $d$, and the common prior puts probability $\alpha$ on $(a,c)$ and on $(b,d)$ and $\tfrac12-\alpha$ on $(a,d)$ and on $(b,c)$, with $0<\alpha<\tfrac12$. What is player 1's belief that player 2 is of type $c$ after learning that he is of type $a$, and when is his type uninformative about player 2's?
- $\alpha$, read off the prior's cell directly, and his type is uninformative if and only if $\alpha = 1/4$
- $2\alpha$, by Bayes' rule on the row of $a$, and his type is uninformative if and only if $\alpha = 1/2$
- $\alpha/(1-\alpha)$, by Bayes' rule on the column of $c$, and his type is uninformative if and only if $\alpha = 1/3$
- $2\alpha$, by Bayes' rule on the row of $a$, and his type is uninformative if and only if $\alpha = 1/4$
<!-- YW5zOjM= -->
> $\Pr\{a\} = \alpha + (\tfrac12-\alpha) = \tfrac12$, so $\phi_1(c\mid a) = \alpha/\tfrac12 = 2\alpha$. The type is uninformative when this equals the marginal $\Pr\{c\} = \tfrac12$, i.e. $\alpha = \tfrac14$, where the prior factors into independent marginals. Tadelis's correlated example is $\alpha = 1/6$, giving $\phi_1(c\mid a) = 1/3$. Conditioning on the column instead of the row computes a belief about player 1, not player 2.
> Ref: Tadelis (2013), Def. 12.2 and eq. (12.1) (pp. 247–249); Gibbons (1992), §3.1.B (p. 149)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 2, p. 323

## bne

Q: In chicken each player swerves (payoff $0$) or drives; driving against a swerver pays $R$, and both driving pays $R/2-k_i$, where $i$'s accident cost $k_i$ is $L$ or $H>L$ with probability $\tfrac12$ each, independent and privately known. Player 2 plays $dc$: drive if lenient ($L$), swerve if harsh ($H$). When is $DC$ (lenient drives, harsh swerves) player 1's best response?
- $L \le R/2 \le H$, since a driving type earns $R/2-k$ against a driver and cares only about that case
- $L \le 3R/2 \le H$, since a driving type earns $\tfrac12(R/2-k)+\tfrac12 R$ against that rival plan
- $L \le 3R/4 \le H$, since a driving type earns $\tfrac14(R/2-k)+\tfrac34 R$ against that rival plan
- $L \le R \le H$, since a driving type earns $\tfrac12(R-k)+\tfrac12 R$ against that rival plan
<!-- YW5zOjE= -->
> Against $dc$, player 1 meets a driver with probability $\tfrac12$ (the lenient rival) and a swerver with probability $\tfrac12$. Driving pays $\tfrac12(R/2-k)+\tfrac12R = \tfrac34R-\tfrac12k$, swerving pays $0$, so type $k$ drives iff $k \le 3R/2$. $DC$ needs the lenient type to drive and the harsh type to swerve: $L \le 3R/2 \le H$. At Tadelis's $R=8$, $H=16$, $L=0$ the cutoff is $12$, which is why $(DC,dc)$ is the unique BNE there.
> Ref: Tadelis (2013), §12.2.1, Fig. 12.3 (pp. 252–255)
> Similar: Tadelis (2013), Exercise 12.3, pp. 266–267; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 3, p. 327

Q: In a static Bayesian game only one type of each player is drawn, yet a strategy must state an action for every type. Why?
- Because the others weigh every type's action by their beliefs to compute expected payoffs, so their best responses need the whole map
- Because Bayes' rule needs the action of every type to compute the player's own posterior beliefs over the other players' types
- Because otherwise the game would have no common prior, since the other players could not agree on how Nature draws the types
- Because types that were not drawn can still move later in the game, so their actions have to be planned before play begins
<!-- YW5zOjA= -->
> Player $j$ does not know $i$'s type, so $j$'s expected payoff from an action is an average over $i$'s types of what each type does. A strategy that left some type unspecified would make that average, and hence $j$'s best response, undefined. Posteriors over types come from the prior alone, not from actions, and in a static game no type moves twice.
> Ref: Tadelis (2013), §12.1.3 (pp. 249–251); Gibbons (1992), §3.1.C (pp. 150–151)
> Similar: Gibbons (1992), Problem 3.1, p. 169

## cournot

Q: Inverse demand is $P = a - q_1 - q_2$. Firm 1's marginal cost $c$ is common knowledge; firm 2's is $c_H$ with probability $\theta$ and $c_L < c_H$ with probability $1-\theta$, known only to firm 2. Quantities are chosen simultaneously. What is firm 1's Bayesian Nash equilibrium quantity, assuming all quantities are interior?
- $q_1^* = \frac{a-2c+c_H}{3}$, the complete-information quantity against the high-cost rival, its cautious benchmark
- $q_1^* = \frac{a-c-\theta c_H-(1-\theta)c_L}{2}$, the best response to the expected cost of firm 2 taken alone
- $q_1^* = \frac{a-2c+\theta c_H+(1-\theta)c_L}{3}$, the best response to the expected quantity of firm 2's two types
- $q_1^* = \frac{a-2c+\theta c_L+(1-\theta)c_H}{3}$, the best response to the expected quantity of firm 2's two types
<!-- YW5zOjI= -->
> Firm 2's types set $q_2^*(c_k) = (a-q_1^*-c_k)/2$; firm 1, linear in $q_2$, sets $q_1^* = (a-c-E[q_2^*])/2$. Averaging firm 2's conditions gives $E[q_2^*] = (a-q_1^*-\bar c)/2$ with $\bar c = \theta c_H + (1-\theta)c_L$; substituting, $q_1^* = (a-2c+\bar c)/3$. The fourth option swaps the weights; the second forgets that firm 2's output responds to $q_1$.
> Ref: Gibbons (1992), §3.1.A (pp. 144–146)
> Similar: Gibbons (1992), Problems 3.2 and 3.3, p. 169; Tadelis (2013), Exercise 12.2, p. 266

Q: With linear demand $P = a - q_1 - q_2$, firm 1's cost $c$ known, and firm 2's cost $c_H$ with probability $\theta$ and $c_L<c_H$ otherwise, privately known to firm 2, how does the high-cost type's equilibrium output compare with its complete-information Cournot output $(a-2c_H+c)/3$?
- Lower by $\frac{\theta}{6}(c_H-c_L)$, since firm 1 expands against an uncertain rival and the high-cost type gives way
- Higher by $\frac{1-\theta}{6}(c_H-c_L)$, since firm 1 produces its average output, less than against a known high-cost rival
- Higher by $\frac{\theta}{6}(c_H-c_L)$, since firm 1 produces its average output, less than against a known high-cost rival
- Higher by $\frac{1-\theta}{3}(c_H-c_L)$, since firm 1 produces its average output, less than against a known high-cost rival
<!-- YW5zOjE= -->
> $q_2^*(c_H) = \frac{a-c_H}{2} - \frac{q_1^*}{2}$ with $q_1^* = \frac{a-2c+\bar c}{3}$ and $\bar c = c_H-(1-\theta)(c_H-c_L)$, which gives $\frac{a-2c_H+c}{3} + \frac{1-\theta}{6}(c_H-c_L)$. The gap is larger the more likely the low cost ($1-\theta$), because then firm 1's average output is further below what it would produce against a known high-cost firm. The low-cost type, symmetrically, produces $\frac{\theta}{6}(c_H-c_L)$ less.
> Ref: Gibbons (1992), §3.1.A (pp. 145–146)
> Similar: Gibbons (1992), Problem 3.2, p. 169; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 5, p. 336

## threshold

Q: Two students each work (cost $c<1$) or shirk on a joint lab that succeeds if at least one works; student $i$ values success at $\theta_i^2$, with $\theta_i \sim U[0,1]$ independent and private. If student $j$ works if and only if $\theta_j \ge \hat\theta_j$, with $\hat\theta_j \ge c$, what is $i$'s best-response cutoff, and what is the symmetric equilibrium cutoff?
- $\sqrt{c/(1-\hat\theta_j)}$, so the symmetric cutoff solves $\hat\theta^{2}(1-\hat\theta) = c$ instead
- $c/\hat\theta_j$, so the symmetric cutoff is $\sqrt{c}$, the cutoff of a student working alone
- $\sqrt{c\,\hat\theta_j}$, so the symmetric cutoff is $c$, the cost of effort itself
- $\sqrt{c/\hat\theta_j}$, so the symmetric cutoff is $c^{1/3}$, above the lone cutoff $\sqrt{c}$
<!-- YW5zOjM= -->
> Working pays $\theta_i^2 - c$; shirking pays $\theta_i^2\Pr\{\theta_j \ge \hat\theta_j\} = \theta_i^2(1-\hat\theta_j)$. Work iff $\theta_i^2\hat\theta_j \ge c$, i.e. $\theta_i \ge \sqrt{c/\hat\theta_j}$. Symmetry gives $\hat\theta^3 = c$, so $\hat\theta^* = c^{1/3} > \sqrt c$: the chance that the partner works lets marginal types free-ride. The first option uses the probability that $j$ shirks where the probability that $j$ works belongs.
> Ref: Tadelis (2013), §12.2.2, eqs. (12.3)–(12.6), Claims 12.1–12.2 (pp. 255–258); MWG (1995), Example 8.E.2 (p. 256)
> Similar: Tadelis (2013), Exercise 12.9, p. 269; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 7 Ex. 6, p. 339

Q: In a Battle of the Sexes, Chris earns $2+t_c$ and Pat $1$ if both go to the Opera, Chris $1$ and Pat $2+t_p$ if both go to the Fight, and both $0$ otherwise; $t_c, t_p \sim U[0,x]$ are independent and private. Chris goes to the Opera iff $t_c \ge c$ and Pat to the Fight iff $t_p \ge p$, with equal cutoffs $c=p$ in equilibrium. What is the cutoff, and what happens to the probability that Chris goes to the Opera as $x \to 0$?
- $c = \frac{-3+\sqrt{9+4x}}{2}$, so $\Pr\{\text{Opera}\} = 1-c/x \to 2/3$, the mixed equilibrium's weight
- $c = \frac{-3+\sqrt{9+4x}}{2}$, so $\Pr\{\text{Opera}\} = c/x \to 1/3$, the mixed equilibrium's weight
- $c = \frac{3-\sqrt{9-4x}}{2}$, so $\Pr\{\text{Opera}\} = 1-c/x \to 1/2$, the uniform split of the two
- $c = x/3$, so $\Pr\{\text{Opera}\} = 1-c/x = 2/3$ for every $x$, with no need for a limit
<!-- YW5zOjA= -->
> Pat goes to the Opera with probability $p/x$, so Chris's Opera pays $\frac px(2+t_c)$ against Fight's $1-\frac px$: Opera iff $t_c \ge x/p - 3$. With $c = p$ this is $c^2+3c-x = 0$, whose positive root is the first expression. Since $\sqrt{9+4x} = 3 + \tfrac{2x}{3} + O(x^2)$, $c/x \to 1/3$ and $\Pr\{\text{Opera}\} = 1-c/x \to 2/3$, the weight in the complete-information mixed equilibrium. The second option reports the probability of Fight.
> Ref: Gibbons (1992), §3.2.A, eqs. (3.2.1)–(3.2.2) (pp. 152–154); Tadelis (2013), §12.5 (pp. 264–266)
> Similar: Gibbons (1992), Problem 3.5, p. 170; Tadelis (2013), Exercise 12.10, p. 269

Q: Harsanyi's purification reinterprets a mixed-strategy equilibrium of a complete-information game. Which reading of it is correct?
- Each player still randomizes with the mixed probabilities, and the small payoff perturbations only select which of several mixed equilibria is played
- Each player plays purely on a small private payoff perturbation, so to the opponent his action is uncertain and its frequency tends to the mixing weight
- Each player's small payoff perturbation makes one action strictly dominant, so the mixed equilibrium is replaced by a pure Nash equilibrium of the original game
- Each player observes the opponent's perturbation before choosing, so play is pure and correlated, and the mixed equilibrium is the average over those draws
<!-- YW5zOjE= -->
> In the perturbed game every type plays a pure, type-contingent action and is not indifferent; only the opponent, who does not see the perturbation, faces uncertainty. As the perturbation shrinks the cutoff converges and the induced action frequencies converge to the mixing probabilities. In Gibbons's words, what matters is not that $j$ randomizes but that $i$ is uncertain about $j$'s choice. Perturbations are private, so nobody observes the other's draw.
> Ref: Tadelis (2013), §12.5, Claim 12.3 (pp. 264–266); Gibbons (1992), §3.2.A (pp. 152–154)
> Similar: Tadelis (2013), Exercise 12.10, p. 269
