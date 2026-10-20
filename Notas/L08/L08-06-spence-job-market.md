---
tags: [notes, lecture-08, signaling, spence, job-market, single-crossing, pooling, separating, hybrid]
date: 2026-10-16
status: estimated
source: "Gibbons (1992) §4.2.B 'Job-Market Signaling', pp. 190–205 (eqs. 4.2.1–4.2.10, Figs. 4.2.3–4.2.9); Milgrom & Roberts (1992) Ch. 5 'Signaling', pp. 154–156 (the 50/20 dollars-per-hour, 30%, 10/20 cost example); MWG §13.C, pp. 450–459 (Lemmas 13.C.1–13.C.2, Fig. 13.C.8 on p. 456)"
---

# 4.2.B · Spence's job market: how much education it takes to be believed

> **Claim.** When education costs the able less **at the margin** (single crossing), a high-ability
> worker can separate by acquiring education the low type will not copy. Competitive firms then
> pay each type its productivity, the low type gets **no** education, and the high type gets
> **more than he would under full information** — at least enough that mimicking costs the low
> type the whole wage premium. With M&R's numbers: **separation needs $e_H\in[1.5,\,3]$**, the
> least-cost level is **1.5**, and the education is **pure social waste**. Whether the high type
> gains from being *able* to signal depends on the prior: at 30% high types he does
> ($35>29$); above 50% he would be better off if signaling were impossible.
>
> Prev: [[L08-05-mba-game]] · Next: [[L08-07-limit-pricing]] · Map: [[L08-00-map]]

---

## 1 · C — the model (Gibbons pp. 190–194)

1. Nature draws ability $\eta\in\{H,L\}$, $\Pr\{\eta=H\}=q$ (this note writes $p$, as in Tadelis;
   MWG writes $\lambda$).
2. The worker learns $\eta$ and chooses education $e\ge0$.
3. Two firms observe $e$ (not $\eta$) and simultaneously offer wages; the worker takes the higher.

Payoffs: worker $w-c(\eta,e)$; employing firm $y(\eta,e)-w$; the other firm 0. High ability is more
productive, $y(H,e)>y(L,e)$, and education does not reduce output, $y_e\ge0$ (footnote 5). Spence's
(1973) stark case: **$y(\eta,e)=y(\eta)$ — education is unproductive.**

**The crucial assumption — single crossing (p. 192):**

$$\boxed{\;c_e(L,e)>c_e(H,e)\quad\text{for every }e\;}$$

The **marginal** cost of education is higher for the low type, so his indifference curves in the
$(e,w)$ plane are **steeper** (Fig. 4.2.3): to stay as well off after one more unit of education he
needs a larger raise.

**Competition pins the wage to the belief (4.2.1, p. 193).** With firms sharing a belief
$\mu(H\mid e)$ after any $e$ (on or off the path), Bertrand-style competition drives expected
profit to zero:

$$w(e)=\mu(H\mid e)\,y(H,e)+[1-\mu(H\mid e)]\,y(L,e).\qquad(4.2.1)$$

(4.2.1) replaces Signaling Requirement 2R ([[L08-04-signaling-games]] §2) in this two-Receiver game.

**The benchmark.** Under complete information $w=y(\eta,e)$ and type $\eta$ chooses
$e^*(\eta)=\arg\max_e\,y(\eta,e)-c(\eta,e)$, earning $w^*(\eta)=y[\eta,e^*(\eta)]$ (Fig. 4.2.4). With
unproductive education, $e^*(\eta)=0$.

**No envy vs envy (pp. 194–196).** If $w^*(L)-c[L,e^*(L)]>w^*(H)-c[L,e^*(H)]$ the low type would not
copy the high type even if copying earned him $w^*(H)$ (Fig. 4.2.5): the full-information outcome
separates by itself. The interesting case — and the only one with unproductive education — is
**envy** (Fig. 4.2.6): the low type *would* copy, so the high type must do more.

---

## 2 · C — separating equilibria (Gibbons pp. 199–202; MWG Lemmas 13.C.1–13.C.2, pp. 453–454)

