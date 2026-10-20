---
tags: [notes, lecture-01, formulas, reference]
date: 2026-10-16
status: taught
source: "Aula/Lecture01.pdf (all slides; wrap-up slide 34); Tadelis (2013) Ch. 3 and §4.1-4.2 (pp. 43-69); Gibbons §1.1.A-B (pp. 2-7); MWG §8.B (pp. 236-240); Cabral §7.1, §14.2; M&R Table 5.1"
---

# Lecture 1 · Formula sheet — every definition, result and number

> Prev: [[L01-08-spatial-competition]] · Next: [[L01-10-pitfalls]] · Map: [[L01-00-map]]

---

## 0 · The exam specification, mapped

The slides' wrap-up (slide 34) lists what the lecture covered; the course learning goals (slide
7) ask you to recognize, solve, and model. Item by item:

| # | Wrap-up item (slide 34) | What you must be able to do | Note |
|---|---|---|---|
| 1 | Normal-form games | write $G=\langle I,\{S_i\},\{u_i\}\rangle$ for a verbal story; fill a bimatrix; piecewise payoffs for continuous strategies | [[L01-01-games-normal-form]] |
| 2 | Static vs dynamic; complete vs incomplete information | define each; state common knowledge; count contingent-plan strategies | [[L01-02-information-and-strategies]] |
| 3 | Solution concepts (slides 21–22) | define equilibrium; judge a concept by existence, uniqueness, invariance | [[L01-03-solution-concepts]] |
| 4 | Dominant and dominated strategies | apply strict and weak definitions with the right quantifier; find all dominated strategies | [[L01-04-dominance]] §1, §5 |
| 5 | Dominant-strategy equilibrium | find it or show it does not exist; prove Prop. 4.1 | [[L01-04-dominance]] §2–§4 |
| 6 | Pareto optimality | find the Pareto set; explain why a DSE can be Pareto dominated; the partnership band $y/n<c<y$ | [[L01-05-pareto-social-dilemmas]] |
| 7 | IESDS | run it round by round with the dominator and the knowledge level of each round; state and prove Prop. 4.2 | [[L01-06-iesds]] |
| 8 | IESDS in continuous games | bound best responses; Cournot intervals and their limit | [[L01-07-cournot-iesds]] |
| 9 | Spatial competition | location payoffs on a line; peel by IESDS; welfare comparison; the role of prices | [[L01-08-spatial-competition]] |

---

## 1 · Definitions and results

