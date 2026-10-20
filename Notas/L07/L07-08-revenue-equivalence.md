---
tags: [notes, lecture-07, auctions, revenue-equivalence, order-statistics]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §13.1.4 'Revenue Equivalence', printed pp. 279–282 (four conditions p. 280, order statistics pp. 280–281, eqs. 13.9–13.10, the uniform computation pp. 281–282); Cabral (2017) §6.4, p. 141. Stated and checked for the uniform IPV case only — mechanism design (Tadelis Ch. 14, MWG Ch. 23) is outside the course."
---

# 13.1.4 · Revenue equivalence: shading in the first-price auction exactly offsets paying the second price

> **Claim.** With independent private values and risk-neutral bidders, **all four standard auctions
> give the seller the same expected revenue**. In the uniform case both the expected highest
> first-price bid and the expected second-highest value equal $\boxed{(n-1)/(n+1)}$ — and the
> equality already holds **type by type**: every bidder expects to pay the same amount in both
> formats. The prices are different random variables with the same mean.
>
> Prev: [[L07-07-first-price-dutch]] · Next: [[L07-09-common-values-curses]] · Map: [[L07-00-map]]

---

## 1 · C — the statement (p. 280)

The **revenue equivalence theorem** (Vickrey 1961; Myerson 1981; Riley and Samuelson 1981): any auction
game satisfying four conditions yields the seller the **same expected revenue** and **each type of
bidder the same expected payoff**:

| # | Condition | Fails when … |
|---|---|---|
| 1 | each type is drawn from a "well-behaved" distribution ($F_i$ strictly increasing and continuous) | values have atoms or gaps |
| 2 | bidders are **risk neutral** | bidders are risk averse (Tadelis exercise 13.7, p. 287) |
| 3 | the bidder with the **highest type wins** | a reserve price keeps the object unsold, or bidders are asymmetric |
| 4 | the lowest possible type $\underline\theta$ has expected payoff **zero** | entry fees or subsidies shift the bottom |

The two easy halves (p. 279): second-price and English share a dominant-strategy outcome; first-price
and Dutch are strategically equivalent. **The surprise is across the halves:** shading in the
first-price auction and settling for the second-highest value in the second-price auction come to the
same thing on average.

*Scope.* The general proof uses the envelope theorem and belongs to mechanism design; these notes
**state** it and **verify** it for $n$ uniform bidders — what Tadelis does (p. 280).

---

## 2 · C — order statistics (pp. 280–281)

Draw $x_1,\dots,x_n$ i.i.d. from $F$. The **first-order statistic** $x_n^{[1]}=\max_ix_i$ is the highest
draw, the **second-order statistic** $x_n^{[2]}$ the second highest.

| Auction | What the seller receives | Expected revenue |
|---|---|---|
| second-price | the second-highest **value** | $E[\theta_n^{[2]}]$ |
| first-price | the highest **bid** $s(\theta)$ | $E[b_n^{[1]}]$ |

**C.d.f. of the maximum.** $\Pr\{\max_ix_i\le x\}=\Pr\{x_1\le x\}\cdots\Pr\{x_n\le x\}=[F(x)]^n$ (independence,
footnote 8, p. 281).

**C.d.f. of the second highest** (pp. 281–282). $\{x_n^{[2]}\le x\}$ happens in two disjoint ways: all $n$ draws
below $x$, or exactly one above and $n-1$ below (which one: $n$ ways):

$$F_n^{[2]}(x)=[F(x)]^n+n\,(1-F(x))[F(x)]^{n-1}=n[F(x)]^{n-1}-(n-1)[F(x)]^n .$$

---

## 3 · C — the first-price side (p. 281)

Each bid is $s(\theta)=\tfrac{n-1}{n}\theta$, so bids are uniform on $\big[0,\tfrac{n-1}{n}\big]$ with c.d.f.
$F(b)=\tfrac{n}{n-1}b$. The highest bid has

$$F_n^{[1]}(x)=\Big(\frac{nx}{n-1}\Big)^n,\quad0\le x\le\frac{n-1}{n},\tag{13.9}$$
$$f_n^{[1]}(x)=n\Big(\frac{n}{n-1}\Big)^n x^{n-1}.$$

$$E\big[b_n^{[1]}\big]=\int_0^{\frac{n-1}{n}}x\cdot n\Big(\frac{n}{n-1}\Big)^nx^{n-1}dx
=n\Big(\frac{n}{n-1}\Big)^n\frac{1}{n+1}\Big(\frac{n-1}{n}\Big)^{n+1}
=\frac{n}{n+1}\cdot\frac{n-1}{n}=\boxed{\frac{n-1}{n+1}}$$

---

## 4 · C — the second-price side (p. 282)

Values are uniform, $F(x)=x$:

$$F_n^{[2]}(x)=nx^{n-1}-(n-1)x^n,\tag{13.10}$$
$$f_n^{[2]}(x)=n(n-1)x^{n-2}-n(n-1)x^{n-1}.$$

