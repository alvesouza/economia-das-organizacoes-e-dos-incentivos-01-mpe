---
tags: [notes, lecture-03, subgame, subgame-perfect-equilibrium, imperfect-information, mutually-assured-destruction]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) §8.2 (pp. 153–158): Definitions 8.2–8.3, Figs. 8.2–8.7 (voluntary Battle of the Sexes, card game), the Fact on p. 158; §8.3.3 (pp. 163–166): mutually assured destruction, Figs. 8.11–8.12; Gibbons (1992) §2.2.A (pp. 71–73), §2.4.B (pp. 122–129); MWG §9.B (pp. 268–281): Definitions 9.B.1–9.B.2, Propositions 9.B.2–9.B.3"
---

# 8.2–8.3.3 · Subgame-perfect equilibrium: backward induction for any tree

> **Claim.** Backward induction stalls at a non-singleton information set, because the mover's best
> action depends on a belief the procedure does not supply. The fix is to cut the tree only where it
> can be cut cleanly, at **proper subgames**, and to require a **Nash equilibrium in every one of them**.
> That is subgame perfection (Selten). It refines Nash, coincides with backward induction under perfect
> information, and **can still leave several equilibria when a subgame has several equilibria of its
> own**, as mutually assured destruction shows.
> Prev: [[L03-04-sequential-rationality-backward-induction]] · Next: [[L03-06-credibility-entry-commitment]] · Map: [[L03-00-map]]

---

## 1 · U — where backward induction gets stuck (Fig. 8.2, p. 154)

**The voluntary Battle of the Sexes.** Player 1 chooses $N$ (both get 1.5) or $Y$; after $Y$ the two
play the *simultaneous* Battle of the Sexes. Player 2's two nodes sit in one information set. To start
backward induction we would need player 2's best action at that set, and it depends on whether she
thinks player 1 chose $O$ or $F$: a belief, which backward induction does not provide (p. 154).

The second obstacle is games with no last node (infinite horizons, Chs. 10–11), which have no terminal
nodes to start from. Subgame perfection handles both.

---

## 2 · C — proper subgames (Definition 8.2, pp. 154–155)

> **Definition 8.2.** A proper subgame $G$ of an extensive-form game $\Gamma$ consists of **a single
> node and all its successors** in $\Gamma$, with the property that **if $x\in G$ and $x'\in h(x)$ then
> $x'\in G$**. The subgame is itself a game tree, with information sets and payoffs inherited from
> $\Gamma$.

Two tests for "can a subgame start at node $x$?":

1. **$x$ is a singleton information set** (otherwise the subgame would have no unique root);
2. **no information set straddles the cut**: every information set that contains a successor of $x$
   lies entirely among the successors of $x$.

| Game | Candidate roots | Proper subgames | Why |
|---|---|---|---|
| Perfect information (Fig. 8.3, p. 155) | every decision node | **one per decision node** | all information sets are singletons |
| Simultaneous BoS | root only | **the whole game** | player 2's nodes share an information set |
| Voluntary BoS (Fig. 8.4) | $x_0$, $x_1$; not $x_2,x_3$ | **two**: the whole game and the one at $x_1$ | $x_2,x_3$ are in one set, so neither can be a root (p. 156) |
| Card game (Fig. 8.5, p. 156) | $x_1$, $x_2$ fail test 2 | **the whole game only** | the subgame at $x_1$ would contain $x_3$ and so, by the definition, $x_4\in h(x_3)$, which $x_1$ does not precede |
| MAD (Fig. 8.11) | root, player 2's node, player 1's war-stage node | **three** | the war stage is simultaneous but starts at a singleton (p. 165) |

Gibbons's Definition (pp. 122–123) adds a parenthetical that the whole game is *not* counted as a
subgame; he notes this is "only a matter of style". Tadelis and MWG (Definition 9.B.1) count the whole
game as a subgame. These notes follow Tadelis.

