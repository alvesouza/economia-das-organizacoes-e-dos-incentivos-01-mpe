---
tags: [notes, lecture-04, formulas, reference]
date: 2026-10-16
status: estimated
source: "Map/study-guide.md, Lecture 4 block; Tadelis (2013) Ch. 9 (pp. 175–189) and Ch. 11 (pp. 220–237); Gibbons (1992) §2.1.D, §2.2 (pp. 68–82); MWG 9.AA (pp. 296–298); M&R (1992) pp. 140–142"
---

# Lecture 4 · Formulas — every definition, result and number, the study guide mapped

> Prev: [[L04-09-bargaining-private-information]] · Next: [[L04-11-pitfalls]] · Map: [[L04-00-map]]

---

## 0 · The exam specification, mapped (estimated)

No slides yet, so the specification is the study guide's Lecture 4 block (`Map/study-guide.md`),
item by item. Reconcile with the slides' learning goals when the Lecture 4 slides arrive.

| # | Study-guide item | What to be able to do | Note |
|---|---|---|---|
| 1 | Tadelis Ch. 9 §9.1–9.3 (pp. 175–180) | define a multistage game; write $v_i=\sum_t\delta^{t-1}v_{it}$; write strategies as history-contingent plans and count them | [[L04-01-multistage-games]] |
| 2 | Tadelis §9.4 (pp. 180–184) | state Props. 9.1–9.3; build a carrot-and-stick SPE; derive $\delta^*$ | [[L04-02-carrot-and-stick]] |
| 3 | Tadelis §9.5 (pp. 184–186) | state and apply the one-stage deviation principle | [[L04-03-one-stage-deviation]] |
| 4 | Gibbons §2.2 (pp. 71–82) | solve two-stage games by "stage-2 NE first": bank runs, tariffs, tournaments | [[L04-01-multistage-games]] §5; [[L04-04-two-stage-applications]] |
| 5 | Tadelis §11.1 (pp. 222–224) | ultimatum game: NE vs SPE (Props. 11.1–11.2) | [[L04-05-ultimatum-game]] |
| 6 | Tadelis §11.2 (pp. 224–227); Gibbons §2.1.D (pp. 68–70); MWG Ex. 9.AA.1 | finite alternating offers by backward induction; (11.1); Prop. 11.3; limits and their order | [[L04-06-finite-alternating-offers]] |
| 7 | Tadelis §11.3 (pp. 228–229); Gibbons pp. 70–71; MWG Ex. 9.AA.2 | Rubinstein by stationarity; asymmetric patience; $\Delta\to0$ and Nash | [[L04-07-rubinstein-infinite-horizon]] |
| 8 | Tadelis §11.4 (pp. 229–235) | closed and open rule legislative bargaining | [[L04-08-legislative-bargaining]] |
| 9 | M&R bargaining over a sale (p. 140) | why private values can make efficient trade infeasible | [[L04-09-bargaining-private-information]] |
| 10 | `Aula/aula-02-notes.md` §5; Listas Block 3; `rules/02_barganha.md` | link Rubinstein to Nash bargaining and to Coase | [[L04-07-rubinstein-infinite-horizon]] §5 |

---

## 1 · Every definition and proposition

### 1.1 · Multistage games (Tadelis Ch. 9)

| Item | Statement | Note |
|---|---|---|
| Multistage game (p. 176) | finite sequence of simultaneous stage-games, same players, each outcome observed before the next stage | 01 §2 |
| Payoffs (p. 177) | $v_i=\sum_{t=1}^{T}\delta^{t-1}v_{it}$ | 01 §3 |
| Pure strategy (p. 179) | $s_i=\{s_{i1},s_{i2}(h_1),\dots,s_{iT}(h_{T-1})\}$, one action per history | 01 §4 |
| **Prop. 9.1** (p. 180) | any sequence of stage NE, played unconditionally, is an SPE path | 02 §1 |
| **Prop. 9.2** (p. 181) | in any NE, play in the last stage is a stage NE | 02 §2 |
| **Prop. 9.3** (p. 181) | every stage has a unique NE $\Rightarrow$ unique SPE | 02 §2 |
| Requirements (p. 183) | (1) two distinct stage-2 equilibria, a carrot and a stick; (2) $\delta$ large enough | 02 §4 |
| Threshold | $\delta^*=g/(c-s)$: one-shot gain over carrot minus stick | 02 §4 |
| **Def. 9.1** (p. 185) | one-stage unimprovable: no single information set where changing the action alone pays | 03 §2 |
| **Thm. 9.1** (p. 185) | one-stage unimprovable $\Rightarrow$ optimal (finite trees) | 03 §2 |

