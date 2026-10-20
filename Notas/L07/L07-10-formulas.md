---
tags: [notes, lecture-07, formulas, reference]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 12 (pp. 241–269) and Ch. 13 (pp. 270–287); Gibbons (1992) Ch. 3 (pp. 143–172); M&R (1992) pp. 149–153; Cabral (2017) pp. 140–142, 174–176; MWG §8.E (pp. 253–257), §13.B (pp. 437–447)"
---

# Lecture 7 · Formulas — every definition, result and number, the study-guide content mapped

> Prev: [[L07-09-common-values-curses]] · Next: [[L07-11-pitfalls]] · Map: [[L07-00-map]]
>
> **Estimated unit**: §0 maps the study guide's block for Lecture 7, not the slides' learning goals
> (there are no slides yet).

---

## 0 · The exam specification, mapped

The Lecture 7 block of `Map/study-guide.md` (title, *Before class*, *Formal side*, *Applications*),
item by item:

| # | Item | Note |
|---|---|---|
| 1 | Incomplete information; types; Nature; common prior; Harsanyi's transformation (Tadelis Ch. 12 opening, §12.1.1) | [[L07-01-bayesian-games-harsanyi]] §1–3 |
| 2 | Beliefs from the prior by Bayes' rule (§12.1.2) | [[L07-01-bayesian-games-harsanyi]] §4 |
| 3 | Strategies as type-contingent plans; Bayesian Nash equilibrium (§12.1.3) | [[L07-02-bayesian-nash-equilibrium]] §1–2 |
| 4 | Solving a finite Bayesian game, ex ante and type by type (§12.2.1) | [[L07-02-bayesian-nash-equilibrium]] §3 |
| 5 | A BNE with continuous actions: Cournot with private costs (Gibbons §3.1.A) | [[L07-03-cournot-private-costs]] |
| 6 | Continuous types and threshold strategies (§12.2.2) | [[L07-04-threshold-strategies-purification]] §1 |
| 7 | Mixed strategies as purified BNE (§12.5; Gibbons §3.2.A) | [[L07-04-threshold-strategies-purification]] §3 |
| 8 | Inefficient trade and adverse selection (§12.3, p. 258) | [[L07-05-adverse-selection-lemons]] §2–4 |
| 9 | Applications: insurance, credit, Cabral's insurer (M&R p. 149; Cabral §7.4 p. 174) | [[L07-05-adverse-selection-lemons]] §5–6 |
| 10 | Two-sided private information: the double auction (Gibbons §3.2.C, p. 158) | [[L07-05-adverse-selection-lemons]] §7 |
| 11 | Committee voting and the swing voter's curse (§12.4) | [[L07-09-common-values-curses]] §1 |
| 12 | Auction formats; IPV; second-price dominance; English auction (§13.1.1–13.1.2; Gibbons §3.2.B) | [[L07-06-second-price-english]] |
| 13 | First-price BNE and the Dutch auction (§13.1.3) | [[L07-07-first-price-dutch]] |
| 14 | Revenue equivalence (§13.1.4) | [[L07-08-revenue-equivalence]] |
| 15 | Common values and the winner's curse (§13.2; Cabral §6.4) | [[L07-09-common-values-curses]] §2–3 |
| G | MWG §8.E (Def. 8.E.1, Prop. 8.E.1), §13.B (Def. 13.B.1, Example 13.B.1, Props. 13.B.1–2) | named in 01, 02, 04, 05 |

---

## 1 · Definitions and results

