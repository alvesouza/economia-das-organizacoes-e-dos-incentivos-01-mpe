---
tags: [notes, lecture-08, formulas, reference, pbe, signaling]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 15–16, pp. 303–338; Gibbons (1992) §4.1–4.2, pp. 175–210, §4.4, pp. 233–244; Milgrom & Roberts (1992) pp. 154–156; MWG §9.C–9.D, §13.C, 13.AA; Map/study-guide.md 'Lecture 8'"
---

# Lecture 8 · Formulas — every definition, every result, every number

> Prev: [[L08-08-intuitive-criterion]] · Next: [[L08-10-pitfalls]] · Map: [[L08-00-map]]

---

## 0 · The exam specification, mapped

**Estimated unit**: no slides yet, so the specification is the study guide's Lecture 8 block
(`Map/study-guide.md`) and the chapters it assigns, item by item.

| # | Item (study guide / chapter content) | Note |
|---|---|---|
| 1 | Why subgame perfection fails under incomplete information (Tadelis §15.1) | [[L08-01-subgame-perfection-fails]] |
| 2 | Beliefs, Bayes' rule on the path, anything off the path; sequential rationality; PBE (Tadelis §15.2; Gibbons §4.1) | [[L08-02-beliefs-and-pbe]] |
| 3 | Prop. 15.1 — a BNE that reaches every information set is a PBE | [[L08-02-beliefs-and-pbe]] §6 |
| 4 | Sequential equilibrium and consistency (Tadelis §15.3) | [[L08-03-sequential-equilibrium]] |
| 5 | Signaling games: pooling, separating, semi-separating; the method (Tadelis Ch. 16 opening; Gibbons §4.2.A) | [[L08-04-signaling-games]] |
| 6 | The MBA game: matrix, BNE, PBE, supporting beliefs (Tadelis §16.1) | [[L08-05-mba-game]] |
| 7 | Education signaling à la Spence (Gibbons §4.2.B; M&R p. 154) | [[L08-06-spence-job-market]] |
| 8 | Limit pricing and entry deterrence (Tadelis §16.2) | [[L08-07-limit-pricing]] |
| 9 | Refinements: the intuitive criterion (Tadelis §16.3; Gibbons §4.4) | [[L08-08-intuitive-criterion]] |
| 10 | Formal side (MWG §9.C, §9.D, §13.C, 13.AA) — **G**, named | notes 02 §7, 03 §4, 06 §7, 08 §6 |
| 11 | Applications: signaling vs screening (M&R pp. 154–157); adverse selection link | [[L08-06-spence-job-market]], [[L08-10-pitfalls]] Part I §8 |

---

## 1 · Definitions and results

### 1.1 · Tadelis, numbered

| Item | Statement | Note |
|---|---|---|
| Def. 15.1 (p. 307) | An information set is **on** the path of a BNE $\sigma^*$ if reached with positive probability, **off** otherwise | 02 §1 |
| Def. 15.2 (p. 308) | A **system of beliefs** $\mu$: a distribution over nodes of every information set, $\sum_{x\in h}\mu(x)=1$ | 02 §2 |
| Req. 15.1 (p. 308) | every player has a belief at each of his information sets | 02 §2 |
| Req. 15.2 (p. 309) | on the path, beliefs follow **Bayes' rule** | 02 §3 |
| Req. 15.3 (p. 310) | off the path, **any** belief | 02 §4 |
| Req. 15.4 (p. 310) | **sequential rationality**: $E[v_i(\sigma_i^*,\sigma_{-i}^*,\theta_i)\mid h,\mu]\ge E[v_i(s_i,\sigma_{-i}^*,\theta_i)\mid h,\mu]$ at every $h$ | 02 §4 |
| Def. 15.3 (p. 310) | **PBE** = BNE $\sigma^*$ + beliefs $\mu$ satisfying Reqs. 15.1–15.4 | 02 §4 |
| Prop. 15.1 (p. 311) | a BNE reaching every information set, with Bayes beliefs, is a PBE | 02 §6 |
| Def. 15.4 (p. 313) | **consistency**: $(\sigma^*,\mu^*)=\lim(\sigma^k,\mu^k)$, $\sigma^k$ totally mixed, $\mu^k$ by Bayes | 03 §2 |
| Def. 15.5 (p. 313) | **sequential equilibrium** = consistent PBE | 03 §2 |
| (16.1)–(16.2) (p. 321) | $\mu_U=\dfrac{p\sigma_H}{p\sigma_H+(1-p)\sigma_L}$, $\mu_D=\dfrac{p(1-\sigma_H)}{p(1-\sigma_H)+(1-p)(1-\sigma_L)}$ | 05 §2 |
| Claims 16.1–16.2 (p. 326) | separating limit pricing: entry iff believed H; $q_1^{1H}=1.5$ | 07 §3 |
| Def. 16.1 (p. 333) | a PBE **fails the intuitive criterion** if some $a_1$ is equilibrium-dominated for $\Theta'$ and, believed not in $\Theta'$, gives some $\theta'\notin\Theta'$ more for sure | 08 §2 |
| (16.3) (p. 334) | $(5-3-1)3+4=7>4+(19/12)^2$: L's deviation breaks limit-pricing pooling | 08 §3 |

