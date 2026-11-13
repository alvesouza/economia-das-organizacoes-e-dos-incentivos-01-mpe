---
quiz: "Topic T12 · Hard conceptual quiz — Repeated games and the folk theorem"
tags:
  folk: "Feasible and individually rational payoffs, minmax and Nash reversion"
  info: "The end game and observability"
  struct: "Strategies off the path and the structure of subgame-perfect equilibria"
---

## folk

Q: In the infinite repetition of a finite stage game, with any discount factor $\delta \in (0,1)$ and perfect monitoring, what is the lowest average payoff that player $i$ can receive in any Nash equilibrium of the repeated game, subgame perfect or not?
- His stage Nash payoff, since a Nash equilibrium of the repeated game must play a stage Nash equilibrium in at least one period after every history
- His maxmin payoff, the most he can guarantee by moving first, since in each period the others may react to the action he takes in that same period
- His minmax payoff, since each period he can best-respond to what the others are prescribed to play then, which is never worth less than the minmax
- His lowest stage payoff, since a threat of the worst punishment forever is part of some Nash equilibrium, and threats off the path need not be credible
<!-- YW5zOjI= -->
> Right: player $i$ knows the history, hence what the others' strategies prescribe for the current period; best-responding to that (possibly mixed) prescription every period gives him at least $\min_{a_{-i}}\max_{a_i}u_i$ each period. So no Nash equilibrium can hold him below his minmax, and threats to do so cannot work. Wrong: nothing forces stage Nash play in a repeated-game Nash equilibrium; the stage game is simultaneous, so the others cannot react within the period, which makes maxmin the wrong bound; and the worst stage payoff is not enforceable, because the player would deviate to his best response.
> Ref: Gibbons (1992), §2.3.B, the reservation payoff $r_i$ (pp. 98–99); Tadelis (2013), §10.6, Theorem 10.1 (p. 211); MWG (1995), Ch. 12 App. A (pp. 417–422)

Q: A folk theorem supports a payoff that gives player 1 less than his stage Nash payoff but more than his minmax, so Nash reversion cannot deter him and the others must hold him to his minmax after a deviation. Holding him there is costly to the punishers themselves. What must the punishment phase look like for the profile to be subgame perfect?
- It must be finite and followed by a reward for the punishers who carried it out, so that inflicting it is itself a best response at every history of that phase
- It must last forever, since only a permanent minmax phase is harsh enough to offset the deviation gain when the target payoff lies below the stage Nash payoff
- It can be any profile that holds player 1 to his minmax, since subgame perfection checks only the deviator's incentives, and the punishers simply follow the strategy
- It must be a stage Nash equilibrium in which player 1 happens to get his minmax payoff, since only stage equilibria are credible punishments in a subgame
<!-- YW5zOjA= -->
> Right: a minmax profile is usually not a stage equilibrium, so each punisher is tempted to stop; the profile stays subgame perfect only if carrying out the punishment is rewarded, by a return to a good path that a shirking punisher would lose. This is the stick-then-carrot logic of Fudenberg and Maskin that lets reservation payoffs replace stage Nash payoffs. Wrong: a permanent minmax phase is exactly what punishers would abandon; subgame perfection checks every player at every history, punishers included; and if a stage equilibrium already gave player 1 his minmax, Nash reversion would suffice and the question would not arise.
> Ref: Gibbons (1992), §2.3.B, on Fudenberg and Maskin (1986) (p. 99); Gibbons (1992), §2.3.C, Abreu's two-phase punishment (pp. 104–106); Lecture 5 slides, slide 15 (carrot and stick)

