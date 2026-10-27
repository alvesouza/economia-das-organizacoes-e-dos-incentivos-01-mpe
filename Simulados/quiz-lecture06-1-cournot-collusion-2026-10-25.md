---
quiz: "Lecture 6 · Quiz 1 of 3 — Tacit collusion in quantities (estimated before the lecture: built from the books and the L06 notes, no slides yet)"
tags:
  template: "The no-deviation inequality (10.5)"
  cournot: "The symmetric Cournot cartel"
  asym: "Asymmetric splits and the binding firm"
  shrink: "Below the cutoff and with n firms"
---

## template

Q: In an infinitely repeated game with discount factor $\delta\in(0,1)$, a player earns $v^c$ per period on the cooperative path, $v^d$ in the period of his best one-shot deviation, and $v^p$ per period in the punishment (the stage Nash equilibrium forever), with $v^d>v^c>v^p$. Under grim trigger, which condition is equivalent to no profitable deviation on the path?
- $\delta\ge(v^c-v^p)/(v^d-v^p)$: the per-period loss from punishment over that loss plus the one-period gain from cheating
- $\delta\ge(v^d-v^c)/(v^c-v^p)$: the one-period gain from cheating over the per-period loss that punishment inflicts afterwards
- $\delta\ge(v^d-v^c)/(v^d-v^p)$: the one-period gain from cheating over that gain plus the per-period loss from punishment
- $\delta\ge(v^d-v^c)/v^d$: the one-period gain from cheating as a share of the deviation payoff, the punishment being sunk
<!-- YW5zOjI= -->
> Conforming is worth $v^c/(1-\delta)$; deviating is worth $v^d+\delta v^p/(1-\delta)$. Multiply by $1-\delta$: $v^c\ge(1-\delta)v^d+\delta v^p$, so $\delta(v^d-v^p)\ge v^d-v^c$. The first option is $1-\delta^*$, the complement of the cutoff. The second confuses $\delta$ with $\delta/(1-\delta)$: the correct second form is $v^d-v^c\le\frac{\delta}{1-\delta}(v^c-v^p)$. The last ignores what the punishment takes away.
> Ref: Tadelis (2013), §10.3 (pp. 197–200) and eq. (10.5) (p. 202); Lecture 6 notes L06-01 §3 (estimated before the lecture)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 2, p. 278

Q: With $v^c$ the cooperative per-period payoff, $v^d$ the best one-shot deviation payoff, $v^p$ the per-period punishment payoff ($v^d>v^c>v^p$) and $\delta$ the discount factor, which is the average-payoff form of the grim-trigger condition, and what does it say about patience?
- $v^c\ge(1-\delta)v^d+\delta v^p$: cooperation must beat a weighted average of deviation and punishment, and a higher $\delta$ puts more weight on $v^p$
- $v^c\ge\delta v^d+(1-\delta)v^p$: cooperation must beat a weighted average of deviation and punishment, and a higher $\delta$ puts more weight on $v^d$
- $(1-\delta)v^c\ge(1-\delta)v^d+\delta v^p$: both sides are average payoffs, and a higher $\delta$ shrinks the cooperative and the deviation terms together
- $v^c\ge v^d-\delta v^p$: cooperation must beat today's deviation net of the discounted punishment, and a higher $\delta$ lowers the right side linearly
<!-- YW5zOjA= -->
> Average payoffs multiply present values by $1-\delta$. Conforming has average $v^c$; deviating has average $(1-\delta)v^d+\delta v^p$, because the deviation lasts one period and the punishment the rest. As $\delta\to1$ the right side tends to $v^p<v^c$, so a patient enough player conforms. Swapping the weights would make patience help the cheater, which reverses the logic of the bootstrap equilibrium.
> Ref: Tadelis (2013), Def. 10.3 (p. 194), §10.4 (pp. 201–202); Lecture 6 notes L06-01 §3
> Similar: Tadelis (2013), Exercise 10.8, p. 218

