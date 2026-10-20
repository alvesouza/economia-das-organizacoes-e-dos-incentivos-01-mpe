---
tags: [notes, lecture-08, signaling, pooling, separating, hybrid, pbe]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 16 opening, pp. 318–319 (the four components; pooling, separating, the Remark on hybrid equilibria); Gibbons (1992) §4.2.A, pp. 183–190 (Signaling Requirements 1, 2R, 2S, 3; Fig. 4.2.1–4.2.2 worked), §4.2.C, pp. 205–207 (Myers–Majluf), §4.2.D, pp. 208–210 (monetary policy, named)"
---

# 16 · 4.2.A · Signaling games: who moves, what is learned, and the four-step method

> **Claim.** A signaling game is the simplest dynamic game of incomplete information: an informed
> **Sender** moves first, an uninformed **Receiver** sees the move and responds. Its PBE come in
> three kinds — **pooling** (the message says nothing; posterior = prior), **separating** (the
> message reveals the type), **hybrid** (it reveals some). Every candidate is checked the same way:
> **guess the Sender's strategy → Bayes on the path → Receiver's best replies → off-path beliefs
> that keep the Sender in line → Sender's incentive constraints.**
>
> Prev: [[L08-03-sequential-equilibrium]] · Next: [[L08-05-mba-game]] · Map: [[L08-00-map]]

---

## 1 · U — why signals have to be costly (pp. 318–319)

A strong entrant would like to tell the incumbent "I am strong, don't waste money fighting me".
But a weak entrant would like to say the same thing, so **saying it** proves nothing. A signal
works only if it is **an action that costs the types differently** — Spence's (1973) insight:
education can raise wages *without* raising productivity, purely because it is cheaper for the
able to acquire. (Costless messages — cheap talk, Tadelis Ch. 18 — are out of this course's
scope.)

Tadelis's four components (p. 318):

1. **Nature** draws player 1's type, which player 2 does not know but **cares about** (common
   values).
2. Player 1 has a **rich action set**: at least as many actions as types, and **each action costs
   each type differently**.
3. Player 1 moves first; player 2 responds **after observing** player 1's choice.
4. Player 2 **updates** his belief from player 1's choice (given his belief about player 1's
   strategy) and best-responds to the updated belief.

---

## 2 · C — the formal game and the PBE requirements (Gibbons pp. 183–188)

Types $T=\{t_1,\dots,t_I\}$ with prior $p(t_i)>0$; messages $M=\{m_1,\dots,m_J\}$; actions
$A=\{a_1,\dots,a_K\}$. A pure strategy for the Sender is a **function** $m(t_i)$; for the Receiver,
a **function** $a(m_j)$. With two types, two messages and two actions each side has four pure
strategies (p. 186):

| Sender strategy | $t_1$ sends | $t_2$ sends | Kind |
|---|---|---|---|
| 1 | $m_1$ | $m_1$ | **pooling** |
| 2 | $m_1$ | $m_2$ | **separating** |
| 3 | $m_2$ | $m_1$ | **separating** |
| 4 | $m_2$ | $m_2$ | **pooling** |

The Sender's information sets are singletons, so Requirement 1 bites only on the Receiver:

> **Signaling Requirement 1.** After any message $m_j$ the Receiver has a belief
> $\mu(t_i\mid m_j)\ge0$ with $\sum_{t_i\in T}\mu(t_i\mid m_j)=1$.
>
> **2R.** For each $m_j$, $a^*(m_j)$ maximizes $\sum_{t_i}\mu(t_i\mid m_j)\,U_R(t_i,m_j,a_k)$.
>
> **2S.** For each $t_i$, $m^*(t_i)$ maximizes $U_S(t_i,m_j,a^*(m_j))$.
>
> **3.** If some type sends $m_j$ in equilibrium (let $T_j=\{t_i: m^*(t_i)=m_j\}\neq\varnothing$),
> the belief after $m_j$ follows Bayes' rule: $\mu(t_i\mid m_j)=\dfrac{p(t_i)}{\sum_{t_i\in T_j}p(t_i)}$ for $t_i\in T_j$.
>
> **Definition (p. 188).** A pure-strategy PBE of a signaling game is $m^*(t_i)$, $a^*(m_j)$ and
> $\mu(t_i\mid m_j)$ satisfying Requirements (1), (2R), (2S) and (3).