| Item | Statement | Derived in |
|---|---|---|
| Normal form (slide 13; Tadelis Def. 3.3, p. 47) | $G=\langle I,\{S_i\}_{i\in I},\{u_i\}_{i\in I}\rangle$, $u_i:S_1\times\dots\times S_n\to\mathbb R$ | [[L01-01-games-normal-form]] §2 |
| Pure strategy (Def. 3.2, p. 46) | a deterministic plan of action; profile $s=(s_1,\dots,s_n)$ | §2 |
| Others' profile (slide 14; p. 59) | $s_{-i}\in S_{-i}=\prod_{j\ne i}S_j$, $s=(s_i,s_{-i})$ | §2.1 |
| Finite game (Def. 3.4, p. 51) | finitely many players and strategies; two players ⇒ bimatrix | §2.2 |
| Common knowledge (Def. 3.1, p. 45; slide 16) | everyone knows $E$, everyone knows that everyone knows $E$, *ad infinitum* | [[L01-02-information-and-strategies]] §2 |
| Strategy (slide 17) | a complete contingent plan; $a$ actions at each of $m$ contingencies ⇒ $a^m$ strategies | §3 |
| Ordinal invariance | dominance, DSE and IESDS unchanged by strictly increasing transforms of each $u_i$ | §4.1 |
| Solution concept, equilibrium (slide 21; p. 54) | a rule selecting reasonable profiles; an equilibrium is a selected **profile of strategies** | [[L01-03-solution-concepts]] §1 |
| Criteria (slide 22; pp. 55–56) | existence, uniqueness, invariance (payoff changes $\le\varepsilon$) | §2 |
| Strict invariance | if $g$ is the smallest strict margin, perturbations with $\varepsilon<g/2$ keep every strict inequality | §3.1 |
| Strictly dominated (slide 23; Def. 4.1, p. 60) | $u_i(s_i,s_{-i})<u_i(s_i',s_{-i})$ for all $s_{-i}$ | [[L01-04-dominance]] §1 |
| Weakly dominated (slide 23; MWG Def. 8.B.3) | $\le$ for all $s_{-i}$, $<$ for at least one | §1 |
| Strictly (weakly) dominant (Def. 4.2, p. 61) | strictly (weakly) dominates every other strategy | §1 |
| Claim 4.1 (p. 60) = Lesson 1 | a rational player never plays a strictly dominated strategy | §1 |
| Strict DSE (Def. 4.3, p. 61; slide 25) | every $s_i^D$ strictly dominant | §2 |
| **Prop. 4.1** (p. 61; slide 25) | a strict DSE is the unique DSE | §2 (proof) |
| Weakly dominant: uniqueness | under the slides' definition a player has at most one weakly dominant strategy; under Tadelis's remark (p. 63) not | §7 |
| Pareto (Def. 3.5, p. 57; slide 26) | $s$ Pareto dominates $s'$: $u_i(s)\ge u_i(s')\ \forall i$, $>$ for some $i$; Pareto optimal: not dominated | [[L01-05-pareto-social-dilemmas]] §1 |
| Lesson 2 (slide 26) | individually rational choices can lead to socially undesirable outcomes | §2 |
| IESDS (slide 29) | $S_i^0=S_i$; $S_i^k=\{s_i\in S_i^{k-1}:\nexists s_i'\in S_i^{k-1},\ u_i(s_i',s_{-i})>u_i(s_i,s_{-i})\ \forall s_{-i}\in S_{-i}^{k-1}\}$; $S_i^\infty=\bigcap_kS_i^k$ | [[L01-06-iesds]] §2 |
| Iterated-elimination equilibrium (Def. 4.4, p. 65) | any profile surviving IESDS | §2 |
| **Prop. 4.2** (p. 68; slide 29) | a strict DSE uniquely survives IESDS (after one round) | §2 (proof) |
| Order independence (MWG pp. 239–240) | strict: the end set does not depend on the order; weak: it can | §6 |
| Round $k$ knowledge | round 1: rationality; round $k$: $(k-1)$-th order knowledge of rationality | §3 |

### 1.1 · Model formulas

