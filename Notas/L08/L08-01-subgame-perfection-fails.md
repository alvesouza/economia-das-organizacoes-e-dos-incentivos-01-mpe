---
tags: [notes, lecture-08, pbe, subgame-perfection, entry-game, incomplete-information]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §15.1 'The Problem with Subgame Perfection', pp. 303–307 (Fig. 15.1, Fig. 15.2, the matrix at p = 1/2 on p. 306, footnote 1); Gibbons (1992) §4.1, pp. 175–177 (Fig. 4.1.1–4.1.2)"
---

# 15.1 · Why subgame perfection has no bite once types are private

> **Claim.** Subgame perfection removes non-credible threats by asking for a Nash equilibrium in
> every *proper subgame*. Add one move by Nature that the second mover cannot see, and the
> second mover's decision nodes are tied together in one information set: **the only proper
> subgame is the whole game**, so subgame perfection collapses into Bayesian Nash equilibrium
> and the incredible threat survives. Sequential rationality has to be imposed **at information
> sets**, which needs beliefs — the next note.
>
> Prev: — · Next: [[L08-02-beliefs-and-pbe]] · Map: [[L08-00-map]]

---

## 1 · U — the benchmark: entry with complete information (Fig. 15.1, pp. 303–304)

An entrant (player 1) chooses Out ($O$) or Enter ($E$); after entry the incumbent (player 2)
chooses Fight ($F$) or Accommodate ($A$). Payoffs (entrant, incumbent): $O\to(0,2)$;
$(E,F)\to(-1,-1)$; $(E,A)\to(1,1)$.

| | $F$ | $A$ |
|---|---|---|
| $O$ | $0,\ 2$ | $0,\ 2$ |
| $E$ | $-1,\ -1$ | $1,\ 1$ |

**Nash equilibria.** $(O,F)$: given $F$, $O$ (0) beats $E$ ($-1$); given $O$, the incumbent is
indifferent (2 = 2), so $F$ is a best response. $(E,A)$: given $A$, $E$ (1) beats $O$ (0); given
$E$, $A$ (1) beats $F$ ($-1$). Two pure equilibria.

**Backward induction** ([[../L03/L03-00-map|Lecture 3]]): after $E$ the incumbent compares
$1>-1$ and accommodates; anticipating this the entrant compares $1>0$ and enters. **Unique SPE
$(E,A)$**; $(O,F)$ rests on a threat the incumbent would never carry out.

---

## 2 · C — add a type: the entry game with incomplete information (Fig. 15.2, pp. 304–305)

Timing (p. 304):

1. Nature draws the entrant's type $\theta_1\in\{W,C\}$ (weak, competitive), $\Pr\{\theta_1=C\}=p$.
   The entrant learns it; the incumbent knows only $p$.
2. The entrant chooses $E$ or $O$; the incumbent observes the choice.
3. After entry the incumbent chooses $A$ or $F$ **without knowing the type**.

Payoffs (entrant, incumbent):

| Type | $O$ | $E$ then $F$ | $E$ then $A$ |
|---|---|---|---|
| $C$ (prob. $p$) | $0,\ 2$ | $-1,\ -1$ | $1,\ 1$ |
| $W$ (prob. $1-p$) | $0,\ 2$ | $-2,\ 0$ | $-1,\ 1$ |

![Left: game tree with Nature choosing C with probability p or W with 1-p; each entrant type chooses O (payoff 0,2) or E; after E the incumbent's two nodes x3 and x4 are joined by a dashed information set; payoffs after F and A are (-1,-1), (1,1) for C and (-2,0), (-1,1) for W; the path C-E-A and W-O is highlighted. Right: the incumbent's expected payoff after entry against the belief mu(x3), flat at 1 for A and falling from 0 to -1 for F](figures/L08-entry-game.png)
*Figure — the entry game of Fig. 15.2 with the separating equilibrium $(EO,A)$ highlighted (left), and the incumbent's expected payoff after entry as a function of its belief (right): $A$ beats $F$ by at least 1 at every belief. Source: Tadelis Fig. 15.2, p. 305, and the argument on p. 310.*

The dashed line is the whole difficulty: after $E$ the incumbent does not know which of $x_3$ (a
competitive entrant) or $x_4$ (a weak one) it is at. On the right, however, the belief does not
matter: $A$ pays 1 against either type while $F$ pays $-1$ or $0$, so *every* belief makes $A$ the
best reply — which is exactly why the threat to fight is not credible (note 02, §5).

### 2.1 · Strategies are type-contingent

A strategy for the entrant is a plan for **each** type: $s_1=s_1^Cs_1^W$ with
$s_1^\theta\in\{O,E\}$, so

$$S_1=\{OO,\ OE,\ EO,\ EE\},\qquad S_2=\{F,A\}$$

($OE$ = "out if competitive, enter if weak"). The incumbent has one information set (after $E$)
with two actions.

### 2.2 · The Bayesian normal form, cell by cell (p. 305)

Each cell averages over Nature. **$(OE,A)$:** with prob. $p$ the type is $C$, plays $O$, payoffs
$(0,2)$; with prob. $1-p$ the type is $W$, plays $E$, the incumbent plays $A$, payoffs $(-1,1)$:

$$Ev_1=p\cdot0+(1-p)(-1)=p-1,\qquad Ev_2=p\cdot2+(1-p)\cdot1=1+p .$$

*(The book prints $Ev_2=1-p$ on p. 305; at $p=1/2$ its own matrix shows $3/2=1+p$, which is the
correct value.)*

