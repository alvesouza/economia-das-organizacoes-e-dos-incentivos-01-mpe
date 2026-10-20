---
tags: [notes, lecture-06, repeated-games, optimal-punishment, price-wars, imperfect-monitoring, renegotiation]
date: 2026-10-16
status: estimated
source: "Gibbons (1992) §2.3.C, pp. 104–107 (Abreu's two-phase strategy, eqs. (2.3.3)–(2.3.4); Rotemberg–Saloner; Green–Porter) and p. 111 (renegotiation); Tadelis (2013) §10.4, pp. 203–204 (price wars, OPEC); Cabral (2017) §9.1 p. 222 and §9.2 'Price wars', pp. 222–227 (Box 9.2)"
---

# Gibbons 2.3.C, Cabral 9.2 · Sharper sticks, and wars that happen on the path

> **Claim.** Grim trigger is the simplest punishment, not the strongest: a **one-period**
> punishment harsher than Cournot, followed by a return to collusion, sustains the monopoly
> outcome at $\delta=1/2<9/17$ and is easier to defend against renegotiation. And when firms
> see only noisy prices, **price wars are part of the equilibrium**, not evidence of cheating:
> no one deviates, yet bad luck must trigger punishment, or everyone would cheat.
> Prev: [[L06-03-bertrand-market-structure]] · Next: [[L06-05-reputation-trust]] · Map: [[L06-00-map]]

---

## 1 · C — Abreu's carrot and stick (Gibbons pp. 104–106)

**Two-phase strategy.** Produce $q_m/2$ in period 1. In period $t$, produce $q_m/2$ if both
firms produced $q_m/2$ in $t-1$, **or if both produced $x$** in $t-1$; otherwise produce
$x$. So a deviation from either phase triggers **one** period of $x$ (the *stick*); obeying
the stick restores collusion (the *carrot*).

Normalize $a-c=1$. Payoffs per firm:

| Symbol | Meaning | Value |
|---|---|---|
| $\pi_m/2$ | collusive | $1/8$ |
| $\pi_d$ | best deviation from collusion | $9/64$ |
| $\pi(x)$ | both produce $x$ | $(1-2x)x$ |
| $\pi_{dp}(x)$ | best deviation from the punishment: $q_j=(1-x)/2$ | $(1-x)^2/4$ |
| $V(x)$ | punishment now, collusion forever after | $\pi(x)+\dfrac{\delta}{1-\delta}\cdot\dfrac{\pi_m}{2}$ |

**Collusive phase** — prefer collusion forever to deviating and then being punished
(2.3.3):

$$\frac{1}{1-\delta}\cdot\frac{\pi_m}{2}\ \ge\ \pi_d+\delta V(x).$$

Substitute $V(x)$: the right side is
$\pi_d+\delta\pi(x)+\frac{\delta^2}{1-\delta}\frac{\pi_m}{2}$. Subtract
$\frac{\delta^2}{1-\delta}\frac{\pi_m}{2}$ from both sides; the left becomes
$\frac{1-\delta^2}{1-\delta}\frac{\pi_m}{2}=(1+\delta)\frac{\pi_m}{2}$:

$$(1+\delta)\frac{\pi_m}{2}\ge\pi_d+\delta\pi(x)\iff
\boxed{\;\delta\Bigl(\frac{\pi_m}{2}-\pi(x)\Bigr)\ \ge\ \pi_d-\frac{\pi_m}{2}\;}$$

**the gain from deviating today must not exceed the discounted loss from tomorrow's one-period
punishment.**

**Punishment phase** — prefer to administer the punishment than to deviate from it and face
it again (2.3.4):

$$V(x)\ \ge\ \pi_{dp}(x)+\delta V(x).$$

With $V(x)=\pi(x)+\delta\frac{\pi_m/2}{1-\delta}$, multiply out $(1-\delta)V(x)\ge\pi_{dp}(x)$:
$(1-\delta)\pi(x)+\delta\frac{\pi_m}{2}\ge\pi_{dp}(x)$, i.e.

$$\boxed{\;\delta\Bigl(\frac{\pi_m}{2}-\pi(x)\Bigr)\ \ge\ \pi_{dp}(x)-\pi(x)\;}$$