> **Why the second test.** Within a subgame, a player's best response should depend only on what
> others do inside it (p. 156). Gibbons's reason (pp. 123–124): test 2 guarantees that the history up
> to $x$ is **common knowledge** among everyone who moves later in the subgame, so the subgame can be
> analysed on its own and the analysis is relevant to the original game.

---

## 3 · C — the equilibrium (Definition 8.3, p. 157)

> **Definition 8.3 (Selten 1975).** Let $\Gamma$ be an $n$-player extensive-form game. A behavioral
> strategy profile $\sigma^*=(\sigma_1^*,\dots,\sigma_n^*)$ is a **subgame-perfect (Nash) equilibrium**
> if for every proper subgame $G$ of $\Gamma$ the restriction of $\sigma^*$ to $G$ is a Nash equilibrium
> in $G$.

Consequences, each one line:

| Statement | Why |
|---|---|
| Every SPE is a Nash equilibrium | the whole game is a proper subgame |
| Not every Nash equilibrium is an SPE | e.g. $(F,ff)$, $(O,oo)$ in the sequential BoS (p. 157) |
| If the only proper subgame is the whole game, SPE = NE | nothing else to check (MWG Exercise 9.B.2(a)); the card game and every simultaneous game |
| **Fact** (p. 158): in finite games of perfect information, **SPE = the profiles that survive backward induction** | every node roots a subgame, and a Nash equilibrium of a one-mover subgame is that mover's best action |
| At least one SPE exists in finite games (Summary, p. 169) | Gibbons p. 124: each finite subgame has a Nash equilibrium (Nash's theorem), and the reduction below builds one |

> **Subgame perfection requires best responses off the equilibrium path as well as on it**: the
> restriction must be a Nash equilibrium "in every proper subgame, including those that are not reached
> in equilibrium" (p. 157).

**Sequential BoS** (p. 157–158): the subgames at $x_1$ and $x_2$ have one player each, so their only
Nash equilibria are $o$ at $x_1$ and $f$ at $x_2$. Of $\{(O,oo),(O,of),(F,ff)\}$ only **$(O,of)$** has
those restrictions.

---

## 4 · C — the method: solve the last subgames, replace, repeat

Gibbons's footnote 20 (p. 124) and MWG Proposition 9.B.3 give the procedure:

1. Find the **smallest** subgames (those containing no other subgame).
2. Find a Nash equilibrium of each, pure or mixed.
3. **Replace** each such subgame by a terminal node carrying that equilibrium's payoffs.
4. Repeat on the reduced game until the root.
5. If a subgame has several equilibria, **branch**: run the rest once for each.

MWG Proposition 9.B.3 (G) is the justification: (i) in any SPE that plays $\sigma_S$ in subgame $S$, the
moves outside $S$ form an SPE of the reduced game; (ii) any SPE of the reduced game, completed by
$\sigma_S$ inside $S$, is an SPE of the whole game.

### 4.1 · Worked — the voluntary Battle of the Sexes (pp. 158–159)

Strategies: $S_1=\{YO,YF,NO,NF\}$ ($NO$ and $NF$ differ only at $x_1$, which $N$ never reaches),
$S_2=\{o,f\}$. Normal form:

| | $o$ | $f$ |
|---|---|---|
| $YO$ | $2,1$ | $0,0$ |
| $YF$ | $0,0$ | $1,2$ |
| $NO$ | $1.5,1.5$ | $1.5,1.5$ |
| $NF$ | $1.5,1.5$ | $1.5,1.5$ |

**Nash equilibria.** Column $o$: player 1's best reply is $YO$ (2 > 1.5 > 0); row $YO$: player 2 plays
$o$ (1 > 0) → $(YO,o)$. Column $f$: player 1's best replies are $NO$, $NF$ (1.5 > 1 > 0); rows $NO,NF$:
player 2 is indifferent, so $f$ is a best reply → $(NO,f)$, $(NF,f)$. Row $YF$: player 2 plays $f$, but
then player 1 prefers $N$ → not an equilibrium.

$$E_{\text{Nash}}=\{(YO,o),\ (NO,f),\ (NF,f)\}\qquad(p.~158)$$

**Subgame perfection.** The subgame at $x_1$ is the simultaneous BoS, whose pure equilibria are
$(O,o)$ and $(F,f)$ (and one mixed, left to Tadelis exercise 8.1, p. 170). Branch:

| Equilibrium in the subgame | Payoffs carried up | Player 1 at $x_0$ | SPE |
|---|---|---|---|
| $(O,o)$ | $(2,1)$ | $Y$: 2 vs $N$: 1.5 → $Y$ | $(YO,o)$ |
| $(F,f)$ | $(1,2)$ | $Y$: 1 vs $N$: 1.5 → $N$ | $(NF,f)$ |

$$E_{\text{SPE}}=\{(YO,o),\ (NF,f)\}\qquad(p.~158)$$

**$(NO,f)$ is a Nash equilibrium but not subgame perfect**: restricted to the subgame at $x_1$ it is
$(O,f)$, which is not an equilibrium of the simultaneous BoS (player 2 would switch to $o$). It survives
the Nash test only because $x_1$ is never reached.

![Left: the voluntary Battle of the Sexes tree, with player 1 choosing Y or N at the root, N ending at (1.5, 1.5), and after Y a simultaneous Battle of the Sexes with player 2's two nodes joined by a dashed information-set line; a box marks the subgame starting at player 1's second node. Middle: the reduced game if the subgame plays (O, o), where Y gives (2, 1) and is chosen over N. Right: the reduced game if the subgame plays (F, f), where Y gives (1, 2) and N is chosen](figures/L03-voluntary-bos-subgames.png)
*Figure — the two proper subgames of the voluntary BoS and the two reduced games, one per pure equilibrium of the subgame. Source: Tadelis Figs. 8.4 and 8.7, pp. 155, 159.*

The box is the only place a subgame can start below the root; the dashed line inside it is why neither
of player 2's nodes can start one. Each right-hand panel is the whole game after the box has been
replaced by one of its equilibria, and player 1's choice flips between them because 1.5 sits between
the two payoffs 2 and 1.

### 4.2 · Worked — mutually assured destruction (§8.3.3, Fig. 8.11, pp. 163–166)

Player 1 (the United States) ignores ($I$, payoffs $(0,0)$) or escalates ($E$). After $E$, player 2
(the USSR) backs down ($B$, $(10,-10)$) or goes nuclear ($N$). After $N$ they play a simultaneous
**war stage**: retreat ($R$, $r$) or Doomsday ($D$, $d$).

| | $r$ | $d$ |
|---|---|---|
| $R$ | $-5,-5$ | $-100,-100$ |
| $D$ | $-100,-100$ | $-100,-100$ |

Strategies: $S_1=\{IR,ID,ER,ED\}$, $S_2=\{Br,Bd,Nr,Nd\}$. The pure Nash equilibria of the whole game
(p. 164):

$$E_{\text{Nash}}=\{(IR,Nr),(IR,Nd),(ID,Nr),(ID,Nd),(ED,Br),(ED,Bd)\}$$

**Step 1, the war stage.** $(R,r)$: neither gains by switching ($-5>-100$). $(D,d)$: either player
switching alone still gets $-100$, so no strict gain: also an equilibrium. Two pure Nash equilibria:
NE1 $=(R,r)$ with $(-5,-5)$, NE2 $=(D,d)$ with $(-100,-100)$ (p. 165).

**Step 2, branch on the war stage** (Fig. 8.12, pp. 165–166):

| Case | War stage worth | Player 2: $N$ vs $B$ | Player 1: $E$ vs $I$ | SPE |
|---|---|---|---|---|
| 1: NE1 | $(-5,-5)$ | $-5>-10$ → $N$ | $E\to-5$ vs $I\to0$ → $I$ | $(IR,Nr)$ |
| 2: NE2 | $(-100,-100)$ | $-10>-100$ → $B$ | $E\to10$ vs $I\to0$ → $E$ | $(ED,Bd)$ |

$$E_{\text{SPE}}=\{(IR,Nr),\ (ED,Bd)\}\qquad(p.~166)$$

Why the other four Nash equilibria fail, each in the first subgame where its restriction is not a
Nash equilibrium:

| Nash equilibrium | War stage played | Fails because |
|---|---|---|
| $(IR,Nd)$ | $(R,d)$ | player 2 switches to $r$: $-5>-100$ |
| $(ID,Nr)$ | $(D,r)$ | player 1 switches to $R$: $-5>-100$ |
| $(ED,Br)$ | $(D,r)$ | player 1 switches to $R$: $-5>-100$ |
| $(ID,Nd)$ | $(D,d)$, an equilibrium | at player 2's node, $B$ gives $-10>-100$ from $N$ followed by $(D,d)$ |

> **In both SPE the war stage is off the path, and still it decides everything** (p. 166): what the
> players expect to happen in a subgame nobody reaches fixes who escalates and who backs down. The
> escalation equilibrium $(ED,Bd)$ works because both expect Doomsday if war comes.

The mixed equilibrium of the war stage and the SPE built on it are Tadelis exercise 8.2 (p. 170).

---

## 5 · C — two-stage games with simultaneous moves (Gibbons §2.2.A, pp. 71–73)

Gibbons's class: players 1 and 2 move simultaneously; players 3 and 4 observe $(a_1,a_2)$ and then
move simultaneously. Assume each second-stage game has a unique Nash equilibrium
$(a_3^*(a_1,a_2),a_4^*(a_1,a_2))$. Then the first stage is the simultaneous game with payoffs
$u_i(a_1,a_2,a_3^*(a_1,a_2),a_4^*(a_1,a_2))$; if its Nash equilibrium $(a_1^*,a_2^*)$ is unique, the
**subgame-perfect outcome** is $(a_1^*,a_2^*,a_3^*(a_1^*,a_2^*),a_4^*(a_1^*,a_2^*))$.

**Outcome versus equilibrium** (Gibbons pp. 125–126): the *outcome* names the moves on the path; the
*equilibrium* names complete strategies,
$(a_1^*,a_2^*,a_3^*(\cdot,\cdot),a_4^*(\cdot,\cdot))$, a reply for every first-stage pair. In the
two-stage perfect-information game the outcome is $(a_1^*,R_2(a_1^*))$ and the SPE is
$(a_1^*,R_2(\cdot))$. **Writing the outcome when an equilibrium is asked for is the most common
error on this topic** ([[L03-10-pitfalls]] §1).

This class is the template for the multistage games of [[../L04/L04-00-map|Lecture 4]] (bank runs,
tariffs, tournaments are Gibbons's §2.2.B–D).

---

## Links

- Next: the economic use of the refinement, credibility and commitment,
  [[L03-06-credibility-entry-commitment]].
- Mixed equilibria of a subgame: [[../L02/L02-00-map|Lecture 2]]. Infinite-horizon SPE:
  [[../L04/L04-00-map|Lecture 4]], [[../L05/L05-00-map|Lecture 5]]. Beliefs at information sets
  (perfect Bayesian equilibrium): [[../L08/L08-00-map|Lecture 8]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] item 2 (*Nash equilibrium in an extensive
  game admits incredible threats that subgame perfection removes*), item 3 (multiplicity).
- Python: `subgame_roots`, `spe` on `vbos`, `card`, `mad`, [[L03-11-python]] §1.
- Exercises: Tadelis 8.1 (p. 170), 8.2 (p. 170), 8.3 (p. 170), 8.5 (p. 170), 8.10 (p. 172);
  Muñoz-Garcia & Toro-González Ch. 4, Exercise 4 (p. 163), Exercise 6 (p. 169).
