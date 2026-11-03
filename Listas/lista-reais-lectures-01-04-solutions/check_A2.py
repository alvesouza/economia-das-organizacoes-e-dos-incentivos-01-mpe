"""Checks items 7-12 (Lecture 2 block): Tadelis 5.6, Munoz-Garcia Ch. 3 Ex. 1, Tadelis 5.8,
Tadelis 6.8, Gibbons 1.6, MWG 8.D.6. Symbolic steps with sympy, brute force on grids as a second route.

Run: python check_A2.py  -> prints "all A2 checks passed" or fails on the first wrong claim.
"""
import random
from fractions import Fraction as F
from itertools import product

import numpy as np
import sympy as sp

random.seed(0)


def pure_ne(S, u):
    """All pure profiles where no player gains by a unilateral deviation; u(i, profile) -> payoff."""
    ne = []
    for p in product(*S):
        if all(u(i, p) >= u(i, p[:i] + (t,) + p[i + 1:]) for i in range(len(S)) for t in S[i]):
            ne.append(p)
    return ne


# ---- item 7: Tadelis 5.6 Hawk-Dove
v, k, d = sp.symbols("v k d", real=True)
hd = {("H", "H"): (v / 2 - k, v / 2 - k), ("H", "D"): (v, sp.S(0)), ("D", "H"): (sp.S(0), v),
      ("D", "D"): (v / 2 - d, v / 2 - d)}
num = {s: tuple(sp.nsimplify(x.subs({v: 10, k: 6, d: 4})) for x in pay) for s, pay in hd.items()}
assert num == {("H", "H"): (-1, -1), ("H", "D"): (10, 0), ("D", "H"): (0, 10), ("D", "D"): (1, 1)}
assert pure_ne([["H", "D"]] * 2, lambda i, p: num[p][i]) == [("H", "D"), ("D", "H")]
for _ in range(2000):                            # any admissible (v, k, d): same two pure NE
    vv = random.uniform(0.1, 20)
    kk = random.uniform(vv / 2 + 1e-6, 3 * vv)
    dd = random.uniform(0, vv / 2 - 1e-6)
    cells = {s: tuple(float(x.subs({v: vv, k: kk, d: dd})) for x in pay) for s, pay in hd.items()}
    assert pure_ne([["H", "D"]] * 2, lambda i, p: cells[p][i]) == [("H", "D"), ("D", "H")]
p = sp.symbols("p")
ph = sp.solve(sp.Eq(-p + 10 * (1 - p), 1 - p), p)
assert ph == [sp.Rational(9, 10)] and (1 - ph[0]) == sp.Rational(1, 10)

# ---- item 8: Munoz-Garcia Ch. 3 Ex. 1, Chicken (index 0 = Straight, 1 = Swerve)
ch = {(0, 0): (0, 0), (0, 1): (3, 1), (1, 0): (1, 3), (1, 1): (2, 2)}
u8 = lambda i, s: ch[s][i]
assert pure_ne([[0, 1]] * 2, u8) == [(0, 1), (1, 0)]
# no strictly dominated strategy: each row is the unique best reply to some column
assert ch[1, 0][0] > ch[0, 0][0] and ch[0, 1][0] > ch[1, 1][0]
q = sp.symbols("q")
EU1St, EU1Sw = 0 * q + 3 * (1 - q), 1 * q + 2 * (1 - q)
assert sp.solve(sp.Eq(EU1St, EU1Sw), q) == [sp.Rational(1, 2)]
assert sp.solve(sp.Eq(3 * (1 - p), p + 2 * (1 - p)), p) == [sp.Rational(1, 2)]
assert EU1St.subs(q, sp.Rational(1, 2)) == sp.Rational(3, 2)
assert sp.solve(sp.Eq(3 + 3 * q, q + 2 - 2 * q), q) == [sp.Rational(-1, 4)]   # the book's typo line
assert sp.expand(EU1St - EU1Sw) == 1 - 2 * q
# grid of mixed profiles: mutual best responses are exactly (1,0), (0,1), (1/2,1/2)
grid = [F(i, 100) for i in range(101)]


def br_ok(own, gain):
    """own is a best reply given the gain from the first pure strategy (in probability units)."""
    return (gain > 0 and own == 1) or (gain < 0 and own == 0) or gain == 0