### 1.2 · Two-stage applications (Gibbons §2.2)

| Item | Statement | Note |
|---|---|---|
| Subgame-perfect outcome (p. 73) | $(a_1^*,a_2^*,a_3^*(a_1^*,a_2^*),a_4^*(a_1^*,a_2^*))$ | 01 §5 |
| Bank runs (p. 75) | two SPE outcomes: run $(r,r)$ and no run $(R,R)$ | 04 §1 |
| Stage-2 Cournot with tariffs (2.2.3) | $h_i^*=\frac{a-c+t_i}{3}$, $e_i^*=\frac{a-c-2t_j}{3}$ | 04 §2.1 |
| Dominant tariff (p. 78) | $t_i^*=\frac{a-c}{3}$; $h^*=\frac{4(a-c)}9$, $e^*=\frac{a-c}9$; joint optimum $t=0$ | 04 §2.2 |
| Tournament FOC (2.2.6) | $(w_H-w_L)\int f^2=g'(e^*)$; normal noise $\int f^2=\frac1{2\sigma\sqrt\pi}$ | 04 §3 |
| Optimal prize (p. 82) | $g'(e^*)=1$ and $(w_H-w_L)\int f^2=1$; participation binds (2.2.8) | 04 §3 |

### 1.3 · Bargaining (Tadelis Ch. 11, Gibbons §2.1.D, MWG 9.AA)

| Item | Statement | Note |
|---|---|---|
| **Prop. 11.1** (p. 223) | $T=1$: every $(x^*,1-x^*)$ is a NE | 05 §2 |
| **Prop. 11.2** (p. 223) | $T=1$: unique SPE, offer $x=1$, accept any $x\le1$ | 05 §3 |
| Two rounds (p. 225) | $(v_1,v_2)=(1-\delta,\delta)$ | 06 §2 |
| **(11.1)** (p. 226) | $T$ odd: $v_1=\frac{1+\delta^T}{1+\delta}$, $v_2=\frac{\delta-\delta^T}{1+\delta}$; all $T$: $x_1=\frac{1-(-\delta)^T}{1+\delta}$ | 06 §3 |
| **Prop. 11.3** (p. 226) | every SPE agrees in round 1 | 06 §4 |
| **(11.2)–(11.3)** (p. 227) | $\lim_T v_1=\frac1{1+\delta}$; then $\lim_{\delta\to1}=\frac12$; reverse order keeps $v_1=1$ | 06 §5 |
| Gibbons three periods (p. 70) | $s_1^*=1-\delta(1-\delta s)$ | 06 §6 |
| Asymmetric, 3 rounds | $s_1=1-\delta_2(1-\delta_1)$ | 06 §6 |
| **(11.4)–(11.5)** (p. 229) | $\underline v=1-\delta\bar v$, $\bar v=1-\delta\underline v\Rightarrow v=\frac1{1+\delta}$ | 07 §2 |
| Fixed point (Gibbons p. 71) | $f(s)=1-\delta+\delta^2s$, $s^*=\frac1{1+\delta}$ | 07 §2.1 |
| Asymmetric, infinite | $x^*=\frac{1-\delta_2}{1-\delta_1\delta_2}$; $\partial x^*/\partial\delta_1>0$, $\partial x^*/\partial\delta_2<0$ | 07 §4 |
| Frequent offers | $\delta_i=e^{-r_i\Delta}$, $\Delta\to0$: $x^*\to\frac{r_2}{r_1+r_2}$ = Nash weight | 07 §5 |
| MWG 9.AA.2 (pp. 297–298) | squeeze $\frac v{1+\delta}\le\underline v_1\le\bar v_1\le\frac v{1+\delta}$ | 07 §6 |
| **(11.6)–(11.8)** (pp. 230–231) | closed rule: $v=\frac1N$, $k=1-\delta\frac{N-1}{2N}$ | 08 §2 |
| **(11.9)** (p. 233) | open rule, guaranteed: $k=\frac1{1+2\delta}$ | 08 §3 |
| **(11.10)–(11.13)** (p. 234) | open rule, risky: $k=\frac{4-\delta^2}{4+2\delta-\delta^2}$, $v(k)=\frac2{4+2\delta-\delta^2}$ | 08 §4 |
| Risky vs guaranteed (p. 235) | risky better iff $\delta>\sqrt3-1$ | 08 §4 |

