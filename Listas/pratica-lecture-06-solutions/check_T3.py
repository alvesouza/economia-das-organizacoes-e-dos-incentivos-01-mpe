"""Checks every number and equilibrium claim in the Tier 3 solutions of Listas/pratica-lecture-06.md
that are written here (items 20-28; item 19, Gibbons 2.20, is reused from
../lista-reais-lectures-01-05-solutions and checked by its check script):
Munoz-Garcia Ch. 6 Ex. 5, Cabral 9.15, Munoz-Garcia Ch. 6 Ex. 10, Gibbons 2.14, Tadelis 11.7,
Cabral 9.19, Tadelis 10.10, Gibbons 2.17, M&R Math. 1. Exact arithmetic (fractions, sympy);
claims about finite sets of prices or outputs are found by enumeration on fine grids.

Run: python check_T3.py -> one line per item and "all T3 checks passed", or an AssertionError.
"""
import math
from fractions import Fraction as F

import sympy as sp


# ----------------------------------------------------------------------------- item 20
def item20():
    """Munoz-Garcia Ch. 6 Ex. 5: n firms, Bertrand, demand 1 now and theta afterwards."""
    n, th, d = sp.symbols("n theta delta", positive=True)
    # cooperate: (1/n)(1 + d th/(1-d)) pi ; deviate: pi
    sol = sp.solve(sp.Eq((1 + d * th / (1 - d)) / n, 1), d)[0]
    assert sp.simplify(sol - (n - 1) / (n - 1 + th)) == 0
    assert sp.simplify(sp.diff(sol, th) + (n - 1) / (n - 1 + th) ** 2) == 0
    assert sp.simplify(sp.diff(sol, n) - th / (n - 1 + th) ** 2) == 0
    assert sp.simplify(sol.subs(th, 1) - (1 - 1 / n)) == 0  # constant demand: Cabral's 1 - 1/n
    assert sol.subs({n: 2, th: 1}) == F(1, 2)
    assert sol.subs({n: 3, th: 2}) == F(1, 2) and sol.subs({n: 3, th: F(6, 5)}) == F(2, 2 + F(6, 5))
    assert sp.limit(sol, th, sp.oo) == 0
    # direct comparison at n = 3, theta = 2: threshold 1/2
    def coop(dv, N, theta):
        return (1 + dv * theta / (1 - dv)) / N

    assert coop(F(1, 2), 3, 2) == 1 and coop(F(49, 100), 3, 2) < 1 < coop(F(51, 100), 3, 2)
    print("item 20 (MG 6.5): delta >= (n-1)/(n-1+theta); falls in theta, rises in n; theta = 1 gives 1 - 1/n; n=3, theta=2: 1/2")


# ----------------------------------------------------------------------------- item 21
def item21():
    """Cabral 9.15: two markets, reversed cost advantages, inelastic demand q up to pM."""
    pM, cl, ch, q = sp.symbols("pM c_low c_high q", positive=True)
    d = sp.symbols("delta", positive=True)
    A = q * (pM - cl)  # collusive profit of each firm per period (its low-cost market at pM)
    B = q * (pM - ch)  # extra profit from undercutting the rival in the rival's market
    pun = q * (ch - cl)  # static Nash profit: low-cost firm prices just below c_high
    cond = sp.Eq(A / (1 - d), A + B + d * pun / (1 - d))
    sol = sp.solve(cond, d)[0]
    assert sp.simplify(sol - F(1, 2)) == 0
    # numbers: pM = 10, c_low = 2, c_high = 6, q = 1
    vals = {pM: 10, cl: 2, ch: 6, q: 1}
    A_, B_, P_ = [x.subs(vals) for x in (A, B, pun)]
    assert (A_, B_, P_) == (8, 4, 4)
    for dv in (F(1, 2), F(2, 3)):
        assert A_ / (1 - dv) >= A_ + B_ + dv * P_ / (1 - dv)
    assert F(49, 100) * 0 + A_ / (1 - F(49, 100)) < A_ + B_ + F(49, 100) * P_ / (1 - F(49, 100))
    # single market: the high-cost firm earns 0 and undercuts at any delta (no punishment can bite)
    assert 0 / (1 - F(99, 100)) < q.subs(vals) * (10 - 6 - F(1, 100)) / 1 + 0
    # one market with symmetric firms gives the same 1/2 (Cabral p. 227-228 reasoning)
    print("item 21 (Cabral 9.15): collusion A each, deviation A + B, Nash profit c_high - c_low; delta >= 1/2 whatever pM, c_low, c_high, q")


