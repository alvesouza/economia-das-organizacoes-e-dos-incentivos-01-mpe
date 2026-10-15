"""Checks every number and closed form stated in items 06, 07, 08, 16, 17, 23, 26, 27.

Run: python check_C.py  -> prints "all C checks passed" or fails on the first wrong assertion.
"""
from sympy import Rational as R, symbols, solve, diff, log, exp, sqrt, simplify, Eq

y, t, s, z = symbols("y t s z", real=True)
half = R(1, 2)

# --- item 06: Edgeworth box, u = ln x1 + ln x2 for both, totals (10,10), omega_A = (8,2)
# contract curve x2/x1 = (10-x2)/(10-x1) is the diagonal
x1, x2 = symbols("x1 x2", positive=True)
assert solve(Eq(x2 / x1, (10 - x2) / (10 - x1)), x2) == [x1]
uA0 = log(8) + log(2)
assert sorted(solve(Eq(2 * log(t), uA0), t)) == [4]
assert sorted(solve(Eq(2 * log(10 - t), uA0), t)) == [6]
# CE with p1 = p2 = 1: A's income 10, half on each good
assert R(8 + 2, 2) == 5
# symmetric Nash product maximized at t = 5
nash = (2 * log(t) - uA0) * (2 * log(10 - t) - uA0)
assert simplify(diff(nash, t).subs(t, 5)) == 0
assert diff(nash, t).subs(t, R(9, 2)).evalf() > 0 and diff(nash, t).subs(t, R(11, 2)).evalf() < 0

# --- item 07: WTP / WTA with u = ln x + a y, w = 100, a = ln 1.5, gain 40
a, w, G = log(R(3, 2)), 100, 40
WTP = simplify(w * (1 - exp(-a)))
WTA = simplify(w * (exp(a) - 1))
assert WTP == R(100, 3) and WTA == 50
assert WTP < G < WTA
assert simplify(log(w - WTP) + a - log(w)) == 0
assert simplify(log(w + WTA) - log(w) - a) == 0

# --- item 08: v_A = 6s - s^2, v_B = -s^2
vA, vB = 6 * s - s**2, -s**2
s_star = solve(diff(vA + vB, s), s)[0]
assert s_star == R(3, 2) and (vA + vB).subs(s, s_star) == R(9, 2)
assert (vA + vB).subs(s, 0) == 0 and (vA + vB).subs(s, 3) == 0
assert vA.subs(s, s_star) == R(27, 4) and vB.subs(s, s_star) == R(-9, 4) and vA.subs(s, 3) == 9
assert diff(vA, s).subs(s, s_star) == 3 == -diff(vB, s).subs(s, s_star)
# rights to A: T in [2.25, 6.75]; Nash T = 4.5; payoffs (11.25, -6.75)
lo, hi = vA.subs(s, 3) - vA.subs(s, s_star), vB.subs(s, s_star) - vB.subs(s, 3)
assert lo == R(9, 4) and hi == R(27, 4)
T = (lo + hi) / 2
assert T == R(9, 2)
assert (vA.subs(s, s_star) + T, vB.subs(s, s_star) - T) == (R(45, 4), R(-27, 4))
# rights to B: A pays T; payoffs (2.25, 2.25)
assert (vA.subs(s, s_star) - T, vB.subs(s, s_star) + T) == (R(9, 4), R(9, 4))
assert R(45, 4) - R(9, 4) == 9  # value of the right

# --- item 16: beach, v1 = v2 = 5y - y^2/2, v3 = 7y - y^2/2, v4 = 4y - y^2
v = [5 * y - half * y**2, 5 * y - half * y**2, 7 * y - half * y**2, 4 * y - y**2]
W = sum(v) - y
assert simplify(W - (20 * y - R(5, 2) * y**2)) == 0
assert simplify(sum(diff(vi, y) for vi in v) - (21 - 5 * y)) == 0
assert solve(diff(W, y), y) == [4] and diff(W, y, 2) == -5
assert [vi.subs(y, 4) for vi in v] == [12, 12, 20, 0]
assert [diff(vi, y).subs(y, 4) for vi in v] == [1, 1, 3, -4]
assert W.subs(y, 4) == 40 and W.subs(y, R(39, 10)) == R(39975, 1000) == W.subs(y, R(41, 10))
assert solve(diff(v[3], y), y) == [2]

