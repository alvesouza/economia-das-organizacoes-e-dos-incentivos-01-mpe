---
tags: [notes, lecture-05, formulas, reference, repeated-games]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.1–10.3, 10.6, pp. 190–214; Gibbons (1992) §2.3.A–B, pp. 82–102; Cabral (2017) §7.3, pp. 172–174; MWG §12.D p. 401, App. A to Ch. 12, pp. 417–422; Map/study-guide.md, Lecture 5 block"
---

# Lecture 5 · Formulas — every definition, every result, every number

> Prev: [[L05-06-folk-theorem]] · Next: [[L05-08-pitfalls]] · Map: [[L05-00-map]]

---

## 0 · The exam specification, mapped

The lecture has no slides yet; the specification is the study guide's Lecture 5 block and the
chapter's own summary (§10.7, pp. 214–215). **Estimated** — reconcile when `Aula/Lecture05.pdf`
arrives.

| # | Item (study guide / Tadelis §10.7) | Note |
|---|---|---|
| 1 | Finitely repeated games; a unique stage NE gives a unique SPE "regardless of the discount factor's value" (Prop. 10.1) | [[L05-01-finite-repetition-unraveling]] |
| 2 | Multiple stage NE: carrot and stick support non-Nash play in early stages | [[L05-02-two-stage-carrot-stick]] |
| 3 | Infinite horizon: discounting, present value, average payoff, $\delta$ as continuation probability | [[L05-03-discounting-histories-strategies]] §1–3 |
| 4 | Histories and strategies; Prop. 10.2 | [[L05-03-discounting-histories-strategies]] §4–5 |
| 5 | Grim trigger, the one-stage deviation principle (Prop. 10.3), (10.3) | [[L05-04-grim-trigger-spe]] |
| 6 | The threshold for any payoffs, (10.5), and what moves it | [[L05-05-critical-discount-factor]] |
| 7 | "The folk theorem teaches us that as the discount factor approaches 1 … almost anything can happen" (§10.7) | [[L05-06-folk-theorem]] |
| 8 | Application pointer: Cabral §7.3, relational contracts | [[L05-04-grim-trigger-spe]] §4.4; the rest in [[../L06/L06-00-map|Lecture 6]] |

---

## 1 · Every definition and proposition

| Result | Statement | Derived in |
|---|---|---|
| **Def. 10.1** (p. 190) | $G(T,\delta)$: stage game $G$ played $T$ consecutive times, common discount factor $\delta$ | [[L05-01-finite-repetition-unraveling]] §1 |
| **Prop. 10.1** (p. 192) | unique stage NE $\Rightarrow$ unique SPE of $G(T,\delta)$: the stage NE every period | §2 |
| Prop. 9.3 (p. 181) | the multistage version | §2 |
| Two-stage example (p. 191, fn. 2) | $(M,m)$ then $(R,r)$, else $(F,f)$: SPE iff $4+3\delta\geq5+\delta\iff\delta\geq\tfrac12$ | [[L05-02-two-stage-carrot-stick]] §1 |
| *Notes' extension* | $T$ rounds, reward phase $k$: last cooperative round needs $b-a\leq(r-p)\dfrac{\delta(1-\delta^{k})}{1-\delta}$; some $k$ works iff $\delta>\dfrac{b-a}{b-a+r-p}$ | §4 |
| **Def. 10.2** (p. 193) | $v_i=\sum_{t=1}^{\infty}\delta^{t-1}v_i^t$, $0<\delta<1$ | [[L05-03-discounting-histories-strategies]] §1 |
| fn. 3 (p. 193) | bounded payoffs: $\sum\delta^{t-1}b=b/(1-\delta)$ | §1.1 |
| fn. 4 (p. 194) | continuation probability $p$ and discount $\delta$: effective factor $p\delta$; Gibbons $\delta=(1-p)/(1+r)$ (p. 90) | §2 |
| **Def. 10.3** (p. 194) | $\bar v_i=(1-\delta)\sum_{t=1}^{\infty}\delta^{t-1}v_i^t$ | §3 |
| (10.1)–(10.2) (pp. 194–195) | $s(v,\delta,T)=\dfrac{v-\delta^{T}v}{1-\delta}$; $s(v,\delta)=\dfrac{v}{1-\delta}$; average of constant $v$ is $v$ | §3 |
| **Def. 10.4** (p. 196) | pure strategy $s_i:H\to S_i$; behavioural $\sigma_i:H\to\Delta S_i$ | §4 |
| **Prop. 10.2** (p. 196) | history-independent stage NE is an SPE of $G(\delta)$ for any $\delta<1$ | §5 |
| **Def. 10.5** (p. 196) | SPE: Nash equilibrium after every history | [[L05-04-grim-trigger-spe]] §1 |
| Grim trigger (p. 198) | $M$ iff the history is all $(M,m)$, else $F$ forever | §2 |
| **Prop. 10.3** (p. 198) | SPE iff no player gains from a single deviation at a single history | §3 |
| Thm 9.1 (p. 185) | a one-stage unimprovable strategy is optimal | §3 |
| **(10.3)** (p. 200) | $4+\dfrac{4\delta}{1-\delta}\geq5+\dfrac{\delta}{1-\delta}\iff\delta\geq\tfrac14$ | §4.2 |
| Gibbons (2.3.1) (p. 92) | $\dfrac{4}{1-\delta}\geq5+\dfrac{\delta}{1-\delta}\iff\delta\geq\tfrac14$ | §4.3 |
| **(10.5)** (p. 202) | $\delta\geq\dfrac{v_i^d-v_i^c}{v_i^d-v_i^*}$ | [[L05-05-critical-discount-factor]] §1 |
| PD labels | $\delta^*=\dfrac{T-R}{T-P}=\dfrac{g}{g+\ell}$, $g=T-R$, $\ell=R-P$ | §2 |
| Signs | $\partial\delta^*/\partial T>0$, $\partial\delta^*/\partial R<0$, $\partial\delta^*/\partial P>0$, $\partial\delta^*/\partial S=0$ | §3 |
| Several players (Gibbons p. 101) | $\delta\geq\max_i\dfrac{d_i-x_i}{d_i-e_i}<1$ | §1 |
| Interest-rate reading | $\delta=\dfrac1{1+r}\geq\delta^*\iff r\leq\ell/g$ | §4 |
| **Def. 10.6** (p. 209) | convex combination $\hat v=\alpha v+(1-\alpha)v'$, $\alpha\in[0,1]$ | [[L05-06-folk-theorem]] §1 |
| **Def. 10.7** (p. 210) | convex hull $\mathrm{CoHull}(V)$ | §1 |
| **Thm 10.1** (p. 211) | feasible $v$ with $v_i>v_i^*\ \forall i$, $\delta$ near 1 $\Rightarrow$ SPE with average arbitrarily close to $v$ | §2 |
| Alternating path (pp. 212–214) | $\bar v_1=\dfrac{5-\delta}{1+\delta}$, $\bar v_2=\dfrac{-1+5\delta}{1+\delta}$; SPE iff $\delta\geq\tfrac12$ | §3 |
| General alternating bad period | $\dfrac{S+\delta T}{1+\delta}\geq P\iff\delta\geq\dfrac{P-S}{T-P}$ | §3 |
| G: MWG Def. 12.AA.1, Lemma 12.AA.1 (p. 418) | Nash reversion; its no-deviation test | [[L05-05-critical-discount-factor]] §5 |
| G: MWG Prop. 12.AA.2 (p. 420) | sustainable at $\delta$ $\Rightarrow$ sustainable at every $\delta'\geq\delta$ | §5 |
| G: MWG Props. 12.AA.3 (p. 420), 12.AA.5 (p. 422) | Nash-reversion folk theorem; minimax (individually rational) folk theorem | [[L05-06-folk-theorem]] §4 |
| G: Fudenberg–Maskin (Gibbons p. 99) | two players: reservation payoffs $r_i$ replace Nash payoffs $e_i$ | §4 |

