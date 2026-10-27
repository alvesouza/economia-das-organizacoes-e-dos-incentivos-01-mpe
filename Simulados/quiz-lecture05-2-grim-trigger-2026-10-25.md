---
quiz: "Lecture 5 · Quiz 2 of 3 — Discounting, grim trigger and the critical discount factor"
tags:
  disc: "Discounting, average payoffs, histories and strategies"
  grim: "Grim trigger and the one-stage deviation principle"
  crit: "The critical discount factor and its comparative statics"
---

## disc

Q: After each period a relationship continues with probability $p \in (0,1)$, and players also discount time by a factor $\beta \in (0,1)$ per period. Which discount factor enters the repeated-game payoff, and what is the probability that the game is played forever?
- $p + \beta - p\beta$, and the probability of playing forever is zero, since some period is certain to be the last one
- $p\beta$, and the probability of playing forever is zero, although at every period another period is still possible
- $p\beta$, and the probability of playing forever is $p/(1-p)$, which is the expected number of periods still to come
- $\beta(1-p)$, and the probability of playing forever is one, since each period is followed by another with certainty
<!-- YW5zOjE= -->
> A payoff in period $t$ is received only if the game survives $t-1$ continuations, with probability $p^{t-1}$, and is worth $\beta^{t-1}$ in time terms, so its weight is $(p\beta)^{t-1}$. The probability of reaching period $t$, $p^{t-1}$, tends to zero, so the game ends in finite time with probability one; what matters is that no period is known to be the last. $p/(1-p)$ is the expected number of further periods, not a probability. Gibbons writes the same object as $\delta = (1-p)/(1+r)$ with $p$ the end probability.
> Ref: Tadelis (2013), §10.2.1 and fn. 4 (pp. 193–194); Gibbons (1992), §2.3.B (p. 90); Cabral (2017), §7.3 (p. 174)
> Similar: Tadelis (2013), Exercise 10.9, pp. 218–219

Q: A payoff stream pays $x$ in odd periods $t = 1, 3, 5, \dots$ and $y$ in even periods. With discount factor $\delta \in (0,1)$, what is its average payoff $(1-\delta)\sum_{t\ge1}\delta^{t-1}v^t$?
- $(x+y)/2$, the simple mean of the two payoffs, since each of them is received in exactly half of all the periods
- $(x+\delta y)/(1-\delta^{2})$, two geometric series in $\delta^{2}$, one per parity, with the $x$ terms undiscounted
- $(\delta x+y)/(1+\delta)$, two geometric series in $\delta^{2}$, with the even-period payoff received before the odd one
- $(x+\delta y)/(1+\delta)$, two geometric series in $\delta^{2}$, with $1-\delta^{2} = (1-\delta)(1+\delta)$ cancelling
<!-- YW5zOjM= -->
> Split by parity: $x(1+\delta^2+\delta^4+\dots) + y(\delta+\delta^3+\dots) = (x+\delta y)/(1-\delta^2)$, which is the present value. Multiplying by $1-\delta$ and using $1-\delta^2=(1-\delta)(1+\delta)$ gives $(x+\delta y)/(1+\delta)$. The simple mean is only the limit as $\delta \to 1$; the second option is the present value, not the average. In Tadelis's alternating path, $x=5$ and $y=-1$ give $(5-\delta)/(1+\delta)$.
> Ref: Tadelis (2013), Def. 10.3 (p. 194), §10.6 alternating path (pp. 212–213)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 9, p. 305

Q: In the infinitely repeated prisoner's dilemma with discount factor $\delta \in (0,1)$, consider the profile in which each player defects after every history. For which $\delta$ is it a subgame-perfect equilibrium, and why?
- For every $\delta$, since play ignores the history, so each period is a one-shot game in which defecting is a best response
- Only for $\delta$ below the cooperation threshold, since above it a player gains by switching to cooperation for good
- For every $\delta$ on the path, but after a history with cooperation a player gains by cooperating to restart it
- For no $\delta$, since a patient player can always gain by cooperating once to signal willingness to cooperate later
<!-- YW5zOjA= -->
> If the opponent's play does not depend on the history, today's action cannot change tomorrow, so each period is strategically a one-shot game and the stage Nash equilibrium is a best response in it, after every history. This is Tadelis's Prop. 10.2: a history-independent stage equilibrium is an SPE of $G(\delta)$ for any $\delta < 1$. A one-period cooperation is met by defection forever, so it only costs the deviator today. Fink forever is always available as a stick.
> Ref: Tadelis (2013), Prop. 10.2 (p. 196), p. 197
> Similar: Gibbons (1992), Exercise 2.12, p. 135

## grim

P: In the infinitely repeated prisoner's dilemma with discount factor $\delta \in (0,1)$, mutual cooperation pays $R$ to each player, mutual defection $P$ to each, and a defector facing a cooperator gets $T$ while the cooperator gets $S$, with $T > R > P > S$. Both players use grim trigger: cooperate in period 1 and as long as every past outcome was mutual cooperation; otherwise defect forever.