In a separating PBE beliefs are 0 or 1 on the path, so by (4.2.1) each type is paid its own
productivity (**MWG Lemma 13.C.1**). The low type is then paid $y(L,e)$ whatever he does on the
path, so he picks his full-information education: **$e(L)=e^*(L)$** — with unproductive education,
**zero** (**MWG Lemma 13.C.2**: any $e>0$ would cost him and earn nothing).

The high type picks $e_s$ such that the low type will not mimic:

$$\underbrace{w^*(L)-c[L,e^*(L)]}_{\text{L's separating payoff}}\ \ge\ \underbrace{y(H,e_s)-c(L,e_s)}_{\text{L's payoff from mimicking}} .$$

Off-path beliefs that support it (p. 200): **"high iff $e\ge e_s$"**, giving
$w(e)=y(L,e)$ for $e<e_s$ and $y(H,e)$ for $e\ge e_s$. Under this schedule the low type's best
$e<e_s$ is $e^*(L)$; for $e\ge e_s$ his best is $e_s$ (steeper curves), and he is indifferent at
the least-cost level (resolved in favour of $e^*(L)$). The high type's best is $e_s$, because his
flatter indifference curve through $(e_s,y(H,e_s))$ lies above $y(L,e)$ for every $e<e_s$.

> **The high type over-invests:** $e_s>e^*(H)$ in the envy case — "the high-ability worker must
> choose $e_s>e^*(H)$ … because the low-ability worker will mimic any value of $e$ between $e^*(H)$
> and $e_s$" (p. 200). **Any** $e\ge e_s$ small enough that the high type still prefers it to being
> thought low is also a separating PBE (p. 202): a **continuum**.

---

## 3 · Worked — Milgrom & Roberts's numbers (pp. 155–156)

High productivity $\theta_H=\$50$/hour, low $\theta_L=\$20$; 30% high; education unproductive; cost
per unit of education $c_H=\$10$, $c_L=\$20$ (so $c(\theta,e)=c_\theta\,e$, linear, and single crossing is
$c_H<c_L$). The low type chooses $E_L=0$. M&R's two **self-selection constraints**:

$$\text{L must not mimic:}\quad 50-c_L E_H\le20\iff 50-20E_H\le20\iff E_H\ge\frac{50-20}{20}=1.5,$$
$$\text{H must prefer to signal:}\quad 50-c_H E_H\ge20\iff 50-10E_H\ge20\iff E_H\le\frac{50-20}{10}=3.$$

$$\boxed{\;E_H\in\Bigl[\tfrac{\theta_H-\theta_L}{c_L},\ \tfrac{\theta_H-\theta_L}{c_H}\Bigr]=[1.5,\ 3]\;}$$

**M&R's check with $E_H=2$ (p. 156):** mimicking nets the low type $50-20\times2=\$10<\$20$; the
high type nets $50-10\times2=\$30>\$20$. Both constraints hold. The least-cost choice is "a
little bit more than 1.5".

> **"If $C_H\le C_L$" fails — i.e. if $c_H\ge c_L$ — "these inequalities cannot both be satisfied"
> (p. 156):** the interval is empty, because any education the high type would buy to be believed
> the low type buys too. **The signal works only because it hurts the low type more.**

**Pooling wage.** With no signal, both types earn expected productivity
$(0.3\times50)+(0.7\times20)=\$29$ (p. 155).

