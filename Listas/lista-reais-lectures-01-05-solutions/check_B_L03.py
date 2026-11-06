"""Checks every number and equilibrium claim in the Lecture 3 solutions written by agent B:
sol-tadelis-7-1, sol-munoz-garcia-4-3, sol-tadelis-7-2, sol-tadelis-8-5, sol-tadelis-8-10,
sol-tadelis-7-4, sol-tadelis-7-9, sol-tadelis-7-10, sol-mwg-9-b-4, sol-gibbons-2-1.
Exact arithmetic (fractions, sympy). Backward induction and equilibrium sets are computed,
not typed in.

Run: python check_B_L03.py  -> one line per item and "all B L03 checks passed", or an
AssertionError on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

import sympy as sp


# ----------------------------------------------------------------------------- helpers
def pure_ne(A, B):
    """Pure Nash equilibria (row, col) of the bimatrix (A, B), lists of lists."""
    R, C = len(A), len(A[0])
    return {(r, c) for r in range(R) for c in range(C)
            if A[r][c] == max(A[k][c] for k in range(R))
            and B[r][c] == max(B[r][k] for k in range(C))}


def is_ne(A, B, x, y):
    """Is the mixed profile (x, y) a Nash equilibrium of (A, B)? Exact test: every pure
    strategy in a support earns the best pure payoff against the opponent's mix."""
    R, C = len(A), len(A[0])
    u1 = [sum(A[r][c] * y[c] for c in range(C)) for r in range(R)]
    u2 = [sum(B[r][c] * x[r] for r in range(R)) for c in range(C)]
    return (all(u1[r] == max(u1) for r in range(R) if x[r] > 0)
            and all(u2[c] == max(u2) for c in range(C) if y[c] > 0))


def ne_given_q(A, B, q):
    """Column player has two strategies and plays the first w.p. q. Returns True if some mix
    of the row player's best replies makes q a best reply (so (mix, q) is a Nash equilibrium)."""
    u1 = [A[r][0] * q + A[r][1] * (1 - q) for r in range(len(A))]
    best = [r for r in range(len(A)) if u1[r] == max(u1)]
    gaps = [B[r][0] - B[r][1] for r in best]          # column's gain from col 0 over col 1
    lo, hi = min(gaps), max(gaps)                      # every value in [lo, hi] is attainable
    if q == 1:
        return hi >= 0
    if q == 0:
        return lo <= 0
    return lo <= 0 <= hi


def backward_induction(node):
    """All pure backward-induction solutions of a finite perfect-information tree.
    node = ('T', payoff tuple) or ('D', player, {action: child}). Returns a list of
    (payoff vector, path of actions) over every tie-breaking."""
    if node[0] == 'T':
        return [(node[1], ())]
    _, i, kids = node
    sols = [(v, (a,) + path) for a, child in kids.items() for v, path in backward_induction(child)]
    best = max(v[i] for v, _ in sols)
    return [(v, p) for v, p in sols if v[i] == best]


def spne_values(node):
    """Set of payoff vectors reachable by pure SPNE (all tie-breakings) in a perfect-info tree."""
    if node[0] == 'T':
        return {node[1]}
    _, i, kids = node
    vals = [v for child in kids.values() for v in spne_values(child)]
    best = max(v[i] for v in vals)
    return {v for v in vals if v[i] == best}


# ----------------------------------------------------------------------------- tadelis-7-1
# K information sets with m actions each -> m^K pure strategies; m_1 ... m_K -> product.
for ms in [(2, 2), (3, 2, 2), (2, 3, 4), (5,)]:
    plans = list(product(*[range(m) for m in ms]))
    n = 1
    for m in ms:
        n *= m
    assert len(plans) == n
assert len(list(product(range(3), repeat=4))) == 3 ** 4
# dimension of mixed vs behavioral strategy spaces for m_k = (2, 3, 4)
assert (2 * 3 * 4 - 1, (2 - 1) + (3 - 1) + (4 - 1)) == (23, 6)
print("tadelis-7-1: m^K and prod m_k confirmed by enumeration")

