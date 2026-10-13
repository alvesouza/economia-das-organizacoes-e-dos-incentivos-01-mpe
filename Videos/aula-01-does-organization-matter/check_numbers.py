"""Recompute every number the Aula 1 video states; abort on the first mismatch.

Run from this directory: python -I check_numbers.py
"""
from fractions import Fraction as Fr
from itertools import permutations, product

# Ford threshold (illustrative fixed cost): q_bar = dF / dc, labour-hours per chassis.
c0, cL = Fr(25, 2), Fr(93, 60)                  # 12.5 h stationary, 93 min on the line
dF = 1_095_000                                   # extra fixed cost of the line, labour-hours/yr
q_bar = dF / (c0 - cL)
assert q_bar == 100_000, q_bar
assert round(float(c0 / cL), 1) == 8.1           # "about eight times less labour"
assert round(260 / 850, 2) == 0.31               # price fell to under a third

# Efficiency wage, e(w) = (w - w0)^beta: w* = w0 / (1 - beta), and it is a minimum of w/e(w).
w0, beta = 2.5, 0.5
w_star = w0 / (1 - beta)
assert w_star == 5.0
g = lambda w: w / (w - w0) ** beta
assert g(w_star) < g(w_star - 0.01) and g(w_star) < g(w_star + 0.01)
e = lambda w: (w - w0) ** beta
h = 1e-6
elasticity = (e(w_star + h) - e(w_star - h)) / (2 * h) * w_star / e(w_star)
assert abs(elasticity - 1) < 1e-6                # the Solow condition holds at w*

# Variety model: n* = a q / F, and Pi''(n) < 0.
a, q, F = 2.0, 50.0, 25.0
n_star = a * q / F
assert n_star == 4.0
Pi = lambda n: q * (a * __import__("math").log(n)) - n * F
assert Pi(n_star) > Pi(n_star - 0.1) and Pi(n_star) > Pi(n_star + 0.1)

# 2x2 table: increasing differences, symmetry, supermodularity.
f = {(0, 0): 0, (1, 0): -2, (0, 1): -1, (1, 1): 5}
assert f[1, 1] - f[0, 1] == 6 and f[1, 0] - f[0, 0] == -2
assert f[1, 1] - f[1, 0] == 7 and f[0, 1] - f[0, 0] == -1
assert f[1, 1] + f[0, 0] == 5 and f[1, 0] + f[0, 1] == -3
assert (f[1, 1] - f[0, 1]) - (f[1, 0] - f[0, 0]) == 8   # the cross-effect

# Two-choice quadratic model: closed forms and the multiplier.
def xy(t, s, b, c):
    d = c * c - b * b
    return Fr(c * t + b * s, d), Fr(c * s + b * t, d)
c, b, s = 2, 1, 1
assert xy(1, s, b, c) == (1, 1)
assert xy(3, s, b, c) == (Fr(7, 3), Fr(5, 3))
assert xy(1, s, 0, c) == (Fr(1, 2), Fr(1, 2)) and xy(3, s, 0, c) == (Fr(3, 2), Fr(1, 2))
mult = (xy(3, s, b, c)[0] - xy(1, s, b, c)[0]) / (xy(3, s, 0, c)[0] - xy(1, s, 0, c)[0])
assert mult == Fr(4, 3) == 1 / (1 - Fr(b, c) ** 2)
assert sum(Fr(b, c) ** (2 * k) for k in range(60)) - Fr(4, 3) < Fr(1, 10**30)
# FOCs hold at the closed form
x1, y1 = xy(3, s, b, c)
assert 3 + b * y1 - c * x1 == 0 and s + b * x1 - c * y1 == 0

# The cube: payoffs, pairwise supermodularity, and the valley.
pi = lambda J, T, S: 10 - 4*J - 2*T - S + 4*J*T + 5*J*S + 2*T*S + 2*J*T*S
want = {(0,0,0): 10, (1,0,0): 6, (0,1,0): 8, (0,0,1): 9,
        (1,1,0): 8, (1,0,1): 10, (0,1,1): 9, (1,1,1): 16}
assert all(pi(*v) == p for v, p in want.items())
for v, w in product(want, repeat=2):              # f(v or w) + f(v and w) >= f(v) + f(w)
    join = tuple(max(i, j) for i, j in zip(v, w)); meet = tuple(min(i, j) for i, j in zip(v, w))
    assert pi(*join) + pi(*meet) >= pi(*v) + pi(*w)
assert pi(1,1,0) + pi(0,0,0) == 18 and pi(1,0,0) + pi(0,1,0) == 14
assert all(pi(*v) < 10 for v in [(1,0,0), (0,1,0), (0,0,1)])     # every first step loses
paths = []
for order in permutations(range(3)):
    v, seen = [0, 0, 0], [10]
    for i in order:
        v[i] = 1; seen.append(pi(*v))
    paths.append((order, seen))
assert len(paths) == 6 and max(min(p[1][1:]) for p in paths) == 9   # best path still dips to 9
assert max(want.values()) == 16 and pi(1,1,1) - pi(0,0,0) == 6

# Two peaks: both corners are local optima (no single change improves); 111 is global.
nbrs = lambda v: [tuple(1 - x if j == i else x for j, x in enumerate(v)) for i in range(3)]
assert [pi(*u) for u in nbrs((0, 0, 0))] == [6, 8, 9]
assert [pi(*u) for u in nbrs((1, 1, 1))] == [9, 10, 8]
assert all(pi(*u) < pi(*v) for v in [(0, 0, 0), (1, 1, 1)] for u in nbrs(v))
assert max(pi(*u) for u in nbrs((0, 0, 0))) - 10 == -1      # best single step: -1
# Stand-alone gain is the smallest gain a practice ever has (supermodularity on the cube).
for i in range(3):
    for v in want:
        if v[i] == 0:
            up = tuple(1 if j == i else x for j, x in enumerate(v))
            e = tuple(1 if j == i else 0 for j in range(3))
            assert pi(*up) - pi(*v) >= pi(*e) - pi(0, 0, 0)

# Variety elasticities: halving F doubles n*.
assert a * q / (F / 2) == 8.0

# Substitutes flipped into complements: g(x, z) = f(x, -z) has g_xz = -f_xy.
fs = lambda x, y: -x * y                        # f_xy = -1
gs = lambda x, z: fs(x, -z)
hh = 1e-4
gxz = (gs(1 + hh, 1 + hh) - gs(1 + hh, 1) - gs(1, 1 + hh) + gs(1, 1)) / hh**2
assert abs(gxz - 1) < 1e-6

# 1987 plant table ratios quoted in the narration.
assert round(31 / 19, 2) == 1.63 and 135 / 45 == 3
print("all numbers check")
for order, seen in paths:
    print("JTS"[order[0]] + "JTS"[order[1]] + "JTS"[order[2]], seen)