Q: Which inequality, in present values, is the on-path condition that no player gains from a one-stage deviation?
- $R/(1-\delta) \ge T + \delta S/(1-\delta)$, since after the deviation the deviator is held at the sucker payoff for good
- $R + \delta R \ge T + \delta P$, since the deviation is punished in the period that follows it, and that period carries the cost
- $R/(1-\delta) \ge T + \delta P/(1-\delta)$, since the deviation earns the temptation once and mutual defection afterwards
- $R \ge T + \delta P/(1-\delta)$, since the cooperative stage payoff is compared with the deviation's discounted value
<!-- YW5zOjI= -->
> Conforming gives $R$ forever, worth $R/(1-\delta)$. Deviating gives $T$ today; the rival then defects forever and defecting is the best reply, so the deviator gets $P$ from tomorrow on, worth $\delta P/(1-\delta)$. With Tadelis's numbers this is (10.3), $4 + 4\delta/(1-\delta) \ge 5 + \delta/(1-\delta)$, i.e. $\delta \ge 1/4$. The second option counts only one period of loss; the fourth mixes an average payoff with a present value.
> Ref: Tadelis (2013), §10.3, (10.3) (pp. 198–200); Gibbons (1992), (2.3.1) (pp. 90–92)
> Similar: Tadelis (2013), Exercise 10.2, p. 215; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 1, p. 274

Q: After a history in which someone has already defected, what does the one-stage deviation check require of grim trigger, and for which $\delta$ does it hold?
- Defecting yields $P$ and cooperating $S$, with the same continuation after both, so the check holds for every $\delta$
- Defecting yields $P$ and cooperating $S$, but cooperating restores the path, so it holds iff $\delta \le (T-R)/(T-P)$
- Defecting yields $P$ and cooperating $R$, as the rival cooperates in reply, so it holds iff $\delta \ge (R-P)/(T-P)$
- No check is needed, since that history is off the equilibrium path, and off-path play does not enter the payoffs at all
<!-- YW5zOjA= -->
> In the punishment state the rival defects now and forever whatever happens, so cooperating today yields $S < P$ and changes nothing tomorrow. Deviating loses $P - S$ with no future gain, for every $\delta$: the threat is credible because it is Prop. 10.2's equilibrium. Off-path histories are subgames, and subgame perfection requires the check there; it is trivial here, but it has to be made.
> Ref: Tadelis (2013), §10.3 (p. 199), Def. 10.5 (p. 196); Gibbons (1992), §2.3.B (p. 95)
> Similar: Tadelis (2013), Exercise 10.2, p. 215

Q: Why is it enough to check single deviations at single histories, even though a deviation from grim trigger could change play in infinitely many periods?
- Because any profitable deviation must start with a gain in the first period, and grim trigger removes every first-period gain
- Because players use stationary strategies, so a deviation that pays once must pay at every history, which one check detects
- Because the set of histories is countable, so checking one representative history per period exhausts all possible deviations
- Because discounting makes payoffs continuous at infinity, so a profitable infinite deviation implies a profitable finite one
<!-- YW5zOjM= -->
> Changes after period $N$ are worth at most a multiple of $\delta^N$, so if an infinite deviation is profitable, some deviation that differs in finitely many periods is too, and a finite deviation can be broken into one-stage deviations as in Theorem 9.1. That is Tadelis's Prop. 10.3 and footnote 6. Without discounting the argument fails. A profitable deviation need not gain in its first period, which rules out the first option.
> Ref: Tadelis (2013), Prop. 10.3 and fn. 6 (pp. 198–199), Theorem 9.1 (p. 185)
> Similar: Gibbons (1992), Exercise 2.12, p. 135

Q: In the finitely repeated version of this game cooperation unravels for lack of a reward. What plays the role of the carrot when the game is infinitely repeated?
- The stage Nash equilibrium played forever, since it pays $P$ to each player and is an SPE for every discount factor
- The grim-trigger profile itself, since every subgame after mutual cooperation is again the whole game $G(\delta)$
- A side payment of $T-R$ from the cooperator to the would-be defector, which the infinite horizon makes credible
- The possibility that the game ends, since the continuation probability $\delta$ rewards those still cooperating
<!-- YW5zOjE= -->
> Tadelis calls it a bootstrap: the stick is defection forever (an SPE by Prop. 10.2), and the carrot is the proposed cooperative equilibrium, which supports itself. The argument is circular but not inconsistent, because every subgame of $G(\delta)$ is identical to the whole game, so "cooperate forever from tomorrow" is the very object being checked. From one stage equilibrium the infinite horizon creates multiple equilibria of the repeated game.
> Ref: Tadelis (2013), §10.3 (pp. 197–198, 200); Gibbons (1992), §2.3.B (p. 94)
> Similar: Tadelis (2013), Exercise 10.7, pp. 217–218

