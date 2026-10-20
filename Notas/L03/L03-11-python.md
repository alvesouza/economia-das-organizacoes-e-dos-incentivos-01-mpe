---
tags: [notes, lecture-03, python, backward-induction, subgame-perfection, stackelberg]
date: 2026-10-16
status: estimated
source: "Tadelis (2013) Ch. 7-8 (pp. 129-174); Gibbons (1992) §2.1.A-B, §2.4 (pp. 57-64, 115-128); Cabral (2017) §7.2 (pp. 167-171); MWG Example 9.B.1 (pp. 268-269)"
---

# Lecture 3 · Computation in Python

> Every routine the lecture needs, each followed by the `assert` checks that must pass against the
> book's own numbers. Python standard library only (no numpy needed here). The blocks run in order as one
> script; all of them were run together before this note was written.
> Map: [[L03-00-map]] · Formulas: [[L03-09-formulas]] · Pitfalls: [[L03-10-pitfalls]]

**Reuse.** The project's existing checkers (`Listas/lista-aulas-01-02-check.py`,
`Aula/notes-aulas-01-02/check_part2.py`) cover normal-form games and bargaining shares; neither
represents a game tree, so the tree solver below is new. Bargaining by backward induction is reused, not
rebuilt, in [[../L04/L04-00-map|Lecture 4]] (`check_part2.py::proposer_share`).

**Design.** A tree is nested tuples: `T(payoffs)` for a terminal node, `D(player, info, moves)` for a
decision node, `N(moves)` for Nature. Nodes that share an `info` label form one information set, which is
how imperfect information is encoded. Everything else (strategies, the normal form, Nash equilibria,
subgames, SPE) is computed from that one object by brute force, which is exact and fast for textbook-sized
trees.

---

## 1 · Trees, strategies, Nash and subgame-perfect equilibria → [[L03-01-extensive-form]] to [[L03-05-subgame-perfection]]

### 1.1 · The solver

```python
from itertools import product
from math import prod, isclose


def T(*payoffs):
    """Terminal node: one payoff per player (player 1 first)."""
    return ("T", tuple(payoffs))


def D(player, info, moves):
    """Decision node of `player` (1-based) in information set `info`; moves: {action: child}."""
    return ("D", player, info, dict(moves))


def N(moves):
    """Nature: {label: (probability, child)}."""
    return ("N", dict(moves))


def nodes(tree, path=()):
    """Yield (path, node) for every node; a path is the tuple of actions from the root."""
    yield path, tree
    if tree[0] == "D":
        for a, child in tree[3].items():
            yield from nodes(child, path + (a,))
    elif tree[0] == "N":
        for a, (_, child) in tree[1].items():
            yield from nodes(child, path + (a,))


def infosets(tree):
    """{info: (player, actions, [member paths])}. Raises if Definition 7.2(3) fails."""
    H = {}
    for path, x in nodes(tree):
        if x[0] == "D":
            _, i, h, moves = x
            if h in H:
                assert H[h][0] == i and H[h][1] == tuple(moves), f"info set {h}: Def. 7.2(3) fails"
                H[h][2].append(path)
            else:
                H[h] = (i, tuple(moves), [path])
    return H


def players(tree):
    return sorted({v[0] for v in infosets(tree).values()})


def pure_strategies(tree, i):
    """Definition 7.4: every map H_i -> A_i(h_i), as a dict {info: action}."""
    H = {h: v for h, v in infosets(tree).items() if v[0] == i}
    hs = sorted(H)
    return [dict(zip(hs, acts)) for acts in product(*(H[h][1] for h in hs))]


def n_pure_strategies(tree, i):
    """|S_i| = m_1 x m_2 x ... x m_k (Tadelis p. 139)."""
    return prod(len(v[1]) for v in infosets(tree).values() if v[0] == i)


def payoff(node, profile):
    """Expected payoff vector from `node` when everyone follows `profile` ({info: action})."""
    if node[0] == "T":
        return node[1]
    if node[0] == "D":
        return payoff(node[3][profile[node[2]]], profile)
    out = None
    for p, child in node[1].values():
        v = [p * u for u in payoff(child, profile)]
        out = v if out is None else [a + b for a, b in zip(out, v)]
    return tuple(out)


def profiles(tree):
    """All pure-strategy profiles, as (tuple of per-player strategies, merged dict)."""
    P = players(tree)
    for combo in product(*(pure_strategies(tree, i) for i in P)):
        merged = {}
        for s in combo:
            merged.update(s)
        yield combo, merged


def _is_nash_from(tree, root, combo):
    """No player gains by a unilateral switch of pure strategy, payoffs measured from `root`."""
    P = players(tree)
    merged = {k: v for s in combo for k, v in s.items()}
    base = payoff(root, merged)
    for k, i in enumerate(P):
        for s_dev in pure_strategies(tree, i):
            u = payoff(root, {**merged, **s_dev})[i - 1]
            if u > base[i - 1] + 1e-12:
                return False
    return True


def pure_nash(tree):
    """Every pure-strategy Nash equilibrium of the normal form of `tree` (Section 7.3)."""
    return [combo for combo, _ in profiles(tree) if _is_nash_from(tree, tree, combo)]


def subgame_roots(tree):
    """Definition 8.2: a node that is a singleton information set (or the root) and whose
    successors' information sets lie entirely inside its subtree."""
    H = infosets(tree)
    where = {}
    for h, (_, _, members) in H.items():
        for m in members:
            where[m] = h
    roots = []
    for path, x in nodes(tree):
        if x[0] == "T":
            continue
        if x[0] == "D" and len(H[x[2]][2]) > 1:
            continue
        inside = all(all(m[:len(path)] == path for m in H[where[q]][2])
                     for q, y in nodes(x, path) if y[0] == "D")
        if inside:
            roots.append((path, x))
    return roots


def spe(tree):
    """Definition 8.3 by brute force: the pure profiles that are a Nash equilibrium in every
    proper subgame (the whole game included)."""
    roots = subgame_roots(tree)
    return [combo for combo, _ in profiles(tree)
            if all(_is_nash_from(tree, r, combo) for _, r in roots)]


def backward_induction(tree):
    """Proposition 8.1 for finite perfect-information games without Nature.
    Returns (payoff vector, plan {info: action}). Ties go to the first-listed action."""
    if tree[0] == "T":
        return tree[1], {}
    assert tree[0] == "D", "backward induction here needs perfect information, no Nature"
    _, i, h, moves = tree
    best, plan = None, {}
    for a, child in moves.items():
        v, sub = backward_induction(child)
        plan.update(sub)
        if best is None or v[i - 1] > best[1][i - 1]:
            best = (a, v)
    plan[h] = best[0]
    return best[1], plan


def label(combo):
    """Readable profile: each strategy as its actions in information-set order."""
    return tuple("".join(s[h] for h in sorted(s)) for s in combo)
```