| Ref. | Statement | Derived / used in |
|---|---|---|
| Tadelis Def. 12.1 (p. 246) | Bayesian game $\langle I,\{A_i\},\{\Theta_i\},\{u_i(\cdot;\theta_i)\},\{\phi_i\}\rangle$ | [[L07-01-bayesian-games-harsanyi]] §3 |
| Def. 12.2, (12.1) (p. 248) | $\Pr\{H\mid S\}=\pi(S\cap H)/\pi(S)$ | 01 §4 |
| Def. 12.3 (p. 249) | pure strategy $s_i:\Theta_i\to A_i$; $\lvert A_i\rvert^{\lvert\Theta_i\rvert}$ of them | [[L07-02-bayesian-nash-equilibrium]] §1 |
| Def. 12.4, (12.2) (p. 251) | BNE: $\forall i,\theta_i,a_i$: $\sum_{\theta_{-i}}\phi_i(\theta_{-i}\mid\theta_i)u_i(s_i(\theta_i),s_{-i}(\theta_{-i});\theta_i)\ge\sum_{\theta_{-i}}\phi_i(\theta_{-i}\mid\theta_i)u_i(a_i,s_{-i}(\theta_{-i});\theta_i)$ | 02 §2 |
| MWG Prop. 8.E.1 (p. 256) | BNE ⟺ each type with positive probability best-responds to his conditional distribution | 02 §2 |
| Gibbons (p. 145) | Cournot BNE: $q_1^*=\frac{a-2c+\theta c_H+(1-\theta)c_L}{3}$; $q_2^*(c_H)=\frac{a-2c_H+c}{3}+\frac{1-\theta}{6}(c_H-c_L)$; $q_2^*(c_L)=\frac{a-2c_L+c}{3}-\frac\theta6(c_H-c_L)$ | [[L07-03-cournot-private-costs]] §3 |
| (12.3)–(12.5) (pp. 255–257) | work iff $\theta_i\ge\sqrt{c/(1-\Pr\{s_j=1\})}$; $BR_i(\hat\theta_j)=\sqrt{c/\hat\theta_j}$ if $\hat\theta_j\ge c$, else 1 | [[L07-04-threshold-strategies-purification]] §1 |
| Claims 12.1–12.2 (pp. 256–257) | best responses are thresholds; unique BNE $\hat\theta^*=c^{1/3}$ | 04 §1.4 |
| Claim 12.3 (p. 265) | perturbed Matching Pennies: $H$ iff $\varepsilon_i\ge0$; → mixed NE as $\varepsilon\to0$ | 04 §3.2 |
| Gibbons (3.2.1)–(3.2.2) (p. 154) | $c=p=\frac{-3+\sqrt{9+4x}}{2}$; $\Pr\{\text{Opera}\}=1-c/x\to\frac23$ | 04 §3.3 |
| Prop. 12.1 (p. 260) | only the lowest type can trade; any $p^*\in[10,14]$ is a BNE price | [[L07-05-adverse-selection-lemons]] §3 |
| Lemons ladder (this unit) | qualities $1..k$ can trade iff $\Delta\ge(k-1)s/2$ | 05 §4 |
| M&R (5.1)–(5.2) (p. 151) | $P_s(x)=\tfrac12(x+\bar x)(1+c)$, $P_b(x)=x+v$; breakdown iff $c\bar x>v$; mandatory coverage efficient iff $v>c\bar x/2$ | 05 §5 |
| Gibbons (3.2.5)–(3.2.8) (pp. 160–161) | $p_b=\tfrac23v_b+\tfrac1{12}$, $p_s=\tfrac23v_s+\tfrac14$; trade iff $v_b\ge v_s+\tfrac14$ | 05 §7 |
| MWG Def. 13.B.1, (13.B.6) (pp. 439, 441) | $w^*=E[\theta\mid r(\theta)\le w^*]$ | 05 §8 |
| Tadelis §12.4 (pp. 262–264) | alone: follow signal iff $p>q$; pivotal: $\Pr\{G\mid\theta_I,\theta_G\}=q$, so $CA$ is not a BNE | [[L07-09-common-values-curses]] §1 |
| Prop. 13.1 (p. 273) | second-price: $s_i(\theta_i)=\theta_i$ weakly dominant | [[L07-06-second-price-english]] §2 |
| Prop. 13.2 (p. 275) | button auction: quit at $p=\theta_i$; outcome-equivalent to second-price | 06 §3 |
| Claim 13.1 (p. 276) | first-price: bidding $\theta_i$ is dominated | [[L07-07-first-price-dutch]] §1 |
| (13.1) (p. 277) | $E u_i=\prod_{j\ne i}F_j(s_j^{-1}(b_i))(\theta_i-b_i)$ | 07 §2 |
| (13.7) (p. 278) | $s(\theta)=\theta-\int_{\underline\theta}^\theta F^{n-1}dx/F(\theta)^{n-1}$ $=E[Y\mid Y<\theta]$ | 07 §3 |
| (13.8) (p. 279) | uniform: $s(\theta)=\frac{n-1}{n}\theta$; Gibbons $n=2$: $v/2$ | 07 §3.1, §4 |
| (13.9) (p. 281) | $F_n^{[1]}(x)=(nx/(n-1))^n$ on $[0,\frac{n-1}{n}]$ | [[L07-08-revenue-equivalence]] §3 |
| (13.10) (p. 282) | $F_n^{[2]}(x)=nx^{n-1}-(n-1)x^n$ | 08 §4 |
| Revenue equivalence (p. 280) | four conditions ⇒ same expected revenue, same expected payoff per type; uniform: $\frac{n-1}{n+1}$ | 08 §1, §5 |
| §13.2 (p. 284) | winner's curse: bidding $E[v\mid\theta_i]$ is not a BNE with common values | 09 §2 |