mutual = [(pp, qq) for pp in grid for qq in grid if br_ok(pp, 1 - 2 * qq) and br_ok(qq, 1 - 2 * pp)]
assert mutual == [(0, 1), (F(1, 2), F(1, 2)), (1, 0)]

# ---- item 9: Tadelis 5.8, n-firm Cournot with P = a - Q, cost c q_i
a, c = sp.symbols("a c", positive=True)
for n in range(1, 7):
    qs = sp.symbols(f"q1:{n + 1}")
    Q = sum(qs)
    foc = [sp.diff((a - Q) * qi - c * qi, qi) for qi in qs]
    sol = sp.solve(foc, qs, dict=True)
    assert len(sol) == 1
    for qi in qs:
        assert sp.simplify(sol[0][qi] - (a - c) / (n + 1)) == 0
    Qs = sp.simplify(Q.subs(sol[0]))
    assert sp.simplify(Qs - n * (a - c) / (n + 1)) == 0
    Ps = sp.simplify(a - Qs)
    assert sp.simplify(Ps - (a + n * c) / (n + 1)) == 0
    assert sp.simplify(Ps - c - (a - c) / (n + 1)) == 0
    assert sp.simplify((Ps - c) * (a - c) / (n + 1) - ((a - c) / (n + 1))**2) == 0
nn = sp.symbols("n", positive=True)
assert sp.limit((a + nn * c) / (nn + 1), nn, sp.oo) == c
# numeric deviation check, a = 100, c = 10, n = 3: q* = 22.5, others at q*, deviations on a fine grid
qstar, others = 22.5, 2 * 22.5
prof = lambda qi: max(0.0, 100 - qi - others) * qi - 10 * qi
best = prof(qstar)
assert abs(best - 22.5**2) < 1e-9
assert all(prof(x) <= best + 1e-9 for x in np.linspace(0, 150, 30001))

