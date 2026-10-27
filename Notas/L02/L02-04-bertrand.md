---
tags: [notes, lecture-02, bertrand, price-competition, existence, strategic-complements, differentiated-products]
date: 2026-10-25
status: taught
source: "Aula/Lecture02.pdf slides 29–40; Tadelis (2013) §5.2.4, printed pp. 88–93 (discrete best response p. 90; Prop. 5.2 p. 91; asymmetric costs and Fig. 5.3 pp. 91–93; Remark on strategic complements p. 93); Gibbons (1992) §1.2.B pp. 21–22 (differentiated products)"
---

# Slides 29–40 · 5.2.4 · Bertrand duopoly: two firms are enough for marginal-cost pricing

> **Claim.** Change the strategy from quantity to price and the same market behaves competitively: with identical
> costs the unique equilibrium of the continuous game is **$p_1=p_2=c$** (Prop. 5.2), proved by showing every other
> profile has a profitable undercut. On a one-cent grid there are exactly **two** equilibria, (10, 10) and
> (10.01, 10.01). With **unequal** costs and continuous prices **no pure equilibrium exists**: the payoff jumps at
> the rival's price, so the efficient firm has no best response. Differentiated products restore interior,
> upward-sloping best responses (**strategic complements**).
>
> Prev: [[L02-03-cournot]] · Next: [[L02-05-commons]] · Map: [[L02-00-map]]

---

## 0 · C — the lecture's version (slides 29–40), in its notation

**Notation.** $p_i\ge0$ firm $i$'s price; $c\ge0$ the common marginal cost; market demand at the lowest price $p$ is
$Q(p)=\frac ab-\frac pb$ for $p<a$ and 0 otherwise (the inverse of $P=a-bQ$); $p^m$ the monopoly price.

**The game (slide 29).** Two firms sell a homogeneous good and choose prices simultaneously; consumers buy from the
cheapest firm and split equally at a tie:
$$u_i(p_i,p_j)=\begin{cases}(p_i-c)\,Q(p_i)&p_i<p_j,\\ \tfrac12(p_i-c)\,Q(p_i)&p_i=p_j,\\ 0&p_i>p_j.\end{cases}\tag{1}$$

**The monopoly price (slide 30).** Maximize $(p-c)Q(p)=(p-c)\dfrac{a-p}{b}$. FOC:
$$\frac{(a-p)-(p-c)}{b}=0\ \Longrightarrow\ p^m=\frac{a+c}{2}.\tag{2}$$
(With Tadelis's numbers $a=100$, $c=10$: $p^m=55$, as in §1 below.)

**Firm $i$'s payoff given $p_j$, case by case (slides 31–33).**

| Rival's price | What firm $i$ can earn | Best response |
|---|---|---|
| $p_j<c$ | any $p_i\le p_j$ sells at a loss; any $p_i>p_j$ sells nothing and earns 0 | every $p_i>p_j$ |
| $p_j=c$ | $p_i<c$ loses; $p_i=c$ and $p_i>c$ both earn 0 | every $p_i\ge p_j$ |
| $c<p_j\le p^m$ | $i$ wants $p_i<p_j$ **as close as possible** to $p_j$; for any such $p_i$ a higher price still below $p_j$ earns more | **none**: the existence problem |
| $p^m<p_j$ | any price below $p_j$ takes the whole market, and the best of them is $p^m$ | $p^m$ |

**Best response (slide 34).**
$$p_i^*(p_j)=\begin{cases}\{p_i:p_i>p_j\}&p_j<c,\\ \{p_i:p_i\ge p_j\}&p_j=c,\\ \emptyset&c<p_j\le p^m,\\ \{p^m\}&p^m<p_j.\end{cases}\tag{3}$$

**$(c,c)$ is a Nash equilibrium (slide 35).** Suppose $p_2=c$. By (3) any $p_1\ge c$ is a best response; in
particular $c$ is. The same argument holds for firm 2.

> **A weakly dominated equilibrium strategy (slide 36).** $p_i^*=c$ is weakly dominated by any higher price at which
> demand is positive: such a price earns 0 when undercut and a strictly positive profit when it is the lowest or tied,
> while $c$ earns 0 always. This is slide 16's caveat in action ([[L02-02-nash-equilibrium]] §2c).

**$(c,c)$ is the unique equilibrium (slides 37–38).**

*Step 1. In any NE, $p_1^*=p_2^*$.* Suppose $p_1^*>p_2^*$. Three cases:
- $p_2^*<c$: firm 2 makes a loss, when it could earn zero with any $p_2'>p_1^*$;
- $p_2^*=c$: firm 2 earns zero, when it could earn a positive profit with $p_2'=p_1^*$ (half the market at a margin
  $p_1^*-c>0$);