Q: Under grim trigger (cooperate while every past outcome was cooperative, otherwise play the stage Nash equilibrium forever), why does checking subgame perfection reduce to one inequality on the cooperative path?
- Because the folk theorem makes every feasible, individually rational payoff an equilibrium for $\delta$ close to one, so histories off the path never need to be checked
- Because histories off the path are reached with probability zero in equilibrium, so subgame perfection places no restriction on what players do there
- Because grim trigger is a Nash equilibrium once the on-path inequality holds, and in an infinitely repeated game every Nash equilibrium is subgame perfect
- Because one-shot deviations suffice, and after any deviation the prescription is stage Nash forever, against which a one-shot deviation only lowers today's payoff
<!-- YW5zOjM= -->
> The one-stage deviation principle (Tadelis Prop. 10.3) says a profile is subgame perfect iff no one-shot deviation pays at any history. Grim trigger splits histories in two classes. After a deviation each player best-responds today and the future does not depend on today's action, so there is no condition. Only the cooperative class yields (10.5). Nash equilibria of repeated games need not be subgame perfect (Tadelis's footnote 9 example), and the folk theorem is an existence claim, not a check.
> Ref: Tadelis (2013), Prop. 10.2 (p. 196), Prop. 10.3 (p. 198), p. 199; Lecture 6 notes L06-01 §2
> Similar: Tadelis (2013), Exercise 10.4, p. 216

## cournot

P: Two firms face inverse demand $P(Q)=a-Q$ and constant marginal cost $c<a$, and play the Cournot game every period forever with discount factor $\delta$. Grim trigger: each firm produces half the monopoly output, $(a-c)/4$, while both always did, and the Cournot output $(a-c)/3$ forever after any deviation. Write $\pi_m/2$, $\pi_d$ and $\pi_c$ for the collusive, best-deviation and Cournot profits per firm.

Q: What is the best one-period deviation against a rival who produces $(a-c)/4$, and what does it earn?
- Output $(a-c)/3$ with profit $(a-c)^2/9$, because the Cournot quantity is the static best response to the rival
- Output $3(a-c)/8$ with profit $9(a-c)^2/64$, because it solves $\max_q\,(a-c-(a-c)/4-q)\,q$ given the rival
- Output $(a-c)/2$ with profit $(a-c)^2/8$, because a deviator takes the whole monopoly quota for itself
- Output $3(a-c)/8$ with profit $3(a-c)^2/32$, because both firms end up producing the best-response quantity
<!-- YW5zOjE= -->
> Against $(a-c)/4$ the first-order condition is $\frac34(a-c)-2q=0$, so $q=\frac38(a-c)$; the price margin is $a-c-\frac14(a-c)-\frac38(a-c)=\frac38(a-c)$, giving $\frac{9}{64}(a-c)^2$. Cournot output is the best response only to a rival producing $(a-c)/3$. Producing $(a-c)/2$ earns $(a-c)^2/8$, no more than conforming. $3(a-c)^2/32$ is the profit when both produce $\frac38(a-c)$, which is not the deviation period.
> Ref: Gibbons (1992), §2.3.C (pp. 102–103); Tadelis (2013), eq. (10.4) (p. 202)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 2, p. 278

Q: What is the smallest $\delta$ for which grim trigger sustains half the monopoly output for both firms?
- $\delta\ge1/2$, from $(\pi_m-\pi_m/2)/\pi_m$: a deviator can grab the monopoly profit and the punishment yields zero
- $\delta\ge8/17$, from $(\pi_m/2-\pi_c)/(\pi_d-\pi_c)$: the stake over the stake plus the temptation, with $(a-c)^2$ cancelling
- $\delta\ge9/17$, from $(\pi_d-\pi_m/2)/(\pi_d-\pi_c)$: the temptation over the temptation plus the stake, with $(a-c)^2$ cancelling
- $\delta\ge9/\bigl(17(a-c)\bigr)$, from $(\pi_d-\pi_m/2)/(\pi_d-\pi_c)$: the same ratio, falling as the market grows in size
<!-- YW5zOjI= -->
> $\pi_d-\pi_m/2=\frac{9}{64}-\frac{8}{64}=\frac1{64}$ and $\pi_d-\pi_c=\frac9{64}-\frac19=\frac{17}{576}$, in units of $(a-c)^2$; the ratio is $\frac{576}{64\cdot17}=\frac9{17}$. The cutoff is a pure number because every profit scales with $(a-c)^2$. $8/17$ is $1-\delta^*$. The $\frac12$ option applies Bertrand logic: in Cournot the deviator does not take the whole market and the punishment leaves positive profit.
> Ref: Gibbons (1992), eq. (2.3.2) (p. 103); Tadelis (2013), eq. (10.5) (p. 202)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 2, p. 278; Gibbons (1992), Problem 2.15, p. 136

