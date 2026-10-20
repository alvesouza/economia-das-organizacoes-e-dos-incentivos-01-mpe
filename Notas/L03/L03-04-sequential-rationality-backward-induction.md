---
tags: [notes, lecture-03, sequential-rationality, backward-induction, zermelo, centipede]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 8 intro and §8.1 (pp. 151–153): Fig. 8.1, Definition 8.1, Proposition 8.1, Corollary 8.1; §8.3.1 (pp. 159–160): the Centipede Game, Fig. 8.8; Gibbons (1992) §2.1.A (pp. 57–61); MWG §9.B (pp. 268–281), Proposition 9.B.1"
---

# 8.1 · Sequential rationality and backward induction

> **Claim.** Ask every player to play a best response **at every information set, reached or not**:
> that is sequential rationality. In a finite game of perfect information it is enforced by solving
> the tree from the end, and the procedure always delivers an answer, unique when no player is ever
> indifferent (Zermelo, Proposition 8.1). The answer can be bleak: in the Centipede game it throws
> away a payoff both players would prefer.
> Prev: [[L03-03-normal-form-and-paths]] · Next: [[L03-05-subgame-perfection]] · Map: [[L03-00-map]]

---

## 1 · U — a coordination game with a silly equilibrium (Fig. 8.1, p. 151)

Player 1 exits ($E$) with $(0,0)$ or proceeds ($P$); after $P$, player 2 exits ($e$) with $(0,0)$ or
proceeds ($p$) with $(1,1)$.

| | $e$ | $p$ |
|---|---|---|
| $E$ | $0,0$ | $0,0$ |
| $P$ | $0,0$ | $1,1$ |

Two Nash equilibria: $(P,p)$ and $(E,e)$. In $(E,e)$ player 1 exits because player 2 "would exit";
but if player 2 were ever asked, $p$ gives 1 against 0 from $e$. Nash equilibrium **puts no restriction
on beliefs off the path**, so it lets $(E,e)$ through (pp. 151–152).

---

## 2 · C — the definition and the procedure (§8.1, pp. 152–153)

> **Definition 8.1.** Given strategies $\sigma_{-i}\in\Delta S_{-i}$ of $i$'s opponents, player $i$ is
> **sequentially rational** if and only if $i$ is playing a best response to $\sigma_{-i}$ **in each of
> his information sets**.

**Backward induction** (p. 153): call "level 1" the nodes that immediately precede terminal nodes;
at each, let the mover pick the action with her highest payoff. Call "level 2" the nodes that precede
level-1 nodes; let the mover pick her best action *given* the level-1 choices. Continue up to the
root. The game is finite, so the procedure ends; at every node the mover best-responds to what comes
after, so the result is sequentially rational everywhere.