**$(EE,F)$:** both types enter and are fought: $Ev_1=p(-1)+(1-p)(-2)=p-2$,
$Ev_2=p(-1)+(1-p)\cdot0=-p$.

At $p=\tfrac12$ (p. 306):

| | $F$ | $A$ |
|---|---|---|
| $OO$ | $0,\ 2$ | $0,\ 2$ |
| $OE$ | $-1,\ 1$ | $-\tfrac12,\ \tfrac32$ |
| $EO$ | $-\tfrac12,\ \tfrac12$ | $\tfrac12,\ \tfrac32$ |
| $EE$ | $-\tfrac32,\ -\tfrac12$ | $0,\ 1$ |

Check two cells. $(EO,F)$: $C$ enters and is fought, $W$ stays out:
$v_1=\tfrac12(-1)+\tfrac12(0)=-\tfrac12$, $v_2=\tfrac12(-1)+\tfrac12(2)=\tfrac12$. $(EE,A)$:
$v_1=\tfrac12(1)+\tfrac12(-1)=0$, $v_2=\tfrac12(1)+\tfrac12(1)=1$.

### 2.3 · The pure Bayesian Nash equilibria

Best responses of player 1: against $F$ the column is $(0,-1,-\tfrac12,-\tfrac32)$, maximum $0$ at
$OO$; against $A$ it is $(0,-\tfrac12,\tfrac12,0)$, maximum at $EO$. Best responses of player 2:
row $OO$ — tie ($2=2$), both; $OE$ — $A$ ($\tfrac32>1$); $EO$ — $A$ ($\tfrac32>\tfrac12$);
$EE$ — $A$ ($1>-\tfrac12$). Mutual best responses:

$$\boxed{\;(OO,F)\quad\text{and}\quad(EO,A)\;}\qquad\text{(p. 306)}$$

> **The two BNE mirror the two NE of the complete-information game**: $(OO,F)$ is the threat that
> keeps everyone out; $(EO,A)$ is accommodation, under which the competitive type enters (1 > 0)
> and the weak type stays out (0 > $-1$).

Footnote 1 (p. 306): $OE$ is strictly dominated by $OO$ and $EE$ by $EO$ (the weak type always
loses by entering: $-2$ or $-1$ against $0$). There is also a continuum of mixed BNE in which the
incumbent fights with probability $\varphi\ge\tfrac12$ and the entrant plays $OO$: the competitive
type then gets $\varphi(-1)+(1-\varphi)(1)=1-2\varphi\le0$ from entering, so staying out is a
best response exactly when $\varphi\ge\tfrac12$.

---

## 3 · C — why subgame perfection cannot remove $(OO,F)$ (p. 306)

$(OO,F)$ has the same flaw as $(O,F)$: **if the incumbent finds itself after entry, $A$ is a strict
best response** (§2's figure, right panel). Yet:

> **Subgame-perfect equilibrium requires a Nash equilibrium in every *proper* subgame. A proper
> subgame must start at a singleton information set and cut no information set. The incumbent's
> nodes $x_3,x_4$ form one information set, and the entrant's nodes hang from Nature's move, so
> the only proper subgame is the whole game** — and both BNE survive as SPE.

| Concept | Removes $(OO,F)$? | Why |
|---|---|---|
| Nash / Bayesian Nash | no | $F$ is never *played* on the path, so it costs the incumbent nothing |
| Subgame-perfect | **no** | no proper subgame begins after entry |
| Perfect Bayesian (note 02) | **yes** | it asks for a best reply **at the information set**, given a belief |

The structural point (p. 307): with incomplete information, **every** move of the uninformed
player is made inside an information set that pools the informed player's types, so this
failure "will carry over to all games of incomplete information."

---

## 4 · U — the same failure without Nature (Gibbons Fig. 4.1.1, pp. 175–177)

The problem is not Nature as such; it is **non-singleton information sets**. Gibbons's game:
player 1 chooses $L$, $M$ or $R$; $R$ ends the game at $(1,3)$; after $L$ or $M$ player 2 knows
only that $R$ was not chosen and picks $L'$ or $R'$. Normal form (Fig. 4.1.2):

| | $L'$ | $R'$ |
|---|---|---|
| $L$ | $2,\ 1$ | $0,\ 0$ |
| $M$ | $0,\ 2$ | $0,\ 1$ |
| $R$ | $1,\ 3$ | $1,\ 3$ |

Pure NE: $(L,L')$ and $(R,R')$. The game has **no proper subgames**, so both are subgame perfect.
But give player 2 a belief $p$ = Pr(node after $L$):

$$E[u_2(R')]=p\cdot0+(1-p)\cdot1=1-p,\qquad E[u_2(L')]=p\cdot1+(1-p)\cdot2=2-p .$$

$2-p>1-p$ for **every** $p$: $R'$ is never a best reply at the information set, so $(R,R')$ is
killed by Gibbons's Requirements 1–2 alone (p. 177). The same move — *a belief at every
information set, and optimality given it* — is what note 02 formalizes.

---

## Links

- Next: beliefs, Bayes' rule and the definition of PBE → [[L08-02-beliefs-and-pbe]].
- Backward induction and subgame perfection: [[../L03/L03-00-map|Lecture 3]].
- Bayesian games, type-contingent strategies and BNE: [[../L07/L07-00-map|Lecture 7]].
- Rules: [[../../rules/game-theory|rules/game-theory]] items 2–3 (name the concept; check
  multiplicity).
- Exercises (number and page only): Tadelis 15.1 (p. 314); Gibbons Problem 4.1 (p. 245);
  Muñoz-Garcia Ch. 9 Exercise 1 (p. 376).