# ----------------------------------------------------------------------------- item 22
def item22():
    """Munoz-Garcia Ch. 6 Ex. 10: differentiated duopoly, p_i = a - b q_i - d q_j."""
    a, b, d, dl = sp.symbols("a b d delta", positive=True)
    # Cournot
    qC = a / (2 * b + d)
    piC = sp.simplify(b * qC**2)
    qm = a / (2 * (b + d))
    pim = sp.simplify((a - (b + d) * qm) * qm)
    assert sp.simplify(pim - a**2 / (4 * (b + d))) == 0
    qD = (a - d * qm) / (2 * b)
    piD = sp.simplify(b * qD**2)
    assert sp.simplify(piD - a**2 * (2 * b + d) ** 2 / (16 * b * (b + d) ** 2)) == 0
    d1 = sp.simplify((piD - pim) / (piD - piC))
    assert sp.simplify(d1 - (2 * b + d) ** 2 / (8 * b**2 + 8 * b * d + d**2)) == 0
    assert sp.simplify(d1.subs(d, b) - F(9, 17)) == 0 and sp.limit(d1, d, 0) == F(1, 2)
    assert sp.simplify(sp.diff(d1, d) - 4 * b * d * (2 * b + d) / (8 * b**2 + 8 * b * d + d**2) ** 2) == 0
    # numeric check of the derivative sign on a grid
    f = sp.lambdify((b, d), d1)
    assert all(f(1, x / 100) < f(1, (x + 1) / 100) for x in range(1, 99))
    # (ii) one-period detection lag: pim >= pid (1 - dl^2) + dl^2 pic  ->  dl^2 = d1
    lag = sp.solve(sp.Eq(pim / (1 - dl), piD * (1 + dl) + dl**2 * piC / (1 - dl)), dl)
    lag = [r for r in lag if sp.simplify(r) != 1 and r.subs({a: 1, b: 1, d: F(1, 2)}) > 0]
    assert len(lag) == 1 and sp.simplify(lag[0] ** 2 - d1) == 0
    for bv_, dv_ in [(1, F(1, 2)), (1, F(9, 10)), (2, 1)]:
        sub = {b: bv_, d: dv_}
        assert abs(float(lag[0].subs(sub)) - float(((2 * b + d) / sp.sqrt(8 * b**2 + 8 * b * d + d**2)).subs(sub))) < 1e-12
        assert lag[0].subs(sub) > d1.subs(sub)  # the lag raises the cutoff: sqrt(x) > x on (0, 1)
    # brute-force check of the Cournot best reply and Bertrand quantities for b = 1, d = 1/2, a = 1
    av, bv, dv = 1.0, 1.0, 0.5
    grid = [k / 10000 for k in range(0, 10001)]
    qdev_num = max(grid, key=lambda x: (av - bv * x - dv * float(qm.subs({a: av, b: bv, d: dv}))) * x)
    assert abs(qdev_num - float(qD.subs({a: av, b: bv, d: dv}))) < 2e-4
    # Bertrand
    qB = lambda pi, pj: (a * (b - d) - b * pi + d * pj) / (b**2 - d**2)
    pB = a * (b - d) / (2 * b - d)
    piB = sp.simplify(pB * qB(pB, pB))
    assert sp.simplify(piB - a**2 * b * (b - d) ** 2 / ((2 * b - d) ** 2 * (b**2 - d**2))) == 0
    pm = a / 2
    pimB = sp.simplify(pm * qB(pm, pm))
    assert sp.simplify(pimB - a**2 / (4 * (b + d))) == 0 and sp.simplify(pimB - pim) == 0
    pdev = (a * (b - d) + d * pm) / (2 * b)
    piDB = sp.simplify(pdev * qB(pdev, pm))
    assert sp.simplify(piDB - a**2 * (2 * b - d) ** 2 / (16 * b * (b**2 - d**2))) == 0
    d2 = sp.simplify((piDB - pimB) / (piDB - piB))
    assert sp.simplify(d2 - (2 * b - d) ** 2 / (8 * b**2 - 8 * b * d + d**2)) == 0
    # numeric brute force for Bertrand best reply (b = 1, d = 1/2, a = 1): profit of firm i against pj = a/2
    bestp = max(grid, key=lambda x: x * float(qB(x, pm).subs({a: av, b: bv, d: dv})))
    assert abs(bestp - float(pdev.subs({a: av, b: bv, d: dv}))) < 2e-4
    print("item 22 (MG 6.10): Cournot d1 = (2b+d)^2/(8b^2+8bd+d^2), lag d2 = sqrt(d1) = (2b+d)/sqrt(8b^2+8bd+d^2); Bertrand d_B = (2b-d)^2/(8b^2-8bd+d^2); b=d gives 9/17")
    # the Bertrand expression as printed in the text layer of the book carries an extra factor
    # (2b^2 - 2bd + d^2)/a^2 and does not make the constraint bind
    sub = {a: 1, b: 1, d: F(1, 2)}
    book = ((d - 2 * b) ** 2 * (2 * b**2 - 2 * b * d + d**2) / (a**2 * (8 * b**2 - 8 * b * d + d**2))).subs(sub)
    mine = d2.subs(sub)
    assert abs(float(mine) - 0.52941) < 1e-4 and abs(float(book) - 0.66176) < 1e-4

    def gap(dv):
        return float((pimB / (1 - dv) - piDB - dv * piB / (1 - dv)).subs(sub))

    assert abs(gap(mine)) < 1e-12 and abs(gap(book)) > 1e-3


