---
tags: [notes, lecture-08, signaling, limit-pricing, entry-deterrence, milgrom-roberts, separating, pooling]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §16.2 'Limit Pricing and Entry Deterrence', pp. 323–332 (§16.2.1 Separating Equilibria, Steps 1–5, Claims 16.1–16.2, footnote 4; §16.2.2 Pooling Equilibria, (IC_H), (IC_L), footnote 5)"
---

# 16.2 · Limit pricing: an incumbent over-produces to prove it is cheap

> **Claim.** Bain's limit pricing — charge a low price now to keep entrants out — survives a formal
> model (Milgrom–Roberts 1982, simplified by Tadelis) **as a signal**: a low-cost incumbent produces
> **more than its monopoly output** in period 1 so that a high-cost incumbent would not find it
> worth copying. Separating PBE need $q_1^L\in[2.62,\,3.32]$ (monopoly output is 2); pooling PBE
> need $q_1\in[1.49,\,1.92]$. Both are continua — until the intuitive criterion (note 08) leaves
> only $q_1^L=2.62$.
>
> Prev: [[L08-06-spence-job-market]] · Next: [[L08-08-intuitive-criterion]] · Map: [[L08-00-map]]

---

## 1 · C — the game (pp. 323–324)

Two periods, inverse demand $P=5-q$ each period. The incumbent (firm 1) has marginal cost
$c_1\in\{1,2\}$ — **L**ow or **H**igh — each with probability $\tfrac12$, known only to itself. The
entrant (firm 2) has $c_2=2$ and a fixed entry cost $F=\tfrac12$.

1. Nature draws $c_1$.
2. Firm 1 produces $q_1^1$ as a monopolist; price $5-q_1^1$.
3. Firm 2 observes $q_1^1$ (not $c_1$) and enters or not.
4. No entry: firm 1 is a monopolist again in period 2. Entry: Cournot duopoly, $P=5-q_1^2-q_2^2$.

Notation: $q_1^{t\theta}$ is type $\theta$'s output in period $t$; $\mu(q_1^1)=\Pr\{c_1=2\mid q_1^1\}$ is the
entrant's belief **that the incumbent is high-cost**; "no entry" is coded $q_2^2=0$ (footnote 3).
No discounting.

---

## 2 · C — the building blocks (Steps 1–2, pp. 324–325)

**Step 1 — monopoly.** $\max_q(5-q-c_1)q$: FOC $5-2q-c_1=0\Rightarrow q=\dfrac{5-c_1}{2}$.

| Type | Monopoly $q$ | Price | Monopoly profit |
|---|---|---|---|
| L ($c_1=1$) | 2 | 3 | $(3-1)\cdot2=4$ |
| H ($c_1=2$) | 1.5 | 3.5 | $(3.5-2)\cdot1.5=2.25$ |

**Step 2 — Cournot with known cost.** FOCs $5-2q_1-q_2-c_1=0$ and $5-q_1-2q_2-2=0$ give
$BR_1(q_2)=\dfrac{5-q_2-c_1}{2}$ and $BR_2(q_1)=\dfrac{3-q_1}{2}$.

- **Known H** ($c_1=2$): $q_1=\dfrac{3-q_2}{2}$, $q_2=\dfrac{3-q_1}{2}$ ⇒ $q_1=q_2=1$, $P=3$;
  $v_1=(3-2)\cdot1=1$, $v_2=(3-2)\cdot1-\tfrac12=\tfrac12>0$ — **entry pays**.
- **Known L** ($c_1=1$): $q_1=\dfrac{4-q_2}{2}$, $q_2=\dfrac{3-q_1}{2}$ ⇒ substitute:
  $q_1=\dfrac{4-(3-q_1)/2}{2}\Rightarrow 4q_1=8-3+q_1\Rightarrow q_1=\tfrac53$, $q_2=\tfrac23$,
  $P=\tfrac83$; $v_1=(\tfrac83-1)\tfrac53=\tfrac{25}{9}$, $v_2=(\tfrac83-2)\tfrac23-\tfrac12=\tfrac49-\tfrac12=-\tfrac1{18}<0$ —
  **entry does not pay**.

> **The entrant wants in only against the high-cost type.** So a low-cost incumbent wants to be
> *recognized*, and a high-cost incumbent wants to be *mistaken* for low cost.

---

## 3 · C — separating equilibria (§16.2.1, pp. 325–330)

**Claim 16.1.** In any separating PBE, after the L type's output the entrant believes $c_1=1$,
stays out, and L produces $q_1^{2L}=2$; after the H type's output it believes $c_1=2$, enters, and
both produce $q_1^{2H}=q_2^2=1$.