| Model | Formula | Note |
|---|---|---|
| Partnership, $n$ partners | $u_i=\frac{y\cdot\#E}{n}-c\cdot\mathbb 1[E]$; $u(E)-u(S)=\frac yn-c$ for every $s_{-i}$ | [[L01-04-dominance]] §4 |
| Partnership dilemma | $S$ dominant and all-E Pareto better $\iff \frac yn<c<y$ | [[L01-05-pareto-social-dilemmas]] §3 |
| Mafia-modified PD | M strictly dominant $\iff z>1$ | §4 |
| Second-price auction | $u_i=v_i-\max_{j\ne i}b_j$ if $i$ wins; bidding $v_i$ weakly dominant | [[L01-04-dominance]] §6 |
| Cournot, $p=a-bq$, costs $c_i$ | $BR_i(q_j)=\max\{0,\frac{a-c_i-bq_j}{2b}\}$; $S_i^k=[BR_i(U_j^{k-1}),BR_i(L_j^{k-1})]$ | [[L01-07-cournot-iesds]] §3–§5 |
| Cournot dominance step | $v_i(x,q_j)-v_i(z,q_j)=(x-z)(a-c_i-b(x+z+q_j))$ | §3 |
| Cournot point | $q_i^*=\frac{a-2c_i+c_j}{3b}$, $p^*=\frac{a+c_1+c_2}{3}$, $v_i^*=\frac{(a-2c_i+c_j)^2}{9b}$; exit if $c_i\ge\frac{a+c_j}{2}$ | §5 |
| Location, 7 blocks | $u_A=\frac{s_A+s_B-1}{2}$ ($s_A<s_B$), $\frac72$ ($=$), $7-\frac{s_A+s_B-1}{2}$ ($>$) | [[L01-08-spatial-competition]] §2 |
| Hotelling (Cabral (14.3)–(14.5)) | $q_i=\frac12+\frac{p_j-p_i}{2t}$; $p_i=\frac{c+t+p_j}{2}$; $p=c+t$ | §6 |

---

## 2 · Every number in the lecture

### 2.1 · Grade game (slides 10–12)

Grades: $(\alpha,\alpha)$ B−/B−, $(\alpha,\beta)$ A/C, $(\beta,\beta)$ B+/B+. Payoffs:
$(0,0)$, $(3,-1)$, $(-1,3)$, $(1,1)$. $\alpha$ strictly dominant ($0>-1$, $3>1$); DSE
$(\alpha,\alpha)$, Pareto dominated by $(\beta,\beta)$.

### 2.2 · Prisoner's dilemma (slide 24; Tadelis p. 48)

$(M,M)=(-2,-2)$, $(M,F)=(-5,-1)$, $(F,M)=(-1,-5)$, $(F,F)=(-4,-4)$. F strictly dominant
(margins 1 and 1); DSE (F, F); Pareto set $\{(M,M),(M,F),(F,M)\}$. Altruistic version (p. 53):
$(-3,-3)$, $(-5\tfrac12,-3\tfrac12)$, $(-3\tfrac12,-5\tfrac12)$, $(-6,-6)$, M dominant. Mafia: $z>1$.

### 2.3 · Matrix (4.1) = slide 27 (Tadelis p. 64)

Rows U, M, D; columns L, C, R: $(4,3),(5,1),(6,2)$ / $(2,1),(8,4),(3,6)$ / $(3,0),(9,6),(2,8)$.
No dominant strategy; C ≺ R; IESDS: C (round 1), M and D (round 2), R (round 3) ⇒ $(U,L)$,
payoffs $(4,3)$, Pareto dominated by $(8,4)$ and $(9,6)$. Pareto set $\{(D,C),(D,R)\}$.

### 2.4 · Cournot (Tadelis pp. 49, 65–68)

Quadratic costs (p. 49): competitive $q_i=25$, $p=50$, profit 625; $q_1=24$ gives 648.
Linear, $p=100-q$, $c=10$: $BR=(90-q_j)/2$; intervals $[0,45]$, $[22.5,45]$, $[22.5,33.75]$,
$[28.125,33.75]$, …; width $45/2^{k-1}$; limit $q=30$, $p=40$, profit 900; at 20 each: 1000;
joint optimum 22.5 each: 1012.5.

### 2.5 · Pharmacy avenue (slides 32–33)

$u_A(1,\cdot)=(3.5,1,1.5,2,2.5,3,3.5)$, $u_A(2,\cdot)=(6,3.5,2,2.5,3,3.5,4)$: $1\prec2$. No dominant
block. IESDS removes $\{1,7\}$, $\{2,6\}$, $\{3,5\}$ ⇒ $(4,4)$, 3.5 customers each. Walking: 12 at
$(4,4)$, minimum 6 at $\{2,5\},\{2,6\},\{3,6\}$.

### 2.6 · Other book examples

| Example | Numbers | Note |
|---|---|---|
| Advertising game (Tadelis p. 60) | L ≺ M ($8>6$, $4>2$, $1>0$); M, H undominated | [[L01-04-dominance]] §5 |
| Battle of the Sexes (Tadelis p. 54) | $(2,1),(0,0)/(0,0),(1,2)$: nothing dominated | [[L01-03-solution-concepts]] §2 |
| Gibbons Fig. 1.1.1 (pp. 5–7) | Right, Down, Left removed ⇒ (Up, Middle) | [[L01-06-iesds]] §4 |
| MWG Fig. 8.B.3 (p. 238) | weak elimination ends at (D, R), (D, L) or $\{D\}\times\{L,R\}$ by order | [[L01-06-iesds]] §6 |
| M&R Table 5.1 (p. 138) | $(-1,-1)$, $(3,-2)$, $(-2,3)$, $(2,2)$; grab dominant; no investment | [[L01-05-pareto-social-dilemmas]] §4 |
| Cabral Fig. 7.1 (p. 161) | $(5,5)$ vs $(4,4)$; B dominant ($6>5$, $4>3$) | §2 |
| Partnership default (companion) | $y=6$, $c=4$, $n=2$: $(2,2),(-1,3),(3,-1),(0,0)$ = PD $+4$ | §3 |
