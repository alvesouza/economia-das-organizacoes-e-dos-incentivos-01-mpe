---
tags: [notes, lecture-08, signaling, intuitive-criterion, refinements, equilibrium-dominance, forward-induction]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §16.3 'Refinements of Perfect Bayesian Equilibrium in Signaling Games', pp. 332–335 (the speech, Def. 16.1, MBA and limit-pricing applications) and §16.4 Summary, p. 335; Gibbons (1992) §4.4, pp. 233–244 (Signaling Requirements 5–6, 'Beer and Quiche' Fig. 4.4.3 on pp. 237–239, Spence on pp. 239–244); MWG Appendix 13.AA, pp. 467–471; MWG §9.D, p. 292"
---

# 16.3 · The intuitive criterion: read a deviation as coming from whoever could gain by it

> **Claim.** PBE lets off-path beliefs be anything, so signaling games have **continua** of
> equilibria. Cho and Kreps's **intuitive criterion** disciplines those beliefs: if an unused
> message could **never** help some type relative to its equilibrium payoff (it is
> *equilibrium-dominated* for that type), the Receiver should not attribute it to that type — and
> if, so attributed, the message makes another type **strictly better off for sure**, the
> equilibrium is broken. In the two-type games of this lecture it **removes every pooling PBE and
> every separating PBE but the least-cost one**: MBA → $(DU,BM)$; Spence → $e_H=1.5$; limit
> pricing → $q_1^{1L}=2.62$.
>
> Prev: [[L08-07-limit-pricing]] · Next: [[L08-09-formulas]] · Map: [[L08-00-map]]

---

## 1 · U — the speech (p. 333)

In the MBA pooling equilibrium $(UU,BB)$ ([[L08-05-mba-game]] §5.2) both types get 6. A high type
deviates to $D$ and says:

> *"I am an H type. To convince you I am going to deviate and choose D. If you believe me, and put
> me in the M job instead of a B job, I will get 8 instead of 6. The reason you should believe me
> is that if I were an L type who chose D and you were to promote me then I would get 5 instead
> of 6. Therefore you should believe me … because no L type in his right mind would do what I am
> about to do."*

The employer can make the deduction alone (p. 333): *if only one type can benefit from the
deviation and the others can only lose, update toward that type.* This is **forward induction**
— reading the past move as rational — as opposed to backward induction, which assumes future
moves are rational (Gibbons p. 239).

---

## 2 · C — the definition, and the MBA pooling equilibrium fails it (pp. 333–334)

Types $\Theta$ (finite), Sender's action $a_1$, Receiver's action $a_2$. For a subset of types
$\hat\Theta\subseteq\Theta$ and an action $a_1$, let

$$BR_2(\hat\Theta,a_1)=\bigcup_{\mu:\ \mu(\hat\Theta)=1}\ \arg\max_{a_2\in A_2}\ \sum_{\theta\in\hat\Theta}v_2(a_1,a_2;\theta)\,\mu(\theta)$$

— the Receiver's best replies to $a_1$ under **some** belief concentrated on $\hat\Theta$. Write
$v_1^*(\theta)$ for type $\theta$'s payoff in the PBE $\sigma^*$.

