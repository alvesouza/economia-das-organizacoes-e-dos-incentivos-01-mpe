---
quiz: "Topic T10 · Multistage games, carrot and stick, one-stage deviation — hard conceptual quiz (10 questions; Lecture 5, Tadelis Ch. 9)"
tags:
  cs: "Carrot and stick: what the later stages must offer"
  msg: "Multistage games: observability and conditional play"
  osd: "The one-stage deviation principle and its limits"
---

## cs

Q: In a two-stage game with observed stage-1 outcomes, every Nash equilibrium of the stage-2 game, pure or mixed, gives player 1 the same payoff, but they differ for player 2. The stage-1 target profile is not a stage Nash equilibrium. When can it be played in a subgame-perfect equilibrium?
- Whenever player 2 is patient enough, since rewarding and punishing player 2 in stage 2 also disciplines player 1 through the profile they play together
- Only if player 1 has no profitable stage-1 deviation, since stage 2 can reward or punish player 2 but gives player 1 the same payoff whatever happened
- Never, since a carrot and a stick need two stage-2 equilibria that differ in total payoff, and the total cannot be moved by player 1's own actions
- Only if player 2 has no profitable stage-1 deviation, since player 2 is the one whose stage-2 payoff varies and so the one the future must leave alone
<!-- YW5zOjE= -->
> In any SPE stage 2 is played at a stage Nash equilibrium after every history, and by assumption all of them give player 1 the same payoff; so player 1's continuation value is a constant, and her stage-1 choice must be a best reply within stage 1 alone. Player 2 can be rewarded and punished, so her temptation can be handled if she is patient enough. The target is therefore supportable only when it already gives player 1 no profitable deviation. Totals are irrelevant (third option): what matters is the gap between carrot and stick for the player who is tempted. The fourth option has the logic backwards.
> Ref: Tadelis (2013), §9.4, the two requirements for a carrot and a stick (pp. 182–184); Lecture 5 slides 10–16
> Similar: Listas/pratica-lecture-05 #17 (Tadelis 9.1)

Q: Stage 2 is the Battle of the Sexes: (O, O) pays Alex 2 and Chris 1, (F, F) pays Alex 1 and Chris 2, and the mixed equilibrium pays each 2/3. If (O, O) is promised after the stage-1 target, how can a stage-1 deviation by Chris be punished?
- Only by switching to the mixed equilibrium, the one stage-2 equilibrium worse for Chris than (O, O), which costs her 1/3 in stage 2
- By switching to (F, F), the equilibrium that Alex dislikes, since punishing the pair as a whole deters whichever of the two is tempted
- By playing a non-equilibrium profile that gives Chris 0, which is credible because her deviation already broke the agreement of stage 1
- It cannot be, since (O, O) is already Chris's worst pure equilibrium, and mixed equilibria cannot serve as punishments in an SPE
<!-- YW5zOjA= -->
> A stick must be a Nash equilibrium of the stage-2 game that is worse for the deviator than the carrot. Against Chris's carrot of 1, (F, F) gives her 2, a reward, not a punishment; the mixed equilibrium gives her 2/3, so it is the only stick, and it deters her if her stage-1 gain is at most $\delta/3$. A mixed equilibrium is a perfectly good continuation in an SPE, which is why Tadelis notes a third SPE built on the mixed equilibrium of the Revenge Game (fourth option). A non-equilibrium punishment is not credible in the last stage (third option).
> Ref: Lecture 3 slides 13–16 (mixed Battle of the Sexes, 2/3 each); Lecture 5 slides 11–16; Tadelis (2013), §9.4 and footnote 4 (pp. 180–184)
> Similar: Listas/pratica-lecture-05 #13 (Tadelis 9.4)