These are Tadelis's Requirements 15.1–15.4 specialized; Requirement 4 ("Bayes where possible off
the path") is vacuous here, because an unused message is reached by no strategy (p. 186).

**What each kind implies for beliefs** (Tadelis pp. 318–319):

| Kind | On-path beliefs | Off-path beliefs | What holds it together |
|---|---|---|---|
| **Pooling** | = the prior | at every unused message: free, but must support the Receiver's reply | the Receiver's reply to the unused message deters deviations |
| **Separating** | 0 or 1 — full revelation | only if there are more messages than types | each type's **incentive compatibility**: no type wants to mimic another |
| **Hybrid** (semi-separating) | strictly between prior and 0/1 | — | a mixing type must be **indifferent** |

---

## 3 · Worked — all four candidates in Gibbons's Fig. 4.2.2 (pp. 188–190)

Two equally likely types; messages $L,R$; actions $u,d$. Payoffs (Sender, Receiver):

| Type | $L$, then $u$ | $L$, then $d$ | $R$, then $u$ | $R$, then $d$ |
|---|---|---|---|---|
| $t_1$ | $1,\ 3$ | $4,\ 0$ | $2,\ 1$ | $0,\ 0$ |
| $t_2$ | $2,\ 4$ | $0,\ 1$ | $1,\ 0$ | $1,\ 2$ |

Receiver's beliefs: $p=\mu(t_1\mid L)$, $q=\mu(t_1\mid R)$. Two facts used throughout:

$$\text{after }L:\ E[u]=3p+4(1-p)=4-p\ >\ E[d]=0\cdot p+1\cdot(1-p)=1-p\quad\Rightarrow\ u\text{ for every }p ;$$
$$\text{after }R:\ E[u]=1\cdot q+0=q,\quad E[d]=0+2(1-q)=2-2q\quad\Rightarrow\ d\iff q\le\tfrac23 .$$

**1. Pooling on $L$, Sender $(L,L)$.** Bayes: $p=0.5$. Reply to $L$: $u$, so $t_1$ earns 1 and $t_2$
earns 2. Keep them from $R$: if the reply to $R$ were $u$, $t_1$ would get $2>1$ — deviation. So
the reply to $R$ must be $d$ (then $t_1$ gets $0<1$, $t_2$ gets $1<2$). $d$ needs $q\le\tfrac23$.
$$\boxed{[(L,L),\ (u,d),\ p=0.5,\ q\le\tfrac23]\ \text{is a pooling PBE.}}$$

**2. Pooling on $R$, Sender $(R,R)$.** Bayes: $q=0.5\le\tfrac23$, so the reply to $R$ is $d$:
$t_1$ earns $0$. But after $L$ the reply is $u$ at **any** $p$, giving $t_1$ a payoff of 1 > 0.
**No such PBE.**

**3. Separating, $t_1\to L$, $t_2\to R$.** Bayes: $p=1$, $q=0$; replies $u$ after $L$, $d$ after $R$;
both types earn 1. But $t_2$ deviating to $L$ is met by $u$ and earns $2>1$. **No such PBE.**

**4. Separating, $t_1\to R$, $t_2\to L$.** Bayes: $p=0$, $q=1$; replies $u$ after $L$ (always),
$u$ after $R$ ($q=1>\tfrac23$); both types earn 2. Deviations: $t_1$ to $L$ gets $1<2$; $t_2$ to
$R$ gets $1<2$.
$$\boxed{[(R,L),\ (u,u),\ p=0,\ q=1]\ \text{is a separating PBE.}}$$

> **The method, every time:** (i) fix the Sender's strategy; (ii) Bayes on every used message;
> (iii) the Receiver's best reply to those beliefs; (iv) for unused messages, pick the reply that
> best deters deviation and check some belief supports it; (v) check every type's incentive
> constraint against every other message.