Q: Under Nash reversion, a stationary path paying player $i$ the amount $v_i$ each period is sustainable iff $v_i \ge (1-\delta)d_i + \delta e_i$, where $d_i$ is his best one-shot deviation payoff and $e_i < v_i \le d_i$ his stage Nash payoff. What happens to the required $\delta$ as the target $v_i$ falls toward $e_i$?
- It falls toward zero, since a target close to the stage Nash payoff is nearly self-enforcing and needs almost no future reward to be sustained
- It rises toward one, since the cutoff $(d_i - v_i)/(d_i - e_i)$ tends to one: the per-period wedge over the punishment shrinks as the temptation grows
- It stays constant, since the cutoff depends only on the deviation gain and the punishment, $d_i$ and $e_i$, which the choice of target does not affect
- It rises toward $1/2$, since half the wedge $d_i - e_i$ must be covered by the future, and a target at $e_i$ leaves exactly that half uncovered
<!-- YW5zOjE= -->
> Right: solving the inequality gives $\delta \ge (d_i - v_i)/(d_i - e_i)$, which tends to 1 as $v_i \to e_i$. With $d_i = 5$ and $e_i = 1$: $v_i = 4$ needs $0.25$, $v_i = 2$ needs $0.75$, $v_i = 1.1$ needs $0.975$. This is why the folk theorem says "for $\delta$ sufficiently close to 1": the closer the target to the stage Nash payoff, the thinner the wedge that pays for the deterrence. Wrong: a target near the stage Nash payoff is not self-enforcing, since the gain from deviating, $d_i - v_i$, stays large while the loss from punishment, $v_i - e_i$, shrinks; the cutoff depends on $v_i$; and there is no $1/2$ rule.
> Ref: Tadelis (2013), §10.6, Theorem 10.1 and the "wedge" argument (pp. 211–212); Lecture 5 slides, slide 29
> Similar: Tadelis (2013), Exercise 10.3, p. 215

## info

Q: A prisoner's dilemma, whose only stage equilibrium is mutual defection, is repeated until a random date: after each period up to period 100 the game continues with positive probability, and it surely ends after period 100. Players know this distribution. Which subgame-perfect outcomes are possible?
- Cooperation in the early periods, for continuation probabilities close to one, since no period before 100 is known to be the last, and the end date is uncertain
- Cooperation until close to period 100, since the expected number of remaining periods stays large until then and acts like a high discount factor
- Cooperation in every period under grim trigger, provided the average continuation probability exceeds the usual cutoff $(T-R)/(T-P)$ for the game
- Mutual defection in every period, since period 100 is surely the last if it is reached, and backward induction from it unravels every earlier period
<!-- YW5zOjM= -->
> Right: if period 100 is reached, it is commonly known to be the last, so both defect there after every history; then period 99 has a fixed continuation and both defect, and so on back to period 1, exactly as with a known horizon. The slide's condition, "no one knows which period is the last one", must be read as "there is no period at which the game is known to end"; a known upper bound restores such a period. Wrong: the first two options treat a bounded random end like geometric continuation; the grim-trigger cutoff applies to a game with no last period.
> Ref: Lecture 5 slides, slides 9, 18 and 22; Tadelis (2013), §10.1, Proposition 10.1 (pp. 190–192) and §10.2.1, footnote 4 (p. 194)

Q: Two players repeat a prisoner's dilemma forever with a discount factor $\delta$ close to 1, but neither ever observes the other's actions, and each player's own stage payoffs are revealed only when the game ends. What can a Nash equilibrium of this repeated game sustain?
- Mutual cooperation under grim trigger, since a patient player still prefers cooperating forever to the one-period temptation, whatever he observes about play
- Mutual cooperation in a fraction of periods close to one, since the folk theorem needs only that the target payoff be feasible and individually rational
- Cooperation in the early periods only, since without monitoring each player must at some point test the other by defecting, which ends cooperation
- Only defection in every period, since nothing a player does can change the other's later play, so each period is a one-shot game with a dominant action
<!-- YW5zOjM= -->
> Right: a strategy can condition only on what its owner observes, here nothing but his own past actions. So player $j$'s future play cannot respond to player $i$'s current action, and that action affects only $i$'s current payoff, where defection strictly dominates. Every Nash equilibrium therefore defects in every period. Wrong: grim trigger needs a trigger, that is, an observed deviation; the folk theorem assumes that past actions are observed (perfect monitoring), which is exactly what fails here; and "testing" is impossible, since nothing would be learned.
> Ref: Lecture 5 slides, slide 3 ("players observe past actions") and slide 26; Tadelis (2013), §10.2.2 (p. 195) and §10.4 on imperfect monitoring (p. 204); Gibbons (1992), §2.3.C (pp. 106–107)

