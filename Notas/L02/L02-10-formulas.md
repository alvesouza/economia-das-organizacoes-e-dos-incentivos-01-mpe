---
tags: [notes, lecture-02, formulas, reference]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §4.3, Ch. 5, Ch. 6 (printed pp. 69–123); Gibbons (1992) §1.1.C–1.3 (pp. 8–48); MWG §8.C–8.D, App. A; Map/study-guide.md, Lecture 2 block"
---

# Lecture 2 · Formulas: every definition, result and number

> Prev: [[L02-09-existence]] · Next: [[L02-11-pitfalls]] · Map: [[L02-00-map]]

---

## 0 · The exam specification, mapped

The lecture has no slides yet; the specification is the study guide's content line ("best responses and
rationalizability; Nash equilibrium; mixed strategies and existence") and its reading list, item by item.

| # | What to be able to do | Note |
|---|---|---|
| 1 | Define a best response, a belief, the best-response correspondence, "never a best response"; run rationalizability (Cournot, beauty contest) | [[L02-01-best-response-rationalizability]] |
| 2 | State Def. 5.1 and Prop. 5.1; find every pure NE of a matrix by the underline method; compare NE with dominance, IESDS and rationalizability | [[L02-02-nash-equilibrium]] |
| 3 | Discuss multiple equilibria (Battle of the Sexes, Stag Hunt), selection, Pareto | [[L02-02-nash-equilibrium]] §4–5 |
| 4 | Solve Cournot with general $a,b,c_1,c_2$; explain why collusion is not an equilibrium | [[L02-03-cournot]] |
| 5 | Solve Bertrand (discrete and continuous, Prop. 5.2); explain non-existence with asymmetric costs; strategic substitutes vs complements | [[L02-04-bertrand]] |
| 6 | Solve the tragedy of the commons and compare with the Pareto optimum | [[L02-05-commons]] |
| 7 | Derive the Hotelling voting best response and the median-voter equilibrium | [[L02-06-hotelling-voting]] |
| 8 | Define mixed strategies, beliefs, expected payoffs, mixed NE; use Prop. 6.1 to compute mixed NE (2×2, RPS) | [[L02-07-mixed-strategies]] |
| 9 | Apply IESDS with mixed dominance; state Prop. 6.2 | [[L02-08-iesds-rationalizability-revisited]] |
| 10 | State Nash's theorem; explain the fixed-point argument and Kakutani's four conditions for 2×2 games | [[L02-09-existence]] |

---

## 1 · Definitions and results (book numbering)