- $p_2^*>c$: firm 1 earns zero, when it could earn a positive profit with any $p_1'\in(c,p_2^*)$.

An analogous argument rules out $p_1^*<p_2^*$.

*Step 2. In any NE, $p_1^*=p_2^*=c$.*
- If $p_1^*=p_2^*>c$, firm 1 could charge $p_1'\in(c,p_2^*)$ close to $p_2^*$ and serve the whole market instead of
  sharing it (almost twice the profit).
- If $p_1^*=p_2^*<c$, both make losses, and each would rather raise its price and sell nothing.

"According to the model, a duopoly in Nash equilibrium works like a competitive market" (slide 38).

**The Bertrand paradox (slide 39).** Two firms behave as if in perfect competition: price equals marginal cost and
profits are zero. The assumptions behind it: (i) **homogeneous products**; (ii) **simultaneous choices**; (iii)
**unlimited production capacity**. Relax any one and prices rise above cost (§5 relaxes (i)).

**Cournot or Bertrand? (slide 40).** It depends on what is harder to adjust.

| Model | Harder to adjust | Strategic decision | Slide's examples |
|---|---|---|---|
| Cournot | quantity (capacity) | how much to produce | cars, cement, steel, commodities |
| Bertrand | price, or quantity expands at almost no cost | the price | software and other digital goods |