### 1.4 · Private information (M&R)

| Item | Statement | Note |
|---|---|---|
| Incentive constraints (pp. 141–142) | seller needs $p\ge1.75$, buyer needs $p\le1.25$: no truthful efficient rule | 09 §2 |

---

## 2 · Every number and worked case

| Case | Numbers | Source | Note |
|---|---|---|---|
| Prisoner-Revenge strategies | $2^5=32$ each, $1024$ profiles | p. 179 | 01 §4 |
| Revenge mixed NE | $q=\tfrac12$, value $-2$ | p. 177 | 01 §2.1 |
| Discounted payoff example | $(F,m)$ then $(L,g)$: $v_1=5-4\delta$, $v_2=-1-\delta$ | p. 177 | 01 §3 |
| Support $(M,m)$ | $4\ge5-3\delta\iff\delta\ge\frac13$ | p. 183 | 02 §3 |
| Support $(F,m)$ | $-1\ge1-3\delta\iff\delta\ge\frac23$ | p. 184 | 02 §5 |
| Reduced stage 1 at $\delta=0.5$ | $(M,m)=(4,4)$, $(F,m)=(3.5,-2.5)$, $(F,f)=(-0.5,-0.5)$ | from p. 182 | 02 §3.1 |
| Bank run (illustrative) | $D=100,r=75,R=150$: NE $(75,75)$ and $(150,150)$ | pp. 73–75 | 04 §1 |
| Tariff game | $72,81,56,65$ in units $(a-c)^2/162$ | p. 78 | 04 §2.2 |
| Tournament (illustrative) | $\sigma=1$: spread $2\sqrt\pi\approx3.54$ | pp. 81–82 | 04 §3 |
| Ultimatum experiments | offers 25–50%, rejections below 20–25% | pp. 223–224 | 05 §4 |
| Finite shares, $\delta=0.6$ | $T=1..6$: $1,\ 0.4,\ 0.76,\ 0.544,\ 0.674,\ 0.596$; limit $0.625$ | (11.1) | 06 §3.1 |
| Asymmetric $\delta_1=0.9,\delta_2=0.7$ | 3 rounds $0.93$; infinite $0.3/0.37=0.811$ | `check_part2.py` | 06 §6, 07 §4 |
| Rubinstein, equal $\delta$ | $0.6\to0.625$; $0.9\to0.526$ | (11.4)–(11.5) | 07 §2 |
| Closed rule, $\delta=0.9$ | $N=3$: $0.70$; $N=5$: $0.64$; $N\to\infty$: $0.55$ | (11.8) | 08 §2 |
| Open rule, $\delta=0.9$ | guaranteed $0.357$; risky $k=0.639$, $v(k)=0.401$ | (11.9), (11.13) | 08 §4 |
| Threshold | $\sqrt3-1\approx0.732$ | p. 235 | 08 §4 |
| M&R sale | efficient trade 96%; $p\ge1.75$ vs $p\le1.25$ | pp. 140–142 | 09 §2 |