> **Definition 16.1.** A PBE $\sigma^*$ **fails the intuitive criterion** if there exist an action
> $a_1$, a set of types $\Theta'\subset\Theta$ and a type $\theta'\notin\Theta'$ such that
> 1. $v_1^*(\theta)>\max_{a_2\in BR_2(\Theta,a_1)}v_1(a_1,a_2;\theta)$ for all $\theta\in\Theta'$;
> 2. $v_1^*(\theta')<\min_{a_2\in BR_2(\Theta\setminus\Theta',a_1)}v_1(a_1,a_2;\theta')$.

*(The book prints $v_2$ inside the minimum in condition 2; it must be the Sender's payoff $v_1$, as
the explanation on pp. 333–334 makes clear.)*

**In words.** (1) Every type in $\Theta'$ does strictly worse with $a_1$ than in equilibrium **whatever
the Receiver believes** — $a_1$ is *equilibrium-dominated* for $\Theta'$. (2) Type $\theta'$ does
strictly better with $a_1$ than in equilibrium **whatever the Receiver does**, as long as it
believes the sender is not in $\Theta'$.

**The four-step test (two types):**

| Step | MBA pooling $(UU,BB)$, off-path $a_1=D$ |
|---|---|
| 1. Equilibrium payoffs | $v^*(H)=6$, $v^*(L)=6$ |
| 2. Best payoff from $a_1$ under any belief ($M$ or $B$ are both possible replies) | $H$: $\max(10-2,\,6-2)=8$; $L$: $\max(10-5,\,6-5)=5$ |
| 3. Who is equilibrium-dominated? | $L$: $5<6$ ⇒ $\Theta'=\{L\}$. $H$: $8\ge6$, kept |
| 4. Belief on the kept types only ($\mu_D=1$) → reply $M$; does a kept type gain for sure? | $H$ gets $8>6$ ⇒ **fails** |

**The separating PBE $(DU,BM)$ passes trivially**: both messages are used, so there is no
off-path action to deviate to, and no type can gain "by convincing player 2 that he is truly that
type" (p. 334). So the criterion selects $(DU,BM)$.

---

## 3 · C — limit pricing (pp. 334–335)

The entrant's best replies to any first-period output: at belief "high cost" it enters with
$q_2^2=1$; at "low cost" it stays out ($q_2^2=0$); at intermediate beliefs it enters with smaller
quantities, down to the level $\underline q<\tfrac56$ at which entry just breaks even. So
$BR_2(\Theta,a_1)=\{0\}\cup[\underline q,1]$ for every $a_1$.

**Pooling fails.** Take $a_1=3$, $\Theta'=\{H\}$, $\theta'=L$.

- (1) H: pooling gives at least 3.25 (its (ICH) constraint), while producing 3 gives at most
  $(5-3-2)\cdot3+2.25=0+2.25=2.25<3.25$ — even with no entry. **Equilibrium-dominated.**
- (2) L, believed to be L, faces no entry: $(5-3-1)\cdot3+4=3+4=7$, while its **best** pooling payoff
  is $4+\bigl(\tfrac{19}{12}\bigr)^2=4+2.507=6.507$. $7>6.507$:

$$(5-3-1)3+4=7\ >\ 4+\Bigl(\tfrac{19}{12}\Bigr)^2\qquad(16.3)$$

**Every pooling PBE fails.**

**Only the best separating PBE survives** (p. 335): of the separating equilibria
$2.62\le q_1^{1L}\le3.32$, only $q_1^{1L}=2.62$ passes. For any $q_1^{1L}>2.62$, an output just above
2.62 is one H would never choose (it gives H less than 3.25 even with no entry — that is what
2.62 means) and that L, believed, strictly prefers (closer to its monopoly output 2). Tadelis
leaves the formal check to Exercise 16.7 (p. 338).

> **Tadelis's summary (p. 335):** "Refinements such as the intuitive criterion help pin down
> equilibria, often resulting in the least-cost separating equilibrium."

---

## 4 · Worked — Gibbons's examples

### 4.1 · Beer and Quiche (Gibbons pp. 237–239, Fig. 4.4.3)

Sender: wimpy (prob. 0.1) or surly (0.9). Message: Beer or Quiche for breakfast. Receiver: duel or
not. Sender payoffs: preferred breakfast (wimpy: Quiche; surly: Beer) is worth 1, avoiding a duel
2. Receiver: duel a wimpy +1, duel a surly −1, not duel 0.

**Pooling on Quiche, Receiver (not after Quiche, duel after Beer).** After Quiche the belief is the
prior: duel pays $0.1(1)+0.9(-1)=-0.8<0$, so *not*. Equilibrium payoffs: wimpy $1+2=3$, surly
$0+2=2$. After the unused Beer, duel needs $q=\Pr\{\text{wimpy}\mid\text{Beer}\}$ with
$q(1)+(1-q)(-1)\ge0$, i.e. $q\ge\tfrac12$. Then Beer gives wimpy $0$ and surly $1$: no deviation. A PBE
for any $q\ge\tfrac12$ (p. 238).

It even passes Gibbons's **Signaling Requirement 5** (no *strictly dominated* message): Beer is not
dominated for the wimpy type, since its best payoff from Beer (2) exceeds its worst from Quiche
(1). But:

| | Equilibrium payoff | Best payoff from Beer (any reply) | Equilibrium-dominated? |
|---|---|---|---|
| wimpy | 3 | 2 (not dueled) | **yes**: $2<3$ |
| surly | 2 | 3 (not dueled) | no |

Remove the wimpy type: $q=0$ ⇒ the Receiver does not duel after Beer ⇒ surly gets $3>2$. **The
pooling-on-Quiche PBE fails the intuitive criterion** (p. 239) — the surly type's "speech" is
believable. (The same game, with the Receiver's payoffs shifted, is Tadelis Exercise 16.8, p. 338;
this note works only the pooling-on-Quiche case that Gibbons works in his text.)

**Equilibrium dominance vs dominance (Gibbons p. 239).** A message is *dominated* for a type if
another message's worst payoff beats its best payoff (Requirement 5); it is
*equilibrium-dominated* if the type's **equilibrium payoff** beats its best payoff (Requirement 6
= the intuitive criterion). Dominated ⇒ equilibrium-dominated, so Requirement 6 is stronger.