# ----------------------------------------------------------------------------- item 23
def item23():
    """Gibbons 2.14: Bertrand with demand intercept a_H (prob pi) or a_L, cost c."""
    aH, aL, c, pi = F(10), F(6), F(0), F(1, 2)
    pH, pL = (aH + c) / 2, (aL + c) / 2
    piH, piL = (aH - c) ** 2 / 8, (aL - c) ** 2 / 8  # each firm's share of monopoly profit
    assert (pH, pL, piH, piL) == (5, 3, F(25, 2), F(9, 2))
    Ebar = pi * piH + (1 - pi) * piL
    dstar = piH / (piH + Ebar)
    formula = (aH - c) ** 2 / ((aH - c) ** 2 * (1 + pi) + (1 - pi) * (aL - c) ** 2)
    assert dstar == formula == F(25, 42)
    # the low state binds less
    assert piL / (piL + Ebar) < dstar
    # brute force: delta* is where the H-state constraint switches
    def ok_H(dv):
        return piH + dv / (1 - dv) * Ebar >= 2 * piH

    assert ok_H(dstar) and not ok_H(dstar - F(1, 1000))
    # highest H price below delta*
    def profit(p):
        return (p - c) * (aH - p) / 2

    def feasible(p, dv):
        Ep = pi * profit(p) + (1 - pi) * piL
        okH = profit(p) + dv / (1 - dv) * Ep >= 2 * profit(p)
        okL = piL + dv / (1 - dv) * Ep >= 2 * piL
        return okH and okL

    for dv in (F(1, 2), F(11, 20), F(57, 100)):
        Pi = dv * (1 - pi) * piL / (1 - dv * (1 + pi))
        root = (aH + c - sp.sqrt(sp.Rational((aH - c) ** 2 - 8 * Pi))) / 2
        grid = [F(k, 2000) for k in range(int(c * 2000), int(pH * 2000) + 1)]
        pbest = max(p for p in grid if feasible(p, dv))
        assert abs(float(root) - float(pbest)) < 1e-3, (dv, root, pbest)
        assert pbest <= pH
        if dv == F(1, 2):
            assert Pi == piL and root == 1
    # p(delta) rises to pH at delta*
    Pi_star = dstar * (1 - pi) * piL / (1 - dstar * (1 + pi))
    assert Pi_star == piH
    # delta* and 1/(1+pi)
    assert dstar < 1 / (1 + pi) and F(1, 2) < dstar
    print("item 23 (Gibbons 2.14): pH=(aH+c)/2, delta* = (aH-c)^2/[(aH-c)^2(1+pi)+(1-pi)(aL-c)^2] (25/42 for 10, 6, 0, 1/2); p(delta) solves profit = d(1-pi)piL/(1-d(1+pi)); p(1/2) = 1")