Q: Can a two-stage carrot-and-stick equilibrium ask a player to accept the sucker's payoff in stage 1, cooperating while the other player defects?
- No, since a player who is asked to accept her worst stage-1 payoff always gains by defecting, whatever happens in the stage that follows
- No, since subgame perfection requires every player to get at least her stage-Nash payoff in each stage, and the sucker's payoff violates this
- Yes, if her one-stage gain from defecting is at most the discounted gap between the stage-2 equilibria that follow; Tadelis needs a factor of 2/3
- Yes, but only without discounting, since the sucker's loss in stage 1 must be fully repaid in stage 2, which no discount factor below 1 allows
<!-- YW5zOjI= -->
> In the Prisoner-Revenge game Tadelis supports (F, m) in stage 1, with (L, l), worth 0 to each, after (F, m) and (G, g), worth $-3$ to each, otherwise. Player 2's incentive is $-1 + 0\cdot\delta \ge 1 - 3\delta$, so $\delta \ge 2/3$: her gain from defecting is 2, more than the gain of 1 from leaving (M, m), so more patience is needed. The incentive constraints are about deviations, not about stage-by-stage participation (second option), and repayment is not required at all, only deterrence (fourth option).
> Ref: Tadelis (2013), §9.4 (pp. 183–184)
> Similar: Listas/pratica-lecture-05 #19 (Tadelis 9.6)

Q: Why does cooperation in a finitely repeated prisoner's dilemma need a second stage-game equilibrium, while in the infinitely repeated game grim trigger sustains it with a unique one?
- Because the infinite game has a higher discount factor, which makes any punishment severe enough, while a finite game caps patience below what is needed
- Because grim trigger uses a non-Nash punishment, which is credible in the infinite game since no one ever reaches the period where it must be carried out
- Because with infinitely many periods the stage game acquires new equilibria, so the infinite game does have a second stage equilibrium after all
- Because a known last stage must be stage Nash, so rewards must come from equilibrium multiplicity; with no last stage, future cooperation is the reward
<!-- YW5zOjM= -->
> In a finite game the last stage is played at a stage Nash equilibrium after every history, so with a unique one the last stage cannot reward or punish, and the argument unravels backwards; a second equilibrium is what creates a carrot and a stick. With no last period, continuation values come from future play itself: grim trigger's carrot is continued cooperation, and its stick is the stage equilibrium (F, f) forever, which is a Nash punishment (second option). The discount factor is a parameter of both games (first option), and repetition never changes the stage game's equilibria (third option).
> Ref: Tadelis (2013), §9.4, Props. 9.2–9.3 (pp. 181–182), §10.3 (pp. 196–201); Lecture 5 slides 9–10, 16–18 and 28–29
> Similar: Listas/pratica-lecture-05 #11 (Gibbons 2.10)

## msg

Q: In a two-stage game, a profile prescribes a stage Nash equilibrium in each stage after every history, but which stage-2 equilibrium is played depends on stage-1 actions. Is it necessarily subgame perfect?
- Yes, since Tadelis shows that any sequence of stage Nash equilibria is subgame perfect, whatever the discount factor and however it is selected
- No, since a stage-1 deviation may now trigger an equilibrium the deviator prefers, so stage-Nash play in stage 1 can stop being a best reply
- Yes, since each stage-2 subgame is played at a Nash equilibrium, and the stage-1 profile is also a Nash equilibrium of the stage-1 game
- No, since a profile that conditions on history must use non-Nash play somewhere, and such play is never sequentially rational in a subgame
<!-- YW5zOjE= -->
> Tadelis's Prop. 9.1 covers *unconditional* strategies, which play the same stage equilibrium whatever happened, and so remove "any strategic link between stages". Once the selection depends on history, a player's stage-1 action also moves her continuation value: if deviating in stage 1 triggers her favourite stage-2 equilibrium, the stage-Nash action can stop being optimal. So the third option checks each stage separately and misses the link, and the first misreads the proposition. Conditioning on history needs no non-Nash play (fourth option); carrot-and-stick profiles use only stage equilibria in the last stage.
> Ref: Tadelis (2013), §9.4, Prop. 9.1 (pp. 180–181); Lecture 5 slides 10–13
> Similar: Listas/pratica-lecture-05 #12 (Tadelis 9.2)