`spe` checks Definition 8.3 literally: a profile passes if, from the root of every proper subgame, no
player gains by switching to another of her pure strategies. Because payoffs are measured from the
subgame's root, only the actions inside the subgame matter, which is exactly "the restriction is a Nash
equilibrium of the subgame". It finds **pure-strategy** SPE only; the mixed ones of exercises 8.1–8.2 are
outside its reach (ceiling stated; add support enumeration per subgame if ever needed).

### 1.2 · Perfect information: Battle of the Sexes, Gibbons, Centipede

```python
# --- Sequential-move Battle of the Sexes, Fig. 7.7 / 8.6 (pp. 138, 157) -------------
bos_seq = D(1, "x0", {"O": D(2, "x1", {"o": T(2, 1), "f": T(0, 0)}),
                      "F": D(2, "x2", {"o": T(0, 0), "f": T(1, 2)})})
bos_sim = D(1, "x0", {"O": D(2, "h2", {"o": T(2, 1), "f": T(0, 0)}),
                      "F": D(2, "h2", {"o": T(0, 0), "f": T(1, 2)})})
assert n_pure_strategies(bos_seq, 2) == 4 and n_pure_strategies(bos_sim, 2) == 2
assert sorted(map(label, pure_nash(bos_seq))) == [("F", "ff"), ("O", "of"), ("O", "oo")]   # p. 145
assert list(map(label, spe(bos_seq))) == [("O", "of")]                                     # p. 157
assert backward_induction(bos_seq) == ((2, 1), {"x1": "o", "x2": "f", "x0": "O"})
assert sorted(map(label, pure_nash(bos_sim))) == [("F", "f"), ("O", "o")]
assert len(subgame_roots(bos_sim)) == 1                    # simultaneous: only the whole game

# --- Gibbons Figure 2.4.1 (p. 116): NE (R,(R',L')) and (L,(R',R')); SPE only the first --
gib = D(1, "a", {"L": D(2, "b", {"L'": T(3, 1), "R'": T(1, 2)}),
                 "R": D(2, "c", {"L'": T(2, 1), "R'": T(0, 0)})})
assert sorted(map(label, pure_nash(gib))) == [("L", "R'R'"), ("R", "R'L'")]
assert list(map(label, spe(gib))) == [("R", "R'L'")]

# --- Gibbons three-move game (pp. 59-60): backward induction ends the game at once -----
gib3 = D(1, "a", {"L": T(2, 0),
                  "R": D(2, "b", {"L'": T(1, 1),
                                  "R'": D(1, "c", {"L''": T(3, 0), "R''": T(0, 2)})})})
v, plan = backward_induction(gib3)
assert v == (2, 0) and plan == {"c": "L''", "b": "L'", "a": "L"}

# --- Centipede, Fig. 8.8 (p. 159): unique BI outcome (1,1), although (3,3) is available --
cent = D(1, "1a", {"N": T(1, 1), "C": D(2, "2a", {"n": T(0, 3), "c": D(1, "1b", {
    "N": T(2, 2), "C": D(2, "2b", {"n": T(1, 4), "c": T(3, 3)})})})})
v, plan = backward_induction(cent)
assert v == (1, 1) and plan == {"2b": "n", "1b": "N", "2a": "n", "1a": "N"}
assert len(spe(cent)) == 1
```