![Education-wage plane with M&R's numbers: the low type's indifference line w = 20 + 20e and the high type's w = 20 + 10e both start at (0, 20); they reach the 50 line at e = 1.5 and e = 3, bounding the green separating interval; the pooled wage 29 line carries a purple pooling interval from 0 to 0.45; the least-cost separating point (1.5, 50) is marked](figures/L08-spence-separating.png)
*Figure — the two indifference lines through the low type's separating point $(0,\theta_L)$ cut the $\theta_H$ line at $e=1.5$ (L indifferent to mimicking) and $e=3$ (H indifferent to signaling): the separating set. The pooled wage line carries the pooling set $[0,0.45]$ of §4. Source: M&R pp. 155–156; Gibbons Fig. 4.2.8.*

Linear costs make the indifference curves straight lines, so the picture is exact: the steeper
(orange) line is the low type's, the flatter (blue) one the high type's — single crossing is
simply "orange steeper than blue". Every $e_H$ on the green segment is a separating PBE; the dot at
1.5 is the cheapest one.

---

## 4 · C — pooling equilibria (Gibbons pp. 196–199)

Both types choose $e_p$; Bayes gives $\mu(H\mid e_p)=q$, so

$$w_p=q\,y(H,e_p)+(1-q)\,y(L,e_p).\qquad(4.2.2)$$

The harshest supporting off-path belief is "**low** for any $e\ne e_p$" (4.2.3), so
$w(e)=y(L,e)$ off the path (4.2.4), and each type compares $e_p$ with its best $e$ against
$y(L,e)$, i.e. $e^*(L)$ (4.2.5). Gibbons stresses (p. 197): *"Although this belief may seem strange,
nothing in the definition of perfect Bayesian equilibrium rules it out."*

**With M&R's numbers** ($w_p=29$, off-path wage 20 at $e=0$): type $\theta$ pools iff
$29-c_\theta e_p\ge20$:

$$\text{L:}\ e_p\le\frac{9}{20}=0.45,\qquad\text{H:}\ e_p\le\frac{9}{10}=0.9\qquad\Rightarrow\qquad \boxed{e_p\in[0,\ 0.45]}$$

— in general $e_p\le q(\theta_H-\theta_L)/\max(c_H,c_L)$. Another continuum, and pooling at
$e_p>0$ burns education for no information at all.

---

## 5 · C — who gains from signaling (MWG pp. 456–457, Fig. 13.C.8; M&R p. 156)

Compare the least-cost separating outcome with a world where signaling is impossible (everyone
paid $w_p$ at $e=0$):

| | Least-cost separating | No signaling | Verdict |
|---|---|---|---|
| Low type | $\theta_L=20$ | $29$ | **always worse off** ($w_p>\theta_L$ whenever $q>0$) |
| High type | $\theta_H-c_H\dfrac{\theta_H-\theta_L}{c_L}=50-10(1.5)=35$ | $29$ | better off **here**; in general iff $q<q^*$ |
| Firms | zero profit | zero profit | indifferent |

The high type gains iff

$$\theta_H-\frac{c_H}{c_L}(\theta_H-\theta_L)\ \ge\ q\theta_H+(1-q)\theta_L
\iff(1-q)(\theta_H-\theta_L)\ge\frac{c_H}{c_L}(\theta_H-\theta_L)
\iff \boxed{\,q\le q^*=1-\frac{c_H}{c_L}\,}=1-\tfrac{10}{20}=0.5 .$$

![Net pay against the prior p: H's least-cost separating pay is flat at 35, L's separating pay flat at 20, and the no-signal wage 20 + 30p rises from 20 to 50; it crosses 35 at p* = 0.5; the region p > 0.5 where H is worse off with signaling is shaded; M&R's point p = 0.3, wage 29 is marked](figures/L08-spence-welfare.png)
*Figure — the separating outcome is the same at every prior (it never uses $p$), while the pooled wage rises with $p$; above $p^*=1-c_H/c_L=0.5$ the high type would rather live where signaling is impossible. Source: MWG p. 456, Fig. 13.C.8; M&R pp. 155–156 numbers.*

The flat green line is the striking fact: **the separating equilibrium does not depend on the
prior at all** (MWG: "the set of separating equilibria is completely unaffected by the fraction
$\lambda$"). As high types become common, the pooled wage approaches $\theta_H$ and the education
they burn to avoid being mistaken for "the handful of bad workers" becomes pure loss.

> **Efficiency (M&R p. 156).** Education here has no productive value, so *"the expenditure on
> education in this example is a pure social waste!"* The expected waste per worker in the
> least-cost separating equilibrium is $q\,c_H\,e_s=0.3\times10\times1.5=\$4.50$ per hour.

> **Interactive companion.** [The Education Signal](companions/companion-spence-signaling.html) —
> move $\theta_L,\theta_H$, the prior and both cost rates; watch the separating interval, the
> least-cost $e^*$, the pooling interval and $p^*$; push $c_H$ up to $c_L$ and separation vanishes.

---

## 6 · U/C — hybrid equilibria (Gibbons pp. 202–205)

The high type chooses $e_h$; the low type randomizes: $e_h$ with prob. $\pi$, $e^*(L)$ with $1-\pi$.

**Belief after $e_h$** (4.2.8), by Bayes:

$$\mu(H\mid e_h)=\frac{q}{q+(1-q)\pi}\equiv r .$$

**Low type indifferent** (4.2.9): $w^*(L)-c[L,e^*(L)]=w_h-c(L,e_h)$. **Wage** (4.2.10):
$w_h=r\,y(H,e_h)+(1-r)\,y(L,e_h)$. Solve (4.2.10) for $r$, then (4.2.8) for $\pi$:

$$\pi=\frac{q(1-r)}{r(1-q)} .$$

**With M&R's numbers and $e_h=1$:** indifference gives $w_h=20+20\times1=40$; then
$40=50r+20(1-r)\Rightarrow r=\tfrac{20}{30}=\tfrac23$; and

$$\pi=\frac{0.3\times\frac13}{\frac23\times0.7}=\frac{0.1}{0.4667}=0.214 .$$

A hybrid needs $q\le r\le1$: $r\ge q$ gives $e_h\ge q(\theta_H-\theta_L)/c_L=0.45$ (the pooling bound,
$\pi\to1$), and $r\le1$ gives $e_h\le1.5$ (the least-cost separating level, $\pi\to0$). **Hybrids
connect the pooling and separating families**: "the separating equilibrium … is the limit of the
hybrid equilibria" (p. 204).

| $e_h$ | $w_h$ | $r$ | $\pi$ |
|---|---|---|---|
| 0.45 | 29 | 0.30 | 1 (pooling) |
| 1.00 | 40 | 0.667 | 0.214 |
| 1.50 | 50 | 1 | 0 (separating) |

---

## 7 · G — MWG §13.C in one paragraph (pp. 450–459)

MWG's version: $\theta_H>\theta_L>0$, $\lambda=\Pr\{\theta_H\}$, cost $c(e,\theta)$ with $c_e>0$,
$c_{ee}>0$, $c_\theta<0$, $c_{e\theta}<0$; utility $w-c(e,\theta)$; PBE with the firms' common belief
$\mu(e)$ (equivalent to sequential equilibrium here). Lemma 13.C.1: separating wages equal
productivities; Lemma 13.C.2: $e^*(\theta_L)=0$; a continuum of separating and of pooling
equilibria follows, exactly as in §2–§4 above; signaling can Pareto-dominate or be
Pareto-dominated by no signaling (Fig. 13.C.8). The refinement that selects $\tilde e$ is in
[[L08-08-intuitive-criterion]] §5. MWG Exercise 13.C.4 (continuum of types, $c=e^2/\theta$) is
beyond the two-type case. Not examinable unless the lecture brings it.

---

## Links

- Prev: [[L08-05-mba-game]] · Next: [[L08-07-limit-pricing]].
- The refinement that selects $e_H=1.5$: [[L08-08-intuitive-criterion]] §5.
- Adverse selection without a signal (the lemons logic the signal escapes):
  [[../L07/L07-00-map|Lecture 7]].
- Rules: [[../../rules/07_selecao_adversa|rules/07]] §Signaling, §Application: labour-market
  signaling.
- Code: `spence` and `hybrid`, asserted on M&R's numbers, in [[L08-11-python]] §6.
- Practice already in the project: `Listas/pratica-aula-01-02.md` item 18 (M&R Food for Thought
  5.2, p. 164, signals of intent) with its solution `Listas/pratica-aula-01-02-solutions/item18.tex`.
- Exercises (number and page only): M&R Ch. 5 Quantitative Q 5.2 (p. 164, extends this
  example); Gibbons Problem 4.7 (p. 249); MWG 13.C.1, 13.C.2, 13.C.4 (pp. 474–475);
  Muñoz-Garcia Ch. 11 Exercise 4 (p. 500).