| Label | Statement | Note |
|---|---|---|
| Def. 4.5 (p. 70) | $s_i$ is a best response to $s_{-i}$ if $v_i(s_i,s_{-i})\ge v_i(s_i',s_{-i})\ \forall s_i'$ | 01 §2 |
| Claim 4.2 (p. 70) | a rational player best-responds to his belief | 01 §2 |
| Prop. 4.3 (p. 70) | strictly dominated ⇒ never a best response (to a pure belief) | 01 §2 |
| Prop. 4.4 (p. 70) | strict DSE or unique IESDS survivor ⇒ each $s_i^*$ is a BR to $s_{-i}^*$ | 01 §2 |
| Def. 4.6 (p. 72) | belief = profile $s_{-i}\in S_{-i}$ | 01 §2 |
| Def. 4.7 (p. 72) | $BR_i(s_{-i})\subseteq S_i$, a correspondence | 01 §2 |
| Def. 4.8 (p. 73) | never a best response: no belief makes $s_i$ a BR | 01 §2 |
| Def. 5.1 (p. 80) | NE: $v_i(s_i^*,s_{-i}^*)\ge v_i(s_i',s_{-i}^*)\ \forall s_i',\forall i$ | 02 §2 |
| Prop. 5.1 (pp. 80–81) | strict DSE, unique IESDS survivor or unique rationalizable profile ⇒ unique NE | 02 §2 |
| Gibbons App. 1.1.C (pp. 12–13) | Prop. A: unique IESDS survivor is the unique NE; Prop. B: every NE survives IESDS | 02 §2 |
| eq. (5.1) (p. 85) | $v_i=\ln k_i+\ln(K-\sum_jk_j)$ | 05 §2 |
| eq. (5.2) (p. 87) | $BR_i(q_j)=(a-bq_j-c_i)/(2b)$ | 03 §1 |
| Prop. 5.2 (p. 91) | continuous homogeneous Bertrand, equal costs: unique NE $p_1=p_2=c$ | 04 §3 |
| Def. 6.1 (p. 102) | mixed strategy $\sigma_i\in\Delta S_i$ | 07 §2 |
| Def. 6.2 (p. 104) | support: $\sigma_i(s_i)>0$ | 07 §2 |
| Def. 6.3 (p. 104) | mixed strategy on an interval: a CDF $F_i$ | 07 §2 |
| Def. 6.4 (p. 105) | belief $\pi_i\in\Delta S_{-i}$ | 07 §2 |
| Def. 6.5 (p. 105) | $v_i(s_i,\sigma_{-i})=\sum_{s_{-i}}\sigma_{-i}(s_{-i})v_i(s_i,s_{-i})$; $v_i(\sigma_i,\sigma_{-i})=\sum_{s_i}\sigma_i(s_i)v_i(s_i,\sigma_{-i})$ | 07 §2 |
| Def. 6.6 (p. 107) | mixed NE: $v_i(\sigma_i^*,\sigma_{-i}^*)\ge v_i(\sigma_i,\sigma_{-i}^*)\ \forall\sigma_i$ | 07 §2 |
| Prop. 6.1 (p. 108) | pure strategies in the support of an equilibrium mix earn equal payoffs | 07 §2 |
| Claims 6.1–6.2 (p. 112) | RPS: no NE with a pure player; none with a two-strategy mix | 07 §4 |
| Def. 6.7 (p. 114) | $s_i$ strictly dominated by $\sigma_i$: $v_i(\sigma_i,s_{-i})>v_i(s_i,s_{-i})\ \forall s_{-i}$ | 08 §1 |
| Def. 6.8 (p. 114) | $\sigma_i$ never a BR: no $\sigma_{-i}$ with $\sigma_i\in BR_i(\sigma_{-i})$ | 08 §1 |
| Fact (p. 116) | strictly dominated ⇒ never a BR | 08 §4 |
| Prop. 6.2 (p. 116) | two players: strictly dominated ⇔ never a BR | 08 §4 |
| Nash's theorem (p. 117) | finite games have a mixed-strategy NE | 09 §1 |
| Brouwer (p. 117) | continuous $f:[0,1]\to[0,1]$ has a fixed point | 09 §2 |
| Def. 6.9 (p. 119) | $BR=BR_1\times\dots\times BR_n:\Delta S\rightrightarrows\Delta S$ | 09 §3 |
| Fact (p. 120) | $\sigma^*$ is a NE ⇔ $\sigma^*\in BR(\sigma^*)$ | 09 §3 |
| Thm. 6.1 Kakutani (p. 120) | non-empty compact convex $X$; $C(x)$ non-empty, convex; closed graph ⇒ fixed point | 09 §4 |
| Gibbons (p. 42) | 2×2 cases (i)–(iv); $q'=(w-y)/((x-z)+(w-y))$ | 07 §6 |
| MWG Def. 8.C.1–8.C.2 (p. 243) | never a BR; rationalizable strategies (G) | 01 §6, 08 §5 |
| MWG Def. 8.D.1 (p. 246), 8.D.2 and Prop. 8.D.1 (p. 250) | pure NE; mixed NE; support characterisation (G) | 02 §6, 07 §8 |
| MWG Props. 8.D.2 (p. 252), 8.D.3 (p. 253); App. A (pp. 260–261) | existence, finite and continuous-quasiconcave (G) | 09 §6 |

### 1.1 · Closed forms

| Model | Result |
|---|---|
| Cournot, $P=a-bQ$, $c_i$ | $q_i^*=\dfrac{a-2c_i+c_j}{3b}$; $Q^*=\dfrac{2a-c_1-c_2}{3b}$; $P^*=\dfrac{a+c_1+c_2}3$; $\pi_i^*=b(q_i^*)^2$; firm $i$ out iff $c_i\ge(a+c_j)/2$ |
| Cournot, $n$ symmetric firms | $q_i^*=\dfrac{a-c}{(n+1)b}$, $P^*=\dfrac{a+nc}{n+1}\to c$ |
| Collusion temptation | $BR(q_m/2)=\dfrac{3(a-c)}{8b}>\dfrac{a-c}{4b}=\dfrac{q_m}2$ |
| Bertrand, homogeneous | $p_1=p_2=c$ (continuous); $\{(c,c),(c+\Delta,c+\Delta)\}$ on a grid |
| Bertrand, differentiated $q_i=a-p_i+bp_j$ | $BR_i=(a+bp_j+c)/2$; $p^*=(a+c)/(2-b)$, $b<2$ |
| Commons, 2 players | $BR_i=(K-k_j)/2$; NE $K/3$; optimum $K/4$; gain $\ln(9/8)$ each |
| Commons, Gibbons | NE: $v(G^*)+\tfrac1nG^*v'(G^*)=c$; optimum: $v(G^{**})+G^{**}v'(G^{**})=c$; $G^*>G^{**}$ |
| Hotelling voting | $BR_i(a_j)=[-a_j+1,a_j-1]$ for $a_j>0$; NE $a_1=a_2=$ median |
| 2×2 mixed NE | $q^*$ solves $v_1(\text{row}_1,q)=v_1(\text{row}_2,q)$; $p^*$ solves $v_2(p,\text{col}_1)=v_2(p,\text{col}_2)$ |

---

## 2 · Every number in the lecture's reading

| Example (page) | Numbers |
|---|---|
| BR with ties (p. 72) | $BR_1(R)=\{U,D\}$, $BR_1(L)=\{M,D\}$ |
| Cournot rationalizability (pp. 73–74) | $BR=(90-q)/2$; rounds $[0,45]$, $[22.5,45]$, $[22.5,33.75]$, … → 30 |
| Beauty contest (pp. 74–75) | 1, 5, 18 → average 8, target 6, player 2 wins; 20 never a BR; 19 rounds → $\{0,1\}$ ($n>2$), $\{0\}$ ($n=2$) |
| Underline method (p. 81) | P1 BR at (D,L), (M,C), (M,R); P2 at (U,R), (M,C), (D,C); unique pure NE (M, C); four more NE in mixed strategies, e.g. $(\tfrac16,\tfrac56,0)$ for both |
| Stag Hunt (p. 84) | (S,S) 5,5 and (H,H) 3,3 both NE |
| Commons (pp. 86–87) | $K/3$ vs $K/4$; $\Delta v=2\ln3-\ln2-\ln4=0.118$ (book prints 0.051, the base-10 value) |
| Cournot (pp. 87–90) | $q_i=30$, $P=40$, $\pi_i=900$; monopoly 45, 55, 2025; competitive 90 at 10; deviation $BR(22.5)=33.75$ |
| Bertrand (pp. 89–91) | monopoly $p=55$; $\Delta v=55.02p_j-0.5p_j^2-501.1$, $0.0002$ at 10.02 (exact $0.0001$); NE (10,10), (10.01,10.01); profits 0 or about 0.45 |
| Asymmetric Bertrand (pp. 91–92) | $c_1=1$, $c_2=2$: (1.99, 2.00) is a NE on cents; continuous: $v_1(p_1,2)\to98$, $=49$ at 2; $p_1^M=50.5$ |
| Hotelling (p. 94) | $a_1=-15$, $a_2=22$: citizen 3 votes 1 (18 vs 19), citizen 4 votes 2; 54 vs 47 |
| Matching Pennies (pp. 108–111) | $v_1(H,q)=2q-1$, $v_1(T,q)=1-2q$; NE $(\tfrac12,\tfrac12)$ |
| RPS (pp. 106, 111–113) | vs $(\tfrac12,\tfrac12,0)$: R $-\tfrac12$, P $\tfrac12$, S 0; NE $(\tfrac13,\tfrac13,\tfrac13)$ |
| All-pay auction (p. 107) | vs $U[0,1]$: every bid in $[0,1]$ earns 0 |
| §6.2.3 game (pp. 113–114) | pure (M,R), (D,C); mixed $p=\tfrac16$, $q=\tfrac37$; payoffs $\tfrac{12}7$, $\tfrac{10}3$ |
| Mixed IESDS (pp. 115–116) | L vs $(0,\tfrac12,\tfrac12)$: 1<2, 2<2.5, 3<3.5; then U vs $(0,\tfrac12,\tfrac12)$: 1<2, 1<1.5 |
| Gibbons Figs. 1.3.1–1.3.2 (pp. 32–33) | $\tfrac12T+\tfrac12M=\tfrac32>1$; B = 2 is a BR iff $\tfrac13<q<\tfrac23$ |
| Battle of the Sexes mixed (Gibbons p. 40) | each attends own favourite with prob. $\tfrac23$; miscoordination $\tfrac59$ |
