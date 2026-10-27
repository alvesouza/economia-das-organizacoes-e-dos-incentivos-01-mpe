---
quiz: "Lecture 6 · Quiz 3 of 3 — Reputation, institutions and efficiency wages (estimated before the lecture: built from the books and the L06 notes, no slides yet)"
tags:
  trust: "The repeated trust game"
  mr: "Reputation in Milgrom and Roberts: the multiplier and the limits"
  inst: "Borrowed reputations: guarantors and brand names"
  wages: "Efficiency wages as a relational contract"
---

## trust

Q: In each period an offeror decides whether to trust a decision maker, who then honours or abuses the trust. Payoffs (offeror, decision maker): no trust $(0,0)$; trust honoured $(V,V)$; trust abused $(-L,V+G)$, with $V,G,L>0$. The game repeats forever with discount factor $\delta$, and the offeror never trusts again after an abuse. When does the decision maker honour trust?
- $\delta\ge V/(V+G)$: the per-period value of the relationship over that value plus the extra gain from abusing trust
- $\delta\ge L/(V+L)$: the offeror's loss from abused trust over that loss plus the value of honoured trust
- $\delta\ge G/(V+G)$: the extra gain from abusing trust over that gain plus the per-period value of the relationship
- $\delta\ge G/V$: the extra gain from abusing trust over the per-period value of the relationship, the round itself sunk
<!-- YW5zOjI= -->
> Honouring forever is worth $V/(1-\delta)$; abusing is worth $V+G$ today and 0 after. So $\frac{\delta}{1-\delta}V\ge G$, i.e. $\delta\ge\frac{G}{V+G}$: in (10.5) terms $v^c=V$, $v^d=V+G$, $v^p=0$. Tadelis's trust game has $V=G=1$, hence $\delta\ge1/2$. $L$ governs whether the offeror wants to trust, not whether the decision maker honours; $G/V$ is the condition with $\delta/(1-\delta)$ read as $\delta$.
> Ref: Tadelis (2013), §10.5.1 (pp. 204–205); Milgrom & Roberts (1992), Ch. 8 (pp. 261–263)
> Similar: Milgrom & Roberts (1992), Ch. 8 Mathematical Exercise 5, p. 286

Q: In the repeated trust game, player 1 trusts until player 2 has once abused trust and never trusts after that, while player 2 follows "cooperate as long as player 1 trusts me". This profile is a Nash equilibrium for a patient player 2, but not subgame perfect. Why?
- Off the path, after an abuse, player 2 cooperates whenever trusted, so player 1's prescription never to trust again is not a best response there
- On the path, player 2 gains by abusing trust whatever $\delta$ is, because player 1's threat to stop trusting is never carried out in equilibrium
- The stage game is sequential, and subgame perfection in repeated games is defined only when the stage game is played simultaneously
- Off the path, after player 1 stops trusting, subgame perfection requires player 2 to punish player 1, and this strategy never does
<!-- YW5zOjA= -->
> Subgame perfection asks for a best response after every history, including those the equilibrium never reaches. After an abuse, player 2's strategy still cooperates whenever trusted, so player 1 would earn 1 by trusting instead of 0: "never trust again" is not optimal there. Tadelis's grim profile fixes this by making player 2 defect forever after a deviation. Every extensive-form stage game has a normal form, so the repeated-game tools still apply.
> Ref: Tadelis (2013), §10.5.1 footnotes 8–9 (pp. 204–205)
> Similar: Tadelis (2013), Exercise 10.4, p. 216

## mr