---

## 2 · Every number and worked case

### 2.1 · The games

| Game | Payoffs | Source |
|---|---|---|
| Tadelis's PD | $(M,m)=(4,4)$, $(M,f)=(-1,5)$, $(F,m)=(5,-1)$, $(F,f)=(1,1)$; $T,R,P,S=5,4,1,-1$ | p. 197 (and p. 210) |
| Tadelis's two-stage game | PD block plus $R$/$r$: $(R,r)=(3,3)$, all other $R$/$r$ cells $(0,0)$ | p. 191 |
| Gibbons's PD | $(L,L)=(1,1)$, $(L_1,R_2)=(5,0)$, $(R_1,L_2)=(0,5)$, $(R,R)=(4,4)$ | pp. 82, 90 |
| Gibbons's 3×3 | adds $(R_1,R_2)=(3,3)$ to his PD (labels $L,M,R$) | p. 85 |
| Cabral's PD | cooperate $5$ each, deviate $6$, Nash $4$ | pp. 172–173 |

### 2.2 · Thresholds

| Case | Threshold |
|---|---|
| Two-stage, one reward round (p. 191) | $\delta\geq1/2$ |
| $T$-round extension, floor | $\delta>1/3$; at $T=10$: $\delta=0.34\to6$ rounds, $0.4\to8$, $0.5\to9$ |
| Grim trigger, Tadelis and Gibbons | $\delta^*=1/4$ |
| Grim trigger, Cabral | $\alpha\geq1/2$ |
| Alternating path, Tadelis | $\delta\geq1/2$ (good period: every $\delta$) |

### 2.3 · Values

| Quantity | Value | Source |
|---|---|---|
| $0.97^{100}$, $0.97^{500}$ | $0.0475$; $2.4315\times10^{-7}$ | p. 194 |
| Information sets at stage 4 of the repeated PD | $4^3=64$ | fn. 5, p. 195 |
| PV of $4$ forever at $\delta=0.9$ | $40$; average $4$ | Def. 10.3 |
| Grim trigger at $\delta=0.2,\ 0.25,\ 0.5$ | $(5,\ 5.25)$, $(5.333,\ 5.333)$, $(8,\ 6)$ (cooperate, deviate) | (10.3) |
| Convex combination | $0.6(4,4)+0.4(5,-1)=(4.4,2)$ | p. 209 |
| Folk region corners (Tadelis PD) | $(1,1),(1,4.6),(4,4),(4.6,1)$ | Fig. 10.4 |
| Alternating path at $\delta=0.9$ | $(2.158,\ 1.842)$ | p. 214 |
| Remark adjustments | $-0.151,\ +0.076$ ($t=26$); $-0.013,\ +0.066$ ($t=36$) → $(1.994,\ 1.984)$ | p. 214 |
| Two-stage folded game at $\delta=1/2$ | $(M,m)=(5.5,5.5)$, $(F,f)=(1.5,1.5)$, $(R,r)=(3.5,3.5)$ | p. 191 |
| Applications for Lecture 6 | Cournot cutoffs $0.595$ and $0.392$ (§10.4, p. 202) | [[../L06/L06-00-map|Lecture 6]] |
