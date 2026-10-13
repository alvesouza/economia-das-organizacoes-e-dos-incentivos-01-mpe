"""Independent check of every result in lista-aulas-01-02.tex (graduate, symbolic).

Run: python Listas/lista-aulas-01-02-check.py
Aborts (AssertionError) on the first mismatch; prints "ALL CHECKS PASSED" otherwise.
Closed forms are checked with sympy; signs, limits and orderings symbolically where
possible and otherwise at many random admissible parameter draws.
"""
import random

import sympy as sp

random.seed(20261013)
DRAWS = 2000
ok = lambda e: sp.simplify(e) == 0


def draw(lo, hi):
    return random.uniform(lo, hi)


# ---------------------------------------------------------------- Block 1, objective
t, s, b, c, c1, c2, x, y = sp.symbols("t s b c c1 c2 x y", real=True)

# 1a: asymmetric quadratic, joint maximisation (Coase), dy*/dt
pi = t * x + s * y + b * x * y - c1 / 2 * x**2 - c2 / 2 * y**2
sol = sp.solve([sp.diff(pi, x), sp.diff(pi, y)], [x, y], dict=True)[0]
key_1a = b / (c1 * c2 - b**2)
assert ok(sp.diff(sol[y], t) - key_1a)
assert ok(sp.diff(sol[x], t) - c2 / (c1 * c2 - b**2))
for d in [b / (c1 * c2), c2 / (c1 * c2 - b**2), -b / (c1 * c2 + b**2), b / (c2**2 - b**2)]:
    assert not ok(d - key_1a), d

# 1b: symmetric cube pi = -al*(J+T+S) + be*(JT+JS+TS)
def cube_conditions(al, be):
    v = {k: -al * k + be * k * (k - 1) / 2 for k in range(4)}  # value with k practices
    unique_global = v[3] > max(v[0], v[1], v[2])
    every_step_loses = v[1] < v[0]
    two_below_status_quo = v[2] < v[0]
    return unique_global and every_step_loses and two_below_status_quo


for _ in range(DRAWS):
    al, be = draw(0.01, 5), draw(0.01, 12)
    assert cube_conditions(al, be) == (al < be < 2 * al)

# 1c: general concave pi: total / direct response = pxx*pyy/(pxx*pyy - pxy^2) > 1
pxx, pyy, pxy, pxt = sp.symbols("pxx pyy pxy pxt", real=True)
dx, dy = sp.symbols("dx dy")
s1c = sp.solve([pxx * dx + pxy * dy + pxt, pxy * dx + pyy * dy], [dx, dy], dict=True)[0]
ratio = sp.simplify(s1c[dx] / (-pxt / pxx))
assert ok(ratio - pxx * pyy / (pxx * pyy - pxy**2))
for _ in range(DRAWS):
    a_, d_ = -draw(0.1, 5), -draw(0.1, 5)
    lim = (a_ * d_) ** 0.5
    e_ = draw(-0.99, 0.99) * lim
    if abs(e_) < 1e-6:
        continue
    assert float(ratio.subs({pxx: a_, pyy: d_, pxy: e_})) > 1  # substitutes too

# 1d: Topkis without concavity: largest argmax non-decreasing (brute force on a grid)
grid = [i / 20 for i in range(21)]
for _ in range(200):
    coeffs = [draw(-3, 3) for _ in range(6)]
    k = draw(0, 2)  # increasing differences: f = g(x) + k*x*t
    def f(xx, tt):
        g = sum(cf * xx**i for i, cf in enumerate(coeffs))  # non-concave polynomial
        return g + k * xx * tt
    prev = -1
    for tt in [i / 10 for i in range(11)]:
        vals = [f(xx, tt) for xx in grid]
        m = max(vals)
        largest = max(xx for xx, v in zip(grid, vals) if v >= m - 1e-12)
        assert largest >= prev - 1e-12
        prev = largest