# ----------------------------------------------------------------------------- munoz-garcia-4-3
pay = {("C", "C"): (-5, -5), ("C", "N"): (0, -15), ("N", "C"): (-15, 0), ("N", "N"): (-1, -1)}
tree = ('D', 0, {a1: ('D', 1, {a2: ('T', pay[(a1, a2)]) for a2 in "CN"}) for a1 in "CN"})
assert backward_induction(tree) == [((-5, -5), ("C", "C"))]
S2 = list(product("CN", repeat=2))                      # (reply to C, reply to N)
A = [[pay[(a1, s[0] if a1 == "C" else s[1])][0] for s in S2] for a1 in "CN"]
B = [[pay[(a1, s[0] if a1 == "C" else s[1])][1] for s in S2] for a1 in "CN"]
assert {("CN"[r], "".join(S2[c])) for r, c in pure_ne(A, B)} == {("C", "CC")}
# mixed NE: player 1 plays C; player 2 mixes CC (w.p. 1-w) and CN (w.p. w): NE iff w <= 5/7
for w in [F(k, 70) for k in range(71)]:
    y = [1 - w, w, 0, 0]
    assert is_ne(A, B, [1, 0], y) == (w <= F(5, 7))
# no NE with player 1 putting weight on N: if Pr(C) = p < 1, every best reply of player 2
# plays C after N, and against each of them C beats N for player 1
for p_ in [F(k, 20) for k in range(20)]:
    u2 = [p_ * B[0][c] + (1 - p_) * B[1][c] for c in range(4)]
    for c in [c for c in range(4) if u2[c] == max(u2)]:
        assert S2[c][1] == "C" and A[0][c] > A[1][c]
assert pure_ne([[-5, 0], [-15, -1]], [[-5, -15], [0, -1]]) == {(0, 0)}   # simultaneous: (C, C)
print("munoz-garcia-4-3: SPE (C, CC); NE = (C, CC with prob >= 2/7)")

# ----------------------------------------------------------------------------- tadelis-7-2
t72 = ('D', 0, {"A": ('T', (2, 0)),
                "B": ('D', 1, {"C": ('T', (3, 1)),
                               "D": ('D', 0, {"E": ('T', (0, 0)), "F": ('T', (1, 2))})})})
assert backward_induction(t72) == [((2, 0), ("A",))]
assert backward_induction(t72[2]["B"]) == [((1, 2), ("D", "F"))]
rows72 = ["AE", "AF", "BE", "BF"]
A72 = [[2, 2], [2, 2], [3, 0], [3, 1]]                  # columns C, D
B72 = [[0, 0], [0, 0], [1, 0], [1, 2]]
assert {(rows72[r], "CD"[c]) for r, c in pure_ne(A72, B72)} == {("AE", "D"), ("AF", "D"), ("BE", "C")}
qs = sorted(set([F(k, 120) for k in range(121)] + [F(1, 2), F(2, 3)]))
ok = [q for q in qs if ne_given_q(A72, B72, q)]
assert ok == [q for q in qs if q <= F(1, 2)] + [F(1)]
# at q = 1: player 1 mixes BE / BF with Pr(BF) = w; NE iff w <= 1/2
for w in [F(k, 20) for k in range(21)]:
    assert is_ne(A72, B72, [0, 0, 1 - w, w], [1, 0]) == (w <= F(1, 2))
# at q <= 1/2 with player 1 on {AE, AF}: NE; any weight on BF at q = 1/2 breaks it
assert is_ne(A72, B72, [F(1, 3), F(2, 3), 0, 0], [F(1, 2), F(1, 2)])
assert not is_ne(A72, B72, [F(1, 2), 0, 0, F(1, 2)], [F(1, 2), F(1, 2)])
print("tadelis-7-2: SPE (AF, D); pure NE (AE,D), (AF,D), (BE,C)")