### 1.2 · Gibbons

| Item | Statement | Note |
|---|---|---|
| Requirements 1–4 (pp. 177–180) | belief at each information set; sequential rationality; Bayes on the path; Bayes **where possible** off it | 02 §7 |
| Signaling Reqs. 1, 2R, 2S, 3 (pp. 187–188) | Receiver belief; Receiver best reply; Sender best reply; Bayes on used messages | 04 §2 |
| Single crossing (p. 192) | $c_e(L,e)>c_e(H,e)$ | 06 §1 |
| (4.2.1) (p. 193) | $w(e)=\mu(H\mid e)y(H,e)+[1-\mu(H\mid e)]y(L,e)$ | 06 §1 |
| (4.2.2) (p. 196) | pooled wage $w_p=q\,y(H,e_p)+(1-q)\,y(L,e_p)$ | 06 §4 |
| (4.2.8)–(4.2.10) (pp. 202–203) | hybrid: $r=\dfrac{q}{q+(1-q)\pi}$; L indifferent; $w_h=r\,y(H,e_h)+(1-r)\,y(L,e_h)$ ⇒ $\pi=\dfrac{q(1-r)}{r(1-q)}$ | 06 §6 |
| (4.2.11)–(4.2.13) (p. 206) | Myers–Majluf: accept iff $s[qL+(1-q)H+R]\ge I(1+r)$; go ahead iff $s\le R/(\pi+R)$; pooling iff $\dfrac{I(1+r)}{pL+(1-p)H+R}\le\dfrac{R}{H+R}$ | 04 §5 |
| Signaling Reqs. 5–6 (pp. 237, 239) | no belief on a type for which the message is **dominated** (5) / **equilibrium-dominated** (6 = intuitive criterion) | 08 §4 |

### 1.3 · Unnumbered but examinable

| Result | Statement | Note |
|---|---|---|
| MBA employer's threshold | $M\iff10\mu\ge3+2\mu\iff\mu\ge\tfrac38$ | 05 §3 |
| MBA separation | $c_H\le w_M-w_B\le c_L$ ($2\le4\le5$) | 05 §5.1 |
| Spence separating set (linear cost) | $e_H\in\Bigl[\dfrac{\theta_H-\theta_L}{c_L},\ \dfrac{\theta_H-\theta_L}{c_H}\Bigr]$, $e_L=0$ | 06 §3 |
| Least-cost separating | $e^*=\dfrac{\theta_H-\theta_L}{c_L}$ — L exactly indifferent to mimicking | 06 §3, 08 §5 |
| Spence pooling set (belief "low" off path) | $e_p\in\Bigl[0,\ \dfrac{p(\theta_H-\theta_L)}{\max(c_H,c_L)}\Bigr]$ | 06 §4 |
| H prefers signaling to no signaling | iff $p\le p^*=1-\dfrac{c_H}{c_L}$ | 06 §5 |
| Expected signaling waste | $p\,c_H\,e^*$ per worker | 06 §5 |
| Intuitive criterion in Spence | pooling at $e_p$ broken by $e\in\Bigl(\dfrac{\theta_H-u_L^*}{c_L},\dfrac{\theta_H-u_H^*}{c_H}\Bigr)$ | 08 §5 |

---

## 2 · Every number

### 2.1 · Entry game (Tadelis pp. 304–311)

| Quantity | Value |
|---|---|
| Payoffs: $O$; $C$ fought / accommodated; $W$ fought / accommodated | $(0,2)$; $(-1,-1)/(1,1)$; $(-2,0)/(-1,1)$ |
| $(OE,A)$, general $p$ | $(p-1,\ 1+p)$ (book prints $1-p$ for the second) |
| $(EE,F)$, general $p$ | $(p-2,\ -p)$ |
| Pure BNE at $p=\tfrac12$ | $(OO,F)$, $(EO,A)$ |
| After entry | $E[v_2(A)]=1>E[v_2(F)]=-\mu$ for all $\mu$ |
| Unique PBE | $(EO,A)$, $\mu(x_3)=1$ |
| Mixed BNE | $OO$ with $\Pr\{F\}\ge\tfrac12$ |

### 2.2 · Gibbons Fig. 4.1.1 and Tadelis Fig. 15.4