# ---------------------------------------------------------------- Block 1, discursive
for n in range(2, 7):
    J = sp.ones(n, n)
    I = sp.eye(n)
    H = -(c + b) * I + b * J
    ev = H.eigenvals()
    assert set(sp.simplify(e) for e in ev) == {sp.simplify(-c + (n - 1) * b), sp.simplify(-(c + b))}
    D = c - (n - 1) * b
    xs = sp.symbols(f"x0:{n}")
    ts = sp.symbols(f"t0:{n}")
    prof = sum(ts[i] * xs[i] for i in range(n)) \
        + b / 2 * sum(xs[i] * xs[j] for i in range(n) for j in range(n) if i != j) \
        - c / 2 * sum(xi**2 for xi in xs)
    opt = sp.solve([sp.diff(prof, xi) for xi in xs], xs, dict=True)[0]
    sym = {ti: t for ti in ts}
    assert ok(opt[xs[0]].subs(sym) - t / D)
    pistar = sp.simplify(prof.subs(opt).subs(sym))
    assert ok(pistar - n * t**2 / (2 * D))
    own = sp.diff(opt[xs[0]], ts[0])
    cross = sp.diff(opt[xs[1]], ts[0])
    assert ok(own - (c - (n - 2) * b) / ((c + b) * D))
    assert ok(cross - b / ((c + b) * D))
    m = sp.simplify(c * own)
    assert ok(m - c * (c - (n - 2) * b) / ((c + b) * D))
    # dm/db numerator (n-1) b (2c - (n-2) b) / ... > 0 ; dm/dc = -(b/c) dm/db (degree-0 homogeneity)
    assert ok(sp.diff(m, c) + b / c * sp.diff(m, b))
    premium = n * t**2 / (2 * D) - n * t**2 / (2 * c)
    assert ok(premium - n * (n - 1) * b * t**2 / (2 * c * D))
    assert ok(premium / pistar - (n - 1) * b / c)
    assert ok(m - 1 - (n - 1) * b**2 / ((c + b) * D))
    assert ok(sp.diff(m, b) - c * (n - 1) * b * (2 * c - (n - 2) * b) / ((c + b) * D) ** 2)
    # round-by-round best replies x <- (t + b (J - I) x)/c: iteration matrix eigenvalues (n-1)b/c and -b/c
    it = (b / c * (J - I)).eigenvals()
    assert set(sp.simplify(e) for e in it) == {sp.simplify((n - 1) * b / c), sp.simplify(-b / c)}
    # Sherman-Morrison inverse used in the key
    Ainv = ((c + b) * I - b * J).inv()
    assert sp.simplify(Ainv - (I + b * J / D) / (c + b)) == sp.zeros(n, n)

nn = sp.symbols("n", positive=True)
Dn = c - (nn - 1) * b
mgen = c * (c - (nn - 2) * b) / ((c + b) * Dn)
xgen = t / Dn
pgen = nn * t**2 / (2 * Dn)
for _ in range(DRAWS):
    cv = draw(0.5, 5)
    nv = random.randint(2, 8)
    bv = draw(0.001, 0.999) * cv / (nv - 1)
    tv = draw(0.1, 5)
    sub = {c: cv, b: bv, nn: nv, t: tv}
    assert float(sp.diff(mgen, b).subs(sub)) > 0
    assert float(sp.diff(mgen, c).subs(sub)) < 0
    assert float(sp.diff(mgen, nn).subs(sub)) > 0
    assert float(sp.diff(xgen, b).subs(sub)) > 0 and float(sp.diff(xgen, nn).subs(sub)) > 0
    assert float(sp.diff(xgen, c).subs(sub)) < 0 and float(sp.diff(xgen, t).subs(sub)) > 0
    assert float(sp.diff(pgen / nn, b).subs(sub)) > 0 and float(sp.diff(pgen / nn, c).subs(sub)) < 0
    assert float(mgen.subs(sub)) > 1
assert sp.limit(mgen.subs(b, 0), c, 1) == 1
assert ok(mgen.subs(nn, 1) - 1)

# ---------------------------------------------------------------- Block 2, objective
M, Dl, v1, v2 = sp.symbols("M Delta v1 v2", positive=True)
cands = {
    "A ln x + v": lambda X, v: sp.log(X) + v,
    "B x e^v": lambda X, v: X * sp.exp(v),
    "C x + v sqrt x": lambda X, v: X + v * sp.sqrt(X),
    "D (x+v)^3": lambda X, v: (X + v) ** 3,
    "E ln x * v": lambda X, v: sp.log(X) * v,
}
no_we = {}
for name, u in cands.items():
    # compensation Delta for switching y1 -> y2 at wealth M: u(M+Delta, v2) = u(M, v1)
    if name.startswith("D"):
        comp = v1 - v2  # cube is strictly increasing: equivalent to M + Delta + v2 = M + v1
        assert ok(u(M + comp, v2) - u(M, v1))
    else:
        comp = sp.solve(sp.Eq(u(M + Dl, v2), u(M, v1)), Dl)[0]
    no_we[name] = ok(sp.diff(comp, M))
