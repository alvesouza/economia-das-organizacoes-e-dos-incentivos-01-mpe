---
tags: [notes, lecture-06, repeated-games, formulas, reference]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §10.3–10.5, pp. 196–209; Gibbons (1992) §2.3.C–D, pp. 102–112; Cabral (2017) Ch. 9, pp. 217–231; Milgrom & Roberts (1992) Ch. 8, pp. 250–268; MWG §12.D, pp. 400–405"
---

# Lecture 6 · Formulas — every result, every number, the study guide mapped

> Prev: [[L06-08-relational-contracts]] · Next: [[L06-10-pitfalls]] · Map: [[L06-00-map]]

---

## 0 · The exam specification, mapped

No slides yet: the specification is the Lecture 6 block of `Map/study-guide.md`, item by item.

| # | Study-guide item | Note |
|---|---|---|
| 1 | Tadelis §10.4 tacit collusion (p. 201) | [[L06-02-cournot-collusion]] §2, §6 |
| 2 | Tadelis §10.5 reputation (pp. 204–209) | [[L06-05-reputation-trust]] §1; [[L06-06-institutions-reputation]] |
| 3 | Gibbons §2.3.C Cournot collusion (p. 102) | [[L06-02-cournot-collusion]] §3–§5; [[L06-04-punishments-price-wars]] §1, §3–§4 |
| 4 | Gibbons §2.3.D efficiency wages (p. 107) | [[L06-07-efficiency-wages]] §2–§5 |
| 5 | M&R "Reputations as contract enforcers" (p. 259), the repeated trust game (pp. 261–263) | [[L06-05-reputation-trust]] §2–§4 |
| 6 | M&R "live and let live" (p. 264), limits of reputation (p. 265) | [[L06-05-reputation-trust]] §5–§6 |
| 7 | Formal: MWG §12.D (p. 400) | [[L06-03-bertrand-market-structure]] §1 (Props. 12.D.1–12.D.2) |
| 8 | Cabral Ch. 9: stability (p. 218), price wars (p. 222) | [[L06-03-bertrand-market-structure]]; [[L06-04-punishments-price-wars]] §2–§5 |
| 9 | M&R efficiency wages (p. 250) | [[L06-07-efficiency-wages]] §6–§7 |
| — | Recap needed from Lecture 5 (one-stage deviation, grim trigger) | [[L06-01-recap-grim-trigger]] |
| — | The unifying inequality | [[L06-08-relational-contracts]] |

---

## 1 · Every definition and result

### 1.1 · The machinery (Tadelis)

| Result | Statement | Where derived |
|---|---|---|
| Def. 10.2–10.3 (pp. 193–194) | PV $\sum\delta^{t-1}v^t$; average $(1-\delta)\sum\delta^{t-1}v^t$ | [[L06-01-recap-grim-trigger]] §2 |
| Prop. 10.2 (p. 196) | stage Nash after every history is an SPE | §2 |
| Prop. 10.3 (p. 198) | one-stage deviation principle for infinitely repeated games | §2 |
| (10.3), p. 200 | PD: $4+\frac{4\delta}{1-\delta}\ge5+\frac{\delta}{1-\delta}\iff\delta\ge\frac14$ | §3.1 |
| **(10.5)**, p. 202 | $\delta\ge\dfrac{v_i^d-v_i^c}{v_i^d-v_i^*}$ | §3 |
| equivalent form | $v^d-v^c\le\frac{\delta}{1-\delta}(v^c-v^p)$; average form $v^c\ge(1-\delta)v^d+\delta v^p$ | §3 |

### 1.2 · Collusion

| Result | Statement | Where |
|---|---|---|
| (10.4), p. 202 | $BR_i(q_j)=(90-q_j)/2$ | [[L06-02-cournot-collusion]] §2 |
| (2.3.2), p. 103 | $\frac{1}{1-\delta}\frac{\pi_m}{2}\ge\pi_d+\frac{\delta}{1-\delta}\pi_c\iff\delta\ge\frac{9}{17}$ | §3 |
| Gibbons p. 104 | $q^*(\delta)=\dfrac{9-5\delta}{3(9-\delta)}(a-c)$ for $\delta<9/17$ | §4 |
| $n$-firm Cournot | $\delta^*=\dfrac{(n+1)^2}{n^2+6n+1}$ | §5 |
| (9.1)–(9.4), p. 219 | $\frac{\frac12\pi_M}{1-\delta}\ge\pi_M\iff\delta\ge\frac12$ | [[L06-03-bertrand-market-structure]] §1 |
| MWG Prop. 12.D.1 (p. 401) | Nash reversion is an SPE of repeated Bertrand iff $\delta\ge\frac12$ | §1 |
| MWG Prop. 12.D.2 (p. 403) | $\delta\ge\frac12$: any $p\in[c,p_M]$ sustainable; $\delta<\frac12$: every SPE prices at $c$ | §1 |
| $n$-firm Bertrand | $\delta\ge1-1/n$ (MWG Ex. 12.D.2, p. 405; Cabral p. 227) | §2 |
| **(9.5)**, p. 220 | $\delta=\dfrac{(1+g)(1-h)}{1+r/f}$; up in $f,g$; down in $h,r$ | §3 |
| (2.3.3), p. 105 | $\delta(\frac{\pi_m}{2}-\pi(x))\ge\pi_d-\frac{\pi_m}{2}$ | [[L06-04-punishments-price-wars]] §1 |
| (2.3.4), p. 106 | $\delta(\frac{\pi_m}{2}-\pi(x))\ge\pi_{dp}(x)-\pi(x)$ | §1 |