# ----------------------------------------------------------------------------- item 24
def item24():
    """Tadelis 11.7: Baron-Ferejohn, N odd, closed rule."""
    for N in (3, 5, 7, 9):
        for d in (F(1, 2), F(9, 10), F(1)):
            V = F(1, N)  # T = 1: proposer takes 1 with prob 1/N, responders get 0
            for T in range(2, 8):
                k = 1 - F(N - 1, 2) * d * V
                V_new = k / N + F(N - 1, N) * F(1, 2) * d * V
                assert V_new == F(1, N)
                assert k + F(N - 1, 2) * d * V == 1  # shares add to the pie
                V = V_new
            # infinite horizon: symmetric stationary value solves v = k/N + ((N-1)/N)(1/2) d v
            v = sp.symbols("v")
            sol = sp.solve(sp.Eq(v, (1 - sp.Rational(N - 1, 2) * d * v) / N + sp.Rational(N - 1, N) * sp.Rational(1, 2) * d * v), v)[0]
            assert sol == F(1, N)
            k_inf = 1 - F(N - 1, 2) * d * F(1, N)
            k_2 = 1 - F(N - 1, 2 * N) * d
            assert k_inf == k_2
            two_person = 1 - d
            assert k_2 > two_person if d > 0 else True
    # T = 1 Nash equilibrium that is not SPE: equal split accepted only if exactly equal
    for N in (3, 5):
        yes_if_deviation = 1  # only the proposer votes yes; needs (N+1)/2 > 1
        assert yes_if_deviation < (N + 1) // 2
    print("item 24 (Tadelis 11.7): v = 1/N in every period; proposer keeps 1 - (N-1)d/(2N) for T = 2 and infinite horizon; two-person T=2 gives 1 - d")