assert no_we == {"A ln x + v": False, "B x e^v": False, "C x + v sqrt x": False,
                 "D (x+v)^3": True, "E ln x * v": False}, no_we

th, p, a = sp.symbols("theta p a", positive=True)
p_sol = M - (sp.sqrt(M) - th / 2) ** 2
a_sol = (sp.sqrt(M) + th / 2) ** 2 - M
assert ok((2 * sp.sqrt(M - p_sol) + th - 2 * sp.sqrt(M)).subs({M: 9, th: 1}))
assert ok(2 * sp.sqrt(M + a_sol) - 2 * sp.sqrt(M) - th)
assert ok(sp.expand(p_sol) - (th * sp.sqrt(M) - th**2 / 4))
assert ok(sp.expand(a_sol) - (th * sp.sqrt(M) + th**2 / 4))
assert ok(a_sol - p_sol - th**2 / 2)
for _ in range(DRAWS):  # p solves the WTP equation on the admissible range 0 < theta < 2 sqrt(M)
    Mv = draw(0.1, 50)
    tv = draw(0.001, 0.999) * 2 * Mv**0.5
    pv = float(p_sol.subs({M: Mv, th: tv}))
    assert abs(2 * (Mv - pv) ** 0.5 + tv - 2 * Mv**0.5) < 1e-9 and 0 < pv < Mv

# 2c: joint max, dy*/dc1 < 0 for b > 0
dyc1 = sp.diff(sol[y], c1)
assert ok(sp.together(dyc1) - (-(b**2 * s + b * c2 * t)) / (c1 * c2 - b**2) ** 2)
# 2d: generalised Nash under TU
d1, d2, beta, W = sp.symbols("d1 d2 beta W", real=True)
u1 = d1 + beta * (W - d1 - d2)
assert ok(sp.diff(u1, d1) - (1 - beta)) and ok(sp.diff(u1, d2) + beta)

# ---------------------------------------------------------------- Block 2, discursive
al, ka, yy, w = sp.symbols("alpha kappa y w", positive=True)
B = al * yy - yy**2 / 2
Wy = B - ka * yy**2 / 2
ystar = sp.solve(sp.diff(Wy, yy), yy)[0]
assert ok(ystar - al / (1 + ka))
Wstar = sp.simplify(Wy.subs(yy, ystar))
assert ok(Wstar - al**2 / (2 * (1 + ka)))
Bstar = B.subs(yy, ystar)
# regime D (downstream holds the right): threat (0, 0); U pays tau_D
tauD = sp.simplify(Bstar - beta * Wstar)
assert ok(tauD - al**2 * (1 + 2 * ka - beta * (1 + ka)) / (2 * (1 + ka) ** 2))
assert ok(tauD - (ka * ystar**2 / 2 + (1 - beta) * Wstar))
# regime U: threat y = alpha, dU = alpha^2/2, dD = -kappa alpha^2/2; D pays tau_U
dU, dD = al**2 / 2, -ka * al**2 / 2
SU = sp.simplify(Wstar - dU - dD)
assert ok(SU - al**2 * ka**2 / (2 * (1 + ka)))
tauU = sp.simplify(dU + beta * SU - Bstar)
assert ok(tauU - al**2 * ka**2 * (1 + beta * (1 + ka)) / (2 * (1 + ka) ** 2))
# D's payoff check in regime U: tau_U paid by D -> uD = -tau_U - kappa y*^2/2 = dD + (1-beta) SU
assert ok(-tauU - ka * ystar**2 / 2 - (dD + (1 - beta) * SU))
# sign of dtau_D/dkappa = alpha^2 (beta(1+kappa) - 2 kappa) / (2 (1+kappa)^3)
assert ok(sp.diff(tauD, ka) - al**2 * (beta * (1 + ka) - 2 * ka) / (2 * (1 + ka) ** 3))
for _ in range(DRAWS):
    sub = {al: draw(0.1, 5), ka: draw(0.01, 10), beta: draw(0.01, 0.99)}
    assert float(sp.diff(ystar, ka).subs(sub)) < 0 and float(sp.diff(ystar, al).subs(sub)) > 0
    assert float(sp.diff(Wstar, ka).subs(sub)) < 0
    assert float(sp.diff(SU, ka).subs(sub)) > 0
    assert float(sp.diff(tauU, ka).subs(sub)) > 0 and float(sp.diff(tauU, beta).subs(sub)) > 0
    assert float(sp.diff(tauD, beta).subs(sub)) < 0
    thr = float((sub[beta] / (2 - sub[beta])))
    assert (float(sp.diff(tauD, ka).subs(sub)) > 0) == (sub[ka] < thr)
    assert float(tauD.subs(sub)) > 0 and float(tauU.subs(sub)) > 0
