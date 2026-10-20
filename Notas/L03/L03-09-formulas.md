---
tags: [notes, lecture-03, formulas, reference]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 7–8 (pp. 129–174), Definitions 7.1–7.8, 8.1–8.3, Proposition 8.1, Corollary 8.1, eqs. (8.1)–(8.9); Gibbons (1992) §2.1.A–B, §2.2.A, §2.4 (pp. 57–64, 71–73, 115–129); Cabral (2017) §7.2 (pp. 167–171); MWG §7.C, §9.A–9.B"
---

# Lecture 3 · Formulas — every definition, result and number, the exam specification mapped

> Prev: [[L03-08-time-inconsistency]] · Next: [[L03-10-pitfalls]] · Map: [[L03-00-map]]

---

## 0 · The exam specification, mapped

The lecture has no slides yet, so the specification is the study guide's block for Lecture 3
(`Map/study-guide.md`: Tadelis Ch. 7–8, Gibbons §2.1.A, §2.2.A, §2.4; formal MWG §7.C, §9.A–9.B;
applications Cabral §7.2) read against the course's learning goal "solve games of every major type,
choosing the appropriate tools according to when each agent moves and what each agent knows" (Lecture 1
slides, p. 7). Item by item:

| # | You should be able to | Note |
|---|---|---|
| 1 | Draw a game tree from a verbal description: players, order, actions, information sets, Nature, payoffs | [[L03-01-extensive-form]] §2–4 |
| 2 | Say whether a game has perfect or imperfect information, and why every simultaneous game is imperfect | [[L03-01-extensive-form]] §5 |
| 3 | Write each player's pure-strategy set and count it, $\lvert S_i\rvert=\prod m_k$ | [[L03-02-strategies]] §1 |
| 4 | Distinguish mixed from behavioral strategies; state Kuhn's equivalence under perfect recall | [[L03-02-strategies]] §2–4 |
| 5 | Build the normal form of a tree and find all pure Nash equilibria | [[L03-03-normal-form-and-paths]] §1–2 |
| 6 | Identify on- and off-path information sets and the threat that supports a Nash equilibrium | [[L03-03-normal-form-and-paths]] §3 |
| 7 | Solve a finite perfect-information game by backward induction; state Zermelo / Prop. 8.1 and when the solution is unique | [[L03-04-sequential-rationality-backward-induction]] |
| 8 | List the proper subgames of a tree and justify each | [[L03-05-subgame-perfection]] §2 |
| 9 | Find all pure SPE, branching when a subgame has several equilibria (voluntary BoS, MAD) | [[L03-05-subgame-perfection]] §4 |
| 10 | Write an SPE as complete strategies, not as an outcome | [[L03-05-subgame-perfection]] §5; [[L03-07-stackelberg]] §3 |
| 11 | Explain why a threat is or is not credible, and value a commitment | [[L03-06-credibility-entry-commitment]] |
| 12 | Solve Stackelberg, compare with Cournot, and exhibit a Nash equilibrium that is not subgame perfect | [[L03-07-stackelberg]] |
| 13 | Treat a time-inconsistent decision maker as a game against her future self | [[L03-08-time-inconsistency]] |

---

## 1 · Definitions and results