| Quantity | Value |
|---|---|
| Fig. 4.1.1: $E[u_2(L')]$ vs $E[u_2(R')]$ | $2-p>1-p$ — $(R,R')$ dies |
| Fig. 15.4: $R$ optimal iff | $3\mu\ge2$, $\mu\ge\tfrac23$ |
| Fig. 15.4: consistent belief | $\mu_2(x_1)=\tfrac12$ ⇒ unique SE $(D,L)$ |

### 2.3 · Gibbons Fig. 4.2.2 (pp. 188–190)

| Quantity | Value |
|---|---|
| After $L$ | $u$ at every $p$ ($4-p>1-p$) |
| After $R$ | $d$ iff $q\le\tfrac23$ |
| PBE | pooling $[(L,L),(u,d),p=0.5,q\le\tfrac23]$; separating $[(R,L),(u,u),p=0,q=1]$ |
| Intuitive criterion (derived, note 08 §4.2) | the pooling PBE fails |

### 2.4 · MBA game (Tadelis pp. 319–323, 333–334)

| Quantity | Value |
|---|---|
| Costs, wages, prior | $c_H=2$, $c_L=5$, $w_M=10$, $w_B=6$, $p=\tfrac14$ |
| Employer profits $H$: $M,B$; $L$: $M,B$ | $10,5$; $0,3$ |
| $(UD,MB)$ | $(3.25,\ 4.75)$ |
| $(DU,BB)$ | $(5.5,\ 3.5)$ (book prints 4.5) |
| Pure BNE | $(UU,BB)$, $(DU,BM)$ |
| Separating PBE | $(DU,BM)$, $\mu_U=0$, $\mu_D=1$; payoffs $H$ 8, $L$ 6 |
| Pooling PBE | $(UU,BB)$, $\mu_U=\tfrac14$, $\mu_D\in[0,\tfrac38]$; payoffs 6, 6 |
| Intuitive criterion | pooling fails ($L$'s best from $D$ is $5<6$; $H$ believed gets $8>6$) |

### 2.5 · Spence with M&R's numbers (pp. 155–156)

| Quantity | Value |
|---|---|
| $\theta_H,\theta_L$, share high, $c_H,c_L$ | $\$50$, $\$20$, 30%, $\$10$, $\$20$ |
| Pooled wage | $0.3(50)+0.7(20)=\$29$ |
| Separating $e_H$ | $[1.5,\ 3]$; M&R's check at $E_H=2$: L nets $\$10<\$20$, H nets $\$30>\$20$ |
| Least-cost $e^*$, H's net pay | $1.5$, $\$35$ |
| Pooling $e_p$ | $[0,\ 0.45]$ |
| $p^*$ | $0.5$ |
| Waste per worker | $0.3\times10\times1.5=\$4.50$ |
| Hybrid at $e_h=1$ | $w_h=40$, $r=\tfrac23$, $\pi=0.214$; hybrids for $e_h\in[0.45,1.5]$ |
| Intuitive criterion at $e_p=0.3$ | breaking deviations $e\in(1.35,\ 2.4)$ |

### 2.6 · Limit pricing (Tadelis pp. 323–335)

| Quantity | Value |
|---|---|
| Demand, costs, entry cost, prior | $P=5-q$; $c_1\in\{1,2\}$, $c_2=2$; $F=\tfrac12$; $\tfrac12$ |
| Monopoly L, H | $q=2$, profit 4; $q=1.5$, profit 2.25 |
| Cournot, known H | $q_1=q_2=1$, $P=3$, $v_1=1$, $v_2=\tfrac12$ |
| Cournot, known L | $q_1=\tfrac53$, $q_2=\tfrac23$, $P=\tfrac83$, $v_1=\tfrac{25}9$, $v_2=-\tfrac1{18}$ |
| H's separating payoff; mimicking at 2 | $3.25$; $4.25$ |
| L's best deviation | $4+2.25=6.25$ |
| Separating $q_1^{1L}$ | $\bigl[\tfrac{3+\sqrt5}2,\ 2+\sqrt{1.75}\bigr]=[2.62,\ 3.32]$ |
| Bayesian Cournot after pooling | $q_1^{2L}=\tfrac{19}{12}$, $q_1^{2H}=\tfrac{13}{12}$, $q_2^2=\tfrac56$; entrant $\tfrac7{36}$ (book prints $\tfrac7{18}$) |
| (ICH), (ICL) | $[1.083,\ 1.917]$, $[1.493,\ 2.507]$ |
| Pooling $\bar q_1$ | $[1.493,\ 1.917]$ |
| Intuitive criterion | pooling broken by $q=3$; only $q_1^{1L}=2.62$ survives |

### 2.7 · Beer and Quiche (Gibbons pp. 237–239)

| Quantity | Value |
|---|---|
| Prior wimpy, surly | 0.1, 0.9 |
| Pooling on Quiche | not after Quiche; duel after Beer iff $q\ge\tfrac12$; payoffs wimpy 3, surly 2 |
| Intuitive criterion | Beer equilibrium-dominated for wimpy ($2<3$), not for surly ⇒ $q=0$ ⇒ surly gets $3>2$: fails |

---

## Links

- Map: [[L08-00-map]] · Pitfalls and self-test: [[L08-10-pitfalls]] · Code: [[L08-11-python]].
- Rules: [[../../rules/07_selecao_adversa|rules/07]] · [[../../rules/game-theory|rules/game-theory]].
