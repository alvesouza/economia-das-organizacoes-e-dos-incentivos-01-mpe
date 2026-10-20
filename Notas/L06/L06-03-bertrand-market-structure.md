---
tags: [notes, lecture-06, repeated-games, tacit-collusion, bertrand, market-structure, discount-factor]
date: 2026-10-16
status: estimated
source: "Cabral (2017) Ch. 9 §9.1 'Stability of collusive agreements', pp. 218–222 (eqs. (9.1)–(9.5), Box 9.1) and §9.3 'Factors that facilitate collusion', pp. 227–231 (Boxes 9.3, 9.5); MWG §12.D, pp. 400–405 (Props. 12.D.1–12.D.2); Tadelis §10.4 footnote 7, p. 203"
---

# Cabral 9.1, 9.3 · Price collusion: $\delta\ge1-1/n$, and what moves $\delta$

> **Claim.** With prices, the stage game's Bertrand trap makes the punishment as harsh as it
> can be (zero profit) **and** the temptation as large as it can be (the whole market), so the
> cartel holds iff $\delta\ge1-1/n$ — an all-or-nothing condition that does not depend on the
> price colluded on. Everything that raises the effective discount factor — **frequent
> interaction, a stable and growing market, few and similar firms, contact in many markets** —
> makes collusion easier; that list is the antitrust checklist.
> Prev: [[L06-02-cournot-collusion]] · Next: [[L06-04-punishments-price-wars]] · Map: [[L06-00-map]]

---

## 1 · C — the repeated Bertrand duopoly (Cabral pp. 218–219)

**Stage game.** Homogeneous product, constant marginal cost $c$, no capacity constraints,
simultaneous prices. The unique stage Nash equilibrium is $p=c$ with zero profit — the
*Bertrand trap* (Cabral §8.1).

**Grim strategies** (Cabral p. 218; MWG calls them *Nash reversion*, p. 401). Set the
monopoly price $p_M$ in period 1; keep setting $p_M$ while every past price was $p_M$;
after any deviation, price at $c$ forever.

**Conform.** Each firm gets half the monopoly profit $\pi_M$ every period:

$$V=\tfrac12\pi_M+\delta\,\tfrac12\pi_M+\delta^2\,\tfrac12\pi_M+\dots=\frac{\tfrac12\pi_M}{1-\delta}\qquad(9.1)\text{–}(9.2)$$

**Deviate.** Future payoff is zero whatever the deviation, so the best deviation maximizes
today's profit: undercut to $p_M-\varepsilon$ and take the whole market,

$$V'=\pi_M\qquad(9.3)$$