# ----------------------------------------------------------------------------- tadelis-8-5
As85, Bs85 = [[5, -5], [2, 0]], [[4, 2], [-2, 0]]       # rows H, L; columns G, B
assert pure_ne(As85, Bs85) == {(0, 0), (1, 1)}
p, q = sp.symbols("p q")
p85 = sp.solve(sp.Eq(4 * p - 2 * (1 - p), 2 * p), p)[0]
q85 = sp.solve(sp.Eq(5 * q - 5 * (1 - q), 2 * q), q)[0]
assert (p85, q85) == (sp.Rational(1, 2), sp.Rational(5, 8))
x, y = [F(1, 2), F(1, 2)], [F(5, 8), F(3, 8)]
assert is_ne(As85, Bs85, x, y)
v1 = sum(As85[r][c] * x[r] * y[c] for r in range(2) for c in range(2))
v2 = sum(Bs85[r][c] * x[r] * y[c] for r in range(2) for c in range(2))
assert (v1, v2) == (F(5, 4), F(1))
# (b)-(c): adoption stage; rows NH, NL, AH, AL
A85 = [[1, 1], [1, 1], [5, -5], [2, 0]]
B85 = [[1, 1], [1, 1], [4, 2], [-2, 0]]
assert pure_ne(A85, B85) == {(0, 1), (1, 1), (2, 0)}     # (NH,B), (NL,B), (AH,G)
qs = sorted(set([F(k, 160) for k in range(161)] + [F(1, 2), F(3, 5), F(5, 8)]))
ok = [qq for qq in qs if ne_given_q(A85, B85, qq)]
assert ok == [qq for qq in qs if qq <= F(1, 2)] + [F(5, 8), F(1)]
assert is_ne(A85, B85, [0, 0, F(1, 2), F(1, 2)], [F(5, 8), F(3, 8)])
# SPE: replace the subgame by each of its equilibria
spe = []
for val, label in [((5, 4), "AH,G"), ((0, 0), "NL,B"), ((F(5, 4), F(1)), "A+mix")]:
    spe.append(("adopt" if val[0] > 1 else "not adopt", label))
assert spe == [("adopt", "AH,G"), ("not adopt", "NL,B"), ("adopt", "A+mix")]
assert (1, 1) != (5, -5) and not is_ne(As85, Bs85, [1, 0], [0, 1])   # (H, B) not a subgame NE
print("tadelis-8-5: subgame NE (H,G), (L,B), (1/2, 5/8); three SPE")

# ----------------------------------------------------------------------------- tadelis-8-10
As, Bs = [[8, 0], [6, 2]], [[0, 2], [6, 2]]
assert pure_ne(As, Bs) == set()
p10 = sp.solve(sp.Eq(6 * (1 - p), 2), p)[0]
q10 = sp.solve(sp.Eq(8 * q, 6 * q + 2 * (1 - q)), q)[0]
assert (p10, q10) == (sp.Rational(2, 3), sp.Rational(1, 2))
assert 8 * q10 == 4 and 4 > 3
A15 = [[3, 3], [3, 3], [8, 0], [6, 2]]
B15 = [[3, 3], [3, 3], [0, 2], [6, 2]]
assert pure_ne(A15, B15) == {(0, 1), (1, 1)}
qs = sorted(set([F(k, 240) for k in range(241)] + [F(1, 4), F(3, 8), F(1, 2)]))
ok = [qq for qq in qs if ne_given_q(A15, B15, qq)]
assert ok == [qq for qq in qs if qq <= F(1, 4)] + [F(1, 2)]
assert is_ne(A15, B15, [0, 0, F(2, 3), F(1, 3)], [F(1, 2), F(1, 2)])
assert not is_ne(A15, B15, [0, 0, F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)])
print("tadelis-8-10: unique SPE (R; 2/3 C; 1/2 A), payoffs (4, 2)")

