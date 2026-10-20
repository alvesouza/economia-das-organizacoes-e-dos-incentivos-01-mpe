---
tags: [notes, lecture-03, stackelberg, cournot, first-mover-advantage, continuous-strategies]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §8.3.2 (pp. 160–163): eqs. (8.1)–(8.2), Figs. 8.9–8.10, Remark on p. 163; Gibbons (1992) §2.1.B (pp. 61–64); Cabral (2017) §7.2 (pp. 170–171) on commitment"
---

# 8.3.2 · Stackelberg competition: the leader's quantity is a commitment

> **Claim.** Make Cournot sequential: firm 1 chooses $q_1$, firm 2 sees it and replies. Backward
> induction turns firm 2's best-response function into a **menu** from which firm 1 picks its favourite
> point: $q_1=45$, $q_2=22.5$, profits $1012.5$ and $506.25$ against Cournot's $900$ each. **The leader
> could have produced its Cournot quantity and chose not to, so it gains; the follower loses; total
> output rises and price falls.** And the outcome is not an equilibrium: the SPE must specify firm 2's
> reply to *every* $q_1$.
> Prev: [[L03-06-credibility-entry-commitment]] · Next: [[L03-08-time-inconsistency]] · Map: [[L03-00-map]]

---

## 1 · C — the game (pp. 160–161)

Tadelis's Cournot example: inverse demand $p=100-q$ with $q=q_1+q_2$, costs $c_i(q_i)=10q_i$. In the
simultaneous game (Lecture 2) each firm solves $\max_{q_i}(100-q_i-q_j)q_i-10q_i$, with first-order
condition $100-2q_i-q_j-10=0$, so

$$q_i(q_j)=\frac{90-q_j}{2}.$$

**Change one detail**: firm 1 chooses $q_1$ first, firm 2 **observes it** and then chooses $q_2$.

| | Cournot (Fig. 8.10) | Stackelberg (Fig. 8.9) |
|---|---|---|
| Firm 2's information | one information set containing every $q_1$ | **a separate information set for each $q_1$** (a continuum) |
| Proper subgames | the whole game only | the whole game **and one per $q_1$** |
| Type | imperfect information | perfect information |

---

## 2 · C — backward induction, every step (pp. 160–161)

**Step 1: the follower.** At the information set where it has seen $q_1$, firm 2 maximizes
$(100-q_1-q_2)q_2-10q_2$. First-order condition: $100-q_1-2q_2-10=0$, so

$$q_2(q_1)=\frac{90-q_1}{2}\qquad(8.1)$$

The formula is Cournot's best response, but its meaning changed: there it answered a *belief* about
$q_1$; here it answers an *observed* $q_1$ (p. 161; Gibbons p. 62).

**Step 2: the leader.** Firm 1 knows (common knowledge of rationality) that firm 2 will follow (8.1),
so it substitutes it in:

$$\max_{q_1}\ \Bigl(100-q_1-\frac{90-q_1}{2}\Bigr)q_1-10q_1\qquad(8.2)$$

Simplify the price: $100-q_1-45+\tfrac{q_1}{2}=55-\tfrac{q_1}{2}$, so the objective is
$(55-\tfrac{q_1}{2})q_1-10q_1=45q_1-\tfrac{q_1^2}{2}$. Its derivative $45-q_1=0$ gives
$q_1=45$. (Tadelis writes the condition unsimplified: $100-2q_1-45+q_1-10=0$.)

**Step 3: the numbers.**

| | Stackelberg | Cournot | Change |
|---|---|---|---|
| $q_1$ | $45$ | $30$ | $+15$ |
| $q_2$ | $\tfrac{90-45}{2}=22.5$ | $30$ | $-7.5$ |
| $Q$ | $67.5$ | $60$ | $+7.5$ ($=\tfrac98\times60$) |
| $p$ | $100-67.5=32.5$ | $40$ | $-7.5$ |
| $\pi_1$ | $(32.5-10)\times45=\mathbf{1012.5}$ | $900$ | $\mathbf{+112.5}$ |
| $\pi_2$ | $(32.5-10)\times22.5=\mathbf{506.25}$ | $900$ | $-393.75$ |
| $\pi_1+\pi_2$ | $1518.75$ | $1800$ | $-281.25$ |
| consumer surplus $Q^2/2$ | $2278.125$ | $1800$ | $+478.125$ |

> **"When two firms are competing by setting quantities, if one firm can somehow commit to move first,
> it will enjoy a first-mover advantage"** (p. 161).