Q: The cutoff for this cartel does not depend on the demand intercept $a$ or on the marginal cost $c$. Why?
- Because collusive, deviation and Cournot profits are each proportional to $(a-c)^2$, so the ratio in (10.5) is scale-free
- Because $a$ and $c$ shift the monopoly price $(a+c)/2$ one for one, so the collusive margin stays fixed as they move
- Because grim trigger reverts to Cournot, whose output $(a-c)/3$ is the same share of the market whatever $a-c$ is
- Because the firms discount future profit at the same rate $\delta$, so any change in $a$ or $c$ cancels across periods
<!-- YW5zOjA= -->
> With linear demand and constant cost each profit is a number times $(a-c)^2$: $\frac18$, $\frac9{64}$ and $\frac19$. The temptation $\pi_d-\pi_m/2$ and the stake $\pi_m/2-\pi_c$ scale together, so their ratio is fixed. The monopoly margin $(a-c)/2$ does move with $a-c$; the Cournot share argument explains only one of the three profits; and a common discount rate says nothing about how profits scale.
> Ref: Gibbons (1992), §2.3.C (pp. 102–103); Lecture 6 notes L06-02 §3
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 5 Ex. 4, p. 228

## asym

Q: A Cournot duopoly ($P=a-Q$, marginal cost $c$, discount factor $\delta$) sustains the monopoly output by grim trigger, but splits it unequally: firm 1 gets the share $\sigma<1/2$ and firm 2 gets $1-\sigma$. Which firm's cutoff from (10.5) binds, and why?
- Firm 2, the larger one: its best response moves further from its quota, so its gain from a one-period deviation is the larger
- Neither: both cutoffs equal the symmetric value whenever total cartel output equals the monopoly output, whatever the split
- Firm 1, the smaller one: it gains less from a one-period deviation, but it has more to lose each period once Cournot returns
- Firm 1, the smaller one: it gains more from a one-period deviation and loses less each period once Cournot returns
<!-- YW5zOjM= -->
> The smaller firm best-responds to a larger rival quota, so its deviation output rises further above its own quota, and its conforming profit (a small share of monopoly profit) is closest to Cournot profit. Both effects raise $\delta_1^*$; the cartel survives iff $\delta\ge\max_i\delta_i^*$. In Tadelis's 22/23 split the gains are 132.25 against 121 and the per-period losses 90 against 135, giving 0.595 against 0.473 (the book prints 0.392 for firm 2, which plugs in the wrong rival output).
> Ref: Tadelis (2013), §10.4 (pp. 201–203); Lecture 6 notes L06-02 §2 (erratum)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 5 Ex. 8, p. 239

Q: In a Cournot duopoly with $P=a-Q$ and marginal cost $c$, normalize $a-c=1$. The cartel produces the monopoly output $1/2$, split as $\sigma/2$ for firm 1 and $(1-\sigma)/2$ for firm 2, with $0<\sigma<1$. What is firm 1's one-period gain from its best deviation, $v_1^d-v_1^c$?
- $\sigma^2/16$, the deviation profit $\bigl((1+\sigma)/4\bigr)^2$ minus the conforming profit $\sigma/4$ of firm 1
- $(1-\sigma)^2/16$, the deviation profit $\bigl((1+\sigma)/4\bigr)^2$ minus the conforming profit $\sigma/4$ of firm 1
- $(1+\sigma)^2/16$, the deviation profit $\bigl((1+\sigma)/4\bigr)^2$ of firm 1, since conforming is already sunk
- $(1-\sigma)^2/16-1/9$, the deviation gain $\bigl((1-\sigma)/4\bigr)^2$ net of the Cournot profit $1/9$ of firm 1
<!-- YW5zOjE= -->
> Firm 1's best response to $(1-\sigma)/2$ is $\bigl(1-(1-\sigma)/2\bigr)/2=(1+\sigma)/4$, with profit $\bigl((1+\sigma)/4\bigr)^2$. Conforming earns the monopoly margin $1/2$ times $\sigma/2$, i.e. $\sigma/4$. The difference is $(1+2\sigma+\sigma^2-4\sigma)/16=(1-\sigma)^2/16$, larger than firm 2's $\sigma^2/16$ exactly when $\sigma<1/2$. The Cournot profit enters the denominator of (10.5), not the gain.
> Ref: Tadelis (2013), §10.4 (pp. 201–202); Gibbons (1992), §2.3.C (pp. 102–103)
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 5 Ex. 8, p. 239