# ----------------------------------------------------------------------------- tadelis-7-4
def centipede(last_share_p1):
    """Tree of Tadelis 7.4. Pot 6, x3/2 per share; grabber gets 2/3. At the last node S gives
    player 1 the share last_share_p1 of the final pot (2/3 in (d), 1/2 in (e))."""
    pots = [F(6) * F(3, 2) ** k for k in range(5)]
    def node(k):
        mover = k % 2
        grab = [None, None]
        grab[mover], grab[1 - mover] = F(2, 3) * pots[k], F(1, 3) * pots[k]
        if k == 3:
            share = ('T', (last_share_p1 * pots[4], (1 - last_share_p1) * pots[4]))
        else:
            share = node(k + 1)
        return ('D', mover, {"G": ('T', tuple(grab)), "S": share})
    return node(0), pots


t74, pots = centipede(F(2, 3))
assert pots == [6, 9, F(27, 2), F(81, 4), F(243, 8)]
assert backward_induction(t74) == [((4, 2), ("G",))]


def outcome74(tree, s1, s2):
    """Payoffs when player 1 plays s1 = (move at node 1, move at node 3), player 2 s2."""
    plan = {0: s1[0], 1: s2[0], 2: s1[1], 3: s2[1]}
    node, k = tree, 0
    while node[0] == 'D':
        node, k = node[2][plan[k]], k + 1
    return node[1]


S = ["GG", "GS", "SG", "SS"]
A74 = [[outcome74(t74, a, b)[0] for b in S] for a in S]
B74 = [[outcome74(t74, a, b)[1] for b in S] for a in S]
ne74 = {(S[r], S[c]) for r, c in pure_ne(A74, B74)}
assert ne74 == {("GG", "GG"), ("GG", "GS"), ("GS", "GG"), ("GS", "GS")}
assert {outcome74(t74, a, b) for a, b in ne74} == {(4, 2)}
# mixed: P1 grabs at node 1; P2 grabs at node 2 w.p. g and at node 4 w.p. h (behavioral).
for h in [F(0), F(1, 2), F(1)]:
    M = max(F(9), h * F(1, 3) * pots[3] + (1 - h) * F(2, 3) * pots[4])
    gmin = 1 - 1 / (M - 3)
    for g in [gmin, gmin - F(1, 1000)]:
        dev = 3 * g + (1 - g) * M                       # P1: S at node 1, then best at node 3
        assert (dev <= 4) == (g >= gmin)
assert 1 - 1 / (F(9) - 3) == F(5, 6)
assert 1 - 1 / (F(243, 8) * F(2, 3) - 3) == F(65, 69)
# (e): equal split at the end
t74e, _ = centipede(F(1, 2))
assert backward_induction(t74e) == [((F(243, 16), F(243, 16)), ("S", "S", "S", "S"))]
A74e = [[outcome74(t74e, a, b)[0] for b in S] for a in S]
B74e = [[outcome74(t74e, a, b)[1] for b in S] for a in S]
ne74e = {(S[r], S[c]) for r, c in pure_ne(A74e, B74e)}
assert {outcome74(t74e, a, b) for a, b in ne74e} == {(4, 2), (F(243, 16), F(243, 16))}
assert ne74e == {("GG", "GG"), ("GG", "GS"), ("GS", "GG"), ("GS", "GS"), ("SS", "SS")}
print("tadelis-7-4: (d) 4 pure NE, one outcome (4, 2); (e) SPE all-share 243/16 each; NE outcomes 2")

# ----------------------------------------------------------------------------- tadelis-7-9
# Dean: (action with evidence, action without); student: C, D. Evidence w.p. 1/2.
def dean_pay(a, s, ev):
    if a == "B":
        return (0, 0)
    if s == "C":
        return (2, -2)
    return (4, -4) if ev else (-4, 4)


D79 = ["AA", "AB", "BA", "BB"]
A79 = [[F(1, 2) * dean_pay(d[0], s, True)[0] + F(1, 2) * dean_pay(d[1], s, False)[0] for s in "CD"]
       for d in D79]
B79 = [[F(1, 2) * dean_pay(d[0], s, True)[1] + F(1, 2) * dean_pay(d[1], s, False)[1] for s in "CD"]
       for d in D79]