Q: In Milgrom and Roberts's trust box, honoured trust pays the decision maker $V$ per meeting and abuse pays $V+G$ once, after which no one trusts him. A stream of $X$ per meeting is worth $NX$ today, with $N=1/(1-\delta)$ and $\delta=(1+r)^{-t}$ for meetings every $t$ periods at interest rate $r$. What is the exact no-cheating condition?
- $NV>G$, i.e. $N>G/V$: the cheater forgoes the whole stream $NV$ and gains only $G$ in the round in which he cheats
- $(N-1)V\ge V+G$: the cheater forgoes every later round and collects both $V$ and $G$ in the round in which he cheats
- $NV\ge V+G-L$: the cheater forgoes the stream $NV$, gains $V+G$ once, and the offeror's loss $L$ is netted out once
- $NV\ge V+G$, i.e. $(N-1)V\ge G$: the round of cheating still pays $V$ plus $G$, and $N$ counts the current round too
<!-- YW5zOjM= -->
> Honouring forever gives $NV$; cheating gives $V+G$ now and nothing after. Since $N-1=\delta/(1-\delta)$, the condition is $\delta\ge G/(V+G)$. M&R print the comparison as $NV>G$, which drops the round's $V$; with $V=G=1$ it would wrongly allow any $\delta>0$. Because $\delta=(1+r)^{-t}$, rarer meetings (larger $t$) lower $N$: frequency is patience. $L$ is the offeror's payoff, not the cheater's.
> Ref: Milgrom & Roberts (1992), Ch. 8 (pp. 261–263, footnote 11); Lecture 6 notes L06-05 §2
> Similar: Milgrom & Roberts (1992), Ch. 8 Mathematical Exercise 5, p. 286

Q: A decision maker meets a different offeror every period; each offeror trusts only if trust was honoured the last time it was offered. What must hold for this reputation to discipline him as a repeated relationship with one partner would?
- Each offeror must be able to sue him for past abuses, because a reputation is only as strong as the court that would enforce it
- Future offerors must observe his past conduct and be able to judge whether trust was honoured, or the incentive disappears
- He must meet every offeror at least twice, because only a partner who has been cheated before has a reason to stop trusting
- The game must end at a date known to all offerors, because otherwise no offeror can compute the value of his reputation
<!-- YW5zOjE= -->
> M&R's point is that the calculation is unchanged when the partners differ: he honours trust to keep future partners offering it, which is what a reputation is. Two preconditions follow: the history must travel, and outsiders must be able to tell honoured from abused trust. Ambiguity and costly outside judgment are exactly where reputations fail, and a known end date destroys them by unravelling. Courts are what reputation substitutes for.
> Ref: Milgrom & Roberts (1992), Ch. 8 (pp. 263–266)
> Similar: Milgrom & Roberts (1992), Ch. 8 Food for Thought 3, p. 284

Q: Milgrom and Roberts list three limits to reputation: ambiguity about what was the right thing to do, the need for outsiders to judge disputes, and the end game. What does the end game predict for a chief executive close to a known retirement date?
- Reputational incentives get stronger near retirement, because a chief executive wants to leave with a clean record that raises his final pay
- Reputational incentives are unaffected by retirement, because the firm itself is long-lived and carries the reputation for the next chief
- Reputational incentives weaken near retirement, because there is little future left to protect, so pay should become more sensitive to performance
- Reputational incentives weaken near retirement, because outsiders can no longer judge his decisions, so the board should rely on fixed pay
<!-- YW5zOjI= -->
> Near a known final date there is little future to protect, so the last periods cannot be disciplined by the threat of losing it, and the argument creeps backwards, as in a finitely repeated game. Explicit incentives must take over: Gibbons and Murphy found CEO pay more sensitive to performance near retirement. A long-lived firm does help, but through the sale of the business (an owner keeps its reputation to get a higher price), not by keeping the retiring executive honest.
> Ref: Milgrom & Roberts (1992), Ch. 8 (pp. 264–266)
> Similar: Milgrom & Roberts (1992), Ch. 8 Mathematical Exercise 4, p. 286

## inst