| Ref. | Statement | Derived in |
|---|---|---|
| Elements 1–7 (pp. 130–131) | players; payoffs; order of moves; actions when moving; **knowledge when moving**; Nature's distributions; common knowledge of 1–6 | [[L03-01-extensive-form]] §2 |
| **Def. 7.1** (p. 133) | game tree: nodes, precedence (transitive, asymmetric, incomplete), one predecessor per node, root $x_0$, terminal nodes $Z$, $v_i:Z\to\mathbb R$ | [[L03-01-extensive-form]] §3 |
| **Def. 7.2** (p. 135) | information sets $h_i\in H_i$ partition $i$'s nodes; same set ⇒ cannot tell apart ⇒ same actions | §4 |
| **Def. 7.3** (p. 136) | perfect information ⇔ all information sets singletons and no Nature | §5 |
| **Def. 7.4** (p. 139) | pure strategy $s_i:H_i\to A_i$, $s_i(h_i)\in A_i(h_i)$ | [[L03-02-strategies]] §1 |
| Count (p. 139) | $\lvert S_i\rvert=m_1\times\cdots\times m_k$ | §1.1 |
| **Def. 7.5** (p. 139) | mixed strategy: distribution over $S_i$ | §2 |
| **Def. 7.6** (p. 140) | behavioral strategy: independent distribution over $A_i(h_i)$ at each $h_i$ | §3 |
| Mixed → behavioral (p. 141) | $\sigma_i(a\mid h)=\sum_{s_i:\,s_i(h)=a}p_{s_i}$ | §3.1 |
| **Def. 7.7** (p. 142) | perfect recall; **Kuhn (1953)**: mixed ≡ behavioral under perfect recall | §4 |
| Normal form of a tree (pp. 143–144) | unique; the converse fails (Fig. 7.12) | [[L03-03-normal-form-and-paths]] §1 |
| **Def. 7.8** (p. 146) | information set on / off the equilibrium path: reached with positive / zero probability | §3 |
| **Def. 8.1** (p. 152) | sequential rationality: best response at **each** information set | [[L03-04-sequential-rationality-backward-induction]] §2 |
| **Prop. 8.1** (Zermelo, p. 153) | finite + perfect information ⇒ a sequentially rational backward-induction solution; unique if no player has equal payoffs at two terminal nodes | §2 |
| **Cor. 8.1** (p. 153) | ⇒ a sequentially rational pure-strategy Nash equilibrium exists; unique under the same condition | §2 |
| MWG **Prop. 9.B.1** | Zermelo: finite perfect-information games have a pure NE derivable by backward induction | §2 |
| **Def. 8.2** (pp. 154–155) | proper subgame: one node, all successors, no broken information sets | [[L03-05-subgame-perfection]] §2 |
| **Def. 8.3** (p. 157) | SPE: restriction of $\sigma^*$ is a Nash equilibrium in **every** proper subgame | §3 |
| **Fact** (p. 158) | finite perfect information: SPE = profiles surviving backward induction | §3 |
| MWG **Def. 9.B.1–9.B.2**, **Prop. 9.B.2–9.B.3** | subgame; SPNE; existence and uniqueness under perfect information; replace-a-subgame reduction | §2–4 (G) |
| Gibbons outcome vs equilibrium (pp. 125–126) | outcome $(a_1^*,R_2(a_1^*))$; SPE $(a_1^*,R_2(\cdot))$ | §5 |
| **(8.1)** (p. 160) | $q_2(q_1)=\dfrac{90-q_1}{2}$ | [[L03-07-stackelberg]] §2 |
| **(8.2)** (p. 161) | $\max_{q_1}\bigl(100-q_1-\tfrac{90-q_1}{2}\bigr)q_1-10q_1$ | §2 |
| Gibbons general (pp. 62–63) | $q_1^*=\tfrac{a-c}{2}$, $q_2^*=\tfrac{a-c}{4}$, $Q^S=\tfrac34(a-c)>Q^C=\tfrac23(a-c)$ | §2.2 |
| Asymmetric, slope $b$ | $q_1^S=\tfrac{a-2c_1+c_2}{2b}$, $q_2^S=\tfrac{a+2c_1-3c_2}{4b}$; follower out iff $c_2\ge\tfrac{a+2c_1}{3}$; Cournot $q_i^C=\tfrac{a-2c_i+c_j}{3b}$ | §2.2 |
| Credibility threshold | bond $B$ makes retaliation credible iff $F_I>D_I-B$, i.e. $B>B^*=D_I-F_I$ | [[L03-06-credibility-entry-commitment]] §3.1 |
| **(8.3)** (p. 166) | $v=\sum_t\delta^{t-1}u(x_t)$ | [[L03-08-time-inconsistency]] §1 |
| **(8.4)–(8.6)** (p. 167) | $x_t=\dfrac{\delta^{t-1}K}{1+\delta+\delta^2}$ for $u=\ln$: time consistent | §1 |
| **(8.9)** (p. 168) | $\ln x_1+\beta\delta\ln x_2+\beta\delta^2\ln x_3$ | §2 |

---

## 2 · Every number and worked case

### 2.1 · Sequential Battle of the Sexes (Figs. 7.7, 8.6; pp. 138–158)

