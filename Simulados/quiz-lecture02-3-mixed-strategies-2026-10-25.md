---
quiz: "Lecture 2 · Quiz 3 of 3 — Mixed strategies, the principle of indifference and existence"
tags:
  mixed: "Mixed strategies and expected payoffs"
  indiff: "The principle of indifference"
  bos: "The Battle of the Sexes in mixed strategies"
  exist: "Interpretations and Nash's theorem"
---

## mixed

Q: Player $i$'s expected payoff from a mixed strategy is $u_i(\sigma_i,\sigma_{-i})=\sum_{s_i\in S_i}\sigma_i(s_i)\,u_i(s_i,\sigma_{-i})$. What does this formula imply about mixing?
- A mixed strategy can earn more than every pure strategy in its support, since averaging smooths out the bad outcomes of each pure strategy
- A mixed strategy is optimal whenever it puts most of its weight on a best pure strategy, even if other strategies in its support earn less
- A mixed strategy never earns more than the best pure strategy in its support, and it is optimal only if every pure strategy in its support is
- A mixed strategy earns the average of the opponents' payoffs, since each player's randomization is weighted by the others' probabilities
<!-- YW5zOjI= -->
> The payoff of $\sigma_i$ is a weighted average, with non-negative weights summing to 1, of the payoffs of the pure strategies it uses, so it cannot exceed the largest of them, and it equals the maximum only if every strategy with positive weight attains that maximum. Any weight on a strictly worse strategy lowers the average: putting "most" of the weight on the best one is not enough. Averaging is over one's own pure strategies, against the fixed $\sigma_{-i}$.
> Ref: Lecture 2 slides 42–43; Tadelis (2013), Def. 6.5 (p. 105), Prop. 6.1 (p. 108)
> Similar: Gibbons (1992), Problem 1.12, p. 51; Tadelis (2013), Exercise 6.1, p. 123

Q: In a $2\times2$ game player 1 chooses U or D, and player 2 plays L with probability $q$ and R otherwise. Player 1's payoffs are $u_1(U,L)=x$, $u_1(U,R)=y$, $u_1(D,L)=z$, $u_1(D,R)=w$, with $x>z$ and $w>y$. At which $q^*$ is player 1 indifferent, and where is U the strict best response?
- $q^*=\dfrac{w-y}{(x-z)+(w-y)}$, and U is the strict best response for every $q>q^*$
- $q^*=\dfrac{x-z}{(x-z)+(w-y)}$, and U is the strict best response for every $q>q^*$
- $q^*=\dfrac{w-y}{(x-z)+(w-y)}$, and U is the strict best response for every $q<q^*$
- $q^*=\dfrac{x-y}{(x-z)+(w-y)}$, and U is the strict best response for every $q<q^*$
<!-- YW5zOjA= -->
> $u_1(U,q)=qx+(1-q)y$ and $u_1(D,q)=qz+(1-q)w$, so $u_1(U,q)-u_1(D,q)=q\,[(x-z)+(w-y)]-(w-y)$. It is zero at $q^*=\tfrac{w-y}{(x-z)+(w-y)}\in(0,1)$ and increasing in $q$ because $(x-z)+(w-y)>0$: U wins when L is likely enough. With the Battle of the Sexes payoffs for Alex ($x=2$, $y=z=0$, $w=1$), $q^*=\tfrac13$, the slides' threshold.
> Ref: Lecture 2 slides 47–48; Gibbons (1992), §1.3.B (pp. 41–44); Tadelis (2013), §6.2 (pp. 108–114)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 3 Ex. 1, pp. 86–87; MWG 8.D.6, p. 264

## indiff