### 1.1 · Worked — $\delta=1/2$ (Gibbons p. 106)

**(2.3.3):** $\tfrac12\bigl(\tfrac18-x+2x^2\bigr)\ge\tfrac{9}{64}-\tfrac{8}{64}=\tfrac1{64}$.
Multiply by 2: $2x^2-x+\tfrac18\ge\tfrac1{32}$, i.e. $2x^2-x+\tfrac{3}{32}\ge0$. Roots
$x=\frac{1\pm\sqrt{1-3/4}}{4}=\frac{1\pm\frac12}{4}$: $\tfrac18$ and $\tfrac38$. Holds for
$x\le\tfrac18$ or $x\ge\tfrac38$ — "$x/(a-c)$ is not between 1/8 and 3/8".

**(2.3.4):** left side $\tfrac1{16}-\tfrac x2+x^2$; right side
$\tfrac{(1-x)^2}{4}-x+2x^2=\tfrac14-\tfrac32x+\tfrac94x^2$. The inequality becomes
$0\ge\tfrac3{16}-x+\tfrac54x^2$; roots $x=\frac{1\pm\sqrt{1-15/16}}{5/2}=\frac{1\pm\frac14}{2.5}$:
$\tfrac{3}{10}$ and $\tfrac12$. Holds for $\tfrac3{10}\le x\le\tfrac12$.

$$\text{Both:}\qquad \boxed{\;\tfrac38\le\frac{x}{a-c}\le\tfrac12\;}$$

![Slack of (2.3.3) and (2.3.4) against x/(a-c) at delta 1/2: (2.3.3) is non-negative outside (1/8, 3/8), (2.3.4) is non-negative on [3/10, 1/2]; the shaded band where both hold is [3/8, 1/2]](figures/L06-carrot-stick.png)
*Figure — each curve is $\delta(\pi_m/2-\pi(x))$ minus the right side of its constraint; the
band is the set of punishments that work. Source: Gibbons pp. 105–106, $\delta=1/2$.*

**Read the band.** The stick must be **harsh enough** ($x\ge3/8$, so the punishment profit
$\pi(3/8)=\tfrac14\cdot\tfrac38=\tfrac3{32}=0.094$ is below even Cournot's $1/9=0.111$) to deter
the collusive-phase deviation, and **not so harsh** that the firms themselves refuse to carry
it out ($x\le1/2$: at $x=1/2$ total output is $a-c$, price equals $c$, profit zero). Since
$1/2<9/17$, **the two-phase strategy reaches the monopoly outcome where grim trigger
cannot** ([[L06-02-cournot-collusion]] §3).

> **Why it beats grim trigger.** Grim trigger's stick is Cournot **forever** — long but mild.
> Abreu's is a price war **for one period** — short but severe — and it is self-enforcing
> because obeying it is the ticket back to collusion. Severity per period, not duration, is
> what deters.

---

## 2 · C — renegotiation: is "forever" credible?

Gibbons (p. 111, for the efficiency-wage version) and Cabral (p. 222, his third reason) raise
the same objection. After a deviation, grim trigger prescribes the stage Nash equilibrium
forever. But **both** firms then prefer to return to collusion — so the deviator can propose
"let bygones be bygones", and if both expect that, the punishment never happens and the
deviation pays. The subgame-perfect equilibrium survives on paper; the **threat** does not
survive negotiation.

| Punishment | Hurts the punisher? | Renegotiation pressure |
|---|---|---|
| Grim trigger (stage Nash forever) | yes, forever | strong — both gain by restarting |
| Two-phase (one period of $x$, then collusion) | yes, for one period | weaker — collusion returns anyway after one period |

*G.* The formal notion is renegotiation-proofness (introduced in Gibbons §2.3.A); it is named
here, not examinable.

---

## 3 · C — imperfect monitoring: price wars on the equilibrium path

**The puzzle** (Tadelis p. 203). Under perfect monitoring a sustainable cartel never fights:
punishment is off-path. Yet cartels have price wars.

**The resolution** (Tadelis pp. 203–204; Gibbons pp. 106–107; Cabral pp. 223–224). Firms do
not see rivals' quantities or secret discounts; they see the **market price** (or their own
sales), which also moves with demand. A low price is then a **noisy signal**: a rival cut, or
demand fell. Each firm is tempted to cheat and plead *"I didn't deviate; demand must have been
low!"* (Tadelis p. 203).

