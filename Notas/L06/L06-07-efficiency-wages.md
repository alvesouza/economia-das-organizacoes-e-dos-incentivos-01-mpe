---
tags: [notes, lecture-06, repeated-games, efficiency-wages, relational-contracts, shapiro-stiglitz]
date: 2026-10-16
status: estimated
source: "Gibbons (1992) §2.3.D 'Efficiency Wages', pp. 107–112 (eqs. (2.3.5)–(2.3.7)); Milgrom & Roberts (1992) Ch. 8, 'Efficiency Wages for Employment Incentives', pp. 250–255 (eqs. (8.1)–(8.6), the USD 50,000 / 40,000 example) and the MacRents box, pp. 260–261"
---

# Gibbons 2.3.D, M&R pp. 250–255 · Efficiency wages: a rent the worker will not risk

> **Claim.** When effort cannot be contracted on, a firm can still buy it with a **promise**:
> pay more than the worker's outside option and fire him if output is ever low. The wage must
> leave a **rent** large enough that the expected loss of the job outweighs the one-period gain
> from shirking — $w^*=w_0+e+\frac{(1-\delta)e}{\delta(1-p)}$. The premium explodes as
> detection fails ($p\to1$) or patience vanishes ($\delta\to0$), and the relationship survives
> only if the job produces enough to pay it. This is the cartel inequality again, with the
> worker as the party tempted to cheat.
> Prev: [[L06-06-institutions-reputation]] · Next: [[L06-08-relational-contracts]] · Map: [[L06-00-map]]

> **Scope.** Covered as a **repeated-game application** only. Incentive contracts with hidden
> effort — agency theory, optimal pay-for-performance — are moral hazard, **out of scope**
> (`CLAUDE.md`); M&R's comparison with incentive pay (§7) is named, not developed.

---

## 1 · U — why pay more than the market

M&R open with an organization that must rely on an employee's honesty — a police officer
offered bribes, a tanker captain who must stay sober, an analyst who must investigate with
diligence — and whose only sanction is **dismissal** (fines are impractical when wealth is
limited, p. 250). Then the threat of firing is the incentive, and it bites only if the job is
worth more than the next one: the worker must earn a **rent**. Marshall's epigraph says it:
"Highly paid labour is generally efficient and therefore not dear labour" (p. 248). Lord Clive,
reforming the East India Company's servants around 1765, saw it too: "it was absurd to give men
power and to require them to live in penury" (p. 252). The Aula 1 notes meet the same logic in
Ford's five-dollar day ([`Aula/aula-01-notes.md`](../../Aula/aula-01-notes.md)).

---

## 2 · C — Gibbons's stage game (pp. 107–108)

1. The firm offers a wage $w$.
2. The worker accepts or rejects; rejecting means self-employment at $w_0$.
3. If he accepts, he supplies effort (disutility $e$) or shirks (no disutility). **Effort is
   not observed; output is.** With effort output is $y>0$ for sure; shirking gives $y$ with
   probability $p$ and $0$ with probability $1-p$. Low output is therefore proof of shirking.

Payoffs when employed at $w$: firm $y-w$ (or $-w$ if output is 0), worker $w-e$ (or $w$ if he
shirks). **Assumptions** (p. 108):

$$y-e>w_0>py$$

— employment with effort is efficient, and self-employment beats employment with shirking.

**One shot.** The wage is paid in advance, so the worker shirks; anticipating it, the firm
offers $w\le w_0$ and the worker stays self-employed. The efficient relationship never forms.

*Why not pay on output?* Courts may be unable to verify output — its quality, unexpected
production difficulties — so output-contingent contracts are infeasible or imperfect, "but
there will remain a role for the repeated-game incentives studied here" (p. 108).

---

## 3 · C — the worker's condition (Gibbons pp. 108–110)

**Strategies.** Call the history *high-wage, high-output* if every past offer was $w^*$, every
offer was accepted and every output was high.

- **Firm:** offer $w^*$ in period 1 and after every high-wage, high-output history; offer
  $w=0$ otherwise.
