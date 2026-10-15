"""Checks the continuous-strategy items: 9 (Tadelis 3.6), 13 (MWG 8.B.1), 15 (Tadelis 4.6),
21 (MWG 8.B.5). Symbolic steps with sympy; IESDS on fine grids with numpy as a second route.

Run: python check_B.py  -> prints "all B checks passed" or fails on the first wrong claim.
"""
from fractions import Fraction as F

import numpy as np
import sympy as sp


def iesds_grid(A, B):
    """IESDS (lecture definition, all strictly dominated rows/columns removed each round) on the
    bimatrix (A, B); returns surviving row and column index arrays."""
    R, C = np.arange(A.shape[0]), np.arange(A.shape[1])
    while True:
        a, b = A[np.ix_(R, C)], B[np.ix_(R, C)]
        # row r is dominated if some row beats it in every surviving column
        dr = np.array([(a > a[r]).all(axis=1).any() for r in range(len(R))])
        dc = np.array([(b[:, c][:, None] < b).all(axis=0).any() for c in range(len(C))])
        if not dr.any() and not dc.any():
            return R, C
        R, C = R[~dr], C[~dc]


# ---- item 9: Tadelis 3.6 Bertrand with D(p) = max(0, 100 - p), zero cost, ties split
def u9(pi, pj):
    d = max(0, 100 - pi)
    return pi * d if pi < pj else pi * d / 2 if pi == pj else 0


grid = range(0, 121)
A = np.array([[u9(p, q) for q in grid] for p in grid], dtype=float)
R, C = iesds_grid(A, A.T)
assert len(R) == len(C) == len(grid)                     # nothing strictly dominated
assert (A[:, 0] == 0).all()                              # against p_j = 0 every price earns 0
assert all((A[50] >= A[p]).all() and (A[50] > A[p]).any() for p in range(100, 121))  # p >= 100 weakly dominated by 50
assert (A[50] >= A[0]).all() and (A[50] > A[0]).any()            # p = 0 weakly dominated by 50
p = sp.symbols("p", real=True)
assert sp.solve(sp.diff(p * (100 - p), p), p) == [50]

# ---- item 13: MWG 8.B.1
a, b, w, h, P, hs = sp.symbols("alpha beta w h P h_star", real=True)
# firm i's payoff, up to terms that do not involve h_i: (alpha + beta*P) h - w h^2, P = prod_{j != i} h_j
ui = (a + b * P) * h - w * h**2
br = sp.solve(sp.diff(ui, h), h)[0]
assert sp.simplify(br - (a + b * P) / (2 * w)) == 0
assert sp.diff(ui, h, 2) == -2 * w                       # strictly concave for w > 0
# beta = 0: u(h*) - u(h) = w (h - h*)^2 with h* = alpha/(2w), independent of the others
gap = sp.simplify((ui.subs(b, 0).subs(h, a / (2 * w)) - ui.subs(b, 0)))
assert sp.simplify(gap - w * (h - a / (2 * w))**2) == 0


def br13(al, be, Pv, wv=1.0):
    return max(0.0, (al + be * Pv) / (2 * wv))