---

## 2 · Every number and worked case

| Case | Inputs | Result | Note |
|---|---|---|---|
| Entry game (pp. 243–245) | $p=2/3$ rational | row $E$: $(1,1),(\tfrac13,\tfrac43),(-\tfrac13,-\tfrac13),(-1,0)$; NE $(O,FA),(O,FF),(E,AF)$; SPE $(E,AF)$ | 01 §2 |
| Correlated prior (p. 249) | $\tfrac16,\tfrac13;\tfrac13,\tfrac16$ | $\phi_1(c\mid a)=\tfrac13$, $\phi_1(d\mid a)=\tfrac23$ | 01 §4 |
| Chicken (pp. 253–255) | $R=8$, $H=16$, $L=0$ | unique BNE $(DC,dc)$, payoffs $(3,3)$; swapped story: $(CD,cd)$ | 02 §3 |
| Cournot (illustrative) | $a=10$, $c=2$, $c_H=3$, $c_L=1$, $\theta=\tfrac12$ | $q_1^*=\tfrac83$, $q_2^*=\tfrac{13}6,\tfrac{19}6$; firm 1 profit $\tfrac{64}9$ vs $\tfrac{65}9$ with information | 03 §5 |
| Study groups (illustrative) | $c=\tfrac18$ | $\hat\theta^*=0.5$; $\sqrt c=0.354$ | 04 §1.5 |
| Purified Battle of the Sexes | $x=1,0.1,0.01$ | $\Pr\{\text{Opera}\}=0.6972,0.6703,0.6670\to\tfrac23$ | 04 §3.3 |
| Orange grove (pp. 258–260) | 10/20/30 vs 14/24/34 | pools 14, 19, 24; BNE prices $[10,14]$; gains realized $\tfrac43$ of 4 | 05 §3–4 |
| M&R insurance (illustrative) | $\bar x=100$, $c=0.1$ | market iff $v\ge10$; mandatory efficient iff $v>5$ | 05 §5 |
| M&R bank (p. 153) | A: 1.1M sure; B: 0.9M or 1.3M | at ~10% only B borrows; B's expected profit 0.1M | 05 §5 |
| Cabral insurer (pp. 174–176) | 10% high; values 20/3, costs 30/1 | $p=4.5$: $-2.55$ (printed $-2.5$); $p=30$: 0 | 05 §6 |
| Double auction (pp. 159–163) | $U[0,1]$ | gains: efficient $\tfrac16$, linear $\tfrac9{64}$, one-price $x(1-x)/2\le\tfrac18$ | 05 §7 |
| MWG Example 13.B.1 (p. 442) | $\theta\sim U[0,2]$, $r=\alpha\theta$ | $\alpha>\tfrac12$: $w^*=0$ | 05 §8 |
| Cabral auction (pp. 140–141) | values both 100 or both 150 | posted 100 → 100; auction → 125 | 06 §4 |
| Second-price, three bidders (illustrative) | 0.9, 0.6, 0.3 | winner pays 0.6 | 06 §2.3 |
| Gibbons first-price (illustrative $v=0.8$) | $n=2$ | $b=0.4$, $E u=0.32$; $n=5$: $b=0.64$, $Eu=0.0655$ | 07 §4 |
| Revenue | $n=2,3,4,5,10$ | $\tfrac13,\tfrac12,\tfrac35,\tfrac23,\tfrac9{11}$; price variance at $n=2$: $\tfrac1{72}$ vs $\tfrac1{18}$ | 08 |
| Jury (§12.4) | $q=0.6$, $p=0.7$ | $\Pr\{G\mid\theta_I\}=0.391$; pivotal posterior $=q$ | 09 §1 |
| Oil field (pp. 283–284) | 10/20/30 w.p. ¼, ½, ¼ | $E[v\mid L]=15$, $E[v\mid H]=25$; bid 15 with $L$: $-1.25$ | 09 §2 |