Q: In a two-stage game, neither player observes the other's stage-1 action before stage 2. What does this do to carrot-and-stick strategies?
- Nothing, since each player still remembers her own stage-1 action and can condition her stage-2 play on it to reward or punish the other player
- It makes them easier, since a deviation that cannot be seen cannot be met with a stick, which removes the reason for others to fear the deviator
- It rules them out, since stage 2 starts no subgames and cannot respond to a deviation, so stage-1 play must be a best reply within stage 1 alone
- It keeps them if players are patient, since the stage-2 equilibrium can still be chosen by a public randomization agreed upon before stage 1
<!-- YW5zOjI= -->
> A stick needs the others' stage-2 play to respond to my deviation, and they cannot respond to what they do not see; conditioning on my own past action changes nothing for the other player's incentives. Formally, each stage-2 information set now contains a node for each of the other player's stage-1 actions, so no stage-2 node starts a subgame, and with stage-2 behavior fixed, each player's stage-1 choice must be optimal within stage 1. Tadelis's multistage games assume stage outcomes are observed and notes that with no information revealed the game is no different from a simultaneous-move game. A pre-agreed lottery is independent of the deviation, so it cannot punish it (fourth option).
> Ref: Tadelis (2013), §9.1 and footnote 2 (p. 176); Lecture 4 slide 22; Lecture 5 slide 3
> Similar: Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25, section msg

Q: In a two-stage game with observed actions, a fixed rule assigns a stage-2 Nash equilibrium to each stage-1 outcome. What characterizes the stage-1 play of the resulting subgame-perfect equilibrium?
- It is a Nash equilibrium of the stage-1 game once each outcome's payoffs are raised by the discounted stage-2 payoffs that the rule assigns to it
- It is a Nash equilibrium of the stage-1 game alone, since stage-2 payoffs arrive after stage 1 ends and so cannot alter any stage-1 incentive
- It maximizes the sum of both players' stage-1 payoffs plus the discounted stage-2 payoffs, since the rule acts as a binding contract between them
- It is the stage-1 profile with the highest discounted stage-2 continuation, since players choose stage-1 actions to reach the best equilibrium
<!-- YW5zOjA= -->
> With stage 2 fixed by the rule, each stage-1 outcome leads to a known continuation payoff, so stage 1 is a one-shot game in which cell $a$ pays $u_i(a) + \delta\, v_i(a)$, with $v_i(a)$ player $i$'s payoff in the equilibrium assigned to $a$; subgame perfection requires a Nash equilibrium of this augmented game. The slides do exactly this: with a constant continuation the augmented game is the stage game shifted by a constant, and with carrot and stick it changes best replies. The second option ignores the continuation; the third and fourth treat players as maximizing a joint or continuation-only objective rather than best-replying.
> Ref: Lecture 5 slides 7–8 and 12–15; Gibbons (1992), §2.3.A (pp. 82–85); Tadelis (2013), §9.4 (pp. 180–184)
> Similar: Listas/pratica-lecture-05 #8 (Tadelis 9.3)

## osd