Q: Each period a new pair of one-shot traders arrives. The second trader can post a bond $b$ with a long-lived guarantor, who returns it if trade was honest and keeps it otherwise, for a fee $w$ per period; traders use the guarantor only while he has always honoured bonds. The guarantor discounts with $\delta$. When does he honour bonds?
- $\delta\ge1-w/b$, from $\frac{w}{1-\delta}\ge b$: the stream of fees must outweigh pocketing one bond and losing all custom
- $\delta\ge w/b$, from $\frac{w}{1-\delta}\ge b$: the stream of fees must outweigh pocketing one bond and losing all custom
- $\delta\ge1-w$, from $\frac{w}{1-\delta}\ge1$: the stream of fees must outweigh the trader's one-period gain from abusing trust
- $\delta\ge1/2$, from the trust game itself: the guarantor inherits the cutoff of the traders whose good faith he guarantees
<!-- YW5zOjA= -->
> Honouring yields $w/(1-\delta)$; keeping a bond yields $b$ once and nothing after, since no trader posts again: $w\ge(1-\delta)b$. In (10.5) terms $v^c=w$, $v^d=b$, $v^p=0$, so $\delta^*=(b-w)/b$. Tadelis's fee 0.1 and bond 2 give 0.95: a thin rent needs a very patient keeper. The design levers follow: a higher fee or a smaller bond (it need only exceed the trader's one-period gain) lowers the cutoff.
> Ref: Tadelis (2013), §10.5.2 (pp. 205–207, footnote 10)
> Similar: Tadelis (2013), Exercise 10.10, p. 219

Q: In Kreps's brand-name equilibrium, each short-lived trusted player buys a clean brand name, honours trust while he holds it, and sells it on at a price $p^*$. Trust honoured pays 1 per period, abuse pays 2 once. Why does the brand sustain trust although no owner lives long?
- Because buyers of the brand inherit the previous owner's discount factor, so the brand makes every owner as patient as an infinitely lived player
- Because the brand lets offerors sue the current owner for past abuses, so the legal system enforces what the reputation alone could not
- Because the brand is sold before the owner's last period, so no owner ever faces a final period in which abusing trust would go unpunished
- Because the brand resells for more than 1 only while clean, so abusing trust gains 1 today but loses a resale value above that gain
<!-- YW5zOjM= -->
> The investment in the name acts as a bond: cheating gives 2 instead of 1 today, and wipes out a resale value $p^*>1$. Through the name, short-lived owners become one infinitely lived player, so there is no terminal period. Discount factors are not inherited and no court is involved. The resale-before-the-end option describes the timing, but the deterrent is the value that cheating destroys, not the date of sale.
> Ref: Tadelis (2013), §10.5.3 (pp. 207–209); Milgrom & Roberts (1992), Ch. 8 (p. 259)
> Similar: Tadelis (2013), Exercise 10.6, p. 217

## wages

Q: In Gibbons's efficiency-wage model a worker with discount factor $\delta$ earns $w_0$ in self-employment; effort costs $e$ and gives high output for sure; shirking gives high output with probability $p$, and low output (proof of shirking, followed by dismissal) otherwise. What is the lowest wage $w^*$ that induces effort?
- $w^*=w_0+e+\frac{(1-\delta)e}{\delta p}$: the outside option, the effort cost and a rent that explodes as $p\to0$ or as $\delta\to0$
- $w^*=w_0+e+\frac{(1-\delta)e}{\delta(1-p)}$: the outside option, the effort cost and a rent that explodes as $p\to1$ or as $\delta\to0$
- $w^*=w_0+\frac{(1-\delta)e}{\delta(1-p)}$: the outside option and a rent that explodes as $p\to1$ or as $\delta\to0$, the rent repaying effort
- $w^*=w_0+e+\frac{\delta e}{(1-\delta)(1-p)}$: the outside option, the effort cost and a rent that explodes as $p\to1$ or as $\delta\to1$
<!-- YW5zOjE= -->
> $V_e=(w^*-e)/(1-\delta)$ and $V_s=w^*+\delta[pV_s+(1-p)w_0/(1-\delta)]$. Setting $V_e\ge V_s$ gives $w^*\delta(1-p)\ge e(1-\delta p)+\delta(1-p)w_0$, and splitting $1-\delta p=\delta(1-p)+(1-\delta)$ gives (2.3.5). Here $p$ is the probability that shirking goes undetected, so the premium rises as $p\to1$. Even with $p=0$ the wage is $w_0+e/\delta$, not $w_0+e$: tomorrow's rent is discounted.
> Ref: Gibbons (1992), §2.3.D eq. (2.3.5) (pp. 108–110)
> Similar: Gibbons (1992), Problem 2.17, pp. 136–137; Milgrom & Roberts (1992), Ch. 8 Mathematical Exercise 3, p. 286