![Left: the q1-q2 plane with firm 2's best-response line q2 = (90 - q1)/2, firm 1's best-response line, the Cournot point (30, 30) where they cross, the Stackelberg point (45, 22.5) on firm 2's line, and two dashed leader isoprofit curves: 900 through Cournot and 1012.5 tangent to firm 2's line at the Stackelberg point. Right: the leader's profit along firm 2's reaction curve, a hump peaking at q1 = 45 with profit 1012.5, with the Cournot quantity 30 and profit 900 marked lower on the same hump](figures/L03-stackelberg-vs-cournot.png)
*Figure — the leader chooses its point on firm 2's reaction curve. Left: quantity space with the Cournot and Stackelberg points and the leader's isoprofits. Right: the reduced objective (8.2). Source: Tadelis eqs. (8.1)–(8.2), numbers p. 161.*

On the left, firm 1's isoprofit curves are hump-shaped and lower curves mean higher profit; the
Stackelberg point is where the lowest isoprofit firm 1 can reach just touches firm 2's line. The Cournot
point also lies on firm 2's line, so it is on the menu; on the right it sits on the same hump at 900,
below the peak.

### 2.1 · Why the leader must gain, the follower must lose, and the total must fall

Gibbons's argument (p. 63) needs no algebra:

1. **Leader gains.** In the Stackelberg game firm 1 could choose its Cournot quantity, and firm 2 would
   reply with its Cournot quantity (because $q_2(30)=30$). It gets 900 that way and chooses something
   else, so it gets at least 900.
2. **Price falls.** Aggregate output rises from $\tfrac23(a-c)$ to $\tfrac34(a-c)$.
3. **Industry profit falls.** Below the monopoly output, more output means less joint profit.
4. **Follower loses.** Joint profit fell and the leader's share rose, so the follower's fell.

### 2.2 · The general linear case (Gibbons pp. 62–63)

With $P(Q)=a-Q$ and marginal cost $c$: $R_2(q_1)=\tfrac{a-q_1-c}{2}$ (for $q_1<a-c$), and the leader
solves $\max_{q_1}q_1\bigl[a-q_1-R_2(q_1)-c\bigr]=\max_{q_1}q_1\tfrac{a-q_1-c}{2}$, so

$$q_1^*=\frac{a-c}{2},\qquad R_2(q_1^*)=\frac{a-c}{4},\qquad Q^S=\frac34(a-c)>Q^C=\frac23(a-c).$$

Check at $a=100$, $c=10$: $45$, $22.5$, $67.5$ and $60$. ✓