### 1.3 · Imperfect information and applications: voluntary BoS, card game, MAD, entry

```python
# --- Voluntary Battle of the Sexes, Fig. 8.2/8.4 (pp. 154-158) ---------------------------
vbos = D(1, "x0", {"Y": D(1, "x1", {"O": D(2, "h2", {"o": T(2, 1), "f": T(0, 0)}),
                                    "F": D(2, "h2", {"o": T(0, 0), "f": T(1, 2)})}),
                   "N": T(1.5, 1.5)})
lab = lambda c: (c[0]["x0"] + c[0]["x1"], c[1]["h2"])          # Tadelis writes YO, NF, ...
assert sorted(map(lab, pure_nash(vbos))) == [("NF", "f"), ("NO", "f"), ("YO", "o")]   # p. 158
assert sorted(map(lab, spe(vbos))) == [("NF", "f"), ("YO", "o")]
assert [p for p, _ in subgame_roots(vbos)] == [(), ("Y",)]       # exactly two subgames

# --- Card game, Fig. 8.5 (p. 156): the only proper subgame is the whole game -----------
card = N({"A": (0.5, D(1, "x1", {"N": T(-1, 1), "Y": D(2, "h2", {"C": T(2, -2), "F": T(1, -1)})})),
          "K": (0.5, D(1, "x2", {"N": T(-1, 1), "Y": D(2, "h2", {"C": T(-2, 2), "F": T(1, -1)})}))})
assert [p for p, _ in subgame_roots(card)] == [()]

# --- Mutually assured destruction, Fig. 8.11 (pp. 163-166) -------------------------------
war = lambda: D(1, "w1", {"R": D(2, "w2", {"r": T(-5, -5), "d": T(-100, -100)}),
                          "D": D(2, "w2", {"r": T(-100, -100), "d": T(-100, -100)})})
mad = D(1, "a", {"I": T(0, 0), "E": D(2, "b", {"B": T(10, -10), "N": war()})})
labm = lambda c: (c[0]["a"] + c[0]["w1"], c[1]["b"] + c[1]["w2"])
assert sorted(map(labm, pure_nash(mad))) == sorted(
    [("IR", "Nr"), ("IR", "Nd"), ("ID", "Nr"), ("ID", "Nd"), ("ED", "Br"), ("ED", "Bd")])  # p. 164
assert sorted(map(labm, spe(mad))) == [("ED", "Bd"), ("IR", "Nr")]                        # p. 166


# --- Cabral's entry game and the value of a bond, Figs. 7.7-7.8 (pp. 168-170) -----------
def cabral(M=50, DE=10, DI=20, FE=-10, FI=10, bond=40):
    """Entrant (player 1) then incumbent (player 2). Payoffs (entrant, incumbent).
    Without the bond, accommodation after entry pays the incumbent DI; with it, DI - bond."""
    entry = lambda di: D(1, None, {"out": T(0, M), "in": D(2, None, {"acc": T(DE, di), "fight": T(FE, FI)})})
    return entry(DI), entry(DI - bond)


def name(tree, tag):
    """Give each information set a unique name (cabral() builds them anonymously)."""
    if tree[0] == "T":
        return tree
    _, i, _, moves = tree
    return D(i, f"{tag}{i}", {a: name(c, tag) for a, c in moves.items()})


no_bond, with_bond = (name(t, k) for t, k in zip(cabral(), ("n", "b")))
assert sorted(map(label, pure_nash(no_bond))) == [("in", "acc"), ("out", "fight")]   # p. 168
assert list(map(label, spe(no_bond))) == [("in", "acc")]                              # p. 169
v0, _ = backward_induction(no_bond)
v1, _ = backward_induction(with_bond)
assert v0 == (10, 20) and v1 == (0, 50) and v1[1] - v0[1] == 30   # value of commitment, p. 170
assert backward_induction(name(cabral(FI=-10)[1], "t"))[0] == (0, 50)   # p. 169 text's -10: same answer

# --- MWG Example 9.B.1 (pp. 268-269): Out (0,2); In-Fight (-3,-1); In-Accommodate (2,1) --
mwg = D(1, "E", {"out": T(0, 2), "in": D(2, "I", {"fight": T(-3, -1), "acc": T(2, 1)})})
assert sorted(map(label, pure_nash(mwg))) == [("in", "acc"), ("out", "fight")]
assert list(map(label, spe(mwg))) == [("in", "acc")]
```