Q: Which statement is the principle of indifference that characterizes a mixed-strategy Nash equilibrium $\sigma^*$?
- For every $i$, every pure strategy in $S_i$ earns the same expected payoff against $\sigma_{-i}^*$, whether or not it is in the support of $\sigma_i^*$
- For every $i$, strategies in the support of $\sigma_i^*$ earn $u_i(\sigma^*)$ against $\sigma_{-i}^*$, and strategies outside it earn no more
- For every $i$, strategies in the support of $\sigma_i^*$ earn $u_i(\sigma^*)$ against $\sigma_{-i}^*$, and strategies outside it earn strictly less
- For every $i$, the mix $\sigma_i^*$ makes player $i$ himself indifferent among all of his own strategies, so any choice is a best response
<!-- YW5zOjE= -->
> $\sigma^*$ is a Nash equilibrium iff, for every $i$, (1) $u_i(\sigma^*)=u_i(s_i,\sigma_{-i}^*)$ for every $s_i$ in the support and (2) $u_i(\sigma^*)\ge u_i(s_i,\sigma_{-i}^*)$ for every $s_i$ outside it. Strategies outside the support may tie, so "strictly less" is too strong; they need not tie either, so "every pure strategy earns the same" is too strong in the other direction. The indifference is produced by the opponents' mixes, not by player $i$'s own.
> Ref: Lecture 2 slide 44; MWG Prop. 8.D.1 (p. 250); Tadelis (2013), Prop. 6.1 (p. 108)
> Similar: Gibbons (1992), Problem 1.14, p. 51; Tadelis (2013), Exercise 6.8, p. 125