## crit

Q: In a symmetric prisoner's dilemma with payoffs $T > R > P > S$, grim trigger is a subgame-perfect equilibrium iff $\delta \ge \delta^* = (T-R)/(T-P)$. How does $\delta^*$ respond to each payoff?
- It rises with $T$, falls with $R$, falls with $P$, and is unaffected by $S$, since a higher $P$ makes the stick harsher
- It falls with $T$, rises with $R$, rises with $P$, and is unaffected by $S$, since the gain shrinks as $T$ rises
- It rises with $T$, falls with $R$, rises with $P$, and is unaffected by $S$, since no one is the sucker on the path
- It rises with $T$, falls with $R$, rises with $P$, and falls with $S$, since a higher $S$ softens the cost of trusting
<!-- YW5zOjI= -->
> $\partial\delta^*/\partial T = (R-P)/(T-P)^2 > 0$, $\partial\delta^*/\partial R = -1/(T-P) < 0$, $\partial\delta^*/\partial P = (T-R)/(T-P)^2 > 0$. A larger temptation needs more future to offset it, a better reward raises the per-period loss, and a higher $P$ is a milder punishment. $S$ is absent: on the grim-trigger path both cooperate, and in punishment both defect, so no one ever gets $S$. Tadelis ($S=-1$) and Gibbons ($S=0$) both get $1/4$.
> Ref: Tadelis (2013), (10.3) (p. 200), (10.5) (p. 202); Gibbons (1992), §2.3.B (pp. 90–92)
> Similar: Tadelis (2013), Exercise 10.3, pp. 215–216

Q: In a symmetric prisoner's dilemma with payoffs $T > R > P > S$, write the discount factor as $\delta = 1/(1+r)$ with $r$ the per-period interest rate. For which $r$ is grim trigger a subgame-perfect equilibrium?
- $r \le (R-P)/(T-R)$, the per-period loss from punishment over the one-time gain from deviating
- $r \le (T-R)/(R-P)$, the one-time gain from deviating over the per-period loss from punishment
- $r \le (T-P)/(T-R)$, the temptation net of punishment over the one-time gain from deviating
- $r \ge (R-P)/(T-R)$, the per-period loss from punishment over the one-time gain from deviating
<!-- YW5zOjA= -->
> $1/(1+r) \ge (T-R)/(T-P)$ iff $1+r \le (T-P)/(T-R)$ iff $r \le (T-P)/(T-R) - 1 = (R-P)/(T-R)$. Cooperation survives interest rates up to the ratio of the per-period loss to the one-time gain; with Tadelis's numbers that ratio is $3$, so any rate up to 300% per period. The third option forgets to subtract 1, and the fourth reverses the inequality: a higher interest rate means less patience.
> Ref: Tadelis (2013), (10.3) (p. 200); Gibbons (1992), §2.3.B (pp. 89–90)
> Similar: Tadelis (2013), Exercise 10.5, pp. 216–217

Q: In an $n$-player game, a stationary profile pays player $i$ the amount $x_i$ per period; $i$'s best one-stage deviation pays $d_i$, and the stage Nash punishment pays $e_i$, with $d_i \ge x_i > e_i$. Under Nash reversion, when is the profile a subgame-perfect equilibrium?
- $\delta \ge \min_i (d_i-x_i)/(d_i-e_i)$, since deterring the most patient player is enough to hold the others in line
- $\delta \ge \max_i (d_i-x_i)/(x_i-e_i)$, the largest ratio of each one-time gain to the per-period loss in reversion
- $\delta \ge \tfrac{1}{n}\sum_i (d_i-x_i)/(d_i-e_i)$, since the common discount factor must cover the average temptation
- $\delta \ge \max_i (d_i-x_i)/(d_i-e_i)$, since every player must be deterred, and each ratio is strictly below one
<!-- YW5zOjM= -->
> Each player conforms iff $x_i/(1-\delta) \ge d_i + \delta e_i/(1-\delta)$, i.e. $\delta \ge (d_i-x_i)/(d_i-e_i)$; this is Tadelis's (10.5) with $v_i^c, v_i^d, v_i^*$. All players must be deterred at once, so $\delta$ must exceed the largest threshold. Because $x_i > e_i$, each ratio is below one, so a patient enough $\delta < 1$ exists. The second option divides by $x_i - e_i$ and can exceed one.
> Ref: Tadelis (2013), (10.5) (p. 202); Gibbons (1992), Appendix 2.3.B (pp. 100–102); MWG (1995), Lemma 12.AA.1 (p. 418)
> Similar: Gibbons (1992), Exercise 2.16, p. 136; MWG (1995), Exercise 12.AA.1, p. 420