The last assert of the Cabral block is the source-detail check of [[L03-06-credibility-entry-commitment]]
§1: with the text's $-10$ instead of the figure's $10$ the answer is unchanged.

---

## 2 · Mixed versus behavioral, and the absent-minded driver → [[L03-02-strategies]]

```python
# --- Mixed vs behavioral strategies, Fig. 7.9 (pp. 140-142) ------------------------------
def behavioral_from_mixed(p):
    """Player 2's mixed strategy (p_oo, p_of, p_fo, p_ff) -> (Pr{o|O}, Pr{o|F})."""
    p_oo, p_of, p_fo, p_ff = p
    return p_oo + p_of, p_oo + p_fo


for p in [(1/3, 0, 1/6, 1/2), (1/6, 1/6, 1/3, 1/3)]:            # the book's two mixes, p. 142
    assert isclose(sum(p), 1) and all(isclose(a, b) for a, b in zip(behavioral_from_mixed(p), (1/3, 1/2)))


# --- Absent-minded driver, Fig. 7.10 (p. 142) --------------------------------------------
driver = lambda p: 0 * p + 4 * p * (1 - p) + 1 * (1 - p) ** 2       # = -3p^2 + 2p + 1
grid = [k / 3000 for k in range(3001)]
p_star = max(grid, key=driver)
assert isclose(p_star, 1 / 3) and isclose(driver(1 / 3), 4 / 3)
```

---

## 3 · Stackelberg and Cournot → [[L03-07-stackelberg]]