- **Worker:** accept iff $w\ge w_0$; supply effort iff the history, **including the current
  offer**, is high-wage, high-output; shirk otherwise. (The stage game is sequential, so a firm
  deviation is detected *within* the stage and answered at once, p. 109.)

**Effort forever.** Output is high for sure, so the same choice recurs next period:

$$V_e=(w^*-e)+\delta V_e\ \Rightarrow\ V_e=\frac{w^*-e}{1-\delta}.$$

**Shirking.** This period he gets $w^*$ (no effort cost). With probability $p$ output is high
and the same situation recurs; with probability $1-p$ he is fired and self-employed forever:

$$V_s=w^*+\delta\Bigl[p\,V_s+(1-p)\frac{w_0}{1-\delta}\Bigr]
\ \Rightarrow\ V_s(1-\delta p)=w^*+\frac{\delta(1-p)w_0}{1-\delta}
\ \Rightarrow\ V_s=\frac{(1-\delta)w^*+\delta(1-p)w_0}{(1-\delta p)(1-\delta)} .$$

**Effort iff $V_e\ge V_s$.** Multiply both by $(1-\delta)(1-\delta p)>0$:

$$(w^*-e)(1-\delta p)\ \ge\ (1-\delta)w^*+\delta(1-p)w_0 .$$

Collect $w^*$: $w^*\bigl[(1-\delta p)-(1-\delta)\bigr]=w^*\,\delta(1-p)$, so

$$w^*\,\delta(1-p)\ \ge\ e(1-\delta p)+\delta(1-p)w_0
\iff w^*\ \ge\ w_0+\frac{1-\delta p}{\delta(1-p)}\,e .$$

Split $1-\delta p=\delta(1-p)+(1-\delta)$:

$$\boxed{\;w^*\ \ge\ w_0+e+\frac{1-\delta}{\delta(1-p)}\,e\;}\qquad(2.3.5)$$

The firm must cover the **outside option** $w_0$, the **effort cost** $e$, and a **wage
premium** $\frac{(1-\delta)e}{\delta(1-p)}$ — the rent.

| Case | Premium | Reading |
|---|---|---|
| $p\to1$ (shirking almost never caught) | $\to\infty$ | "the wage premium must be extremely high" (p. 110) |
| $p=0$ (perfect monitoring) | $\frac{1-\delta}{\delta}e$ | (2.3.6): $w^*\ge w_0+\bigl(1+\frac{1-\delta}{\delta}\bigr)e=w_0+e/\delta$ |
| $\delta\to1$ | $\to0$ | a patient worker needs almost no rent |
| $\delta\to0$ | $\to\infty$ | no future, no discipline |

**The template, recovered.** Rearranging (2.3.5):

$$\underbrace{e}_{\text{gain today}}\ \le\ \underbrace{(1-p)}_{\text{detection}}\cdot\frac{\delta}{1-\delta}\cdot\underbrace{(w^*-e-w_0)}_{\text{rent per period}} .$$

Exactly [[L06-01-recap-grim-trigger]] §3's second form, with the loss weighted by the
probability that cheating is caught.

---

## 4 · C — the firm's condition and the patience required (p. 110)

Given the worker's strategy, the firm compares paying $w^*$ forever ($y-w^*$ a period) with
offering 0 and getting 0:

$$y-w^*\ \ge\ 0\qquad(2.3.7)$$

Together with (2.3.5) at its lowest wage:

$$y-e\ \ge\ w_0+\frac{1-\delta}{\delta(1-p)}\,e .$$

Solve for $\delta$: write $S=y-e-w_0>0$ for the surplus of the relationship. Then
$S\,\delta(1-p)\ge(1-\delta)e\iff\delta\bigl[(1-p)S+e\bigr]\ge e$:

$$\boxed{\;\delta\ \ge\ \delta_{\min}=\frac{e}{e+(1-p)(y-e-w_0)}\;}$$

"the familiar restriction that $\delta$ must be sufficiently large" (p. 111). Efficiency
($S>0$) is necessary, not sufficient.