> **Proposition 8.1 (Zermelo's Theorem).** Any finite game of perfect information has a backward
> induction solution that is sequentially rational. Furthermore if no two terminal nodes prescribe the
> same payoffs to any player then the backward induction solution is unique.
>
> **Corollary 8.1.** Any finite game of perfect information has at least one sequentially rational
> Nash equilibrium **in pure strategies**. If no two terminal nodes prescribe the same payoffs to any
> player, the game has a unique sequentially rational Nash equilibrium.

| Hypothesis | What fails without it |
|---|---|
| **finite** | there may be no last nodes to start from (Rubinstein bargaining, repeated games: [[../L04/L04-00-map\|Lecture 4]], [[../L05/L05-00-map\|Lecture 5]]) |
| **perfect information** | at a non-singleton information set the mover's best action depends on a belief about where she is, which the procedure does not supply (p. 154; see [[L03-05-subgame-perfection]]) |
| **no ties** (for uniqueness) | an indifferent mover can pick either action and each choice can change earlier players' choices (footnote 1, p. 153) |

**History** (Remark, p. 153): Zermelo (1913) showed that in games like chess a player can guarantee at
least a draw; neither backward induction nor strategies appear in his paper. MWG state the same result
as **Proposition 9.B.1** (§9.B): every finite game of perfect information has a pure-strategy Nash
equilibrium that can be derived by backward induction, unique if no player has the same payoffs at
two terminal nodes.

### 2.1 · Worked — the sequential Battle of the Sexes (p. 152)

| Step | Node | Comparison | Choice |
|---|---|---|---|
| 1 | $x_1$ (after $O$), player 2 | $o$: 1 vs $f$: 0 | $o$ |
| 1 | $x_2$ (after $F$), player 2 | $o$: 0 vs $f$: 2 | $f$ |
| 2 | $x_0$, player 1 | $O\to(2,1)$ vs $F\to(1,2)$: 2 vs 1 | $O$ |

Result: player 1 plays $O$, player 2 plays $of$. **$(O,of)$ is the only one of the three Nash
equilibria of [[L03-03-normal-form-and-paths]] that survives** (p. 152). $(O,oo)$ dies because $o$ at
$x_2$ is not a best response there; $(F,ff)$ dies because $f$ at $x_1$ is not.

> **Backward induction predicts play off the path as well as on it**: "if player 1 chooses $F$ then
> player 2 will choose $f$" (p. 152). That off-path prediction is part of the answer.

---

## 3 · Worked — Gibbons's games (§2.1.A, pp. 57–61; §2.4.B, p. 126)

**Two stages** (Gibbons pp. 57–58). Player 1 picks $a_1$; player 2 sees it and solves
$\max_{a_2}u_2(a_1,a_2)$, with solution $R_2(a_1)$; player 1 anticipates this and solves
$\max_{a_1}u_1(a_1,R_2(a_1))$, with solution $a_1^*$. **$(a_1^*,R_2(a_1^*))$ is the backwards-induction
outcome.** It "does not involve noncredible threats: player 1 gives no credence to threats by player 2
to respond in ways that will not be in 2's self-interest when the second stage arrives" (p. 58).

**Fig. 2.4.1 solved** (p. 126; matrix in [[L03-03-normal-form-and-paths]] §4): after $L$, player 2
prefers $R'$ (2 > 1); after $R$, $L'$ (1 > 0). Player 1 compares $L\to1$ with $R\to2$ and plays $R$.
Outcome $(R,L')$; equilibrium $(R,(R',L'))$.

**Three moves, player 1 moves twice** (pp. 59–60). $L$ ends with $(2,0)$. After $R$, player 2 plays
$L'$ $(1,1)$ or $R'$; after $R'$, player 1 plays $L''$ $(3,0)$ or $R''$ $(0,2)$.

| Step | Mover | Comparison | Choice |
|---|---|---|---|
| 3 | player 1 at stage 3 | $L''$: 3 vs $R''$: 0 | $L''$ |
| 2 | player 2 | $L'$: 1 vs $R'$ then $L''$: 0 | $L'$ |
| 1 | player 1 | $L$: 2 vs $R$ then $L'$: 1 | $L$ |

The game ends at once, at $(2,0)$. **Gibbons's point** (pp. 60–61): the argument depends on what
player 2 would believe *after* player 1 has played $R$, a move backward induction says will not
happen. If 1 played $R$, it cannot be common knowledge that both are rational, yet there are reasons
for $R$ consistent with 1 being rational (for instance, 1 doubts that 2 is rational and hopes for
$R'$). Backward induction assumes deviations are explained that way; where it is more plausible that a
deviator is simply irrational, it loses appeal.

---

## 4 · Worked — the Centipede Game (§8.3.1, Fig. 8.8, pp. 159–160)

Players alternate; each can stop ($N$ for 1, $n$ for 2) or continue ($C$, $c$). Payoffs if stopped at
each node, and at the end:

| Node | Mover | Stop gives | Continue leads to |
|---|---|---|---|
| 1 | 1 | $(1,1)$ | node 2 |
| 2 | 2 | $(0,3)$ | node 3 |
| 3 | 1 | $(2,2)$ | node 4 |
| 4 | 2 | $(1,4)$ | end $(3,3)$ |

Backward induction:

| Step | Node | Mover compares | Choice | Value carried back |
|---|---|---|---|---|
| 1 | 4 | player 2: $n$ → 4 vs $c$ → 3 | $n$ | $(1,4)$ |
| 2 | 3 | player 1: $N$ → 2 vs $C$ → 1 | $N$ | $(2,2)$ |
| 3 | 2 | player 2: $n$ → 3 vs $c$ → 2 | $n$ | $(0,3)$ |
| 4 | 1 | player 1: $N$ → 1 vs $C$ → 0 | $N$ | $(1,1)$ |

![A horizontal centipede tree with four decision nodes alternating between players 1 and 2. Each node has a downward stop edge to payoffs (1,1), (0,3), (2,2), (1,4) and a rightward continue edge, ending at (3,3). All stop edges are highlighted as chosen; all continue edges are dashed as rejected; step numbers run from 4 at the first node to 1 at the last](figures/L03-centipede-backward-induction.png)
*Figure — backward induction in the Centipede Game: every mover stops, so play ends at once with $(1,1)$ although $(3,3)$ is on the table. Source: Tadelis Fig. 8.8, p. 159.*

Read the figure right to left: each step compares one stop payoff with the value that the next step
has already carried back, and stopping wins every time by exactly 1.

> **The sum of payoffs rises by 1 at every continuation, so the structure can be stretched to make the
> end as attractive as one likes; the unique backward induction outcome stays $(1,1)$** (p. 159–160).

**Evidence** (Remark, p. 160): in the lab, people mostly do not stop at once (McKelvey and Palfrey,
1992). Two explanations: players care about each other's payoffs, or rationality is not common
knowledge. Palacios-Huerta and Volij (2009) ran it with chess players: 69% stopped immediately, and
grandmasters always did, which supports the second explanation.

---

## 5 · G — MWG's framing (§9.B, Examples 9.B.2 and 9.B.5)

MWG motivate the same procedure with the *principle of sequential rationality*: "a player's strategy
should specify optimal actions at every point in the game tree" (p. 269), and solve a three-player
perfect-information game by successive reduction (Example 9.B.2). Their Example 9.B.5 is a 100-stage
centipede. Not examinable beyond the statement of Proposition 9.B.1.

---

## Links

- Next: what to do when the end of the tree contains a non-singleton information set,
  [[L03-05-subgame-perfection]].
- The same logic in finite bargaining and finitely repeated games: [[../L04/L04-00-map|Lecture 4]],
  [[../L05/L05-00-map|Lecture 5]].
- Rules pack: [[../../rules/game-theory|rules/game-theory]] item 7 (*backward induction for finite games
  of perfect information*).
- Python: `backward_induction` on `bos_seq`, `gib3`, `cent`, [[L03-11-python]] §1.
- Practice: [Listas/pratica-aula-01-02.md](../../Listas/pratica-aula-01-02.md) item 19 (Cabral 7.14,
  Centipede, p. 182).
- Exercises: Tadelis 7.4 (p. 148), 7.5 (p. 148), 8.11(b) (p. 172–173);
  Muñoz-Garcia & Toro-González Ch. 4, Exercise 9 (p. 176), Exercise 19 (p. 202), Exercise 20 (p. 204).