Q: In the proof that a Nash equilibrium $\sigma^*$ satisfies the principle of indifference, $s_j'$ and $s_j''$ are in the support of $\sigma_j^*$ with $u_j(s_j'',\sigma_{-j}^*)>u_j(s_j',\sigma_{-j}^*)$, and $\hat\sigma_j$ moves all the probability of $s_j'$ onto $s_j''$. By how much does player $j$'s expected payoff change?
- By $\sigma_j^*(s_j'')\,[u_j(s_j'',\sigma_{-j}^*)-u_j(s_j',\sigma_{-j}^*)]$, the weight already on $s_j''$ times the payoff gap
- By $[\sigma_j^*(s_j'')-\sigma_j^*(s_j')]\,u_j(s_j'',\sigma_{-j}^*)$, the change in the weight on $s_j''$ times its payoff
- By $u_j(s_j'',\sigma_{-j}^*)-u_j(s_j',\sigma_{-j}^*)$ in full, since the deviation replaces the worse strategy by the better one
- By $\sigma_j^*(s_j')\,[u_j(s_j'',\sigma_{-j}^*)-u_j(s_j',\sigma_{-j}^*)]$, the weight moved times the payoff gap, which is positive
<!-- YW5zOjM= -->
> Expected payoff is linear in the weights: $\hat\sigma_j$ removes $\sigma_j^*(s_j')$ from $s_j'$ and adds it to $s_j''$, so the payoff changes by $\sigma_j^*(s_j')\,u_j(s_j'',\sigma_{-j}^*)-\sigma_j^*(s_j')\,u_j(s_j',\sigma_{-j}^*)$. It is positive because $s_j'$ is in the support ($\sigma_j^*(s_j')>0$) and the gap is positive, which contradicts $\sigma_j^*$ being a best response. The full gap would be gained only if all of the weight sat on $s_j'$.
> Ref: Lecture 2 slides 45–46; Tadelis (2013), Prop. 6.1 (p. 108); MWG Prop. 8.D.1 (p. 250)
> Similar: Gibbons (1992), Problem 1.14, p. 51

Q: To check that a candidate profile $\sigma^*$ is a Nash equilibrium, why is it enough to compare $u_i(\sigma^*)$ with the payoffs of pure deviations $u_i(s_i,\sigma_{-i}^*)$, $s_i\in S_i$?
- Because a mixed deviation changes the opponents' beliefs, so only pure deviations keep $\sigma_{-i}^*$ fixed during the comparison
- Because $u_i(\sigma_i,\sigma_{-i}^*)$ is an average of the pure payoffs $u_i(s_i,\sigma_{-i}^*)$, so no mix beats the best pure deviation
- Because Nash's theorem guarantees that a pure best response exists in finite games, so mixed deviations $\sigma_i$ need not be checked
- Because the support of $\sigma_i^*$ contains every pure strategy in equilibrium, so a mixed deviation $\sigma_i$ only reshuffles weights
<!-- YW5zOjE= -->
> If no pure deviation earns more than $u_i(\sigma^*)$, then any mixed deviation, being an average of pure deviations with weights $\sigma_i(s_i)$, earns at most $u_i(\sigma^*)$: this is the "indifference implies Nash" half of the proof. A deviation by player $i$ leaves $\sigma_{-i}^*$ unchanged in any case; Nash's theorem is about existence of an equilibrium, not about how to verify one; and supports need not be full.
> Ref: Lecture 2 slides 44–45; MWG §8.D (pp. 250–251); Tadelis (2013), Def. 6.6 (p. 107)
> Similar: Tadelis (2013), Exercise 6.8, p. 125; Tadelis (2013), Exercise 6.5, p. 124

## bos

Q: Alex and Chris each choose O or F. Alex gets $\alpha>0$ at (O, O) and 1 at (F, F); Chris gets 1 at (O, O) and $\beta>0$ at (F, F); both get 0 when apart. With $p$ the probability that Alex plays O and $q$ the probability that Chris plays O, what is the mixed Nash equilibrium?
- $(p,q)=\left(\tfrac{\alpha}{1+\alpha},\tfrac{1}{1+\beta}\right)$, since each player leans toward his favourite event in proportion to how much he values it
- $(p,q)=\left(\tfrac{1}{1+\beta},\tfrac{\alpha}{1+\alpha}\right)$, since each player's mix must make the other player's two pure strategies earn the same
- $(p,q)=\left(\tfrac{\beta}{1+\beta},\tfrac{1}{1+\alpha}\right)$, since each player's mix must make the other player's two pure strategies earn the same
- $(p,q)=\left(\tfrac{\beta}{1+\beta},\tfrac{\alpha}{1+\alpha}\right)$, since each player's mix must make the other player's two pure strategies earn the same
<!-- YW5zOjI= -->
> Chris is indifferent when $u_C(O,p)=p$ equals $u_C(F,p)=\beta(1-p)$, so $p=\tfrac{\beta}{1+\beta}$. Alex is indifferent when $u_A(O,q)=\alpha q$ equals $u_A(F,q)=1-q$, so $q=\tfrac{1}{1+\alpha}$. With $\alpha=\beta=2$ this is the slides' $(p,q)=(\tfrac23,\tfrac13)$. Alex's probability depends only on Chris's payoff $\beta$, and Chris's only on Alex's $\alpha$: each mix is pinned by the other player's indifference.
> Ref: Lecture 2 slides 47–50; Tadelis (2013), §6.2 (pp. 108–114); Gibbons (1992), §1.3.B (p. 40)
> Similar: Tadelis (2013), Exercise 6.1, p. 123; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 3 Ex. 1, pp. 86–87

Q: Alex and Chris each choose O or F; Alex gets $\alpha>0$ at (O, O) and 1 at (F, F), Chris gets 1 at (O, O) and $\beta>0$ at (F, F), and both get 0 apart. Alex comes to like the opera more: $\alpha$ rises and $\beta$ is unchanged. What happens to the mixed-equilibrium probabilities $p$ (Alex plays O) and $q$ (Chris plays O)?
- $p$ stays at $\tfrac{\beta}{1+\beta}$ and $q=\tfrac{1}{1+\alpha}$ falls: Chris must go to the opera less often to keep Alex indifferent
- $p=\tfrac{\alpha}{1+\alpha}$ rises and $q$ stays at $\tfrac{1}{1+\beta}$: Alex goes to the opera more often because he now values it more
- $p$ stays at $\tfrac{\beta}{1+\beta}$ and $q=\tfrac{\alpha}{1+\alpha}$ rises: Chris goes to the opera more often in order to please Alex
- $p=\tfrac{\alpha}{1+\alpha}$ rises and $q=\tfrac{1}{1+\alpha}$ falls: both adjust, since one payoff change moves both players' mixes
<!-- YW5zOjA= -->
> Alex's mix must keep Chris indifferent, and Chris's payoffs did not change, so $p=\tfrac{\beta}{1+\beta}$ stays put. Chris's mix must keep Alex indifferent: with O now worth more to Alex, Chris must play O less often, $q=\tfrac{1}{1+\alpha}$, for Alex to remain willing to mix. The counter-intuitive part is the point: a player's own payoffs move the other player's equilibrium probability, not his own.
> Ref: Lecture 2 slide 50; Tadelis (2013), §6.2 (pp. 108–111); Gibbons (1992), §1.3.B (pp. 40–41)
> Similar: Tadelis (2013), Exercise 6.5, p. 124; Gibbons (1992), Problem 1.12, p. 51

Q: Alex and Chris each choose O or F; Alex gets $\alpha>0$ at (O, O) and 1 at (F, F), Chris gets 1 at (O, O) and $\beta>0$ at (F, F), and both get 0 apart. Which statement about the expected payoffs in the mixed Nash equilibrium is correct?
- Alex gets $\tfrac{\alpha}{1+\alpha}$ and Chris $\tfrac{\beta}{1+\beta}$, more than in the pure equilibrium each likes less, since mixing averages over both events
- Alex gets $\tfrac{1}{1+\alpha}$ and Chris $\tfrac{1}{1+\beta}$, less than in either pure equilibrium, since the players miscoordinate with positive probability
- Alex gets $\tfrac{\alpha}{1+\alpha}$ and Chris $\tfrac{\beta}{1+\beta}$, the average of the two pure equilibria, since each pure profile occurs with equal probability
- Alex gets $\tfrac{\alpha}{1+\alpha}$ and Chris $\tfrac{\beta}{1+\beta}$, less than in either pure equilibrium, since the players miscoordinate with positive probability
<!-- YW5zOjM= -->
> Alex is indifferent, so his payoff equals that of F: $1-q=1-\tfrac{1}{1+\alpha}=\tfrac{\alpha}{1+\alpha}$; likewise Chris gets $p=\tfrac{\beta}{1+\beta}$. Since $\tfrac{\alpha}{1+\alpha}<\min\{1,\alpha\}$, Alex does worse than in both pure equilibria (where he gets $\alpha$ or 1), and the same holds for Chris. With $\alpha=\beta=2$ each expects $\tfrac23$, the slides' number, because they end up apart with probability $\tfrac59$.
> Ref: Lecture 2 slide 50; Tadelis (2013), §6.2 (pp. 108–114); Gibbons (1992), §1.3.B (p. 40)
> Similar: Tadelis (2013), Exercise 6.1, p. 123

## exist

Q: A penalty taker shoots left in about 40% of a long record of penalties, and goalkeepers use that record to choose a side. Which of the lecture's interpretations of a mixed strategy does this description use?
- The population interpretation: the 40% is the share of all penalty takers in the league who prefer to shoot to the left side of the goal
- The beliefs interpretation only: the 40% must describe the goalkeeper's subjective guess, since a single player never really randomizes
- The empirical-frequency interpretation: the 40% is the long-run frequency of an action across repeated plays of the same interaction
- None of them, since a mixed strategy requires a physical randomizing device, such as a coin, to be used before each penalty is taken
<!-- YW5zOjI= -->
> The slides list three readings of $\sigma_j$: beliefs (what others believe $j$ will do), empirical frequencies (long-run frequencies of actions in repeated interactions) and population distribution (the share of a population using each action). A record of one player's past penalties is an empirical frequency; the population reading would concern many different takers. No coin is needed under any of the three readings.
> Ref: Lecture 2 slide 51; Tadelis (2013), §6.1 (p. 105); Gibbons (1992), §1.3.A (pp. 39–40)
> Similar: Tadelis (2013), Exercise 6.5, p. 124

Q: Nash's theorem (1950) states that every finite normal-form game has a Nash equilibrium in mixed strategies. Which statement is consistent with it?
- Every finite game has a Nash equilibrium in pure strategies, since a pure profile is a degenerate mixed profile and the theorem covers both
- A finite game with no pure equilibrium still has a mixed one, and pure equilibria count too, since pure profiles are degenerate mixes
- Games with infinite strategy sets, such as Cournot with continuous outputs, have no Nash equilibrium because the theorem excludes them
- Every finite game has a unique Nash equilibrium in mixed strategies, since mixing convexifies best responses and removes multiplicity
<!-- YW5zOjE= -->
> The theorem guarantees at least one equilibrium, possibly mixed; a pure profile is the degenerate mix with probability 1 on one strategy, so pure equilibria are among those it counts. It does not promise a pure equilibrium (a game where each player wants to outguess the other has none), nor uniqueness (the Battle of the Sexes has three). It is sufficient, not necessary: Cournot has infinite strategy sets and still has an equilibrium, found by solving the best responses.
> Ref: Lecture 2 slide 51; Tadelis (2013), §6.4 (p. 117); Gibbons (1992), §1.3.B (p. 45)
> Similar: MWG 8.D.6, p. 264; Gibbons (1992), Problem 1.14, p. 51