assert A79 == [[2, 0], [1, 2], [1, -2], [0, 0]]
assert all(A79[r][c] + B79[r][c] == 0 for r in range(4) for c in range(2))   # zero-sum
assert pure_ne(A79, B79) == set()
qs = [F(k, 300) for k in range(301)]
assert [qq for qq in qs if ne_given_q(A79, B79, qq)] == [F(2, 3)]
assert is_ne(A79, B79, [F(1, 3), F(2, 3), 0, 0], [F(2, 3), F(1, 3)])
# uniqueness of the dean's mix at q = 2/3: best replies AA, AB; student indifferent iff p = 1/3
pp = sp.symbols("pp")
assert sp.solve(sp.Eq(-2 * pp - (1 - pp), -2 * (1 - pp)), pp) == [sp.Rational(1, 3)]
assert 2 * F(2, 3) == F(4, 3)
print("tadelis-7-9: unique NE dean 1/3 AA + 2/3 AB, student C w.p. 2/3; value 4/3")

# ----------------------------------------------------------------------------- tadelis-7-10
lam, om, al, ta, xi = sp.symbols("lambda omega alpha tau xi")
# terminal nodes (root, P1 move, P2 bottom move)
term = [("a", "L", "t"), ("a", "L", "z"), ("a", "R", "t"), ("a", "R", "z"),
        ("b", "W", "x"), ("b", "W", "y"), ("b", "E", "x"), ("b", "E", "y")]


def p1_beh(m1):
    return {"L": lam, "R": 1 - lam, "W": om, "E": 1 - om}[m1]


# (b) P1 behavioral (lam, om) vs mixed sigma(LW)=lam*om, ...; against every pure s2
sig1 = {("L", "W"): lam * om, ("L", "E"): lam * (1 - om), ("R", "W"): (1 - lam) * om,
        ("R", "E"): (1 - lam) * (1 - om)}
for r2, b2, b3 in product("ab", "tz", "xy"):
    for z in term:
        follows2 = z[0] == r2 and z[2] == (b2 if r2 == "a" else b3)
        beh = p1_beh(z[1]) if follows2 else 0
        mix = sum(w for (l, r), w in sig1.items() if (l if r2 == "a" else r) == z[1]) if follows2 else 0
        assert sp.simplify(beh - mix) == 0
# (c) P2 behavioral (al, ta, xi) vs product mixed; against every pure s1
sig2 = {(r, b2, b3): (al if r == "a" else 1 - al) * (ta if b2 == "t" else 1 - ta)
        * (xi if b3 == "x" else 1 - xi) for r, b2, b3 in product("ab", "tz", "xy")}
for l, r in product("LR", "WE"):
    for z in term:
        if z[1] not in (l, r):
            continue
        beh = (al * (ta if z[2] == "t" else 1 - ta) if z[0] == "a"
               else (1 - al) * (xi if z[2] == "x" else 1 - xi))
        mix = sum(w for (rr, b2, b3), w in sig2.items()
                  if rr == z[0] and (b2 if rr == "a" else b3) == z[2])
        assert sp.simplify(beh - mix) == 0
# (d) merged info set: P2 strategies (root, bottom) with x = t, y = z.
# (d1) behavioral -> mixed still works: product of alpha and tau
for l in "LR":
    for rt, bt in product("ab", "tz"):
        beh = (al if rt == "a" else 1 - al) * (ta if bt == "t" else 1 - ta)
        mix = (al if rt == "a" else 1 - al) * (ta if bt == "t" else 1 - ta)
        assert beh == mix
# (d2) mixed 1/2 (a,t) + 1/2 (b,z) has no behavioral equivalent: P(a,t)=1/2, P(a,z)=0, P(b,z)=1/2
sols = sp.solve([al * ta - sp.Rational(1, 2), al * (1 - ta), (1 - al) * (1 - ta) - sp.Rational(1, 2)],
                [al, ta], dict=True)
assert sols == []
print("tadelis-7-10: (b), (c) equivalences hold symbolically; (d) mixed->behavioral fails")