Cabral walks through the three candidate policies (p. 223):

| Policy after low demand | Outcome |
|---|---|
| **Never punish** (assume it was demand) | not an equilibrium: each firm secretly cuts and blames the market |
| **Infinite price war** | deters cheating, but sooner or later a downturn triggers permanent war with nobody cheating |
| **Price war for $T$ periods, then back to collusion** | with $\delta$ close enough to 1, some $T$ deters cheating: **collusion and wars alternate, and no one ever cheats** |

> **"If price cuts are difficult to observe, then occasional price wars may be necessary to
> discipline collusive agreements"** (Cabral p. 224). Wars are the price of incentive
> compatibility under noise — a "necessary evil" — not a breakdown.

Gibbons's version: Green and Porter (1984) *trigger-price* equilibria — any price below a
critical level starts a Cournot phase; in equilibrium no firm deviates, yet an especially bad
shock triggers punishment; because punishments happen by accident, **finite** punishments beat
infinite ones, and Abreu–Pearce–Stacchetti (1986) show two-phase strategies can be optimal
(p. 107).

**Box 9.2 — the Joint Executive Committee, 1880–1886** (Cabral p. 224). A legal railroad
cartel on eastbound Chicago–Atlantic freight. Several times it thought cheating had occurred,
cut prices for a while and returned to the collusive rate; the wars were caused by
**unpredictable disturbances**, not by entry or by the predictable lake-navigation season.

*G.* Repeated games with imperfect monitoring are "extremely technical and beyond the scope"
of Tadelis (p. 204; Mailath and Samuelson 2006). Named, not examinable; the drill is
Muñoz-Garcia Ch. 6 Ex. 10 (p. 310) and Cabral Exercise 9.19 (p. 245).

---

## 4 · C — observable demand shocks: wars in booms (Rotemberg–Saloner)

If demand varies but **everyone sees** the current shock before pricing (Gibbons p. 106;
Cabral p. 225), deviations are detectable, yet the temptation varies: the gain from
undercutting is proportional to **current** demand, while the future loss (with i.i.d.
shocks) is the same in every state. The no-deviation constraint binds in **high-demand**
periods, so the cartel must **lower its price in booms** to keep members loyal.

| | Green–Porter (unobserved shocks) | Rotemberg–Saloner (observed shocks) |
|---|---|---|
| when wars/low prices come | **after** low demand | **during** high demand |
| price over the cycle | pro-cyclical | **counter-cyclical** |
| Cabral's evidence | JEC railroads, 1880–1886 | cement 1947–1981: +1% GDP, relative price −0.5% to −1% (p. 225) |

---

## 5 · U — a firm whose $\delta$ falls starts the war (Cabral pp. 225–227)

A firm in financial trouble attaches a higher probability to exiting — a higher hazard $h$ in
(9.5), so a lower $\delta$. If its $\delta$ drops below its cutoff, it deviates and a price war
follows: "Fares are dictated not by the strongest, but by the financially troubled" (airline
executive, p. 226). Wars can also be started by the **strong**: the *Times* cut its price
from 45 to 30 pence in July 1993 and to 20 pence ten months later; Google cut cloud prices by
30–85% in March 2014 (pp. 226–227).

---

## Links

- Previous: [[L06-03-bertrand-market-structure]]. Next: [[L06-05-reputation-trust]].
- Template and one-stage deviation: [[L06-01-recap-grim-trigger]]; renegotiation in the
  employment relation: [[L06-07-efficiency-wages]] §5.
- Code: [[L06-11-python]] §5. Pitfalls: [[L06-10-pitfalls]] items 5–6.
- Exercises: Muñoz-Garcia Ch. 6 Ex. 3 (temporary punishments, p. 282), Ex. 10 (imperfect
  monitoring, p. 310); Cabral 9.19 (p. 245) and 9.20 (p. 246).