# --- item 17: equal shares
n = [vi - y / 4 for vi in v]
assert [ni.subs(y, 4) for ni in n] == [11, 11, 19, -1]
assert [max(solve(ni, y)) for ni in n] == [R(19, 2), R(19, 2), R(27, 2), R(15, 4)]
ybar = R(15, 4)
nb = [ni.subs(y, ybar) for ni in n]
assert nb == [R(1380, 128), R(1380, 128), R(2340, 128), 0]  # 10.78125, 18.28125
assert float(nb[0]) == 10.78125 and float(nb[2]) == 18.28125
assert W.subs(y, ybar) == R(3984375, 100000) == sum(nb)
gain = W.subs(y, 4) - W.subs(y, ybar)
assert gain == R(5, 32)
assert solve(diff(n[3], y), y) == [R(15, 8)]  # family 4's favourite level 1.875
exact_t = [vi.subs(y, 4) - nbi - gain / 4 for vi, nbi in zip(v, nb)]
assert sum(exact_t) == 4 and gain / 4 == R(5, 128)
contrib = [R(118, 100), R(118, 100), R(168, 100), R(-4, 100)]
assert all(abs(c - e) < R(1, 100) for c, e in zip(contrib, exact_t))
assert sum(contrib) == 4
net4 = [vi.subs(y, 4) - c for vi, c in zip(v, contrib)]
assert net4 == [R(1082, 100), R(1082, 100), R(1832, 100), R(4, 100)]
assert all(a_ > b_ for a_, b_ in zip(net4, nb))
# nonnegative alternative at y = 3.9
y2 = R(39, 10)
assert [vi.subs(y, y2) for vi in v] == [R(11895, 1000), R(11895, 1000), R(19695, 1000), R(39, 100)]
c2 = [R(110, 100), R(110, 100), R(140, 100), R(30, 100)]
assert sum(c2) == y2
net2 = [vi.subs(y, y2) - c for vi, c in zip(v, c2)]
assert net2 == [R(10795, 1000), R(10795, 1000), R(18295, 1000), R(9, 100)]
assert all(a_ > b_ for a_, b_ in zip(net2, nb))
assert n[3].subs(y, ybar) == 0 and R(15, 4) ** 2 == R(140625, 10000)

# --- item 23: hold-up, K = 100, R = 150, 50/50 ex-post split
K, Rv = 100, 150
assert Rv > K and Rv / 2 == 75 < K and Rv - K == 50

# --- item 26: equal-split construction and affordability counterexample
# construction on the beach: G/N = 5/128 and contributions sum to -P(4) = 4 (checked above)
Wa, Wb = 0 + 5, 10 + 0
assert Wa == 5 and Wb == 10
w1 = 1
max_u2_at_b = w1  # x2 = -x1 <= w1
assert max_u2_at_b < 5

# --- item 27: quasilinear example and Cobb-Douglas counterexample
yy, yp = symbols("y yp", positive=True)
C = symbols("C", real=True)
vq = solve(Eq(C + 2 * sqrt(1), 2 * sqrt(yy)), C)[0]
assert simplify(vq - (2 * sqrt(yy) - 2)) == 0
Cq = solve(Eq(z + C + 2 * sqrt(yy), z + 2 * sqrt(yp)), C)[0]
assert simplify(Cq - (2 * sqrt(yp) - 2 * sqrt(yy))) == 0 and not Cq.has(z)
Ccd = solve(Eq((z + C) * yy, z * yp), C)[0]
assert simplify(Ccd - z * (yp - yy) / yy) == 0 and Ccd.has(z)

print("all C checks passed")
