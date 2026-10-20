---
tags: [notes, lecture-02, bertrand, price-competition, existence, strategic-complements, differentiated-products]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §5.2.4, printed pp. 88–93 (discrete best response p. 90; Prop. 5.2 p. 91; asymmetric costs and Fig. 5.3 pp. 91–93; Remark on strategic complements p. 93); Gibbons (1992) §1.2.B pp. 21–22 (differentiated products)"
---

# 5.2.4 · Bertrand duopoly: two firms are enough for marginal-cost pricing

> **Claim.** Change the strategy from quantity to price and the same market behaves competitively: with identical
> costs the unique equilibrium of the continuous game is **$p_1=p_2=c$** (Prop. 5.2), proved by showing every other
> profile has a profitable undercut. On a one-cent grid there are exactly **two** equilibria, (10, 10) and
> (10.01, 10.01). With **unequal** costs and continuous prices **no pure equilibrium exists**: the payoff jumps at
> the rival's price, so the efficient firm has no best response. Differentiated products restore interior,
> upward-sloping best responses (**strategic complements**).
>
> Prev: [[L02-03-cournot]] · Next: [[L02-05-commons]] · Map: [[L02-00-map]]

---

## 1 · C — the game (p. 88)

Demand $p=100-q$, $c_i(q_i)=10q_i$, prices $p_i\in[0,\infty)$; the lower price takes the market, a tie splits it:

$$v_i(p_i,p_j)=\begin{cases}(100-p_i)(p_i-10)&p_i<p_j\\ \tfrac12(100-p_i)(p_i-10)&p_i=p_j\\ 0&p_i>p_j\end{cases}$$

**Monopoly benchmark (p. 89).** $\max_p(100-p)(p-10)$: FOC $110-2p=0$, so $p=55$, $q=45$, profit $45\cdot45=2025$.

---

## 2 · C — the best response on a cent grid (pp. 89–90)

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

## 3 · C — Proposition 5.2: continuous prices (p. 91)

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

## 4 · C — unequal costs: no equilibrium in pure strategies (pp. 91–93)

$c_1=1$, $c_2=2$, $p=100-q$.

**With cents.** $(p_1,p_2)=(1.99,2.00)$ is an equilibrium: firm 1 takes the market at a margin of 0.99 and would lose
by raising to 2.00 (split) or above (nothing); firm 2 sells nothing and would lose money by pricing below 2.
(Tadelis exercise 5.12, p. 98, asks for the others.)

**Continuous prices.** The "limit" $p_1=p_2=2$ is **not** an equilibrium: firm 1 earns
$\tfrac12(98)(1)=49$ and would earn almost $98$ by pricing a hair below 2. But there is no best "hair":

$$v_1(p_1,2)=\begin{cases}(100-p_1)(p_1-1)&p_1<2\ \ (\to98)\\ 49&p_1=2\\ 0&p_1>2\end{cases}$$

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

## 5 · C — strategic complements and differentiated products

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