$$E\big[\theta_n^{[2]}\big]=\int_0^1\big(n(n-1)x^{n-1}-n(n-1)x^n\big)dx
=\Big[(n-1)x^n-\frac{n(n-1)}{n+1}x^{n+1}\Big]_0^1=(n-1)-\frac{n(n-1)}{n+1}=\boxed{\frac{n-1}{n+1}}$$

| $n$ | 2 | 3 | 4 | 5 | 6 | 10 |
|---|---|---|---|---|---|---|
| expected revenue $\frac{n-1}{n+1}$ | $\tfrac13$ | $\tfrac12$ | $\tfrac35$ | $\tfrac23$ | $\tfrac57$ | $\tfrac9{11}$ |

Revenue rises with $n$ toward the top of the support, 1: competition transfers surplus to the seller.

![Left: for n = 3, the density of the highest first-price bid (rising, cut off at 2/3) and the density of the second-highest value (a hump on [0, 1]), both with mean 1/2. Right: expected revenue (n-1)/(n+1) for n = 2 to 10 with simulated first-price and second-price revenues lying on the curve](figures/L07-revenue-equivalence.png)
*Figure — left: the two price distributions of (13.9)–(13.10) at $n=3$ differ in shape and range and share the mean $\tfrac12$. Right: $(n-1)/(n+1)$ against Monte Carlo revenues (200,000 draws per $n$). Source: Tadelis pp. 281–282.*

The first-price price never exceeds $\tfrac{n-1}{n}$ and is more concentrated; the second-price price
ranges over all of $[0,1]$. **Same mean, different risk:** at $n=2$ the first-price price
$\tfrac12\max(\theta_1,\theta_2)$ has variance $\tfrac14\cdot\tfrac1{18}=\tfrac1{72}\approx0.014$, the second-price price
$\min(\theta_1,\theta_2)$ has variance $\tfrac1{18}\approx0.056$ (both computed in [[L07-12-python]] §8) — a
reason a risk-averse *seller* might prefer the first-price format even though the means agree.

---

## 5 · Worked — equivalence type by type

Fix a bidder of value $\theta$ facing $n-1$ uniform rivals; let $Y$ be the highest rival value, c.d.f.
$y^{n-1}$, density $(n-1)y^{n-2}$. Both formats allocate efficiently, so he wins iff $Y<\theta$, with
probability $\theta^{n-1}$.

| | First-price | Second-price |
|---|---|---|
| He pays, when he wins | his bid $\tfrac{n-1}{n}\theta$ | $Y$ |
| Expected payment | $\theta^{n-1}\cdot\tfrac{n-1}{n}\theta$ | $\int_0^\theta y\,(n-1)y^{n-2}dy=\tfrac{n-1}{n}\theta^n$ |
| Expected surplus | $\theta^n-\tfrac{n-1}{n}\theta^n=\tfrac{\theta^n}{n}$ | $\tfrac{\theta^n}{n}$ |

**Identical for every $\theta$** — the second claim of the theorem — and the lowest type $\theta=0$ gets 0
(condition 4). Average the payment over $\theta\sim U[0,1]$ and multiply by the $n$ bidders:
$$n\int_0^1\frac{n-1}{n}\theta^n\,d\theta=\frac{n-1}{n+1},$$
the revenue of §3–4 by a third route. This is [[L07-07-first-price-dutch]] §3.2 at work: the
first-price bid **is** the expected second-price payment conditional on winning.

**Numbers ($n=2$, $\theta=0.8$):** wins with probability $0.8$; first-price pays $0.4$ → expected payment
$0.32$; second-price expected payment $\tfrac12\cdot0.8^2=0.32$; surplus $0.8^2/2=0.32$ in both.

> **Interactive companion.** [The Bid Shading Desk](companions/companion-auction-bidding.html) — the
> "expected payment", "expected surplus" and "seller's revenue" tiles are computed once and labelled
> "both formats": move $\theta$ and $n$ and they never split.

---

## 6 · U — what the result does and does not say

- **It does not say the auctions are the same game.** Bids, the winner's payment in a given
  realization, and the price's variance all differ.
- **It says the format is not a revenue lever** under its four conditions (Cabral p. 141: with
  independent valuations, "several auction designs yield on average the same revenue level"), so the
  choice can rest on speed, transparency or collusion-resistance.
- **The lever is in breaking a condition**: a reserve price (condition 3), risk-averse bidders
  (condition 2), correlated or common values ([[L07-09-common-values-curses]]). Each is a Tadelis
  exercise, cited below.

---

## Links

- Prev: [[L07-07-first-price-dutch]] · Next: [[L07-09-common-values-curses]].
- The second-price side's dominance: [[L07-06-second-price-english]].
- Code: [[L07-12-python]] §8 (`revenue_fpa`, `revenue_spa` by quadrature; type-by-type payments;
  Monte Carlo; the variance comparison).
- **Exercises (number + page only):** Tadelis 13.3 (pp. 285–286), 13.4, 13.5 (p. 286), 13.6
  (pp. 286–287), 13.7 (p. 287); Muñoz-Garcia Ch. 8 Ex. 3 (p. 355), Ex. 7 (p. 371).