**Off the path** (p. 111): after any other history the worker never works, so the firm should
induce self-employment ($w=0$ forever), and the worker should shirk and accept only $w\ge w_0$.
Note the subgames now begin **within** stages too — after the worker sees the offer.

---

## 5 · C — renegotiation and outside options (Gibbons pp. 111–112)

- **Permanent self-employment is a strange punishment.** Both players prefer to restart the
  high-wage relationship — the renegotiation problem of [[L06-04-punishments-price-wars]] §2.
  A firm with **many** workers may refuse to renegotiate with one, to protect the equilibrium
  with the others; firms may refuse to hire workers fired elsewhere — a possible account of low
  mid-career mobility among large Japanese firms.
- **Outside jobs set $w_0$.** If fired workers find jobs they prefer to self-employment, the
  **net wage in those jobs** plays the role of $w_0$. If a fired worker loses nothing, there is
  no punishment and no effort in any SPE.
- **Sovereign debt** (Bulow and Rogoff 1989, p. 112): if a defaulting country can replicate
  long-term loans with cash-in-advance trades, creditors have no punishment and lending
  collapses. Same logic: no loss, no discipline.

---

## 6 · C — Milgrom & Roberts's Shapiro–Stiglitz model (pp. 250–252)

**Notation** (M&R's, different from Gibbons's): $w$ the current wage, $\bar w$ the wage after
being fired (net of search costs), $g$ the gain from cheating, **$p$ the probability that
cheating is detected**, $N$ a multiplier for the long-term value of the relationship
($N=1$ for a one-period job, larger the longer and more certain re-hiring is). The employee
cheats iff

$$g\ >\ p\,(w-\bar w)\,N\qquad(8.1)$$

— gain from cheating against the probability of detection times the income lost by being
fired. $w-\bar w$ is the **rent**.

### 6.1 · Worked — M&R's numbers (p. 251)

$w=$ USD 50,000, $\bar w=$ USD 40,000, $g=$ USD 1,000, $p=0.05$, $N=1$:

$$p(w-\bar w)N=0.05\times10{,}000\times1=500\ <\ 1{,}000=g\quad\Rightarrow\quad\text{cheating pays.}$$

**The efficiency wage** — the smallest wage that deters (p. 252):

$$\boxed{\;w=\bar w+\frac{g}{Np}\;}=40{,}000+\frac{1{,}000}{0.05N}=40{,}000+\frac{20{,}000}{N}:\qquad N=1\to60{,}000,\quad N=2\to50{,}000 .$$

The USD 50,000 job deters cheating only if the relationship is worth twice a single period.

