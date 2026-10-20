---
tags: [notes, lecture-07, auctions, first-price, dutch-auction, bid-shading]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §13.1.3 'First-Price Sealed-Bid and Dutch Auctions', printed pp. 276–279 (Claim 13.1, Assumption 13.1, eqs. 13.1–13.8, footnote 5); Gibbons (1992) §3.2.B 'An Auction' and Appendix 3.2.B, pp. 155–158; Cabral (2017) §6.4, p. 141"
---

# 13.1.3 · First-price and Dutch auctions: shade the bid until margin and win probability balance

> **Claim.** When the winner pays his own bid, bidding one's value guarantees zero, so every bidder
> **shades**. With no dominant strategy, the bid depends on beliefs about the others' bids, and the
> symmetric BNE solves one differential equation: $s(\theta)=\theta-\int_{\underline\theta}^{\theta}F^{n-1}/F(\theta)^{n-1}$,
> which for uniform values is $\boxed{s(\theta)=\tfrac{n-1}{n}\theta}$. The Dutch auction is the same
> game in different clothes.
>
> Prev: [[L07-06-second-price-english]] · Next: [[L07-08-revenue-equivalence]] · Map: [[L07-00-map]]

---

## 1 · C — bidding your value is dominated (p. 276)

> **Claim 13.1.** In a first-price sealed-bid auction it is a dominated strategy for a player to bid
> his valuation.

Bidding $\theta_i$ pays $0$ if you lose and $\theta_i-\theta_i=0$ if you win: **zero always**. Bidding
slightly less wins with positive probability (against low enough rival bids) at a positive margin:
expected payoff $>0$. The domination is **weak** — against rival bids above $\theta_i$ both bids earn 0.

**The trade-off** (p. 276): lowering the bid raises the margin $\theta_i-b_i$ when you win (marginal
benefit) and lowers the probability of winning (marginal cost). Unlike §13.1.1, the best bid now
**depends on the others' strategies** — no weakly dominant strategy exists (p. 277).

---

## 2 · C — the expected payoff (p. 277)