```python
from math import isclose, log


def br(q_other, a, b, c):
    """Best response to an observed (or believed) rival quantity, P = a - bQ, cost c:
    max(0, (a - c - b q_other) / (2b))  -- eq. (8.1) with a=100, b=1, c=10."""
    return max(0.0, (a - c - b * q_other) / (2 * b))


def profits(q1, q2, a, b, c1, c2):
    P = max(0.0, a - b * (q1 + q2))
    return P, (P - c1) * q1, (P - c2) * q2


def cournot(a, b, c1, c2):
    """Simultaneous-move Nash equilibrium, corners included.
    Interior: q_i = (a - 2c_i + c_j) / (3b)."""
    q1, q2 = (a - 2 * c1 + c2) / (3 * b), (a - 2 * c2 + c1) / (3 * b)
    if q1 < 0:
        q1, q2 = 0.0, br(0, a, b, c2)
    elif q2 < 0:
        q1, q2 = br(0, a, b, c1), 0.0
    return (q1, q2) + profits(q1, q2, a, b, c1, c2)


def stackelberg(a, b, c1, c2):
    """Subgame-perfect outcome with firm 1 leading. The leader maximizes
    pi_1(q1, R2(q1)) where R2 = br(., a, b, c2) is kinked at q1 = (a - c2)/b; each piece
    is concave, so compare the best point on each piece."""
    kink = max(0.0, (a - c2) / b)
    qa = min(max((a - 2 * c1 + c2) / (2 * b), 0.0), kink)     # follower active
    qb = max((a - c1) / (2 * b), kink)                          # follower shut out
    pi = lambda q: profits(q, br(q, a, b, c2), a, b, c1, c2)[1]
    q1 = max((qa, qb), key=pi)
    q2 = br(q1, a, b, c2)
    return (q1, q2) + profits(q1, q2, a, b, c1, c2)


# --- Tadelis Section 8.3.2 (pp. 160-161): p = 100 - q, c = 10 -----------------------
S, C = stackelberg(100, 1, 10, 10), cournot(100, 1, 10, 10)
assert S[:2] == (45.0, 22.5) and isclose(S[3], 1012.5) and isclose(S[4], 506.25)
assert C[:2] == (30.0, 30.0) and isclose(C[3], 900) and isclose(C[4], 900)
assert isclose(S[3] - C[3], 112.5) and isclose(S[4] - C[4], -393.75)   # first-mover advantage
assert isclose(S[2], 32.5) and isclose(C[2], 40)                       # price falls

# --- Gibbons Section 2.1.B (pp. 62-63): general (a, c) -----------------------------
for a, c in [(100, 10), (50, 5), (12, 3)]:
    S, C = stackelberg(a, 1, c, c), cournot(a, 1, c, c)
    assert isclose(S[0], (a - c) / 2) and isclose(S[1], (a - c) / 4)
    assert isclose(S[0] + S[1], 3 * (a - c) / 4) and isclose(C[0] + C[1], 2 * (a - c) / 3)
    assert S[3] > C[3] and S[4] < C[4] and S[3] + S[4] < C[3] + C[4]

# --- Unobserved q1 (Gibbons p. 63): if 2 expects (a-c)/2, 1 would rather play 3(a-c)/8 --
a, c = 100, 10
assert isclose(br(br((a - c) / 2, a, 1, c), a, 1, c), 3 * (a - c) / 8)


# --- Nash but not subgame perfect (pp. 162-163) ----------------------------------------
def leader_profit(q1, strategy2, a=100, c=10):
    return profits(q1, strategy2(q1), a, 1, c, c)[1]


flat30 = lambda q1: 30.0                                         # q2(q1) = 30 for every q1
grid = [k / 4 for k in range(0, 401)]
assert max(grid, key=lambda q: leader_profit(q, flat30)) == 30.0   # q1 = 30 is a BR to it
assert br(30, 100, 1, 10) == 30.0                                  # and 30 is a BR on the path
assert br(45, 100, 1, 10) != flat30(45)                            # but off the path it is not


def flood(q_hat):
    """Tadelis's remark: best-respond to q_hat, flood the market (q2 = 100) otherwise."""
    return lambda q1: br(q_hat, 100, 1, 10) if q1 == q_hat else 100.0


assert br(20, 100, 1, 10) == 35.0     # the remark's on-path quantity is 35 (p. 163 prints 40)
for q_hat in [5.0, 20.0, 45.0, 60.0, 85.0]:                      # a continuum of NE outcomes
    s2 = flood(q_hat)
    assert max(grid + [q_hat], key=lambda q: leader_profit(q, s2)) == q_hat
    assert s2(q_hat) == br(q_hat, 100, 1, 10)
```

`stackelberg` is exact: the leader's reduced profit is concave on each side of the kink
$q_1=(a-c_2)/b$ where the follower exits, so the optimum is the better of the two pieces' optima. The
companion's JavaScript uses the same expression and
[companions/check_companions.py](companions/check_companions.py) verifies it against a brute-force grid
search.

---

## 4 · Hyperbolic discounting → [[L03-08-time-inconsistency]]

```python
# --- Section 8.3.4 (pp. 166-169): beta = 1/2, delta = 1, u = ln ------------------------
def v1(x1, K=1.0, beta=0.5):
    """Self 1's payoff when self 2 best-responds with x2 = 2K2/3, x3 = K2/3 (p. 168)."""
    K2 = K - x1
    return log(x1) + beta * log(2 * K2 / 3) + beta * log(K2 / 3)


xs = [k / 20000 for k in range(1, 20000)]
x1_star = max(xs, key=v1)
assert isclose(x1_star, 0.5)                        # the correct derivative gives x1 = K/2
assert v1(0.5) > v1(2 / 3)                          # p. 169 prints 2K/3: not the maximum
# self 1's own preferred plan (commitment): ln x1 + .5 ln x2 + .5 ln x3 -> (1/2, 1/4, 1/4)
best = max(((x1, x2) for x1 in xs[::40] for x2 in xs[::40] if x1 + x2 < 1),
           key=lambda z: log(z[0]) + 0.5 * log(z[1]) + 0.5 * log(1 - z[0] - z[1]))
assert all(isclose(u, w, abs_tol=2e-3) for u, w in zip(best, (0.5, 0.25)))
```

The second assert is the correction of [[L03-08-time-inconsistency]] §2.2: the book's printed
$x_1=	frac23K$ is not the maximum of the objective it prints.

---

## 5 · Run everything

```bash
python Notas/L03/figures/make_figures.py          # 7 figures + their asserts
python Notas/L03/companions/check_companions.py   # both companions vs Python, needs node
```