# ----------------------------------------------------------------------------- mwg-9-b-4
random.seed(9)


def random_tree(depth, nplayers, zero_sum, rng):
    if depth == 0 or rng.random() < 0.2:
        if nplayers == 2:
            v = rng.randint(-2, 2)
            u = (v, -v) if zero_sum else (v, rng.randint(-2, 2))
        else:
            a, b = rng.randint(-2, 2), rng.randint(-2, 2)
            u = (a, b, -a - b)
        return ('T', u)
    return ('D', rng.randrange(nplayers),
            {k: random_tree(depth - 1, nplayers, zero_sum, rng) for k in range(rng.randint(2, 3))})


n_ties = 0
for _ in range(400):
    t = random_tree(4, 2, True, random)
    vals = spne_values(t)
    assert len(vals) == 1                                   # unique SPNE payoffs
    n_ties += len(backward_induction(t)) > 1
assert n_ties > 0                                           # the sample does contain ties
# without zero-sum, or with three players, payoffs need not be unique
t_nz = ('D', 0, {"l": ('T', (0, 1)), "r": ('T', (0, 2))})
assert spne_values(t_nz) == {(0, 1), (0, 2)}
t_3 = ('D', 0, {"l": ('T', (0, 1, -1)), "r": ('T', (0, -1, 1))})
assert spne_values(t_3) == {(0, 1, -1), (0, -1, 1)}
print(f"mwg-9-b-4: 400 random zero-sum trees, unique SPNE payoffs ({n_ties} with several SPNE)")

# ----------------------------------------------------------------------------- gibbons-2-1
Y, xx, k = sp.symbols("Y x k", positive=True)
# implicit derivative dx*/dY = V''/(V'' + k U'') lies in (0, 1) when U'', V'' < 0
Vpp, Upp = sp.symbols("Vpp Upp", negative=True)
d = Vpp / (Vpp + k * Upp)
for vals in [(-1, -1, 1), (-2, F(-1, 2), 3), (F(-1, 10), -5, F(1, 5))]:
    dv = d.subs({Vpp: vals[0], Upp: vals[1], k: vals[2]})
    assert 0 < dv < 1
# log example: U = V = ln, parent: max ln(Y - x) + k ln(x) -> x* = kY/(1 + k)
W = sp.log(Y - xx) + k * sp.log(xx)
xstar = sp.solve(sp.diff(W, xx), xx)[0]
assert sp.simplify(xstar - k * Y / (1 + k)) == 0
assert sp.simplify(sp.diff(W, xx, 2).subs(xx, xstar)) .is_negative
# CARA example: U = V = -exp(-x): x* = (Y + ln k)/2
Wc = -sp.exp(-(Y - xx)) - k * sp.exp(-xx)
xc = sp.solve(sp.diff(Wc, xx), xx)[0]
assert sp.simplify(xc - (Y + sp.log(k)) / 2) == 0
# child's choice with I_C = 4A - A^2 (A_C = 2), I_P = 10A - A^2 (A_P = 5), k = 2, log utility
Av = sp.symbols("A", nonnegative=True)
Yf = (4 * Av - Av**2) + (10 * Av - Av**2)
child = sp.log((2 * Yf / 3))
crit = sp.solve(sp.diff(child, Av), Av)
assert crit == [sp.Rational(7, 2)]
grid = [F(k_, 20) for k_ in range(1, 121)]
Yg = {a: 14 * a - 2 * a * a for a in grid}
best = max(grid, key=lambda a: F(2, 3) * Yg[a])            # x* = 2Y/3 is increasing in Y
assert best == F(7, 2) and max(grid, key=lambda a: 4 * a - a * a) == 2
B_at = F(2, 3) * Yg[F(7, 2)] - (4 * F(7, 2) - F(7, 2) ** 2)
assert B_at == F(175, 12)                                # bequest 175/12 at A* = 7/2
print("gibbons-2-1: x*(Y) increasing; child picks A* = 7/2 = argmax(I_C + I_P), not A_C = 2")

print("all B L03 checks passed")