Q: In Gibbons's efficiency-wage model (output $y$ with effort, outside option $w_0$, effort cost $e$, shirking undetected with probability $p$, discount factor $\delta$), the firm pays $w^*$ only if $y-w^*\ge0$. What does this add to the worker's condition, and when does the relationship exist?
- $\delta\ge\frac{e}{e+(1-p)(y-e-w_0)}$, so an efficient relationship, $y-e>w_0$, is necessary but not sufficient for it to exist
- $\delta\ge\frac{e}{e+p(y-e-w_0)}$, so an efficient relationship, $y-e>w_0$, is necessary but not sufficient for it to exist
- $\delta\ge\frac{e}{e+(1-p)(y-w_0)}$, so an efficient relationship, $y>w_0$, is necessary but not sufficient for it to exist
- $\delta>0$ is enough once $y-e>w_0$, so an efficient relationship always leaves a rent that is large enough for the firm to pay
<!-- YW5zOjA= -->
> Combine $y\ge w^*$ with (2.3.5): $y-e-w_0\ge\frac{(1-\delta)e}{\delta(1-p)}$. Writing $S=y-e-w_0$, $S\delta(1-p)\ge(1-\delta)e$, so $\delta[(1-p)S+e]\ge e$. The surplus must be net of effort, and detection enters as $1-p$. Efficiency is not enough: with M&R's calibration and $y=41$, the notes' example needs $\delta\ge0.952$.
> Ref: Gibbons (1992), §2.3.D eq. (2.3.7) (pp. 110–111); Lecture 6 notes L06-07 §4
> Similar: Gibbons (1992), Problem 2.17, pp. 136–137

Q: Milgrom and Roberts write the efficiency-wage condition as: the employee cheats iff $g>p(w-\bar w)N$, with $g$ the gain from cheating, $p$ the probability of detection, $w$ the wage, $\bar w$ the wage after dismissal and $N$ the multiplier for the relationship's value. How does this map into Gibbons's $w^*\ge w_0+e+\frac{(1-\delta)e}{\delta(1-p)}$, where $p$ is the probability that shirking goes undetected?
- M&R's $p$ is Gibbons's $p$, $w-\bar w$ is $w^*-w_0$, and $N$ plays the part of $1/(1-\delta)$, so the efficiency wage is $\bar w+gNp$
- M&R's $p$ is Gibbons's $1-p$, $w-\bar w$ is $w^*-w_0$, and $N$ plays the part of $1-\delta$, so the efficiency wage is $\bar w+g/(Np)$
- M&R's $p$ is Gibbons's $1-p$, $w-\bar w$ is $w^*-e-w_0$, and $N$ plays the part of $\delta/(1-\delta)$, so the efficiency wage is $\bar w+g/(Np)$
- M&R's $p$ is Gibbons's $p$, $w-\bar w$ is $w^*-e-w_0$, and $N$ plays the part of $\delta/(1-\delta)$, so the efficiency wage is $\bar w+gp/N$
<!-- YW5zOjI= -->
> Rearranged, (2.3.5) reads $e\le(1-p)\frac{\delta}{1-\delta}(w^*-e-w_0)$: gain today against detection times the discounted rent. So $g\leftrightarrow e$, M&R's detection $p\leftrightarrow1-p$, the rent $w-\bar w\leftrightarrow w^*-e-w_0$ (M&R's outside wage is already net of effort), and $N\leftrightarrow\delta/(1-\delta)$ up to M&R's bookkeeping of the current period. Solving $p(w-\bar w)N=g$ gives $w=\bar w+g/(Np)$: USD 60,000 at $N=1$ and USD 50,000 at $N=2$ in M&R's example.
> Ref: Milgrom & Roberts (1992), Ch. 8 eq. (8.1) (pp. 250–252); Gibbons (1992), §2.3.D (p. 110); Lecture 6 notes L06-07 §6.2
> Similar: Milgrom & Roberts (1992), Ch. 8 Mathematical Exercises 1 and 3, pp. 285–286