Q: A single decision maker chooses Continue or Stop in every period of an infinite horizon; she gets 1 if she never stops and 0 if she ever stops. Is the strategy "stop at every node" optimal, and does it pass the one-stage deviation test?
- It is optimal and passes the test, since at every node stopping ends the game at once, and a payoff of 0 now is as good as any later payoff of 0
- It fails the test and is not optimal, since continuing once at any node and then following the strategy again already earns the payoff of 1
- It is not optimal and fails the test, which shows that the one-stage deviation principle holds in this game just as it does with discounting
- It passes the test but is not optimal, since a single deviation still leads to a stop, and only the infinite deviation of never stopping earns 1
<!-- YW5zOjM= -->
> A one-stage deviation continues once and then reverts to stopping, so it still stops and earns 0: the strategy is one-stage unimprovable. Yet never stopping earns 1, so it is not optimal, and every finite truncation of that improvement earns 0. The payoff is not continuous at infinity: paths that agree for $n$ periods differ by 1 however large $n$ is. Discounting with bounded stage payoffs restores continuity, which is what Tadelis's footnote uses to extend Theorem 9.1 to infinitely repeated games; in finite games the principle holds without it. The second option miscomputes the one-stage deviation, which reverts to stopping.
> Ref: Tadelis (2013), §9.5, Def. 9.1 and Theorem 9.1 (pp. 184–186); §10.3, Prop. 10.3 and footnote 6 (pp. 198–199); Lecture 5 slides 14 and 24–25
> Similar: Simulados/quiz-lecture05-2-grim-trigger-2026-10-25, section grim

Q: The one-stage deviation principle for infinitely repeated games with discounting is proved by reducing any improving deviation to one that changes play at finitely many histories. Which property of discounted payoffs allows that reduction?
- Stationarity: every subgame of the infinitely repeated game is a copy of the whole game, so a deviation can be moved forward to the first period
- Finiteness of the action sets: with finitely many actions there are finitely many deviations at each history, so one of them must improve on its own
- Continuity at infinity: two strategies that agree over a long initial stretch give payoffs whose gap vanishes as that stretch grows longer
- Existence of a stage Nash equilibrium: a deviation can always be ended by reverting to it, which caps the gain from any later deviation at zero
<!-- YW5zOjI= -->
> Tadelis's footnote: "the discounting of payoffs implies a useful notion of continuity"; if a deviation improves, a strategy that copies it for $n<\infty$ stages and follows the original afterwards also improves for $n$ large, because the payoff from stage $n$ on carries weight $\delta^n$; then the finite induction of Theorem 9.1 applies (Fudenberg and Tirole, Theorem 4.2). Stationarity is convenient for computing payoffs but proves nothing about truncation (first option); finitely many actions per history still allow infinitely many histories (second option); and reverting to a stage equilibrium is a feature of particular strategies, not of the principle (fourth option).
> Ref: Tadelis (2013), §10.3, Prop. 10.3 and footnote 6 (pp. 198–199); Lecture 5 slides 24–25
> Similar: Listas/pratica-lecture-05 #5 (Tadelis 10.2)

Q: To verify a profile, a student checks one-stage deviations only at histories on the equilibrium path. Why can a profile pass this check and still fail to be a Nash equilibrium?
- Because one-stage deviations ignore the other players' replies, and a Nash equilibrium requires checking every deviation against every possible reply
- Because each check holds the player's off-path plan fixed, and a two-step deviation that also corrects a bad off-path plan can still pay
- Because one-stage deviations are defined only for finite games, and a profile checked on its path alone may hide an infinite chain of deviations
- Because the check applies only to pure strategies, and a Nash equilibrium must also be immune to mixed deviations at histories on the path
<!-- YW5zOjE= -->
> Take one player who chooses $a$, which ends the game with 1, or $b$, after which she chooses $c$ (0) or $d$ (2). The strategy "$a$, and $c$ after $b$" passes the on-path check: switching to $b$ while keeping $c$ yields 0. But "$b$ then $d$" yields 2, so the strategy is not even optimal. The one-stage deviation principle states that a profile with no profitable one-stage deviation *at any history* is subgame perfect; dropping the off-path histories drops the step that makes the proof work. Others' strategies are held fixed by the definition of a best reply (first option), the example is finite (third option), and mixed deviations never beat the best pure one (fourth option).
> Ref: Tadelis (2013), §9.5, Def. 9.1 and Theorem 9.1 (pp. 184–186); Lecture 5 slide 14
> Similar: Simulados/quiz-lecture04-1-multistage-carrot-stick-2026-10-25, section osd