**Claim 16.2.** In any separating PBE, $q_1^{1H}=1.5$ (H's monopoly output). *Proof:* H is going to
face entry and Cournot profit 1 anyway. If it produced anything but 1.5 in period 1, switching to
1.5 would raise period-1 profit and could not lower period-2 profit — after the switch the entrant
either keeps believing $c_1=2$ (same Cournot game) or believes less, which only helps firm 1. ∎

**Step 4 — off-path beliefs.** Make every deviation as unattractive as possible: believe **high
cost** after any output other than $q_1^{1L}$ —
$\mu(q_1^1)=0$ if $q_1^1=q_1^{1L}$, and $1$ otherwise — so the entrant enters (with $q_2^2=1$) after
anything but $q_1^{1L}$.

**Step 5 — what can $q_1^{1L}$ be?** Two incentive-compatibility constraints.

**First try: L's monopoly output, $q_1^{1L}=2$.** H's equilibrium payoff: $2.25+1=3.25$. H mimicking
2: period 1 $(5-2-2)\cdot2=2$, then no entry and monopoly $2.25$:

$$2+2.25=4.25>3.25\qquad\text{(p. 328) — H mimics, so } q_1^{1L}=2\text{ is not separating.}$$

The sacrifice in period 1 (2.25 → 2) is small next to the gain in period 2 (1 → 2.25).

**IC of H (H must not mimic)** — lower bound on $q_1^{1L}$:

$$(5-q-2)q+2.25\ \le\ 3.25\iff(3-q)q\le1\iff q^2-3q+1\ge0\iff q\ \ge\ \frac{3+\sqrt5}{2}=2.618 .$$

(The other branch, $q\le\tfrac{3-\sqrt5}{2}=0.382$, also stops H from mimicking, but it violates
L's own constraint below, which needs $q\ge0.677$.)

**IC of L (L must not deviate)** — upper bound. Any deviation triggers entry with $q_2^2=1$; L's best
deviation is its monopoly output 2 (profit 4) followed by the best reply to $q_2^2=1$:
$\max_q(5-q-1-1)q$, at $q=1.5$, profit 2.25. Best deviation total: $4+2.25=6.25$. So

$$(5-q-1)q+4\ \ge\ 6.25\iff(4-q)q\ge2.25\iff q^2-4q+2.25\le0\iff q\in\Bigl[2-\sqrt{1.75},\ 2+\sqrt{1.75}\Bigr]=[0.677,\ 3.323].$$

> **Conclusion (p. 329).** A continuum of separating PBE: $q_1^{1H}=1.5$, $q_1^{2L}=2$, $q_1^{2H}=1$,
> beliefs and entry as in Step 4, and
> $$\boxed{\;2.62\ \le\ q_1^{1L}\ \le\ 3.32\;}$$

![Two panels of two-period profit against first-period output q. Left: H's profit from producing q and deterring entry, (3-q)q + 2.25, peaks at 4.5 and falls below H's best entry payoff 3.25 at q = 2.618; L's profit (4-q)q + 4 stays above its best deviation 6.25 up to q = 3.323; the band [2.62, 3.32] is shaded as the separating set. Right: the same with Bayesian-Cournot continuation profits (13/12)^2 and (19/12)^2; H stays above 3.25 on [1.083, 1.917] and L above 6.25 on [1.493, 2.507]; their intersection [1.49, 1.92] is shaded as the pooling set](figures/L08-limit-pricing.png)
*Figure — every incentive constraint of §16.2 as a parabola against a flat line: separating needs H's mimicking payoff below 3.25 and L's payoff above 6.25 (left); pooling needs both types above their best deviation (right). Source: Tadelis pp. 327–332; all functions exact.*

Read the left panel from the right edge leftward: L would happily produce as much as 3.32 to be
believed, but H would mimic anything below 2.62 — the band in between is the separating set. The
right panel's band is narrower because both types must stay put at the *same* output.

> **The signal is credible because it is expensive for the type that would fake it** (p. 329):
> "for a signal to be credible, it must be the case that no other type would want to use the
> signal." Here L's price ($5-2.62=2.38$) is still above its marginal cost 1; with a growing market
> or more periods of deterrence the required output rises until the price falls **below** marginal
> cost — Bain's predatory limit pricing (pp. 329–330). Discounting the second period can change
> the first-try verdict (footnote 4; Tadelis Exercise 16.2, p. 335).

---

## 4 · C — pooling equilibria (§16.2.2, pp. 330–332)

Both types produce the same $\bar q_1$, so the entrant learns nothing: $\mu(\bar q_1)=\tfrac12$. If it
enters, period 2 is a **Cournot game with incomplete information**
([[../L07/L07-00-map|Lecture 7]]). Three best replies:

$$q_1^{2L}=\frac{4-q_2^2}{2},\qquad q_1^{2H}=\frac{3-q_2^2}{2},\qquad
q_2^2=\frac{3-\tfrac12(q_1^{2L}+q_1^{2H})}{2}.$$

Solve: $q_1^{2L}+q_1^{2H}=\dfrac{7-2q_2^2}{2}$, so
$q_2^2=\dfrac{3-\tfrac{7-2q_2^2}{4}}{2}\Rightarrow 8q_2^2=12-7+2q_2^2\Rightarrow q_2^2=\tfrac56$; then
$q_1^{2L}=\dfrac{4-5/6}{2}=\tfrac{19}{12}$ and $q_1^{2H}=\dfrac{3-5/6}{2}=\tfrac{13}{12}$.

Profits: H $=(5-\tfrac{13}{12}-\tfrac56-2)\tfrac{13}{12}=(\tfrac{13}{12})^2=1.174$; L $=(\tfrac{19}{12})^2=2.507$;
entrant $=\tfrac56\bigl(3-\tfrac56-\tfrac{16}{12}\bigr)-\tfrac12=\tfrac56\cdot\tfrac56-\tfrac12=\tfrac{25}{36}-\tfrac{18}{36}=\tfrac{7}{36}>0$.
*(The book prints $\tfrac{7}{18}$ on p. 331; the arithmetic gives $\tfrac7{36}$. Either way it is positive,
so the entrant enters after the pooled output.)*

Off the path: believe **high cost** (μ = 1) after any $q_1^1\ne\bar q_1$, so deviations meet entry
with $q_2^2=1$; best deviations are worth 3.25 (H) and 6.25 (L), as before.

**IC of H:** $(3-\bar q)\bar q+\bigl(\tfrac{13}{12}\bigr)^2\ge3.25\iff\bar q^2-3\bar q+\tfrac{299}{144}\le0$.
Discriminant $9-\tfrac{1196}{144}=\tfrac{100}{144}$, root $\tfrac{10}{12}$:
$\bar q\in\bigl[\tfrac{3-5/6}{2},\tfrac{3+5/6}{2}\bigr]=[1.083,\ 1.917]$. (ICH)

**IC of L:** $(4-\bar q)\bar q+\bigl(\tfrac{19}{12}\bigr)^2\ge6.25\iff\bar q^2-4\bar q+\tfrac{539}{144}\le0$.
Discriminant $16-\tfrac{2156}{144}=\tfrac{148}{144}$, root $\tfrac{\sqrt{148}}{12}=1.014$:
$\bar q\in[1.493,\ 2.507]$. (ICL)

> **Conclusion (p. 332).** A continuum of pooling PBE: $q_1^{2L}=\tfrac{19}{12}$, $q_1^{2H}=\tfrac{13}{12}$,
> $q_2^2=\tfrac56$ after $\bar q_1$ and 1 otherwise, beliefs $\tfrac12$ on the path and 1 off it, and
> $$\boxed{\;1.493\ \le\ \bar q_1\ \le\ 1.917\;}$$

Footnote 5 (p. 332): each interval is **symmetric around that type's monopoly output** (1.5 for H,
2 for L), because each type's best deviation is its monopoly output.

Pooling deters nothing — the entrant enters anyway — so in pooling the "limit price" buys nothing;
Tadelis calls pooling "somewhat artificial" (p. 332), and §16.3 makes that precise.

---

## 5 · U — political incumbents (p. 332)

Epstein and Zemsky (1995): strong incumbents raise large campaign war chests as a **signal of
strength** to deter challengers — the same entry-deterrence logic with money instead of output.

---

## Links

- Prev: [[L08-06-spence-job-market]] · Next: [[L08-08-intuitive-criterion]] (§3: why only
  $q_1^{1L}=2.62$ survives).
- Cournot best replies and the Bayesian Cournot game: [[../L02/L02-00-map|Lecture 2]],
  [[../L07/L07-00-map|Lecture 7]].
- Entry deterrence by commitment rather than information: [[../L03/L03-00-map|Lecture 3]];
  project practice `Listas/pratica-aula-01-02.md` item 18 (M&R FFT 5.2, p. 164).
- Code: every number of this note, asserted, in [[L08-11-python]] §7.
- Exercises (number and page only): Tadelis 16.1, 16.2, 16.3 (p. 335), 16.7 (p. 338);
  Muñoz-Garcia Ch. 9 Exercise 6 (p. 432); Ch. 11 Exercises 5 (p. 506) and 6 (p. 510).