assert sp.limit(SU, ka, 0) == 0 and sp.limit(tauD, ka, 0) == al**2 * (1 - beta) / 2
assert sp.limit(tauD, ka, sp.oo) == 0 and sp.limit(Wstar, ka, sp.oo) == 0
# wealth effects: Pareto frontier, max u_U = m_U + B(y) - tau  s.t.  ln(m_D + tau) - kappa y^2/2 = ubar
tau, lam, mD = sp.symbols("tau lambda m_D", positive=True)
L = B - tau + lam * (sp.log(mD + tau) - ka * yy**2 / 2)
lam_sol = sp.solve(sp.diff(L, tau), lam)[0]
assert ok(lam_sol - (mD + tau))
y_eff = sp.solve(sp.diff(L, yy).subs(lam, w), yy)[0]
assert ok(y_eff - al / (1 + ka * w))
uD_front = sp.log(w) - ka * y_eff**2 / 2
assert sp.simplify(sp.diff(uD_front, w) - (1 / w + al**2 * ka**2 / (1 + ka * w) ** 3)) == 0  # > 0
assert ok(y_eff.subs(w, 1) - ystar)  # w = 1 reproduces the quasi-linear benchmark

# ---------------------------------------------------------------- Block 3
dA, dS, rA, rS, Dt, sg = sp.symbols("delta_A delta_S r_A r_S Delta sigma", positive=True)
# 3a (objective): three rounds, A proposes in 1 and 3
shareA3 = 1 - dS * (1 - dA)
key_3a = shareA3
for d in [1 - dA * (1 - dS), (1 - dS) / (1 - dA * dS), dA * (1 - dS), (1 - dA) / (1 - dA * dS)]:
    assert not ok(d - key_3a), d
# infinite horizon (stationary): VA = W - dS*VS', VS' = W - dA*VA
VA, VS = sp.symbols("V_A V_S")
st = sp.solve([VA - (1 - dS * VS), VS - (1 - dA * VA)], [VA, VS], dict=True)[0]
assert ok(st[VA] - (1 - dS) / (1 - dA * dS))
# 3b (objective): Delta -> 0 with delta_i = exp(-r_i Delta)
lim = sp.limit(((1 - dS) / (1 - dA * dS)).subs({dA: sp.exp(-rA * Dt), dS: sp.exp(-rS * Dt)}), Dt, 0)
assert ok(lim - rS / (rA + rS))
# equal deltas -> 1/(1+delta) -> 1/2
assert sp.limit(1 / (1 + dA), dA, 1) == sp.Rational(1, 2)
# finite horizon, common delta: first proposer's share (1 + d^T)/(1+d) for odd T, (1 - d^T)/(1+d) for even T
dd = sp.symbols("delta", positive=True)
def finite_share(T):
    share = 1  # last proposer takes all
    for _ in range(T - 1):
        share = 1 - dd * share
    return sp.simplify(share)
for T in range(1, 9):
    target = (1 + dd**T) / (1 + dd) if T % 2 else (1 - dd**T) / (1 + dd)
    assert ok(finite_share(T) - target), T