$S_1=\{O,F\}$, $S_2=\{oo,of,fo,ff\}$. Normal form rows $O$: $(2,1),(2,1),(0,0),(0,0)$; $F$:
$(0,0),(1,2),(0,0),(1,2)$. **NE** $\{(O,oo),(O,of),(F,ff)\}$; **SPE** $(O,of)$, outcome $(2,1)$.
Simultaneous version: NE $(O,o)$, $(F,f)$ and the mixed one with $O$ at $\tfrac23$, $o$ at $\tfrac13$ (p. 145).

### 2.2 · Behavioral ↔ mixed (pp. 140–142)

$\sigma_2(o\mid O)=\tfrac13$, $\sigma_2(o\mid F)=\tfrac12$ ⇐ $(\tfrac13,0,\tfrac16,\tfrac12)$ or
$(\tfrac16,\tfrac16,\tfrac13,\tfrac13)$; general $(t,\tfrac13-t,\tfrac12-t,\tfrac16+t)$, $t\in[0,\tfrac13]$.

### 2.3 · Absent-minded driver (p. 142)

$V(p)=-3p^2+2p+1$, $p^*=\tfrac13$, $V^*=\tfrac43$.

### 2.4 · Gibbons Fig. 2.4.1 and the three-move game (pp. 59–60, 116–128)

NE $\{(R,(R',L')),(L,(R',R'))\}$; SPE $(R,(R',L'))$, outcome $(2,1)$. Three-move game: backward
induction $L''$, $L'$, $L$; outcome $(2,0)$.

### 2.5 · Centipede (Fig. 8.8, p. 159)

Stops $(1,1),(0,3),(2,2),(1,4)$; end $(3,3)$. Unique backward-induction outcome $(1,1)$.

### 2.6 · Voluntary BoS (Figs. 8.2–8.7, pp. 154–159)

Two proper subgames. NE $\{(YO,o),(NO,f),(NF,f)\}$; SPE $\{(YO,o),(NF,f)\}$.

### 2.7 · Card game (Fig. 8.5, p. 156)

Only proper subgame: the whole game. (Fig. 7.6 variant: calling is worth $0$ in expectation, folding $-1$.)

### 2.8 · Mutually assured destruction (Fig. 8.11, pp. 163–166)

War stage NE: $(R,r)$ with $(-5,-5)$, $(D,d)$ with $(-100,-100)$. Six pure NE; **SPE** $\{(IR,Nr),(ED,Bd)\}$.

### 2.9 · Entry and commitment (Cabral pp. 168–170; MWG pp. 268–269)

Cabral: out $(0,50)$, accommodate $(10,20)$, retaliate $(-10,10)$ [text: incumbent $-10$]. NE
$\{(e,\bar r),(\bar e,r)\}$; SPE $(e,\bar r)$. Bond 40: accommodation $\to-20$, retaliate, entrant out,
incumbent 50; **value of commitment 30**; $B^*=10$ (30 with the text's value). MWG 9.B.1: out $(0,2)$,
fight $(-3,-1)$, accommodate $(2,1)$; SPE (in, accommodate).

### 2.10 · Stackelberg vs Cournot (pp. 160–163)

| | $q_1$ | $q_2$ | $p$ | $\pi_1$ | $\pi_2$ |
|---|---|---|---|---|---|
| Stackelberg | 45 | 22.5 | 32.5 | 1012.5 | 506.25 |
| Cournot | 30 | 30 | 40 | 900 | 900 |

First-mover advantage $+112.5$; follower $-393.75$; $Q^S/Q^C=\tfrac98$. Nash, not SPE: $(30,\ q_2\equiv30)$;
the flood strategy with $\hat q_1=20$, on-path reply 35 (printed "40" on p. 163). Unobserved $q_1$:
Cournot again (Gibbons p. 63–64).

### 2.11 · Hyperbolic discounting (pp. 166–169)

$\delta=1$, $\beta=\tfrac12$: self 2 $x_2=\tfrac23K_2$, $x_3=\tfrac13K_2$. Self 1 (corrected) $x_1=\tfrac K2$,
so $(\tfrac12,\tfrac13,\tfrac16)K$; printed $\tfrac23K$. Self 1's committed ideal $(\tfrac12,\tfrac14,\tfrac14)K$.
Exponential benchmark $(\tfrac13,\tfrac13,\tfrac13)K$.