### 4.2 · Check: Gibbons's Fig. 4.2.2 pooling equilibrium (derived here)

[[L08-04-signaling-games]] §3 found the pooling PBE $[(L,L),(u,d),p=0.5,q\le\tfrac23]$ with
payoffs $t_1$: 1, $t_2$: 2. The unused message $R$: $t_1$ gets at most $\max(2,0)=2\ge1$ (kept);
$t_2$ gets at most $\max(1,1)=1<2$ (**equilibrium-dominated**). Believing $t_1$ ($q=1$), the Receiver
plays $u$ after $R$ ($1>0$), and $t_1$ gets $2>1$. **This pooling PBE fails too**; the separating
$[(R,L),(u,u)]$ uses both messages and passes.

---

## 5 · C/G — Spence: only the least-cost separating equilibrium survives (Gibbons pp. 239–244; MWG pp. 468–471)

With M&R's numbers ([[L08-06-spence-job-market]] §3–4), both kinds of PBE are broken the same
way: find an education level that **the low type would refuse even at wage $\theta_H$** but that
**the high type would take if paid $\theta_H$**.

**Separating at $e_H>1.5$**, e.g. $e_H=2$: equilibrium payoffs L 20, H $50-20=30$. Any
$e\in(1.5,2)$: L's best is $50-20e<50-30=20$ — equilibrium-dominated; H believed high gets
$50-10e>50-20=30$. Broken. At $e_H=1.5$ there is no such gap: $(1.5,1.5)$ is empty.

**Pooling at $e_p$** (wage $\bar w=29$): $u_L^*=29-20e_p$, $u_H^*=29-10e_p$. A deviation $e$ breaks it if

$$\underbrace{50-20e<u_L^*}_{\text{L excluded}}\ \text{ and }\ \underbrace{50-10e>u_H^*}_{\text{H gains}}
\iff e\in\Bigl(\frac{50-u_L^*}{20},\ \frac{50-u_H^*}{10}\Bigr)=\Bigl(\tfrac{21}{20}+e_p,\ \tfrac{21}{10}+e_p\Bigr),$$

which is never empty because $c_H<c_L$ and $\theta_H>\bar w$. At $e_p=0.3$: $(1.35,\,2.4)$.

