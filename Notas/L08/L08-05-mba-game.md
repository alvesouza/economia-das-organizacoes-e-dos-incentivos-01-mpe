---
tags: [notes, lecture-08, signaling, mba-game, separating, pooling, pbe]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §16.1 'Education Signaling: The MBA Game', pp. 319–323 (Fig. 16.1; eqs. 16.1–16.2; the 4×4 matrix at p = 1/4 on p. 322; footnote 2)"
---

# 16.1 · The MBA game: one separating and one pooling equilibrium, held up by beliefs

> **Claim.** In Tadelis's MBA game the degree adds nothing to productivity, yet there is a
> **separating PBE** in which only the high-skill worker studies and is made a manager — because
> the degree costs him 2 and his low-skill twin 5, and the manager's premium is 4. There is also a
> **pooling PBE** in which nobody studies and everybody is put in blue-collar work, **held up only
> by the employer's off-path belief** that an MBA signals low skill with probability at least
> $5/8$. One threshold, $\mu^*=3/8$, settles every information set.
>
> Prev: [[L08-04-signaling-games]] · Next: [[L08-06-spence-job-market]] · Map: [[L08-00-map]]

---

## 1 · C — the game (pp. 319–321)

1. Nature draws the worker's skill $\theta\in\{H,L\}$, $\Pr\{\theta=H\}=p>0$; the worker learns it.
2. The worker chooses an MBA ($D$) or not ($U$). Private cost $c_H=2$, $c_L=5$ (if $D$), $0$ otherwise.
3. The employer sees $D$ or $U$ (not $\theta$) and assigns the worker to manager ($M$, wage
   $w_M=10$) or blue-collar ($B$, wage $w_B=6$).
4. Employer's net profit (the degree adds nothing to productivity):

| Skill | $M$ | $B$ |
|---|---|---|
| $H$ | 10 | 5 |
| $L$ | 0 | 3 |

Worker's payoff = wage − cost. All eight terminal payoffs (worker, employer), as in Fig. 16.1:

| Type, message | $M$ | $B$ |
|---|---|---|
| $H$, $U$ | $10,\ 10$ | $6,\ 5$ |
| $H$, $D$ | $10-2=8,\ 10$ | $6-2=4,\ 5$ |
| $L$, $U$ | $10,\ 0$ | $6,\ 3$ |
| $L$, $D$ | $10-5=5,\ 0$ | $6-5=1,\ 3$ |

![The MBA game tree: Nature in the middle draws H (top, probability p) or L (bottom); each type chooses U to the left or D to the right; the employer's information sets I_U and I_D join the two types' nodes vertically; leaf payoffs 10,10 / 6,5 / 8,10 / 4,5 for H and 10,0 / 6,3 / 5,0 / 1,3 for L; H-D-M and L-U-B highlighted](figures/L08-mba-tree.png)
*Figure — Tadelis's Fig. 16.1 redrawn with the separating PBE $(DU,BM)$ in green: the high type studies and is made a manager (8, 10); the low type does not and is put in blue-collar work (6, 3). Source: Tadelis pp. 320–322.*

The two dashed lines are the employer's information sets $I_U$ and $I_D$: at each it knows the
message, not the type. Only the green branches are played; the employer's replies at both sets are
still part of its strategy, which is what lets a reply after an unused message do the work in the
pooling equilibrium (§5).

---

## 2 · C — beliefs by Bayes' rule (eqs. 16.1–16.2, p. 321)

Let type $H$ choose $U$ with probability $\sigma_H$ and type $L$ with $\sigma_L$. With
$\mu_U=\Pr\{H\mid U\}$ and $\mu_D=\Pr\{H\mid D\}$:

$$\mu_U=\frac{p\,\sigma_H}{p\,\sigma_H+(1-p)\,\sigma_L}\quad(16.1),\qquad
\mu_D=\frac{p\,(1-\sigma_H)}{p\,(1-\sigma_H)+(1-p)(1-\sigma_L)}\quad(16.2).$$

- $\sigma_H=\sigma_L=1$ (both choose $U$): $\mu_U=p$; (16.2) is $\tfrac00$ — $\mu_D$ is **free**.
- $\sigma_H=\sigma_L=0$ (both choose $D$): $\mu_D=p$; $\mu_U$ free.
- $\sigma_H=0,\ \sigma_L=1$ (strategy $DU$): $\mu_U=\dfrac{0}{0+(1-p)}=0$, $\mu_D=\dfrac{p}{p+0}=1$
  (footnote 2, p. 322).

---

## 3 · C — the employer's best reply at any information set (p. 323)

At belief $\mu$:

$$E[\pi(M)]=10\mu+0\,(1-\mu)=10\mu,\qquad E[\pi(B)]=5\mu+3(1-\mu)=3+2\mu .$$

$$M\ \text{optimal}\iff 10\mu\ge3+2\mu\iff 8\mu\ge3\iff \boxed{\mu\ge\mu^*=\tfrac38}.$$

![Employer's expected profit against the belief mu: the M line 10 mu rises from 0 to 10, the B line 3 + 2 mu from 3 to 5; they cross at mu* = 3/8; the region mu_D <= 3/8 is shaded as the beliefs that support the pooling equilibrium; dots mark mu_U = 0 and mu_D = 1 for the separating equilibrium and mu_U = 1/4 for the pooling one](figures/L08-mba-beliefs.png)
*Figure — one threshold settles every information set: M iff $\mu\ge3/8$. Separating: $\mu_U=0\Rightarrow B$, $\mu_D=1\Rightarrow M$. Pooling on $U$: $\mu_U=p=1/4<3/8\Rightarrow B$, and the unused $D$ must be met with a belief in the shaded band. Source: Tadelis pp. 321–323.*

Everything the employer does in any equilibrium is a reading of this one picture: where the
belief at $I_U$ and at $I_D$ falls relative to $3/8$. The prior $p=1/4$ sits left of the threshold
— which is why pooling on $U$ gets $B$, not $M$, at the book's numbers (§6 asks what happens when
it does not).

---

## 4 · C — the Bayesian normal form at $p=1/4$ (p. 322)

Worker strategies $a_Ha_L$, employer strategies $a_Ua_D$. One cell in full: **$(UD,MB)$** — with
prob. $\tfrac14$ type $H$ plays $U$, gets $M$: $(10,10)$; with prob. $\tfrac34$ type $L$ plays $D$,
gets $B$: $(6-5,3)=(1,3)$:

$$(v_1,v_2)=\tfrac14(10,10)+\tfrac34(1,3)=(2.5+0.75,\ 2.5+2.25)=(3.25,\ 4.75).$$

| | $MM$ | $MB$ | $BM$ | $BB$ |
|---|---|---|---|---|
| $UU$ | $10,\ 2.5$ | $10,\ 2.5$ | $6,\ 3.5$ | $6,\ 3.5$ |
| $UD$ | $6.25,\ 2.5$ | $3.25,\ 4.75$ | $5.25,\ 1.25$ | $2.25,\ 3.5$ |
| $DU$ | $9.5,\ 2.5$ | $8.5,\ 1.25$ | $6.5,\ 4.75$ | $5.5^{\dagger},\ 3.5$ |
| $DD$ | $5.75,\ 2.5$ | $1.75,\ 3.5$ | $5.75,\ 2.5$ | $1.75,\ 3.5$ |

$^\dagger$ $(DU,BB)$: $\tfrac14(6-2)+\tfrac34(6)=1+4.5=5.5$; the book prints 4.5. It changes no best
response (column $BB$'s maximum is $UU$'s 6 either way).

**Best responses.** Worker, by column: $MM\to UU$ (10); $MB\to UU$ (10); $BM\to DU$ (6.5);
$BB\to UU$ (6). Employer, by row: $UU\to BM$ or $BB$ (3.5); $UD\to MB$ (4.75); $DU\to BM$ (4.75);
$DD\to MB$ or $BB$ (3.5). Mutual best responses:

$$\boxed{(UU,BB)\quad\text{and}\quad(DU,BM)}\qquad\text{— the two pure BNE (p. 322).}$$

($(UU,BM)$ fails: against $BM$ the worker prefers $DU$, 6.5 > 6.)

---

## 5 · Worked — which BNE are PBE (pp. 322–323)

### 5.1 · $(DU,BM)$ — separating

Both messages are used, so by **Prop. 15.1** the BNE with Bayes beliefs $\mu_U=0$, $\mu_D=1$ is a
PBE. Checking every information set anyway:

| Who | Belief | Prescribed | Payoff | Deviation | Payoff | Holds because |
|---|---|---|---|---|---|---|
| Employer at $I_U$ | $\mu_U=0<\tfrac38$ | $B$ | 3 | $M$ | 0 | $3>0$ |
| Employer at $I_D$ | $\mu_D=1\ge\tfrac38$ | $M$ | 10 | $B$ | 5 | $10>5$ |
| Worker $H$ | — | $D$ | $10-2=8$ | $U$ (→ $B$) | 6 | $c_H=2<w_M-w_B=4$ |
| Worker $L$ | — | $U$ | 6 | $D$ (→ $M$) | $10-5=5$ | $c_L=5>w_M-w_B=4$ |