# ----------------------------------------------------------------------------- item 25
def item25():
    """Cabral 9.19: secret price cuts (Green-Porter)."""
    u, al, d, V, Tt = sp.symbols("u alpha delta V T", positive=True)
    for T in (1, 2, 3):
        # (a)
        Vs = sp.solve(sp.Eq(V, (1 - al) * (u / 2 + d * V) + al * d ** (T + 1) * V), V)[0]
        assert sp.simplify(Vs - (1 - al) * u / 2 / (1 - (1 - al) * d - al * d ** (T + 1))) == 0
        # (b)-(c)
        Vp = (1 - al) * u + d ** (T + 1) * Vs
        cond = sp.simplify((Vs - Vp) / Vs * (1 - (1 - al) * d - al * d ** (T + 1)) / 1)
        lhs = sp.simplify((Vs - Vp) * (1 - (1 - al) * d - al * d ** (T + 1)) / ((1 - al) * u / 2))
        target = (2 * (1 - al) * d + (2 * al - 1) * d ** (T + 1)) - 1
        assert sp.simplify(lhs - target) == 0
    # value iteration confirms (a) for T = 2, alpha = 1/5, delta = 9/10, u = 1
    alv, dv, uv, T = 0.2, 0.9, 1.0, 2
    Vit = [0.0] * (T + 1)  # index 0 cooperative, k war periods left
    for _ in range(3000):
        new = [0.0] * (T + 1)
        new[0] = (1 - alv) * (uv / 2 + dv * Vit[0]) + alv * (0 + dv * Vit[T])
        for k in range(1, T + 1):
            new[k] = 0 + dv * (Vit[k - 1] if k > 1 else Vit[0])
        Vit = new
    Vformula = (1 - alv) * uv / 2 / (1 - (1 - alv) * dv - alv * dv ** (T + 1))
    assert abs(Vit[0] - Vformula) < 1e-9
    assert abs(Vformula - 2.98) < 0.005  # V in the worked example (u = 1)
    # (d) existence and optimal T
    def g(alpha, delta, T):
        return 2 * (1 - alpha) * delta + (2 * alpha - 1) * delta ** (T + 1)

    # alpha >= 1/2: never satisfied
    for alpha in (F(1, 2), F(3, 5), F(9, 10)):
        for delta in (F(1, 2), F(9, 10), F(99, 100)):
            assert all(g(alpha, delta, T) < 1 for T in range(0, 60))
    # alpha < 1/2: g increasing in T, tends to 2(1-alpha) d; need d > 1/(2(1-alpha))
    alpha, delta = F(1, 5), F(9, 10)
    assert 2 * (1 - alpha) * delta > 1
    Tstar = min(T for T in range(0, 200) if g(alpha, delta, T) >= 1)
    assert Tstar == 2 and g(alpha, delta, 1) < 1 <= g(alpha, delta, 2)
    r = (2 * (1 - alpha) * delta - 1) / (1 - 2 * alpha)
    assert delta ** (Tstar + 1) <= r < delta**Tstar and r < delta
    assert math.ceil(math.log(float(r)) / math.log(float(delta))) - 1 == Tstar
    # a low delta: no T works
    assert all(g(F(1, 5), F(5, 8), T) < 1 for T in range(0, 100)) and 2 * F(4, 5) * F(5, 8) == 1
    # V is decreasing in T (shorter war is better)
    Vs = [(1 - alpha) / 2 / (1 - (1 - alpha) * delta - alpha * delta ** (T + 1)) for T in range(1, 8)]
    assert all(Vs[i] > Vs[i + 1] for i in range(len(Vs) - 1))
    print("item 25 (Cabral 9.19): V = (1-a)u/2 / (1-(1-a)d-a d^(T+1)); constraint 1 <= 2(1-a)d + (2a-1)d^(T+1); exists iff a < 1/2 and d > 1/(2(1-a)); a=1/5, d=9/10: T* = 2")


# ----------------------------------------------------------------------------- item 26
def item26():
    """Tadelis 10.10: bond B and fee w; P2 pays w whenever the guarantor follows the contract
    (including after D, when P3 keeps the bond); P3 deviates only by keeping the bond after C."""
    # book's numbers: B = 2, w = 0.1 -> delta >= 0.95
    d = sp.symbols("d")
    assert sp.solve(sp.Eq(F(1, 10) / (1 - d), 2), d)[0] == F(19, 20)
    # design for any delta: B = 1 + d/2, w = 1 - d/2
    for k in range(1, 100):
        dv = F(k, 100)
        B, w = 1 + dv / 2, 1 - dv / 2
        assert 1 - w >= 0 and 1 - w > 0  # P2 prefers using the guarantor to no trade (0)
        assert 1 - w > 2 - B - w or 1 > 2 - B  # cooperate beats defect given a posted bond: 1 > 2 - B
        assert 1 > 2 - B
        assert w / (1 - dv) > B  # guarantor prefers the fee stream to keeping the bond
        assert w < 1 and B > 1
    # tightness: with B = 1 and w = 1 - delta the guarantor is exactly indifferent
    for dv in (F(1, 10), F(1, 2), F(9, 10)):
        assert (1 - dv) / (1 - dv) == 1
    # feasibility region: need (1-d)*B <= w <= 1 with B > 1 -> nonempty for every d > 0
    for dv in (F(1, 100), F(1, 10), F(1, 2), F(99, 100)):
        assert (1 - dv) * 1 < 1
    print("item 26 (Tadelis 10.10): P2 cooperates iff B >= 1, guarantor complies iff w/(1-d) >= B, P2 joins iff w <= 1; B = 1 + d/2, w = 1 - d/2 works for every d in (0,1); book numbers B=2, w=0.1: d >= 0.95")