![Education-wage plane: pooling point (0.3, 29); L's equilibrium indifference line w = 23 + 20e reaches the theta_H = 50 line at e' = 1.35; H's line w = 26 + 10e reaches it at e'' = 2.4; the green segment between them on the 50 line marks deviations L would never make even if paid 50 but H gains from if believed](figures/L08-intuitive-criterion.png)
*Figure — why pooling at $e_p=0.3$ fails: between $e'=1.35$ and $e''=2.4$ the low type is worse off than in equilibrium even at the best possible wage, while the high type gains if recognized. Source: Gibbons pp. 239–244 (Figs. 4.4.4–4.4.5); MWG Fig. 13.AA.2 (p. 470); M&R numbers.*

The gap opens because the two equilibrium indifference lines through the pooling point have
different slopes — single crossing again. Any pooling point has such a gap, so **no pooling PBE
survives**, and the only survivor is the separating equilibrium in which the low type is exactly
indifferent to mimicking: **$e_H=(\theta_H-\theta_L)/c_L=1.5$** (Gibbons Fig. 4.4.4: "just enough
education to make the low-ability worker indifferent about mimicking"). The
[Education Signal companion](companions/companion-spence-signaling.html) reports this survivor as
its headline number.

> **Interactive companion.** [The MBA Game](companions/companion-mba-game.html) — the last column
> of its table applies this test to every PBE; drag $c_L$ below $w_M-w_B$ and the pooling PBE
> *survives*, because then $D$ is no longer equilibrium-dominated for the low type.

---

## 6 · G — MWG Appendix 13.AA (pp. 467–471) and forward induction

MWG builds the refinement in four steps (pp. 468–471):

| Eq. | Test on action $a$ for type $\theta$ | What it removes in the education model |
|---|---|---|
| (13.AA.1) | strictly dominated: some $a'$ has $\min_{s'}u_1(a',s',\theta)>\max_{s}u_1(a,s,\theta)$ over **all** responses | — |
| (13.AA.2) | the same, but only over **equilibrium** responses $S^*(\Theta,a)$ | every separating PBE but the best; pooling PBE that H likes less than $(\theta_H,\tilde e)$ |
| (13.AA.3) | **equilibrium dominated**: $u_1^*(\theta)>\max_{s\in S^*(\Theta,a)}u_1(a,s,\theta)$ | also **every** pooling PBE (Fig. 13.AA.2, p. 470) |
| (13.AA.4) | intuitive criterion: some type has $\min_s u_1(a,s,\theta)>u_1^*(\theta)$ once equilibrium-dominated types are excluded | leaves "the best separating equilibrium" |

With **two types** the intuitive criterion and the reasonable-beliefs refinement based on
(13.AA.3) coincide (p. 471); MWG's Example 13.AA.1 (three types) shows a PBE that passes the
intuitive criterion but fails the reasonable-beliefs test — named only. The general idea of
disciplining off-path beliefs by the deviator's rationality is MWG's **forward induction** (§9.D,
p. 292). Cho and Kreps also show every signaling game in this class has a PBE satisfying the
criterion (Gibbons p. 239).

---

## Links

- Prev: [[L08-07-limit-pricing]] · Next: [[L08-09-formulas]].
- The equilibria being refined: [[L08-05-mba-game]], [[L08-06-spence-job-market]],
  [[L08-07-limit-pricing]]; the first refinement: [[L08-03-sequential-equilibrium]].
- Rules: [[../../rules/game-theory|rules/game-theory]] item 3 (state the selection argument) and
  item 18 (do not pick the refinement after seeing the answer).
- Code: `intuitive_fails`, tested on the MBA game, Gibbons Fig. 4.2.2 and Beer–Quiche, in
  [[L08-11-python]] §5.
- Exercises (number and page only): Tadelis 16.7, 16.8 (p. 338); Muñoz-Garcia Ch. 9
  Exercise 9 (p. 447), Ch. 11 Exercise 4 (p. 500); MWG 13.AA.1 (p. 476).