**Lord Clive and the Maghribi traders** (p. 252) in the formula: the Company's servants had
**large $g$** (power to extort) and **small $p$** (remote posts), so only a large premium
worked; the Maghribi coalition **lowered $\bar w$** and **raised $N$** (an ostracized agent
lost all merchants' business) and **raised $p$** (dense correspondence) —
[[L06-06-institutions-reputation]] §3.

### 6.2 · The two models are one inequality

| Gibbons (2.3.5) rearranged | M&R (8.1) | Note |
|---|---|---|
| gain from shirking $e$ | $g$ | |
| detection probability $1-p$ | $p$ | **opposite uses of the letter $p$** |
| rent $w^*-e-w_0$ | $w-\bar w$ | so $\bar w\leftrightarrow w_0+e$: M&R's outside wage is already net of the effort an honest worker supplies in either job |
| $\delta/(1-\delta)$ | $N$ | Gibbons counts the future only; M&R's $N=1$ for a one-period job counts the current period's rent too (footnote 4) — same algebra, different bookkeeping |

**Calibrated into Gibbons** — $e=1$, $w_0=39$ (so $w_0+e=40=\bar w$), $p=0.95$ (detection
0.05), in USD thousands:

$$w^*=40+\frac{1-\delta}{\delta}\times\frac{1}{0.05}=40+20\,\frac{1-\delta}{\delta}:\qquad
\delta=\tfrac12\ (N=1)\to60,\qquad\delta=\tfrac23\ (N=2)\to50 .$$

![Minimum no-shirking wage w* against delta for p = 0.95, 0.5 and 0: each curve falls from very high values to the floor w0 + e = 40 as delta approaches 1; on the p = 0.95 curve the points delta 1/2 (w* = 60) and delta 2/3 (w* = 50) are marked, with M&R's current wage 50 as a dashed line](figures/L06-efficiency-wage.png)
*Figure — Gibbons (2.3.5) at M&R's calibration: $w_0+e=40$, $e=1$; detection $1-p$ of 5%, 50%
and 100%. Source: Gibbons p. 110; M&R pp. 251–252.*

The vertical gap between a curve and the dotted floor is the premium. At 5% detection the
premium is twenty times what perfect monitoring needs at the same $\delta$; the M&R wage of 50
crosses the blue curve exactly at $\delta=2/3$, $N=2$.

> **Interactive companion.** [The No-Shirking Wage](companions/companion-efficiency-wage.html) —
> move $\delta$, the detection rate and the effort cost and watch $w^*$, the rent, and the two
> value lines $V_e$, $V_s$ cross; raise $y$ to see when the firm will pay. Defaults reproduce
> M&R's USD 60,000.

---

## 7 · U — monitoring, the alternative, and the evidence (M&R pp. 252–255, 260–261)

**Monitoring against wages** (pp. 254–255). If detection costs $M(p)$ per period, the firm
solves the *minimum cost implementation problem*

$$\min_{p,w}\ M(p)+w\quad\text{s.t.}\quad p(w-\bar w)N\ge g\qquad(8.2)$$

The wage is set at its floor, $w=\bar w+g/(Np)$ (8.3); substituting, minimize
$M(p)+\bar w+g/(Np)$ (8.4). First-order condition $M'(p^*)=g/(p^{*2}N)$ (8.5); second-order
$M''(p^*)+2g/(p^{*3}N)\ge0$ (8.6). **How does $p^*$ move with $N$?** Differentiate (8.5):

$$M''(p^*)\,dp^*=-\frac{2g}{p^{*3}N}\,dp^*-\frac{g}{p^{*2}N^2}\,dN
\ \Rightarrow\ \frac{dp^*}{dN}=-\frac{g/(p^{*2}N^2)}{M''(p^*)+2g/(p^{*3}N)}<0$$

by (8.6) holding strictly. "As the potential length of a relationship increases, there is more
trust and less direct monitoring" (p. 255).

**Why not explicit incentive pay?** (pp. 252–253). Wealth limits (the worker cannot bear low
pay or fines), and **subjective evaluations**: a firm that pays on its own assessment is tempted
to underrate; a flat efficiency wage removes that temptation. (The incentive-contract side is
moral hazard — out of scope.)

**Unemployment as the stick** (p. 253): not every firm can pay above every other; Shapiro and
Stiglitz close the model with unemployment, so a fired worker loses income while searching —
at the social cost of idle labour. Okuno-Fujiwara's alternative, lifetime employment with no
mid-career hiring, is "very fragile" (p. 254).

**MacRents** (pp. 260–261, Krueger 1990). Company-owned fast-food outlets, managed by salaried
managers who monitor less than franchisee-owners, should pay more. They do: supervisors earn
**8.9%** more and full-time non-managerial workers **1.7%** more than in franchised outlets;
company outlets are only two thirds as likely to start workers at the minimum wage, and give
more generous benefits (free meals).

---

## Links

- Previous: [[L06-06-institutions-reputation]]. Next: [[L06-08-relational-contracts]].
- Template: [[L06-01-recap-grim-trigger]] §3. Rent and incomplete contracts:
  [[../../rules/06_racionalidade_limitada_contratos|rules/06]].
- Code: [[L06-11-python]] §7. Formulas: [[L06-09-formulas]] §1.4, §2.5.
- Exercises: M&R Quantitative Exercises 1 (p. 285) and 3 (p. 286).