## shrink

Q: In the repeated Cournot duopoly with $P=a-Q$, marginal cost $c$ and discount factor $\delta<9/17$, half the monopoly output cannot be sustained by grim trigger with Cournot reversion. What is the most collusive symmetric output $q^*$ that it can sustain?
- $q^*=\frac{9-5\delta}{3(9-\delta)}(a-c)$, falling from the Cournot output at $\delta=0$ to half the monopoly output at $\delta=9/17$
- $q^*=\frac{9-\delta}{3(9-5\delta)}(a-c)$, rising from the Cournot output at $\delta=0$ as patience grows, up to $\delta=9/17$
- $q^*=(a-c)/3$, the Cournot output, because below the cutoff the cartel collapses to the stage game, as Bertrand does below $1/2$
- $q^*=\frac{9-5\delta}{3(9-\delta)}(a-c)$, rising from half the monopoly output at $\delta=0$ to the Cournot output at $\delta=9/17$
<!-- YW5zOjA= -->
> With $q$ in units of $a-c$ the condition $(1-2q)q\ge(1-\delta)(1-q)^2/4+\delta/9$ becomes $9(9-\delta)q^2-18(3-\delta)q+(9-5\delta)\le0$. One root is $1/3$; the product of the roots gives the other, $\frac{9-5\delta}{3(9-\delta)}$, which is $1/3$ at $\delta=0$ and $1/4$ at $\delta=9/17$. Cournot does not collapse like Bertrand: a shortfall in patience is absorbed by colluding less. The inverted formula climbs above the Cournot output, which no cartel would choose.
> Ref: Gibbons (1992), §2.3.C (pp. 103–104); Lecture 6 notes L06-02 §4
> Similar: Gibbons (1992), Problem 2.15, p. 136; Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 3, p. 282

Q: With $n$ identical Cournot firms, inverse demand $P=a-Q$, marginal cost $c$ and discount factor $\delta$, grim trigger supports the monopoly output split equally. What is the cutoff $\delta^*(n)$ and how does it move with $n$?
- $\delta^*(n)=1-1/n$, which rises with $n$ and tends to 1, since each member's share falls while the gain from undercutting stays put
- $\delta^*(n)=(n-1)^2/(n^2+6n+1)$, which rises with $n$ and tends to 1, because more members share the same cartel profit
- $\delta^*(n)=(n+1)^2/(n^2+6n+1)$, which rises with $n$ and tends to 1, because more members share the same cartel profit
- $\delta^*(n)=(n+1)^2/(n^2+6n+1)$, which falls with $n$, because a deviator's extra output depresses the price for more rivals
<!-- YW5zOjI= -->
> Collusive share $(a-c)^2/(4n)$; best deviation $q_d=\frac{(n+1)(a-c)}{4n}$ with profit $\frac{(n+1)^2(a-c)^2}{16n^2}$; Cournot $(a-c)^2/(n+1)^2$. The numerator of (10.5) is $\frac{(n-1)^2}{16n^2}$ and the denominator factors as $\frac{(n-1)^2(n^2+6n+1)}{16n^2(n+1)^2}$, so $\delta^*=\frac{(n+1)^2}{n^2+6n+1}$: $9/17$ at $n=2$, rising toward 1. $1-1/n$ is the Bertrand cutoff, and $(n-1)^2$ is only the numerator before the denominator is factored.
> Ref: Gibbons (1992), §2.3.C (p. 103); Cabral (2017), §9.3 (p. 227); Lecture 6 notes L06-02 §5
> Similar: Muñoz-Garcia & Toro-Gonzalez (2019), Ch. 6 Ex. 4, p. 287; Gibbons (1992), Problem 2.15, p. 136