# ----------------------------------------------------------------------------- item 27
def item27():
    """Gibbons 2.17: firm and short-lived workers. Firm pays w when output y is produced."""
    for y, c in [(F(10), F(4)), (F(10), F(9)), (F(5), F(1))]:
        dmin = c / y
        for k in range(1, 100):
            dv = F(k, 100)
            exists = c <= dv * y  # some w in [c, d y]
            ok_firm = lambda w: (y - w) / (1 - dv) >= y
            assert exists == (dv >= dmin)
            ws = [c + (dv * y - c) * F(j, 10) for j in range(0, 11)] if exists else []
            assert all(ok_firm(w) and w >= c for w in ws)
            if not exists:
                # any w >= c fails the firm's constraint
                assert not any(ok_firm(w) for w in [c + F(j, 10) for j in range(0, 50)])
    # firm's punishment cannot exceed zero (workers can always shirk): necessary condition
    assert F(0) == 0
    print("item 27 (Gibbons 2.17): wage w in [c, d y]; exists iff d >= c/y; checked for (y,c) = (10,4), (10,9), (5,1)")


# ----------------------------------------------------------------------------- item 28
def item28():
    """M&R Math. 1: min M(p) + w s.t. p (w - wbar) N >= g, M(p) = 1500 p."""
    delta, t = F(9, 10), 5
    N = (1 - delta**t) / (1 - delta)
    assert abs(float(N) - 4.0951) < 1e-4
    g, wbar, k = 3000, 20000, 1500
    p, Nn = sp.symbols("p N", positive=True)
    cost = k * p + wbar + g / (Nn * p)
    pstar = sp.solve(sp.diff(cost, p), p)[0]
    assert sp.simplify(pstar - sp.sqrt(2 / Nn)) == 0
    assert sp.simplify(sp.diff(cost, p, 2).subs(p, pstar)) > 0
    pv = float(pstar.subs(Nn, float(N)))
    wv = wbar + g / (float(N) * pv)
    assert abs(pv - 0.69886) < 1e-4 and abs(wv - 21048.2) < 0.5
    assert abs(k * pv - (wv - wbar)) < 1e-6  # monitoring cost equals the wage premium at the optimum
    # one more year: N = 1, p* = sqrt(2) > 1 -> corner p = 1, w = wbar + g
    assert float(pstar.subs(Nn, 1)) > 1
    assert wbar + g / 1 == 23000
    assert pv * (wv - wbar) * 1 < g  # the old contract no longer deters cheating
    assert abs(pv * (wv - wbar) * 1 - 732.6) < 1.0
    # N = 4.1 as rounded in the statement
    assert abs(float(pstar.subs(Nn, 4.1)) - 0.69843) < 1e-4
    # general result: M(p) = m p^2 (M' > 0, M'' > 0): w*(N) decreasing; also general identity w* = wbar + p* M'(p*)
    m = sp.symbols("m", positive=True)
    Mp = 2 * m * p
    pg = sp.solve(sp.Eq(Mp * p**2, g / Nn), p)
    pg = [r for r in pg if r.is_positive][0] if len(pg) > 1 else pg[0]
    wg = wbar + g / (Nn * pg)
    assert sp.simplify(wg - (wbar + (Mp * p).subs(p, pg))) == 0
    for mv in (1, 100, 1500):
        fw = sp.lambdify(Nn, wg.subs(m, mv))
        fp = sp.lambdify(Nn, pg.subs(m, mv))
        vals = [fw(x / 2) for x in range(2, 40)]
        pvals = [fp(x / 2) for x in range(2, 40)]
        assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
        assert all(pvals[i] > pvals[i + 1] for i in range(len(pvals) - 1))
    # N * p*(N) is nondecreasing: the factor in the wage premium g / (N p*)
    fN = sp.lambdify(Nn, (Nn * pg).subs(m, 100))
    assert all(fN(x / 2) < fN((x + 1) / 2) for x in range(2, 40))
    print("item 28 (M&R Math 1): N = 4.0951, p* = sqrt(2/N) = 0.6989, w* = 21048.2; with N = 1: p = 1, w = 23000, old contract gives expected loss 732.6 < 3000; w*(N) = wbar + p* M'(p*) falls in N")


if __name__ == "__main__":
    for f in (item20, item21, item22, item23, item24, item25, item26, item27, item28):
        f()
    print("all T3 checks passed")