Q: A finite stage game has a unique Nash equilibrium, which pays each player strictly more than his minmax payoff, and it is repeated a known number $T$ of times. Which statement about the repeated game is correct?
- Its unique subgame-perfect path plays the stage equilibrium throughout, but for large $T$ some Nash equilibria sustain other play early, backed by late minmax threats
- Its Nash and subgame-perfect equilibria coincide, since with a unique stage equilibrium any threat to play something else in the final periods is ruled out by unravelling
- Its subgame-perfect equilibria can sustain other play early for $T$ large, since minmax punishments become credible once the gap over the minmax is large enough
- Neither its Nash nor its subgame-perfect equilibria can sustain other play, since a unique stage equilibrium is always also the minmax outcome of the stage game
<!-- YW5zOjA= -->
> Right: subgame perfection unravels from the last period (Tadelis's Proposition 10.1). A Nash equilibrium, however, needs optimality only on the path, so an untested threat to minmax a deviator in the final periods costs him the gap between the stage Nash payoff and his minmax in each of them, and with enough such periods it outweighs any one-shot gain. A small example checked in Python: a unique stage equilibrium paying $(2,2)$, minmax payoffs of $0$, and mutual cooperation worth $4$ in period 1 of a two-period game. In the prisoner's dilemma the stage Nash payoff equals the minmax, which is why every Nash equilibrium there defects throughout. Wrong: Nash and SPE differ precisely through off-path threats; minmax threats are not credible in the last period; and a unique equilibrium need not be the minmax.
> Ref: Tadelis (2013), §10.1, Proposition 10.1 (pp. 190–192); Lecture 5 slides, slides 9–10; Gibbons (1992), §2.3.A (pp. 84–88) and the further reading on Benoit and Krishna (p. 130)

## struct

Q: In the repeated prisoner's dilemma with stage payoffs $(M,m) = (4,4)$, $(F,m) = (5,-1)$, $(M,f) = (-1,5)$, $(F,f) = (1,1)$ and discount factor $\delta$, both players use tit-for-tat. After a history in which player 2 alone defected last period, tit-for-tat tells player 1 to defect now. When is that a best response?
- For every $\delta$, since defecting against a cooperator pays $5 > 4$ today, and tit-for-tat then returns both players to mutual cooperation from the next period on
- Only for $\delta \le 1/5$, since punishing starts the cycle $Fm, Mf, \dots$ worth $(5-\delta)/(1+\delta)$, while forgiving restores $(M,m)$ forever, worth $4$
- Only for $\delta \ge 1/5$, since a patient player values the deterrent effect of punishing, which stops player 2 from defecting again in later periods
- Only for $\delta \ge 1/2$, since punishing yields $(-1+5\delta)/(1+\delta)$ against $1$ from switching to permanent defection, as on the path of grim trigger
<!-- YW5zOjE= -->
> Right: after $Mf$, tit-for-tat has player 1 play $F$ while player 2 plays $m$, and the echo $Fm, Mf, Fm, \dots$ follows, worth $(5-\delta)/(1+\delta)$; forgiving with $M$ meets $m$ and restarts cooperation forever, worth $4$. Punishing is optimal iff $5 - \delta \ge 4 + 4\delta$, i.e. $\delta \le 1/5$, while the on-path check needs $\delta \ge 1/5$ and the check after $Fm$ needs $\delta \ge 1/2$, so tit-for-tat is a subgame-perfect equilibrium for no $\delta$ (checked numerically). Patience helps on the path and hurts off it: punishing the opponent also punishes yourself. Wrong: tit-for-tat does not return to cooperation after a punishment; deterrence of the past is worthless once a deviation has happened; the $\delta \ge 1/2$ condition belongs to the history $Fm$.
> Ref: Lecture 5 slides, slides 30–32; Tadelis (2013), §10.3, one-stage deviation principle (pp. 198–200)

Q: A stage game has a non-equilibrium profile $(M,m)$ paying $4$ to each player, a best one-shot deviation from it paying $5$, and two stage equilibria paying $3$ and $1$ to each. It is repeated $T$ times with no discounting. As $T$ grows, what can subgame-perfect equilibria sustain?
- $(M,m)$ in every period but the last, with the good equilibrium last and the bad one forever after any deviation, so the average payoff tends to $4$
- $(M,m)$ in the first period only, since the carrot and the stick differ by $3 - 1 = 2$ in one period, which can offset only a single deviation gain of $1$
- $(M,m)$ in the first half of the game, since each cooperative period must be backed by a later period of the good equilibrium that serves as its own carrot
- No $(M,m)$ at all once $T > 2$, since the end game of a long finitely repeated game unravels whenever a non-equilibrium profile is on the path
<!-- YW5zOjA= -->
> Right: a deviation in period $t < T$ gains $1$ and loses $3$ in every remaining cooperative period plus $3 - 1 = 2$ in the last, so even in period $T-1$ the loss $2$ exceeds the gain; the bad equilibrium is a stage equilibrium, so the punishment is credible after every history. One final period of carrot supports every earlier period, and the average $(4(T-1)+3)/T \to 4$. Wrong: the same last-period carrot backs every earlier period, not just one, because a deviation forfeits it once; a carrot per cooperative period is not needed; unravelling needs a unique stage equilibrium.
> Ref: Lecture 5 slides, slides 11–16; Tadelis (2013), §10.1 (pp. 190–192); Gibbons (1992), §2.3.A (pp. 84–88)

Q: In an infinitely repeated game with discount factor $\delta$, let $W$ be the set of subgame-perfect equilibrium payoff vectors. A strategy profile prescribes some continuation after a deviation by player $i$. Which statement about the harshest credible punishment of player $i$ is correct?
- It is always the stage Nash payoff repeated forever, since a continuation that gives player $i$ less would make the punishers deviate to the stage equilibrium
- It is player $i$'s minmax payoff for every $\delta$, since subgame perfection imposes no restriction on what is played after a deviation has occurred
- It is the lowest payoff of player $i$ within $W$ itself, since every continuation of a subgame-perfect profile is again a subgame-perfect equilibrium
- It is the lowest payoff of player $i$ among all feasible payoffs, since the game's stationarity lets any feasible path be prescribed after a deviation
<!-- YW5zOjI= -->
> Right: every subgame of the infinitely repeated game is the game itself, and a profile is subgame perfect iff its continuation after every history is a Nash equilibrium there, in fact a subgame-perfect one. So any punishment is itself an element of $W$, and the harshest is the worst payoff for $i$ in $W$; Abreu's two-phase strategies show it can lie below the stage Nash payoff. Wrong: Nash reversion is one credible punishment, not always the harshest; subgame perfection restricts play after deviations most of all; and a feasible path that is not an equilibrium would not be carried out.
> Ref: Lecture 5 slides, slides 23–24 (continuation strategies); Gibbons (1992), §2.3.C, Abreu's two-phase punishments (pp. 104–106); MWG (1995), Ch. 12 App. A (pp. 417–422)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 3, p. 282

Q: A stage game has two Nash equilibria, $a$ and $b$. In its infinite repetition with discount factor $\delta$, consider the profile that plays $a$ in odd periods and $b$ in even periods after every history, ignoring what was played before. For which $\delta$ is it subgame perfect?
- Only for $\delta$ above a cutoff, since a player who prefers $a$ is tempted to deviate in even periods, and only the threat of losing future $a$ periods deters him
- For no $\delta$, since a profile that ignores history cannot punish deviations, so some player can always gain by deviating from the less preferred equilibrium
- Only for $\delta$ below a cutoff, since patient players would coordinate on their preferred equilibrium forever, which the alternating profile does not allow
- For every $\delta$, since play ignores the history, so only the current payoff matters in each period, and there each stage equilibrium is a best response
<!-- YW5zOjM= -->
> Right: if no future action responds to today's, a one-stage deviation changes only today's payoff, and today the prescribed profile is a stage Nash equilibrium, so no deviation pays, after any history and for any $\delta$. This extends Tadelis's Proposition 10.2 from one stage equilibrium to any history-independent sequence of them. Wrong: no threat is needed because nothing on the path is tempting; deviating from $b$ in an even period cannot pay, since $b$ is a stage equilibrium; and "coordinating on the preferred equilibrium" is not a unilateral deviation.
> Ref: Tadelis (2013), Proposition 10.2 (p. 196); Lecture 5 slides, slide 10
> Similar: Gibbons (1992), Exercise 2.12, p. 135