In both models the NE predicts **more output than a cartel**, but the Bertrand prediction is much more extreme
($Q^*=q^{cp}$ against Cournot's $\tfrac43q^m$).

The sections below are Tadelis's treatment. §1 and §3 are the same result in his numbers; **§2 (cent grid), §4
(unequal costs) and §5 (differentiated products) were not covered in class** and are reading.

## 1 · C — the game (p. 88)

Demand $p=100-q$, $c_i(q_i)=10q_i$, prices $p_i\in[0,\infty)$; the lower price takes the market, a tie splits it:

$$u_i(p_i,p_j)=\begin{cases}(100-p_i)(p_i-10)&p_i<p_j\\ \tfrac12(100-p_i)(p_i-10)&p_i=p_j\\ 0&p_i>p_j\end{cases}$$

**Monopoly benchmark (p. 89).** $\max_p(100-p)(p-10)$: FOC $110-2p=0$, so $p=55$, $q=45$, profit $45\cdot45=2025$.

---

## 2 · Not covered in class — the best response on a cent grid (pp. 89–90)

Prices in steps of $\Delta=0.01$. Go case by case over the rival's price $p_j$:

| $p_j$ | Best response | Why |
|---|---|---|
| $p_j>55$ | $55$ | the monopoly price already undercuts $p_j$ |
| $10.02\le p_j\le55$ | $p_j-0.01$ | undercutting by a cent beats tying (below) |
| $p_j=10.01$ | $10.01$ | undercutting to 10 earns 0; tying earns $\tfrac12(89.99)(0.01)>0$ |
| $p_j=10$ | any $p_i\ge10$ | every such price earns exactly 0 |
| $p_j<10$ | any $p_i>p_j$ | matching or undercutting sells below cost |

**The undercut beats the tie, every step (p. 89).** Let $\Delta v$ be the gain from $p_j-0.01$ over $p_j$:

$$\Delta v=(100-(p_j-0.01))((p_j-0.01)-10)-\tfrac12(100-p_j)(p_j-10).$$

Expand the first product: $(100.01-p_j)(p_j-10.01)=-p_j^2+110.02p_j-1001.1001$. The second:
$\tfrac12(-p_j^2+110p_j-1000)=-0.5p_j^2+55p_j-500$. Subtract:

$$\Delta v=-0.5p_j^2+55.02p_j-501.1001\approx55.02p_j-0.5p_j^2-501.1 .$$

At $p_j=10.02$ the book's rounded form gives $551.3004-50.2002-501.1=0.0002>0$; the exact constant gives
$0.0001$, which is also the direct comparison: undercutting to 10.01 earns $89.99\times0.01=0.8999$, tying at 10.02
earns $\tfrac12\times89.98\times0.02=0.8998$. Either way it is positive. And
$d\Delta v/dp_j=55.02-p_j>0$ for $p_j<55.02$, so $\Delta v>0$ on all of $[10.02,55]$.

**Equilibria.** Look for mutual best replies: $BR_i(10.01)=\{10.01\}$ and $10\in BR_i(10)$, so

$$(p_1,p_2)\in\{(10,10),\ (10.01,10.01)\}.$$

No other pair works: at or above 10.02 the higher-priced (or tied) firm undercuts; $(10,p)$ with $p>10$ fails because
the firm at **10** earns zero and would rather raise its price to just below $p$ for a positive profit.

> **Tadelis's warning (p. 90).** When $p_2=10$, *every* $p_1\ge10$ is a best reply for firm 1. It does **not**
> follow that $(p_1,10)$ is an equilibrium for every $p_1\ge10$: if $p_1>10$, firm 2's price of 10 is no longer a
> best reply to $p_1$. **An equilibrium needs both players best-responding, not one.**

![Left: the symmetric Bertrand best response on a cent grid, p_j minus one cent between 10.02 and 55 and flat at 55 above, with the two equilibria at (10, 10) and (10.01, 10.01). Right: firm 1's profit when p2 = 2 with c1 = 1, rising toward 98 below 2, dropping to 49 at 2 and to zero above](figures/L02-bertrand.png)
*Left: the cent-grid best response, computed by brute force; the shaded vertical band is $BR_i(10)=\{10, 10.01,\dots\}$. Right: Tadelis's Fig. 5.3 with the book's numbers ($c_1=1$, $p_2=2$): the supremum 98 is approached but never attained. Source: pp. 88–93.*

On the left, the best response hugs the 45° line one cent below it, so the only places it can meet its mirror image
are where undercutting stops paying: at 10 and 10.01. On the right, the open circle is the whole existence problem.

**Profits compared (p. 90).** Cournot: 900 each. Bertrand: 0 at (10, 10) or about 0.45 at (10.01, 10.01). Monopoly:
2025. Adding a third or fourth Bertrand firm changes nothing.

---

## 3 · C — Proposition 5.2: continuous prices (p. 91; the slides' result, slides 35–38)

**Proposition 5.2.** With $\Delta=0$, $c_i(q_i)=cq_i$ for both firms and $p=a-bq$, $a>c$, the unique Nash equilibrium
is $p_1=p_2=c$.

*Proof, every case.*
1. No equilibrium has $p_i<c$: the firm with the lower price sells at a loss and would rather raise its price.
   So $p_i\ge c$ for both.
2. $p_1=p_2=\hat p>c$: each earns half the market at margin $\hat p-c$; cutting to $\hat p-\varepsilon$ takes the whole
   market at almost the same margin, nearly doubling profit. Not an equilibrium.
3. $p_1>p_2>c$ (or the mirror): firm 2 earns the whole market but can raise its price to $p_1-\varepsilon$ and earn more
   (as long as $p_2$ is below the monopoly price; above it, firm 1 undercuts). Not an equilibrium.
4. $p_1>p_2=c$: firm 2 earns zero and can raise its price toward $p_1$ for a positive profit. Not an equilibrium.
5. $p_1=p_2=c$: both earn zero; any $p_i>c$ sells nothing (zero), any $p_i<c$ loses. Every price $\ge c$ is a best
   reply to $c$, so $c$ is one. **Equilibrium.** ∎

> **Two firms reproduce perfect competition.** "One firm may have monopoly power, but when we let one more firm
> compete, and they compete on prices, then the market will behave competitively" (p. 90).

---

## 4 · Not covered in class — unequal costs: no equilibrium in pure strategies (pp. 91–93)

$c_1=1$, $c_2=2$, $p=100-q$.

**With cents.** $(p_1,p_2)=(1.99,2.00)$ is an equilibrium: firm 1 takes the market at a margin of 0.99 and would lose
by raising to 2.00 (split) or above (nothing); firm 2 sells nothing and would lose money by pricing below 2.
(Tadelis exercise 5.12, p. 98, asks for the others.)

**Continuous prices.** The "limit" $p_1=p_2=2$ is **not** an equilibrium: firm 1 earns
$\tfrac12(98)(1)=49$ and would earn almost $98$ by pricing a hair below 2. But there is no best "hair":

$$u_1(p_1,2)=\begin{cases}(100-p_1)(p_1-1)&p_1<2\ \ (\to98)\\ 49&p_1=2\\ 0&p_1>2\end{cases}$$

The supremum 98 is **not attained**: for any $p_1<2$, a price closer to 2 earns more. Firm 1 has **no best
response** to $p_2=2$, nor to any $p_2<50.5$ (its monopoly price, footnote 7, p. 92).

*Ruling out every candidate (pp. 92–93).* $p_i\ge p_j>2$: firm $i$ deviates to a price in $(2,p_j)$. $p_i\ge p_j<1$:
firm $j$ sells at a loss and deviates up. So any equilibrium has prices in $[1,2]$; there, $p_1\ge p_2$ fails (firm 1
undercuts just below $p_2$) and $p_2\ge p_1$ fails (firm 2 prefers any price above $p_1$). **No pure equilibrium.**

> **The culprit is a discontinuous payoff, not the solution concept.** Nash's existence theorem
> ([[L02-09-existence]]) needs finite games (or continuous payoffs); this game has neither. Tadelis's pragmatic
> line (p. 93): discreteness removes the problem, so continuous prices are a convenience to be dropped when they
> create such anomalies.

---

## 5 · Not covered in class — strategic complements and differentiated products

**Tadelis's Remark (p. 93).** Cournot best replies fall in the rival's choice (**strategic substitutes**; also the
commons). Bertrand best replies **rise** with the rival's price between marginal cost and the monopoly price
(**strategic complements**). Note a slip in the printed text: the Remark says the monopoly price is "equal to 45";
in the leading example it is **55** (45 is the monopoly *quantity*, p. 89).

**Gibbons §1.2.B (pp. 21–22): differentiated products.** Demand $q_i=a-p_i+bp_j$ with $0<b<2$, marginal cost $c<a$.
Profit $\pi_i=(a-p_i+bp_j)(p_i-c)$.

$$\frac{\partial\pi_i}{\partial p_i}=(a-p_i+bp_j)-(p_i-c)=0\ \Longrightarrow\ p_i=\frac{a+bp_j+c}{2}.$$

Slope $b/2>0$: **upward-sloping** best responses. Symmetric solution $p^*=\frac{a+bp^*+c}{2}\Rightarrow(2-b)p^*=a+c$:

$$\boxed{\;p_1^*=p_2^*=\frac{a+c}{2-b}\;}$$

which is why the model needs $b<2$. Prices are above cost: product differentiation softens price competition.
Gibbons stresses that "Cournot equilibrium" and "Bertrand equilibrium" are **the same concept (Nash) applied to two
different games** (p. 21).

| | Cournot (quantities) | Bertrand, homogeneous | Bertrand, differentiated |
|---|---|---|---|
| Best response slope | $-1/2$ (substitutes) | $+1$ one cent below (complements) | $+b/2$ (complements) |
| Price, $a=100$, $c=10$ | 40 | 10 | $(a+c)/(2-b)$ |
| Market power with 2 firms | partial | none | partial |

---

## Links

- Neighbours: [[L02-03-cournot]] (quantities), [[L02-09-existence]] (why discontinuity breaks existence).
- Applications: Cabral §7.1 (pp. 161–167) for the IO setting; Lecture 6 revisits Bertrand collusion under
  repetition ([[../L06/L06-00-map|Lecture 6]]).
- Code: [[L02-12-python]] §4 (the cent-grid best response, brute force).
- Practice: Tadelis 5.12 (p. 98), 5.16 (p. 99); Gibbons 1.7 (pp. 49–50).