With slope $b$ and costs $c_1,c_2$ (the companion's model, same steps):
$q_1^S=\tfrac{a-2c_1+c_2}{2b}$, $q_2^S=\tfrac{a+2c_1-3c_2}{4b}$, and the follower is shut out when
$c_2\ge\tfrac{a+2c_1}{3}$; Cournot gives $q_i^C=\tfrac{a-2c_i+c_j}{3b}$.

> **Interactive companion.** [The First-Mover Desk](companions/companion-stackelberg-vs-cournot.html) —
> move $a$, $b$, $c_1$, $c_2$ and read the first-mover advantage live; raise $c_2$ past
> $(a+2c_1)/3$ (40 at the defaults) to watch the leader's commitment shut the follower out while Cournot
> still lets it in, and past $(a+c_1)/2$ (55) where both games become monopoly and the advantage is 0.

---

## 3 · C — an equilibrium is not an outcome (p. 161)

> **"Writing down $(q_1,q_2)=(45,22.5)$ is not identifying a Nash equilibrium because $q_1=45$ is not a
> best response to $q_2=22.5$."** (p. 161)

Check it: if firm 2 produced 22.5 regardless, firm 1's best response would be
$q_1(22.5)=\tfrac{90-22.5}{2}=33.75\ne45$. The pair of numbers is the **outcome**; the equilibrium is

$$\Bigl(q_1=45,\ \ q_2(q_1)=\frac{90-q_1}{2}\Bigr),$$

a number for the leader and **a function** for the follower, one action at each of its continuum of
information sets. This is the Gibbons distinction of [[L03-05-subgame-perfection]] §5: outcome
$(a_1^*,R_2(a_1^*))$, equilibrium $(a_1^*,R_2(\cdot))$.

---

## 4 · C — Nash equilibria that are not subgame perfect (pp. 162–163)

**Cournot's outcome is a Nash equilibrium of the Stackelberg game.** Take $q_1=30$ and the *constant*
strategy $q_2(q_1)=30$ for every $q_1$.

| Check | Computation | Holds? |
|---|---|---|
| firm 2's plan is a best reply on the path | $q_2(30)$ should be $\tfrac{90-30}{2}=30$ | yes |
| firm 1's $q_1=30$ is a best reply to "30 whatever you do" | $\max_{q_1}(100-q_1-30-10)q_1$ ⇒ $q_1=30$ | yes |
| firm 2's plan is a best reply **off** the path | at $q_1=45$ it plays 30, but $\tfrac{90-45}{2}=22.5$ | **no** |

So it is a Nash equilibrium and not subgame perfect: "mutual best responses on the equilibrium path is
all that Nash equilibrium requires" (p. 163). The only sequentially rational strategy for firm 2 is
$q_2(q_1)=\tfrac{90-q_1}{2}$, which makes $(45,\tfrac{90-q_1}{2})$ **the unique SPE**.

**A continuum of Nash equilibria** (Remark, p. 163). Firm 2 threatens to flood the market unless firm 1
produces exactly 20:

$$q_2(q_1)=\begin{cases}35 & \text{if } q_1=20\\ 100 & \text{if } q_1\ne20\end{cases}$$

Against it, $q_1=20$ earns $(100-20-35-10)\times20=700>0$, while any other $q_1$ faces a price of
$\max\{0,100-q_1-100\}=0$ and earns $-10q_1\le0$. So $q_1=20$ is a best reply, and 35 is firm 2's best
reply to 20 since $\tfrac{90-20}{2}=35$. Replacing 20 by any $\hat q_1\in[0,90]$ and 35 by
$\tfrac{90-\hat q_1}{2}$ gives a Nash equilibrium for each $\hat q_1$: **every point of firm 2's
reaction curve is a Nash outcome; one is subgame perfect.** The flooding threat is the textbook
non-credible threat: having seen $q_1\ne20$, producing 100 would drive the price to 0 and lose firm 2
money.

> *Source detail.* The printed text on p. 163 says "$q_2=40$ is a best response to $q_1=20$"; with
> (8.1) the best response is $\tfrac{90-20}{2}=35$, which is also the value in the displayed strategy.
> These notes use 35 (checked in [[L03-11-python]] §3).

---

## 5 · U — more information can hurt (Gibbons p. 63)

In single-person decisions more information never hurts. Here firm 2 knows $q_1$ **and firm 1 knows
that firm 2 knows it**, and firm 2 ends up worse off than in Cournot. Gibbons's check: let firm 1 move
first but firm 2 *not observe* $q_1$. If firm 2 believed $q_1=\tfrac{a-c}{2}$, it would reply
$\tfrac{a-c}{4}$; but firm 1's best response to $\tfrac{a-c}{4}$ is
$\tfrac{a-c-(a-c)/4}{2}=\tfrac38(a-c)$, not $\tfrac{a-c}{2}$, so that belief is inconsistent. The unique
Nash equilibrium of the unobserved game is Cournot, $\tfrac{a-c}{3}$ each. **Moving first is worth
nothing unless the move is observed**, which is the [[L03-01-extensive-form]] lesson (information,
not clock time) with a price tag.

---

## 6 · Organizational reading

The Stackelberg leader is a firm whose capacity, plant or contract is sunk before rivals choose: a
commitment in the sense of [[L03-06-credibility-entry-commitment]] §3.2, implemented by moving first
rather than by a bond. Gibbons's example is General Motors' leadership role in the U.S. car industry
(p. 61). The same structure, a leader that sets a variable and a follower that best-responds, is
Leontief's monopoly union (Gibbons §2.1.C, pp. 64–68): the union sets the wage, the firm picks
employment on its labour demand curve, and the outcome is inefficient, which [[../L04/L04-00-map|Lecture 4]]
takes up as bargaining.

---

## Links

- Cournot's best responses and Nash equilibrium: [[../L02/L02-00-map|Lecture 2]]; IESDS in Cournot:
  [[../L01/L01-00-map|Lecture 1]].
- Collusion among Cournot firms when the game repeats: [[../L06/L06-00-map|Lecture 6]].
- Python: `stackelberg`, `cournot`, `flood`, [[L03-11-python]] §3. Figure code:
  `figures/make_figures.py::stackelberg_vs_cournot`.
- Exercises: Tadelis 8.4 (p. 170), 8.6 (p. 170–171), 8.9 (p. 172); Muñoz-Garcia & Toro-González Ch. 4,
  Exercise 11 (p. 180), 12 (p. 185), 13 (p. 189), 14 (p. 192), 15 (p. 195).