(Whether the pooling PBE in case 1 survives the intuitive criterion is settled in
[[L08-08-intuitive-criterion]] §4.)

---

## 4 · U — hybrid equilibria (Tadelis Remark, p. 319; Gibbons pp. 186, 202–205)

In a hybrid (semi-separating) equilibrium one type plays a pure message and the other
randomizes. If $t_1$ always sends $m$ and $t_2$ sends it with probability $\pi$:

$$\mu(t_1\mid m)=\frac{p(t_1)}{p(t_1)+p(t_2)\,\pi}\ \in\ \bigl(p(t_1),\,1\bigr)\quad\text{for }\pi\in(0,1).$$

The message is **informative but not conclusive**. The mixing type must be indifferent, which pins
$\pi$ — worked numerically for Spence in [[L08-06-spence-job-market]] §6. Tadelis defers the
general treatment to Ch. 17 (reputation), beyond this lecture.

---

## 5 · U — two more applications in Gibbons §4.2 (pp. 205–210)

**Corporate investment and capital structure (Myers–Majluf, §4.2.C).** An entrepreneur whose
existing firm earns $\pi\in\{L,H\}$ ($H>L>0$, $\Pr\{L\}=p$) needs $I$ to fund a project returning
$R>I(1+r)$, and offers an equity stake $s$. The investor accepts iff
$s[qL+(1-q)H+R]\ge I(1+r)$ (4.2.11), with $q=\Pr\{L\mid s\}$; type $\pi$ prefers to go ahead iff
$s\le R/(\pi+R)$ (4.2.12). Pooling needs

$$\frac{I(1+r)}{pL+(1-p)H+R}\ \le\ \frac{R}{H+R}\qquad(4.2.13)$$

— the **high type subsidizes the low type** through the larger pooled stake. When (4.2.13) fails
there is a separating equilibrium in which the low type is financed at
$s=I(1+r)/(L+R)$ and the high type **forgoes a profitable project**: "financing terms that are
attractive to the high-profit type are even more attractive to the low-profit type" (p. 207). The
signal space (equity stakes) cannot sort, which pushes firms toward debt or internal funds.

**Monetary policy (§4.2.D).** A two-period version of the policy game, with the central bank's
distaste for inflation private: first-period inflation is the message, employers' second-period
expectation the reply. The separating constraint makes the strong type choose **lower** inflation
than under complete information — over-signaling, like the over-investment in education in note
06. Named only; the repeated-game background is [[../L05/L05-00-map|Lecture 5]].

---

## 6 · C — classifying the entry game (Tadelis p. 319)

| BNE of [[L08-01-subgame-perfection-fails]] | Kind | PBE? |
|---|---|---|
| $(OO,F)$ | pooling (both types stay out) | **no** — $F$ is never a best reply |
| $(EO,A)$ | separating (entry reveals $C$, staying out reveals $W$) | **yes**, $\mu(x_3)=1$ |

---

## Links

- Prev: [[L08-03-sequential-equilibrium]] · Next: [[L08-05-mba-game]] (the book's own two-type
  example, solved with this method).
- The continuous-message version: [[L08-06-spence-job-market]]; a continuous-message IO
  application: [[L08-07-limit-pricing]].
- Rules: [[../../rules/07_selecao_adversa|rules/07]] (signaling; labour-market application) ·
  [[../../rules/game-theory|rules/game-theory]] item 19 ("signalling needs the asymmetry
  modelled").
- Adverse selection, the problem signaling responds to: [[../L07/L07-00-map|Lecture 7]].
- Code: the generic two-type solver `pure_pbe`, tested on this example, in [[L08-11-python]] §3.
- Exercises (number and page only): Gibbons Problems 4.3 (p. 246), 4.4 (p. 247), 4.5–4.6
  (p. 249); Muñoz-Garcia Ch. 9 Exercises 1 (p. 376), 5 (p. 422), 7 (p. 437); Ch. 11 Exercises
  1 (p. 482), 3 (p. 497).