Ps = [0.0, 0.5, 1.0, 3.0, 10.0, 1e3]                     # attainable values of prod_{j != i} h_j
for al, be in [(1, 0), (0, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (0, 1), (0, -1), (-1, -1)]:
    constant = len({br13(al, be, x) for x in Ps}) == 1
    # constant best reply  <=>  beta = 0, or (beta < 0 and alpha <= 0): the corner case
    assert constant == (be == 0 or (be < 0 and al <= 0)), (al, be)

# ---- items 15 and 21: the quadratic-payoff lemma u(a) - u(t) = k (t - a)(t + a - 2x)
t, s, x, k = sp.symbols("t s x k", real=True)
quad = lambda z: k * z * (2 * x - z)                     # payoff with unconstrained peak at x
assert sp.factor(quad(s) - quad(t)) in (sp.factor(k * (t - s) * (t + s - 2 * x)),
                                       sp.factor(-k * (s - t) * (t + s - 2 * x)))
# roommates: (10 - t_j) t_i - t_i^2 = 1 * t_i (2x - t_i) with x = (10 - t_j)/2
ti, tj = sp.symbols("t_i t_j", real=True)
assert sp.expand((10 - tj) * ti - ti**2 - quad(ti).subs({k: 1, x: (10 - tj) / 2})) == 0
assert sp.solve(sp.diff((10 - tj) * ti - ti**2, ti), ti) == [5 - tj / 2]
# Cournot: (a - b(q_i + q_j) - c) q_i = b q_i (2x - q_i) with x = m - q_j/2, m = (a - c)/(2b)
A_, B_, c_, qi, qj = sp.symbols("a b c q_i q_j", positive=True)
m = (A_ - c_) / (2 * B_)
assert sp.expand((A_ - B_ * (qi + qj) - c_) * qi - quad(qi).subs({k: B_, x: m - qj / 2})) == 0


def rounds(m, K):
    """Intervals S^k = [L_k, U_k], k = 1..K, for best reply max(0, m - q/2) starting from [0, inf)."""
    L, U, out = F(0), m, [(F(0), m)]
    for _ in range(K - 1):
        L, U = max(F(0), m - U / 2), m - L / 2
        out.append((L, U))
    return out


r15 = rounds(F(5), 40)
assert r15[:4] == [(0, 5), (F(5, 2), 5), (F(5, 2), F(15, 4)), (F(25, 8), F(15, 4))]
assert r15[4] == (F(25, 8), F(55, 16))                             # [3.125, 3.4375]
u15 = lambda a_, b_: (10 - b_) * a_ - a_ * a_
assert u15(F(10, 3), F(10, 3)) == F(100, 9) and u15(F(5, 2), F(5, 2)) == F(25, 2)
assert sp.solve(sp.diff(2 * ((10 - t) * t - t**2), t), t) == [sp.Rational(5, 2)]  # joint optimum
for kk, (L, U) in enumerate(r15, start=1):
    assert U - L == F(5, 2**(kk - 1))                                      # width halves
    assert (L + U) / 2 - F(10, 3) == F(-1, 2)**(kk - 1) * F(-5, 6)         # midpoint closed form
assert abs(float(r15[-1][0]) - 10 / 3) < 1e-10
# grid route for roommates: times in multiples of 1/6 on [0, 10]
g = np.arange(0, 61) / 6
U15 = np.array([[(10 - y) * z - z * z for y in g] for z in g])
R, C = iesds_grid(U15, U15.T)
assert np.allclose(g[R], [10 / 3]) and np.allclose(g[C], [10 / 3])

# Cournot duopoly with m = (a - c)/(2b): limit 2m/3 = (a - c)/(3b)
mm = F(1)
r21 = rounds(mm, 60)
assert r21[:3] == [(0, 1), (F(1, 2), 1), (F(1, 2), F(3, 4))]
assert r21[3] == (F(5, 8), F(3, 4))
assert all(U - L == F(1, 2**(kk - 1)) for kk, (L, U) in enumerate(r21, start=1))
assert abs(float(r21[-1][1]) - 2 / 3) < 1e-12
assert sp.simplify(sp.Rational(2, 3) * m - (A_ - c_) / (3 * B_)) == 0
fp = sp.solve(sp.Eq(qi, m - qi / 2), qi)[0]
assert sp.simplify(fp - (A_ - c_) / (3 * B_)) == 0
# three firms: best reply to Q = q_j + q_h is max(0, m - Q/2); every q in [0, m] is the unique
# best reply to Q = 2(m - q), which splits as two quantities in [0, m]; so S^1 = S^2 = [0, m]
for q in [F(0), F(1, 4), F(1, 2), F(1)]:
    Q = 2 * (mm - q)
    assert 0 <= Q <= 2 * mm and max(F(0), mm - Q / 2) == q and 0 <= Q / 2 <= mm
assert max(F(0), mm - (2 * mm) / 2) == 0                # lower bound stays at 0
# grid route for three firms: a - c = 12, b = 1 (m = 6), quantities 0, 0.5, ..., 14
gq = np.arange(0, 29) / 2


def u3(q, Q):
    return (12 - (q + Q)) * q


surv = list(range(len(gq)))
while True:
    pairs = [gq[j] + gq[l] for j in surv for l in surv]
    pay = np.array([[u3(gq[i], Q) for Q in pairs] for i in surv])
    dom = [any((pay[r2] > pay[r1]).all() for r2 in range(len(surv))) for r1 in range(len(surv))]
    if not any(dom):
        break
    surv = [s_ for s_, d in zip(surv, dom) if not d]
assert np.allclose(gq[surv], np.arange(0, 13) / 2)      # all of [0, m] = [0, 6] survives

print("all B checks passed")