### 1.3 · Reputation

| Result | Statement | Where |
|---|---|---|
| Trust game, p. 205 | $\frac{1}{1-\delta}\ge2\iff\delta\ge\frac12$ | [[L06-05-reputation-trust]] §1 |
| M&R footnote 11, p. 263 | $N=\frac{1}{(1+r)^t-1}+1=\frac{1}{1-\delta}$, $\delta=(1+r)^{-t}$ | §2 |
| M&R trust box, pp. 261–263 | exact: $NV\ge V+G\iff\delta\ge\frac{G}{V+G}$ (M&R print $NV>G$) | §2 |
| Guarantor, p. 207 | $\frac{0.1}{1-\delta}\ge2\iff\delta\ge0.95$ | [[L06-06-institutions-reputation]] §1 |

### 1.4 · Efficiency wages

| Result | Statement | Where |
|---|---|---|
| Gibbons p. 109 | $V_e=\frac{w^*-e}{1-\delta}$ | [[L06-07-efficiency-wages]] §3 |
| Gibbons p. 110 | $V_s=\frac{(1-\delta)w^*+\delta(1-p)w_0}{(1-\delta p)(1-\delta)}$ | §3 |
| **(2.3.5)**, p. 110 | $w^*\ge w_0+e+\frac{(1-\delta)e}{\delta(1-p)}$ | §3 |
| (2.3.6), p. 110 | $p=0$: $w^*\ge w_0+\bigl(1+\frac{1-\delta}{\delta}\bigr)e$ | §3 |
| (2.3.7), p. 110 | $y-w^*\ge0$ | §4 |
| combined | $\delta\ge\frac{e}{e+(1-p)(y-e-w_0)}$ | §4 |
| (8.1), p. 251 | cheat iff $g>p(w-\bar w)N$ ($p$ = **detection**) | §6 |
| p. 252 / (8.3) | efficiency wage $w=\bar w+g/(Np)$ | §6 |
| (8.2)–(8.6), p. 254 | $\min M(p)+w$ s.t. IC; $M'(p^*)=g/(p^{*2}N)$; $dp^*/dN<0$ | §7 |

---

## 2 · Every number

### 2.1 · Tadelis's Cournot cartel ($p=100-q$, $c=10$)

| | Firm 1 ($q^c=22$) | Firm 2 ($q^c=23$) |
|---|---|---|
| $v^c$ | 990 | 1035 |
| $q^d$ | 33.5 | 34 |
| $v^d$ | 1122.25 | **1156** (book prints 1122) |
| $\delta^*$ | **0.595** | **0.473** (book prints 0.392) |

Cournot 30 each, price 40, profit 900; monopoly split 22.5 each, price **55** (book's p. 203
"45" is total output), profit 1012.5.

### 2.2 · Gibbons's symmetric cartel ($a-c=1$; Tadelis numbers in brackets)

$\pi_m/2=1/8$ [1012.5], $\pi_d=9/64$ [1139.06, $q_d=33.75$], $\pi_c=1/9$ [900] →
$\delta^*=9/17=0.529$. At $\delta=1/2$: $q^*=6.5/25.5=0.2549$ [22.94 each, price 54.12,
profit 1012.1]. $n$-firm cutoffs: 0.529, 0.571, 0.610, 0.643 for $n=2,3,4,5$; 0.752 at $n=10$.

### 2.3 · Bertrand and Cabral

$\delta^*=0.5,\ 0.667,\ 0.75,\ 0.8,\ 0.9$ for $n=2,3,4,5,10$. Cabral p. 221: $r=10\%$, monthly
prices → $\delta=0.9917$, $n\le121$; annual prices → $\delta=0.909$, $n\le11$. Box 9.1:
industrial diamonds USD 3 → under USD 1.80 per carat (1981). Box 9.3: average route contact
402.3. Cement: +1% GDP → −0.5% to −1% relative price.

### 2.4 · Punishments, reputation, institutions

Abreu at $\delta=1/2$: (2.3.3) holds for $x\notin(1/8,3/8)$, (2.3.4) for $x\in[3/10,1/2]$ →
$x/(a-c)\in[3/8,1/2]$. Trust game $\delta\ge1/2$; guarantor fee 0.1, bond 2 → $\delta\ge0.95$
(bond need only exceed 1). M&R multiplier at $r=10\%$: $N=11$ (yearly), 2.64 (every 5 years),
1.17 (every 20 years).

### 2.5 · Efficiency wages

M&R: $w=50$, $\bar w=40$, $g=1$, $p=0.05$ (USD thousands) → $0.05\times10\times N$ vs $1$:
cheat at $N=1$; efficiency wage $40+20/N$ = 60 ($N=1$), 50 ($N=2$). In Gibbons's terms
($w_0=39$, $e=1$, $p=0.95$): $w^*=40+20(1-\delta)/\delta$ — 60 at $\delta=1/2$, 50 at
$\delta=2/3$. MacRents: supervisors +8.9%, non-managerial +1.7% in company outlets.

---

## Links

[[L06-00-map]] · [[L06-10-pitfalls]] · [[L06-11-python]] (every number here is asserted there).