> **The two incentive-compatibility constraints are the whole story:**
> $$c_H\ \le\ w_M-w_B\ \le\ c_L\qquad(2\le4\le5).$$
> The premium must be worth the degree to the high type and not worth it to the low type. This
> is the discrete version of Spence's single-crossing condition (note 06).

### 5.2 · $(UU,BB)$ — pooling

$I_U$ is on the path: $\mu_U=p=\tfrac14<\tfrac38$, so $B$ is a best reply. $I_D$ is **off** the path
(nobody studies): $\mu_D$ is free, but $B$ there must be a best reply:

$$5\mu_D+3(1-\mu_D)\ \ge\ 10\mu_D\iff 3\ge8\mu_D\iff \mu_D\le\tfrac38 .$$

Worker: $U$ gives 6 to both types; $D$ (met with $B$) gives $6-2=4$ to $H$ and $6-5=1$ to $L$. Nobody
deviates.

$$\boxed{(UU,BB),\ \mu_U=\tfrac14,\ \mu_D\in[0,\tfrac38]\ \text{is a pooling PBE.}}$$

> **The pooling equilibrium lives on a belief:** if an MBA were read as "high skill with
> probability above 3/8", the employer would promote, and the high type would study (8 > 6). The
> belief that sustains it — *an MBA means probably low skill* — is exactly what the intuitive
> criterion calls unreasonable ([[L08-08-intuitive-criterion]] §2).

| PBE | Kind | Beliefs | Worker payoffs ($H$, $L$) | Employer (expected) |
|---|---|---|---|---|
| $(DU,BM)$ | separating | $\mu_U=0,\ \mu_D=1$ | $8,\ 6$ | $\tfrac14\cdot10+\tfrac34\cdot3=4.75$ |
| $(UU,BB)$ | pooling | $\mu_U=\tfrac14,\ \mu_D\le\tfrac38$ | $6,\ 6$ | $\tfrac14\cdot5+\tfrac34\cdot3=3.5$ |

---

## 6 · Worked extension — what the prior changes (same model, derived here)

The book fixes $p=\tfrac14$. Varying $p$ with everything else at the book's values:

- **Separating $(DU,BM)$** uses beliefs 0 and 1 and the constraints $c_H\le4\le c_L$: **it does not
  depend on $p$ at all.**
- **Pooling on $U$** gets the reply the prior dictates: $B$ if $p<\tfrac38$, $M$ if $p>\tfrac38$, both at
  $p=\tfrac38$. With $M$ after $U$, both types earn 10 and no one gains from $D$ (at most
  $10-2=8$), so $(UU,MM)$ and $(UU,MB)$ are PBE for any $\mu_D$ that supports the reply after $D$.
- **Pooling on $D$** never works at the book's numbers: after $D$ the reply is $M$ or $B$; if $M$,
  type $L$ earns 5 and would switch to $U$ unless $U$ is met with $B$ **and** $6<5$ — impossible; if
  $B$, both earn less than the 6 that $U$ guarantees.

| $p$ | Pure PBE (book's costs and wages) |
|---|---|
| $p<\tfrac38$ (e.g. $\tfrac14$) | $(DU,BM)$; $(UU,BB)$ with $\mu_D\le\tfrac38$ |
| $p=\tfrac38$ | $(DU,BM)$; $(UU,BB)$; $(UU,MM)$; $(UU,MB)$ |
| $p>\tfrac38$ | $(DU,BM)$; $(UU,MM)$ with $\mu_D\ge\tfrac38$; $(UU,MB)$ with $\mu_D\le\tfrac38$ |

> **Interactive companion.** [The MBA Game](companions/companion-mba-game.html) — move the prior
> across $3/8$ and watch pooling on $U$ switch from $B$ to $M$; push $c_L$ below $w_M-w_B$ and the
> separating equilibrium disappears (the low type would mimic); the table lists every pure PBE,
> its supporting beliefs and the intuitive-criterion verdict.

---

## Links

- Prev: [[L08-04-signaling-games]] · Next: [[L08-06-spence-job-market]].
- The refinement that removes $(UU,BB)$: [[L08-08-intuitive-criterion]] §2.
- Prop. 15.1 and the requirements used above: [[L08-02-beliefs-and-pbe]] §4–6.
- Rules: [[../../rules/07_selecao_adversa|rules/07]] (labour-market signaling).
- Code: the 16-cell matrix, the BNE and the PBE enumeration, all asserted, in
  [[L08-11-python]] §4.
- Exercises (number and page only): Tadelis 16.4 "School Choice" (p. 336), 16.5 "Drug Ads"
  (p. 337); Muñoz-Garcia Ch. 9 Exercises 2 (p. 385), 3 (p. 394), 4 (p. 406); MWG 13.C.5
  (pp. 474–475).