(strictly $\pi_M$ minus an arbitrarily small amount; Cabral's footnote c sets it equal).

**Condition** $V\ge V'$:

$$\frac{\tfrac12\pi_M}{1-\delta}\ge\pi_M\iff\tfrac12\ge1-\delta\iff\boxed{\delta\ge\tfrac12}\qquad(9.4)$$

In the template's terms, $v^c=\pi_M/2$, $v^d=\pi_M$, $v^p=0$:
$(\pi_M-\pi_M/2)/(\pi_M-0)=1/2$.

**MWG's statement** (C-level content, G-level proof). **Proposition 12.D.1** (p. 401): the
Nash reversion strategies are an SPE of the infinitely repeated Bertrand duopoly iff
$\delta\ge\frac12$. **Proposition 12.D.2** (p. 403): for $\delta\ge\frac12$ **any** price in
$[c,p_M]$ can be supported the same way; for $\delta<\frac12$ **every** SPE has all sales at
$p=c$ in every period.

> **All or nothing.** Replace $p_M$ by any $p\in(c,p_M]$: conform gives $\frac12\pi(p)/(1-\delta)$,
> deviate gives $\pi(p)$, and $\pi(p)$ cancels. The cutoff is $\frac12$ **whatever the price**.
> Contrast Cournot, where a shortfall in $\delta$ is absorbed by colluding *less*
> ([[L06-02-cournot-collusion]] §4). In Bertrand, a cartel short of patience has no fallback.

*G — why nothing survives below $\frac12$ (MWG p. 403, small type).* In any SPE, at any
date $t$ each firm could undercut the lowest price, take (almost) the whole industry profit
$\pi_t$ today, and still guarantee itself at least zero afterwards. Conforming therefore
requires $v_{jt}\ge\pi_t$ for $j=1,2$ (12.D.3), where $v_{jt}$ is firm $j$'s equilibrium value
from $t$ on. Adding the two: $v_{1t}+v_{2t}\ge2\pi_t$. At a date where industry profit is at
its largest (case (i) of the proof), the two values together are at most
$\pi_t+\delta\pi_t+\delta^2\pi_t+\dots=\pi_t/(1-\delta)$. So $2\pi_t\le\pi_t/(1-\delta)$, which
fails for every $\pi_t>0$ when $\delta<\frac12$. (Case (ii), a supremum never attained, needs a
limit argument.) Named, not examinable.

---

## 2 · C — $n$ firms: $\delta\ge1-1/n$

With $n$ symmetric firms the collusive share is $\pi_M/n$, the undercutter still takes
$\pi_M$, and the punishment still yields zero:

$$\frac{\pi_M/n}{1-\delta}\ge\pi_M\iff\frac1n\ge1-\delta\iff\boxed{\delta\ge1-\frac1n}$$

Cabral's reading (p. 227): "profit per firm would be smaller. However, the profit that a price
cutter would gain would still be the same." MWG sets the $J$-firm version as Exercise 12.D.2
(p. 405).

| $n$ | Bertrand $1-1/n$ | Cournot $(n+1)^2/(n^2+6n+1)$ | Which needs more patience |
|---|---|---|---|
| 2 | **0.500** | **0.529** | Cournot |
| 3 | 0.667 | 0.571 | Bertrand |
| 4 | 0.750 | 0.610 | Bertrand |
| 6 | 0.833 | 0.671 | Bertrand |
| 10 | 0.900 | 0.752 | Bertrand |

**Why the ranking flips after $n=2$.** Bertrand punishes harder (zero, against Cournot's
positive profit) — that lowers its cutoff; but it also tempts harder (the whole monopoly
profit, against a best response that leaves the rivals some sales) — that raises it. At $n=2$
the harsher stick wins by a hair; from $n=3$ on, the bigger carrot for cheating dominates.

![Left: critical delta against n for Bertrand (1-1/n) and Cournot ((n+1)^2/(n^2+6n+1)), crossing between n = 2 and n = 3; right: largest n with Bertrand collusion against pricing frequency on log axes, a straight line through (12, 121) and a lower dashed line when the industry ends with probability 10 percent a year](figures/L06-threshold-vs-n.png)
*Figure — left, the two cutoffs by number of firms (Cabral p. 227; [[L06-02-cournot-collusion]] §5);
right, the largest Bertrand cartel $n\le1/(1-\delta)$ when $\delta$ comes from Cabral (9.5) with
$r=10\%$ a year. Source: Cabral pp. 219–221, 227.*

The right panel is the same inequality read backwards: $\delta\ge1-1/n\iff n\le1/(1-\delta)$.
With $h=0$ and $g=0$, $1/(1-\delta)=1+f/r$, a straight line on log axes; a 10% annual chance
that the industry disappears halves the sustainable cartel at every frequency.

> **Interactive companion.** [The Cartel Patience Dial](companions/companion-collusion-threshold.html)
> — switch between Bertrand and Cournot at the same $n$ and $\delta$: the Bertrand cutoff
> jumps past Cournot's from $n=3$ on, and below its cutoff the Bertrand cartel has no partial
> fallback.

---

## 3 · C — what the discount factor is made of (Cabral pp. 219–220)

Cabral builds $\delta$ from four primitives:

| Ingredient | Effect on the value of one unit of money next period | Factor |
|---|---|---|
| interest rate $r$ per year, prices reset $f$ times a year | one period is $1/f$ years: discount at $r/f$ | $\dfrac{1}{1+r/f}$ |
| hazard $h$: probability the industry is gone next period | the payoff arrives only with probability $1-h$ | $(1-h)$ |
| demand growth $g$ per period | next period's profit is $(1+g)$ times bigger | $(1+g)$ |

$$\boxed{\;\delta=\frac{(1+g)(1-h)}{1+r/f}\;}\qquad(9.5)$$

**Signs** (p. 220): $\delta$ rises with $f$ and $g$, falls with $h$ and $r$. Hence Cabral's
summary: **"Collusion is normally easier to maintain when firms interact frequently and when
the probability of industry continuation and growth is high."** Gas stations that reprice
daily collude more easily than holiday resorts that set annual rates; a pharmaceutical market
with fast obsolescence (high $h$) less easily than cement (p. 220). MWG makes the same three
points — growth, a probability of ending, and the **time it takes to detect a deviation** —
on p. 403.

### 3.1 · Worked — "why don't firms collude more often?" (Cabral p. 221)

Annual interest 10%, monthly prices, $h=g=0$:

$$\delta=\frac{1}{1+0.10/12}=\frac{1}{1.008\overline{3}}=0.99174,\qquad
n\le\frac{1}{1-\delta}=1+\frac{f}{r}=1+\frac{12}{0.10}=121 .$$

So "even if there are dozens of symmetric price setting firms", monopoly pricing is an
equilibrium. With **annual** prices instead, $\delta=1/1.1=0.909$ and $n\le11$.

> **The model now over-predicts collusion** — the opposite of the static Bertrand trap.
> Cabral's four answers (p. 222): (1) **antitrust** makes explicit cartels illegal and can
> catch tacit ones; (2) **turnover** — high entry and exit means a high $h$ and a low $\delta$;
> (3) the infinite price war is **not credible**: after a deviation both firms gain by
> renegotiating back to collusion, which removes the threat; (4) **prices are not perfectly
> observed**, so secret price cuts are possible. (3) and (4) are
> [[L06-04-punishments-price-wars]] §2–§3.

**Box 9.1 (De Beers, p. 221)** is the punishment made visible: when Zaire left the CSO in
1981, about a million carats of industrial diamonds flooded the market and the price fell from
USD 3 to under USD 1.80 per carat; in 1983 Zaire asked to return, on worse terms.

---

## 4 · C — structure that facilitates collusion (Cabral §9.3, pp. 227–231)

| Factor | Mechanism in the model | Cabral's evidence |
|---|---|---|
| **Few firms** | $1-1/n$ rises with $n$: smaller share, same temptation | Exercise 9.17 (p. 245) |
| **Symmetric firms** | with a cost gap, the jointly efficient cartel gives the high-cost firm zero — it has **nothing to lose** and undercuts for any $\delta$; an equal-price cartel instead tempts the low-cost firm, whose margin is large and whose punishment (rival pricing at its own higher cost) is weak | bromide cartel, six price wars 1885–1914 over **profit division** (p. 228) |
| **Multimarket contact** | identical markets: the stick and the carrot both double, cutoff unchanged; markets where each firm has its own cost advantage: the threat to retaliate **in the other market** sustains collusion a single market cannot | Box 9.3 airlines (p. 229); Box 9.4 dog food (p. 230) |
| **Facilitating practices** | most-favoured-customer clauses make a price cut to one buyer costly on all buyers — they lower $v^d$ | Box 9.5 GE/Westinghouse price book, 1963–1975 (p. 231) |

**Multimarket contact, worked (p. 228–229).** Two identical markets, each a Bertrand duopoly.
Colluding in both: $2\times\frac12\pi_M/(1-\delta)$. Deviating in both (the best deviation,
since any deviation triggers war everywhere): $2\pi_M$ today, zero after. Condition
$\pi_M/(1-\delta)\ge2\pi_M\iff\delta\ge\frac12$ — identical to one market. Contact matters only
when the markets differ.

**Box 9.3, the number.** On a route served by American, Delta and Northwest in 1988, the
pairs met on 527, 357 and 323 of the top 1,000 routes: average contact
$(527+357+323)/3=402.3$ — and higher contact predicts higher fares.

---

## Links

- Previous: [[L06-02-cournot-collusion]] (quantities). Next: [[L06-04-punishments-price-wars]].
- Static Bertrand: [[../L02/L02-00-map|Lecture 2]]. Template: [[L06-01-recap-grim-trigger]] §3.
- Code: [[L06-11-python]] §4. Formulas: [[L06-09-formulas]] §1.2.
- Rules: [[../../rules/game-theory|rules/game-theory]] items 4 and 16 (outside options and
  participation — the "nothing to lose" firm).
- Exercises: Tadelis 10.8 (p. 218); Muñoz-Garcia Ch. 5 Ex. 5 (p. 231), Ch. 6 Ex. 5 (p. 290);
  Cabral 9.17 and 9.18 (p. 245); MWG Exercise 12.D.2 (p. 405).