# ---- item 10: Tadelis 6.8 market entry, entrant earns 150/n - 62
pi = lambda n: F(150, n) - 62
assert [pi(1), pi(2), pi(3)] == [88, 13, -12]
u10 = lambda i, s: pi(sum(s)) if s[i] == 1 else 0
assert pure_ne([[0, 1]] * 3, u10) == [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
uE = (1 - p)**2 * 88 + 2 * p * (1 - p) * 13 + p**2 * (-12)
assert sp.expand(uE - (88 - 150 * p + 50 * p**2)) == 0
assert sorted(sp.solve(uE, p)) == [sp.Rational(4, 5), sp.Rational(11, 5)]
assert uE.subs(p, sp.Rational(4, 5)) == 0
assert all(uE.subs(p, F(i, 100)) > 0 for i in range(0, 80))
assert all(uE.subs(p, F(i, 100)) < 0 for i in range(81, 101))
assert F(4, 5)**3 == F(64, 125)                  # all three enter with probability 0.512

# ---- item 11: Gibbons 1.6, asymmetric Cournot with P = max(0, a - Q)
c1, c2, q1, q2 = sp.symbols("c1 c2 q1 q2", real=True)
sol = sp.solve([sp.diff((a - q1 - q2 - c1) * q1, q1), sp.diff((a - q1 - q2 - c2) * q2, q2)], [q1, q2])
assert sp.simplify(sol[q1] - (a - 2 * c1 + c2) / 3) == 0 and sp.simplify(sol[q2] - (a - 2 * c2 + c1) / 3) == 0
Pst = a - sol[q1] - sol[q2]
assert sp.simplify(Pst - (a + c1 + c2) / 3) == 0
assert sp.simplify((Pst - c1) * sol[q1] - sol[q1]**2) == 0


def br11(qj, ci, A):
    return max(F(0), (A - ci - qj) / 2)


def ne11(A, C1, C2):
    """Iterate exact best responses (a contraction, slope 1/2) from (0, 0) to the NE."""
    x, y = F(0), F(0)
    for _ in range(200):
        x, y = br11(y, C1, A), br11(x, C2, A)
    return x, y


def profit11(qi, qj, ci, A):
    return max(F(0), A - qi - qj) * qi - ci * qi


A = F(100)
for _ in range(300):                             # case 1: 0 < c_i < a/2
    C1, C2 = F(random.randint(1, 4999), 100), F(random.randint(1, 4999), 100)
    x, y = ne11(A, C1, C2)
    assert abs(x - (A - 2 * C1 + C2) / 3) < F(1, 10**30) and abs(y - (A - 2 * C2 + C1) / 3) < F(1, 10**30)
for _ in range(300):                             # case 2: c1 < c2 < a, 2 c2 > a + c1
    C1 = F(random.randint(0, 9800), 100)
    lo = max(C1, (A + C1) / 2)
    C2 = lo + (A - lo) * F(random.randint(1, 999), 1000)
    assert C1 < C2 < A and 2 * C2 > A + C1
    x, y = ne11(A, C1, C2)
    assert x == (A - C1) / 2 and y == 0 and A - x < C2
# deviation grid at one point of each case, including outputs with Q > a
for C1, C2, x, y in [(F(10), F(20), F(100, 3), F(70, 3)), (F(10), F(70), F(45), F(0))]:
    for z in [F(i, 4) for i in range(0, 601)]:
        assert profit11(z, y, C1, A) <= profit11(x, y, C1, A)
        assert profit11(z, x, C2, A) <= profit11(y, x, C2, A)

# ---- item 12: MWG 8.D.6, existence in every 2x2 game
U, L_, W, Y, V, M, X, Z, pp_, qq_ = sp.symbols("u l w y v m x z p q", real=True)
D1 = (qq_ * U + (1 - qq_) * L_) - (qq_ * W + (1 - qq_) * Y)
D2 = (pp_ * V + (1 - pp_) * X) - (pp_ * M + (1 - pp_) * Z)
assert sp.expand(D1 - (qq_ * (U - W) + (1 - qq_) * (L_ - Y))) == 0
assert sp.expand(D2 - (pp_ * (V - M) + (1 - pp_) * (X - Z))) == 0
assert sp.simplify(sp.solve(D1, qq_)[0] - (Y - L_) / ((U - W) + (Y - L_))) == 0
assert sp.simplify(sp.solve(D2, pp_)[0] - (Z - X) / ((V - M) + (Z - X))) == 0


def gains(g):
    """g = (u, l, w, y, v, m, x, z); returns D1(q), D2(p) as functions."""
    u, l, w, y, v, m, x, z = g
    return (lambda q: q * (u - w) + (1 - q) * (l - y)), (lambda p: p * (v - m) + (1 - p) * (x - z))


def construct(g):
    """The case construction of item 12; returns (p, q)."""
    D1, D2 = gains(g)
    pick = lambda D: 1 if D >= 0 else 0           # a pure best reply given the gain
    if D1(0) >= 0 and D1(1) >= 0:                  # case A
        return 1, pick(D2(1))
    if D1(0) <= 0 and D1(1) <= 0:                  # case B
        return 0, pick(D2(0))
    qs = F(D1(0)) / (D1(0) - D1(1))                # case C
    if D2(0) >= 0 and D2(1) >= 0:
        return pick(D1(1)), 1
    if D2(0) <= 0 and D2(1) <= 0:
        return pick(D1(0)), 0
    ps = F(D2(0)) / (D2(0) - D2(1))
    assert 0 < ps < 1 and 0 < qs < 1
    return ps, qs


def is_ne(g, p, q):
    D1, D2 = gains(g)
    return br_ok(p, D1(q)) and br_ok(q, D2(p))


manual_undefined = 0
for trial in range(20000):
    if trial % 2:
        g = tuple(F(random.randint(-2, 2)) for _ in range(8))
    else:
        g = tuple(F(random.randint(-1000, 1000), 97) for _ in range(8))
    p0, q0 = construct(g)
    assert 0 <= p0 <= 1 and 0 <= q0 <= 1 and is_ne(g, p0, q0), g
    # the manual's case 5: neither player has a strictly dominant strategy
    u, l, w, y, v, m, x, z = g
    strict1 = (u > w and l > y) or (u < w and l < y)
    strict2 = (v > m and x > z) or (v < m and x < z)
    if not strict1 and not strict2:
        den_a, den_b = u + y - l - w, v + z - x - m
        if den_a == 0 or den_b == 0:
            assert (den_a == 0 and y - l == 0) or (den_b == 0 and z - x == 0)   # 0/0, never k/0
            manual_undefined += 1
            continue
        al, be = (y - l) / den_a, (z - x) / den_b
        assert 0 <= al <= 1 and 0 <= be <= 1 and is_ne(g, be, al), g      # formula works when defined
assert manual_undefined > 0                      # the gap in the manual's "all other cases" occurs

print("all A2 checks passed")