# joint system
X, Y = sp.symbols("X Y", real=True)
R = t * (X + Y) + b * X * Y
Wj = R - c / 2 * X**2 - c / 2 * Y**2
eff = sp.solve([sp.diff(Wj, X), sp.diff(Wj, Y)], [X, Y], dict=True)[0]
assert ok(eff[X] - t / (c - b)) and ok(eff[Y] - t / (c - b))
Wjs = sp.simplify(Wj.subs(eff))
assert ok(Wjs - t**2 / (c - b))
# regime II: fixed share sigma of R, private costs, simultaneous choice
ne = sp.solve([sp.diff(sg * R - c / 2 * X**2, X), sp.diff((1 - sg) * R - c / 2 * Y**2, Y)], [X, Y], dict=True)[0]
den = c**2 - sg * (1 - sg) * b**2
assert ok(ne[X] - sg * t * (c + (1 - sg) * b) / den)
assert ok(ne[Y] - (1 - sg) * t * (c + sg * b) / den)
half = {sg: sp.Rational(1, 2)}
assert ok(ne[X].subs(half) - t / (2 * c - b))
WN = sp.simplify(Wj.subs({X: ne[X], Y: ne[Y]}).subs(half))
assert ok(WN - t**2 * (3 * c - b) / (2 * c - b) ** 2)
loss = sp.simplify(Wjs - WN)
assert ok(loss - t**2 * c**2 / ((c - b) * (2 * c - b) ** 2))
rel = sp.simplify(loss / Wjs)
assert ok(rel - c**2 / (2 * c - b) ** 2)
assert ok(sp.diff(rel, b) - 2 * c**2 / (2 * c - b) ** 3)
assert rel.subs(b, 0) == sp.Rational(1, 4) and sp.limit(rel, b, c) == 1
# no sigma reaches the efficient pair: A's FOC at (x*, y*) forces sigma = 1, S's forces sigma = 0
at_eff = {X: t / (c - b), Y: t / (c - b)}
sgf = sp.Symbol("sigma_free")
assert sp.solve(sp.diff(sgf * R - c / 2 * X**2, X).subs(at_eff), sgf) == [1]
assert sp.solve(sp.diff((1 - sgf) * R - c / 2 * Y**2, Y).subs(at_eff), sgf) == [0]
# 3d (objective, F): dy^N/dsigma = c t q(sigma) / den^2, q = b^2 (1-sigma)^2 + b c (1 - 2 sigma) - c^2
q = b**2 * (1 - sg) ** 2 + b * c * (1 - 2 * sg) - c**2
assert ok(sp.diff(ne[Y], sg) - c * t * q / den**2)
assert ok(sp.diff(ne[X], sg) - c * t * (c**2 + b * c * (1 - 2 * sg) - b**2 * sg**2) / den**2)
assert ok(sp.diff(ne[Y], sg).subs(half) - 4 * c * t / (b**2 - 4 * c**2))  # < 0 at sigma = 1/2
golden = (sp.sqrt(5) - 1) / 2  # q(0) > 0  <=>  b/c > golden
assert ok(sp.expand(q.subs({sg: 0, b: golden * c})))
counter = {c: 1, b: sp.Rational(9, 10), t: 1, sg: sp.Rational(1, 20)}
assert sp.diff(ne[Y], sg).subs(counter) > 0  # explicit counterexample used in the key
for _ in range(DRAWS):
    cv = draw(0.5, 5)
    sub = {c: cv, b: draw(0.001, 0.999) * cv, t: draw(0.1, 5), sg: draw(0.001, 0.999),
           dA: draw(0.01, 0.99), dS: draw(0.01, 0.99)}
    assert (float(sp.diff(ne[Y], sg).subs(sub)) > 0) == (float(q.subs(sub)) > 0)
    assert float(ne[X].subs(sub)) < float((t / (c - b)).subs(sub))
    assert float(ne[Y].subs(sub)) < float((t / (c - b)).subs(sub))
    shareA = (1 - dS) / (1 - dA * dS)
    assert float(sp.diff(shareA, dA).subs(sub)) > 0 and float(sp.diff(shareA, dS).subs(sub)) < 0
    assert float(sp.diff(t / (c - b), b).subs(sub)) > 0 and float(sp.diff(t**2 / (c - b), c).subs(sub)) < 0
# 3b distractors differ from the key
for d in [rA / (rA + rS), sp.Rational(1, 2), rS / rA, rA * rS / (rA + rS) ** 2]:
    assert not ok(d - rS / (rA + rS)), d
# transfer in regime I: S's payoff tau - c y*^2/2 = delta_S (1 - delta_A) W*/(1 - delta_A delta_S)
tauI = c / 2 * (t / (c - b)) ** 2 + dS * (1 - dA) * Wjs / (1 - dA * dS)
assert ok(tauI - c / 2 * (t / (c - b)) ** 2 - (1 - st[VA]) * Wjs)

shA = (1 - dS) / (1 - dA * dS)
assert ok(sp.diff(shA, dA) - dS * (1 - dS) / (1 - dA * dS) ** 2)
assert ok(sp.diff(shA, dS) - (dA - 1) / (1 - dA * dS) ** 2)
assert ok(sp.diff(rel, c) + 2 * b * c / (2 * c - b) ** 3)
assert ok(ne[X].subs(half) / (t / (c - b)) - (c - b) / (2 * c - b))
# Block 2 d: general h, y_eff = alpha / (1 + kappa / h'(w))
hp = sp.symbols("hprime", positive=True)
assert ok(sp.solve(sp.diff(B, yy) - lam * ka * yy, yy)[0].subs(lam, 1 / hp) - al / (1 + ka / hp))

print("ALL CHECKS PASSED")