> **Assumption 13.1.** The higher a player's valuation, the higher his bid: $\theta_j>\theta_j'\Rightarrow
> s_j(\theta_j)>s_j(\theta_j')$.

So $s_j$ is invertible: a bid $b$ comes from exactly one type $s_j^{-1}(b)$, and

$$\Pr\{s_j(\theta_j)<b_i\}=\Pr\{\theta_j<s_j^{-1}(b_i)\}=F_j\big(s_j^{-1}(b_i)\big).$$

Independence multiplies these across rivals:

$$E_{\theta_{-i}}\big[u_i(b_i,s_{-i}(\theta_{-i});\theta_i)\mid\theta_i\big]=\prod_{j\ne i}F_j\big(s_j^{-1}(b_i)\big)\times(\theta_i-b_i).\tag{13.1}$$

> **Here the common prior has real bite** (p. 277): $F_j$ and $s_j$ both enter (13.1). In the
> second-price auction neither did.

---

## 3 · C — the symmetric equilibrium, every step (pp. 277–279)

Symmetric bidders: values on $[\underline\theta,\overline\theta]$ with common $F$, density $f$; all rivals use $s(\cdot)$.
Type $\theta_i$ solves

$$\max_{b\ge0}\;\big[F(s^{-1}(b))\big]^{n-1}(\theta_i-b).\tag{13.2}$$

**FOC** (interior), product rule:

$$-\big[F(s^{-1}(b))\big]^{n-1}+(n-1)\big[F(s^{-1}(b))\big]^{n-2}f(s^{-1}(b))\,\frac{d\,s^{-1}(b)}{db}\,(\theta_i-b)=0.\tag{13.3}$$

**Impose equilibrium.** $b=s(\theta)$ must solve (13.3) for every $\theta$. Then $s^{-1}(b)=\theta$ and
$\frac{d\,s^{-1}(b)}{db}=\frac1{s'(\theta)}$:

$$-[F(\theta)]^{n-1}+(n-1)[F(\theta)]^{n-2}f(\theta)\,\frac{\theta-s(\theta)}{s'(\theta)}=0.\tag{13.4}$$

**Rearrange.** Multiply by $s'(\theta)$ and move the $s(\theta)$ term left:

$$[F(\theta)]^{n-1}s'(\theta)+(n-1)[F(\theta)]^{n-2}f(\theta)s(\theta)=(n-1)[F(\theta)]^{n-2}f(\theta)\,\theta.\tag{13.5}$$

**Spot the product rule.** The left side is $\frac{d}{d\theta}\big([F(\theta)]^{n-1}s(\theta)\big)$, since
$\frac{d}{d\theta}[F]^{n-1}=(n-1)[F]^{n-2}f$. Integrate from $\underline\theta$ (where $F=0$):

$$[F(\theta)]^{n-1}s(\theta)=\int_{\underline\theta}^{\theta}(n-1)[F(x)]^{n-2}f(x)\,x\,dx.\tag{13.6}$$

**Integrate by parts** (footnote 5, p. 278) with $g'(x)=(n-1)[F(x)]^{n-2}f(x)$, $g=[F]^{n-1}$, $h(x)=x$:

$$\int_{\underline\theta}^{\theta}(n-1)[F(x)]^{n-2}f(x)\,x\,dx=[F(\theta)]^{n-1}\theta-\int_{\underline\theta}^{\theta}[F(x)]^{n-1}dx$$

(the boundary term at $\underline\theta$ vanishes because $F(\underline\theta)=0$). Divide by $[F(\theta)]^{n-1}$:

$$\boxed{\;s(\theta)=\theta-\frac{\int_{\underline\theta}^{\theta}[F(x)]^{n-1}dx}{[F(\theta)]^{n-1}}\;}\tag{13.7}$$

The bid is below the value, by an amount that depends on $F$, $n$ and $\theta$; this is the unique
symmetric BNE (p. 278, proof beyond the book).

### 3.1 · Uniform values on $[0,1]$ (p. 279)

$F(x)=x$: $\int_0^\theta x^{n-1}dx=\theta^n/n$, so

$$s(\theta)=\theta-\frac{\theta^n/n}{\theta^{n-1}}=\theta-\frac\theta n=\boxed{\;\theta\,\frac{n-1}{n}\;}\tag{13.8}$$

The **bid-shading factor** $(n-1)/n\in(0,1)$ rises with $n$: more bidders, fiercer competition, bids
closer to values.

| $n$ | 2 | 3 | 5 | 10 | $\to\infty$ |
|---|---|---|---|---|---|
| $s(\theta)/\theta$ | 0.5 | 0.667 | 0.8 | 0.9 | 1 |

### 3.2 · A reading of (13.7) that pays off in the next note

The highest of the $n-1$ rival values, $Y$, has c.d.f. $F^{n-1}$. Integrating by parts as above,
$E[Y\mid Y<\theta]=\theta-\int_{\underline\theta}^\theta F^{n-1}/F(\theta)^{n-1}$. So

> **the first-price bid equals the expected highest rival value, given that it is below yours** —
> exactly the price you would expect to pay *when you win* in a second-price auction. Uniform case:
> $E[Y\mid Y<\theta]=\tfrac{n-1}{n}\theta$. Revenue equivalence ([[L07-08-revenue-equivalence]]) is this
> line averaged over types.

---

## 4 · Worked — Gibbons's two-bidder auction (pp. 155–158)

Two bidders, $v_i\sim U[0,1]$ independent, highest bid wins and pays it, ties by coin flip.

**Guess linear, $b_j(v_j)=a_j+c_jv_j$** (not a restriction on strategies — a question whether a linear
equilibrium exists). For $a_j\le b_i\le a_j+c_j$:

$$\max_{b_i}\;(v_i-b_i)\Pr\{b_i>a_j+c_jv_j\}=(v_i-b_i)\frac{b_i-a_j}{c_j}.$$

FOC: $-(b_i-a_j)+(v_i-b_i)=0\Rightarrow b_i=\dfrac{v_i+a_j}{2}$ when $v_i\ge a_j$ (else bid $a_j$, lose).
Linearity rules out $0<a_j<1$ (the reply would be flat, then rising) and $a_j\ge1$ (it would mean
$b_j(v_j)\ge v_j$), so $a_j\le0$, giving $c_i=\tfrac12$, $a_i=a_j/2$; symmetry gives $a=a/2=0$:

$$b_i(v_i)=\frac{v_i}{2}\qquad\text{(p. 156) — (13.8) at }n=2.$$

**Without the linear guess** (Appendix 3.2.B, pp. 157–158): with $b(\cdot)$ increasing and differentiable,
$\Pr\{b_i>b(v_j)\}=b^{-1}(b_i)$, so bidder $i$ maximizes $(v_i-b_i)\,b^{-1}(b_i)$. FOC:
$-b^{-1}(b_i)+(v_i-b_i)\frac{d\,b^{-1}(b_i)}{db_i}=0$. Impose $b_i=b(v_i)$, so $b^{-1}(b_i)=v_i$ and the
derivative is $1/b'(v_i)$:
$$-v_i+\frac{v_i-b(v_i)}{b'(v_i)}=0\iff b'(v_i)\,v_i+b(v_i)=v_i\iff\frac{d}{dv_i}\big[b(v_i)v_i\big]=v_i .$$
Integrate: $b(v)v=\tfrac12v^2+k$; no one bids above his value and bids are nonnegative, so $b(0)=0$,
$k=0$, $b(v)=v/2$ — the $n=2$, $F(x)=x$ case of (13.5).

**Numbers, $v=0.8$** (illustrative): the rival bids $v_j/2$, so a bid $b$ wins iff $v_j<2b$.

| Bid $b$ | $\Pr\{\text{win}\}=\min(1,2b)$ | Margin $0.8-b$ | Expected payoff |
|---|---|---|---|
| 0.30 | 0.60 | 0.50 | 0.300 |
| **0.40** | **0.80** | **0.40** | **0.320** |
| 0.50 | 1.00 | 0.30 | 0.300 |
| 0.80 | 1.00 | 0.00 | 0.000 |

![Left: equilibrium bid functions b = (n-1) theta / n for n = 2, 3, 5, 10 below the 45-degree second-price line. Right: expected payoff of own bid for value 0.8, peaking at 0.40 (payoff 0.32) with n = 2 and at 0.64 (payoff 0.066) with n = 5, and falling to zero at b = 0.8](figures/L07-fpa-bidding.png)
*Figure — left: (13.8) for four values of $n$, against the second-price bid $b=\theta$. Right: (13.2) with rivals playing (13.8), $\theta=0.8$; the peaks sit at $(n-1)\theta/n$ with height $\theta^n/n$. Sources: Tadelis pp. 277–279, Gibbons p. 156; $\theta=0.8$ illustrative.*

The $n=2$ curve has a kink at $b=0.5$: above it the bidder beats every rival bid (rivals never bid more
than $\tfrac12$), so raising the bid only lowers the margin. With five bidders winning is rarer and the
peak is lower and further right — **more competition, less shading, less surplus**.

> **Interactive companion.** [The Bid Shading Desk](companions/companion-auction-bidding.html) — move
> your bid $b$ and watch the first-price payoff tile fall on both sides of $(n-1)\theta/n$; raise $n$ and
> watch the optimum slide toward $\theta$.

---

## 5 · C — the Dutch auction is the first-price auction (p. 279)

In a Dutch auction each bidder decides **at what price to shout "buy"**. While the price falls nothing
useful is learned — the only news, "someone shouted", ends the auction. So a strategy is a map from
value to a stopping price, the highest stopping price wins and pays it: **the same normal form as the
first-price sealed-bid auction**. The two are **strategically equivalent** and share their BNE, (13.7).

| Pair | Relation | Why |
|---|---|---|
| Dutch ↔ first-price | **strategically equivalent** (same normal form) | nothing observed during the descent changes anyone's choice |
| English ↔ second-price | **outcome-equivalent under private values** (Prop. 13.2) | in the English auction bidders *do* see others quit — harmless with private values, informative with common values |

---

## Links

- Prev: [[L07-06-second-price-english]] · Next: the revenue comparison,
  [[L07-08-revenue-equivalence]].
- Threshold and monotone strategies with continuous types: [[L07-04-threshold-strategies-purification]].
- Lecture 1's discrete first-price auction by IESDS: `Listas/pratica-lecture-01.md` item 17
  (Tadelis 4.3, p. 76) and `Listas/pratica-lecture-01-solutions/item17.tex`.
- Code: [[L07-12-python]] §7 (`fpa_bid` for any $F$ via (13.7), `fpa_best_reply`).
- **Exercises (number + page only):** Tadelis 13.5 (p. 286), 13.6 (pp. 286–287), 13.7, 13.9 (p. 287);
  Gibbons 3.6 (p. 170), 3.7 (pp. 170–171); Muñoz-Garcia Ch. 8 Ex. 1 (p. 350), Ex. 2 (p. 352), Ex. 3
  (p. 355), Ex. 8 (p. 371).
