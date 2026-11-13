"""Checks every number and equilibrium claim in the Tier 2 solutions of Listas/pratica-lecture-06.md
that are written here (items 9-11, 13-18; item 12, Tadelis 11.5, is reused from
../lista-reais-lectures-01-05-solutions and checked by its check_C_L05.py):
Tadelis 10.8, Tadelis 11.2, Gibbons 2.19, Munoz-Garcia Ch. 6 Ex. 3, Gibbons 2.15, Tadelis 10.4,
M&R Math. 5, M&R Math. 3, Tadelis 10.6. Exact arithmetic (fractions, sympy); equilibrium claims
of the finite games are found by enumeration.

Run: python check_T2.py -> one line per item and "all T2 checks passed", or an AssertionError.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp


# ----------------------------------------------------------------------------- item 9
def item9():
    """Tadelis 10.8: p = 200 - Q, zero cost."""
    q = sp.symbols("q")
    # (a) Cournot: best reply (200 - qj)/2 -> 200/3, profit (200/3)^2
    qc = sp.solve(sp.Eq(q, (200 - q) / 2), q)[0]
    pic = (200 - 2 * qc) * qc
    assert (qc, pic) == (F(200, 3), F(40000, 9))
    # monopoly: Q = 100, profit 10000, split 5000
    Q = sp.symbols("Q")
    Qm = sp.solve(sp.diff((200 - Q) * Q, Q), Q)[0]
    pim = (200 - Qm) * Qm / 2
    assert (Qm, pim) == (100, 5000)
    qd = (200 - 50) / sp.Integer(2)
    pid = (200 - qd - 50) * qd
    assert (qd, pid) == (75, 5625)
    # (b) grim trigger: pim/(1-d) >= pid + d pic/(1-d)
    d = sp.symbols("d")
    sol = sp.solve(sp.Eq(pim / (1 - d), pid + d * pic / (1 - d)), d)[0]
    assert sol == F(9, 17)
    # (c)-(d) Bertrand: p = c = 0, zero profit; monopoly price 100; undercut gives 10000
    sold = sp.solve(sp.Eq(5000 / (1 - d), 10000), d)[0]
    assert sold == F(1, 2)
    # (e) two-period punishment: 5000 (1 + d + d^2) >= 10000  <=>  d + d^2 >= 1
    sole = [r for r in sp.solve(sp.Eq(d + d**2, 1), d) if r > 0][0]
    assert sp.simplify(sole - (sp.sqrt(5) - 1) / 2) == 0 and abs(float(sole) - 0.618034) < 1e-6
    assert F(1, 2) < float(sole) < 1
    print("item 9  (Tadelis 10.8): qC = 200/3, piC = 40000/9; monopoly 100, 5000 each; deviation 75 -> 5625; Cournot cutoff 9/17; Bertrand 1/2; two-period (sqrt5-1)/2 = 0.618")


# ----------------------------------------------------------------------------- item 10
def item10():
    """Tadelis 11.2: holdup. Enumerate the Nash equilibria of a grid version."""
    vL, vH, cL, cH = 6, 12, 2, 5  # vH > vL, cH > cL, vH - cH = 7 > vL - cL = 4
    assert vH > vL > 0 and cH > cL > 0 and vH - cH > vL - cL
    pie = {"L": vL, "H": vH}
    cost = {"L": cL, "H": cH}
    offers = {k: range(0, pie[k] + 1) for k in pie}  # P1's offer to P2 (integer grid)
    thr_range = {k: range(0, pie[k] + 2) for k in pie}  # P2 accepts iff offer >= threshold (pie+1 = reject all)

    def payoffs(inv, yL, yH, tL, tH):
        y = {"L": yL, "H": yH}[inv]
        t = {"L": tL, "H": tH}[inv]
        if y >= t:
            return pie[inv] - y, y - cost[inv]
        return 0, -cost[inv]

    profiles = list(product(offers["L"], offers["H"], "LH", thr_range["L"], thr_range["H"]))
    ne = []
    for yL, yH, inv, tL, tH in profiles:
        u1, u2 = payoffs(inv, yL, yH, tL, tH)
        if any(payoffs(inv, a, b, tL, tH)[0] > u1 for a in offers["L"] for b in offers["H"]):
            continue
        if any(payoffs(i2, yL, yH, a, b)[1] > u2 for i2 in "LH" for a in thr_range["L"] for b in thr_range["H"]):
            continue
        ne.append(((yL, yH, inv, tL, tH), (u1, u2)))
    outcomes = {u for _, u in ne}
    # SPE outcome: P2 invests L, proposer takes everything: (vL, -cL)
    assert (vL, -cL) in outcomes
    better = [u for u in outcomes if u[0] > vL and u[1] > -cL]
    assert better, outcomes
    # the Nash outcomes with H that beat the SPE for both: offer y with cH - cL < y < vH - vL
    ys = sorted({u[1] + cH for u in better})
    assert min(ys) > cH - cL and max(ys) < vH - vL
    # subgame perfection: only the L-outcome survives (backward induction)
    spe_y = 0
    assert pie["L"] - spe_y == vL and spe_y - cL == -cL > spe_y - cH
    print("item 10 (Tadelis 11.2): SPE outcome (vL, -cL) = (6, -2) is a Nash outcome; Nash outcomes beating it for both use H with cH - cL = 3 < y < vH - vL = 6, grid y = %s" % ys)


# ----------------------------------------------------------------------------- item 11
def item11():
    """Gibbons 2.19: three-period Rubinstein, period-3 split (s, 1-s) fixed."""
    for d, s in [(F(9, 10), F(1, 2)), (F(1, 2), F(3, 10)), (F(4, 5), F(9, 10))]:
        s2 = d * s  # P2's period-2 offer to P1
        s1 = 1 - d * (1 - s2)  # P1's period-1 demand
        assert s1 == 1 - d * (1 - d * s) == 1 - d + d * d * s
        # P1's payoff from any period-1 demand x on a fine grid, given P2's acceptance rule
        # (accept iff 1 - x >= d * (1 - s2)); a rejected demand leads to period 2 where P1 gets d * s2... discounted d^2 s
        best = max((x if x <= s1 else d * d * s, x) for x in [F(k, 1000) for k in range(0, 1001)])
        assert best[0] == max(s1, 0) and abs(best[1] - s1) <= F(1, 1000)
        # P2 in period 2: demanding more than 1 - s2 is rejected (P1 then gets s in period 3 -> P2 gets d(1-s)... )
        assert 1 - s2 > (1 - s) * d  # P2 prefers the accepted offer to waiting for period 3
        assert 1 - s1 == d * (1 - s2)  # P2 indifferent in period 1: accepts at equality
    # on the path agreement is in period 1 with s1 = 1 - d + d^2 s (cf. Gibbons p. 69)
    print("item 11 (Gibbons 2.19): s2 = d s, s1 = 1 - d + d^2 s; acceptance rules s1 <= s1* (P2) and s2 >= d s (P1) verified on grids for 3 parameter pairs")


# ----------------------------------------------------------------------------- item 13
def item13():
    """Munoz-Garcia Ch. 6 Ex. 3: temporary punishments of length T."""
    pim, pic, pid = F(2025, 2), F(900), F(18225, 16)
    assert pid == F(11390625, 10000)  # 1139.0625
    ratio = (pid - pim) / (pim - pic)
    assert ratio == F(9, 8)
    d = sp.symbols("d")
    # (c) grim trigger
    dg = (pid - pim) / (pid - pic)
    assert dg == F(9, 17) and abs(float(dg) - 0.5294) < 1e-4
    # book prints 0.901: it does not satisfy the inequality
    assert pim / (1 - F(3, 5)) >= pid + F(3, 5) * pic / (1 - F(3, 5))  # d = 0.6 < 0.901 already sustains cooperation
    assert pim / (1 - F(530, 1000)) >= pid + F(530, 1000) * pic / (1 - F(530, 1000))
    # (d)-(f): sum_{j=1}^T d^j >= 9/8
    roots = {}
    for T in (1, 2, 3):
        expr = sum(d**j for j in range(1, T + 1)) - F(9, 8)
        rs = [r for r in sp.Poly(expr, d).nroots() if abs(sp.im(r)) < 1e-12 and sp.re(r) > 0]
        roots[T] = float(sp.re(rs[0]))
    assert roots[1] == 1.125
    assert abs(roots[2] - 0.67260) < 1e-4 and abs(roots[3] - 0.58424) < 1e-4
    assert 1.125 > roots[2] > roots[3] > float(dg)
    # direct comparison of the two streams for T = 2 at d = 0.68 and 0.67 (horizon long enough)
    def stream(dv, T, coop):
        tot = 0.0
        for t in range(600):
            if coop:
                tot += float(pim) * dv**t
            elif t == 0:
                tot += float(pid)
            elif t <= T:
                tot += float(pic) * dv**t
            else:
                tot += float(pim) * dv**t
        return tot
    assert stream(0.68, 2, True) >= stream(0.68, 2, False)
    assert stream(0.67, 2, True) < stream(0.67, 2, False)
    print("item 13 (MG 6.3): pim=1012.5, pic=900, pid=1139.0625; ratio 9/8; grim 9/17=0.529 (book prints 0.901); T=1 d>=1.125; T=2 d>=%.4f; T=3 d>=%.4f" % (roots[2], roots[3]))


# ----------------------------------------------------------------------------- item 14
def item14():
    """Gibbons 2.15: n-firm Cournot, P = a - Q, zero cost."""
    a, n, dl = sp.symbols("a n delta", positive=True)
    pic = a**2 / (n + 1) ** 2
    pim = a**2 / (4 * n)
    qm = a / (2 * n)
    qD = (a - (n - 1) * qm) / 2
    pid = sp.simplify(qD**2)
    dstar = sp.simplify((pid - pim) / (pid - pic))
    assert sp.simplify(dstar - (n + 1) ** 2 / (n**2 + 6 * n + 1)) == 0
    assert sp.simplify(dstar - (1 - 4 * n / (n**2 + 6 * n + 1))) == 0
    assert dstar.subs(n, 2) == F(9, 17)
    assert [round(float(dstar.subs(n, k)), 3) for k in (2, 3, 5, 10)] == [0.529, 0.571, 0.643, 0.752]
    vals = [dstar.subs(n, k) for k in range(2, 12)]
    assert all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)) and vals[-1] < 1
    assert sp.limit(dstar, n, sp.oo) == 1
    # below delta*: smallest feasible symmetric output q(d) = C (n+1) / (A a)
    A = n + (1 - dl) * (n - 1) ** 2 / 4
    C = (1 - dl) / 4 + dl / (n + 1) ** 2
    qd = sp.simplify((n + 1) * C / A)  # in units of a
    # at delta = delta* the output is the monopoly output 1/(2n); at delta = 0 it is Cournot 1/(n+1)
    assert sp.simplify(qd.subs(dl, dstar) - 1 / (2 * n)) == 0
    assert sp.simplify(qd.subs(dl, 0) - 1 / (n + 1)) == 0
    # brute-force: for n = 3, delta = 1/2, the smallest q on a fine grid satisfying the no-deviation
    # constraint equals qd * a
    nn, dd = 3, F(1, 2)
    qdd = sp.Rational(qd.subs({n: nn, dl: dd}))

    def ok(q):
        prof = (1 - nn * q) * q
        qdev = (1 - (nn - 1) * q) / 2
        dev = qdev * qdev
        return prof / (1 - dd) >= dev + dd * F(1, (nn + 1) ** 2) / (1 - dd)

    grid = [F(k, 100000) for k in range(1, 40000)]
    qmin = min(q for q in grid if ok(q))
    assert abs(qmin - F(qdd.p, qdd.q)) < F(2, 100000), (qmin, qdd)
    assert ok(F(qdd.p, qdd.q)) and not ok(F(qdd.p, qdd.q) - F(1, 10**4))
    # profit decreasing in q above the monopoly output: the smallest feasible q is the best
    assert (1 - nn * qmin) * qmin > (1 - nn * F(1, nn + 1)) * F(1, nn + 1)
    print("item 14 (Gibbons 2.15): delta* = (n+1)^2/(n^2+6n+1) (n=2: 9/17), increasing to 1; q(delta) = (n+1)[(1-d)/4 + d/(n+1)^2] a / [n + (1-d)(n-1)^2/4] (n=3, d=1/2: %s a)" % qdd)


# ----------------------------------------------------------------------------- item 15
def item15():
    """Tadelis 10.4: trust game of Figure 10.1: N -> (0,0); T,C -> (1,1); T,D -> (-1,2)."""
    d = sp.symbols("d")
    assert sp.solve(sp.Eq(1 / (1 - d), 2), d)[0] == F(1, 2)
    # P2's strategy 'cooperate whenever trusted': Nash for d >= 1/2 against P1's grim trust
    for dv in (F(1, 2), F(3, 4), F(9, 10)):
        assert 1 / (1 - dv) >= 2 + dv * 0  # on path vs deviation (2 now, then never trusted: 0)
    # not subgame perfect: after a past defection P1 plays N forever (his strategy), but if he trusts
    # once at t+1 (off path) P2's continuation after that is 0 whatever P2 does, so D (2) beats C (1)
    for dv in (F(1, 10), F(1, 2), F(99, 100)):
        value_C = 1 + dv * 0
        value_D = 2 + dv * 0
        assert value_D > value_C
    # Nash check by enumerating P1 deviations (switch to N at period k) against P2 'C whenever trusted'
    dv = F(9, 10)
    on = sum(dv**t for t in range(400))
    for k in range(0, 6):
        dev = sum(dv**t for t in range(k))  # trust until k then N forever
        assert dev <= on
    print("item 15 (Tadelis 10.4): 1/(1-d) >= 2 iff d >= 1/2; after a past defection D (2) beats C (1) for every d, so the strategy is not subgame perfect")


# ----------------------------------------------------------------------------- item 16
def item16():
    """M&R Math. 5: honour iff V/(1-p) >= V + G."""
    V, G, p = sp.symbols("V G p", positive=True)
    sol = sp.solve(sp.Eq(V / (1 - p), V + G), p)[0]
    assert sp.simplify(sol - G / (V + G)) == 0
    for Vv, Gv in [(3, 2), (1, 10), (10, 1)]:
        pstar = F(Gv, Vv + Gv)
        assert 0 < pstar < 1
        assert F(Vv) / (1 - pstar) == Vv + Gv
        assert F(Vv) / (1 - (pstar + F(1, 100))) > Vv + Gv > F(Vv) / (1 - (pstar - F(1, 100)))
    assert F(2, 5) == F(2, 3 + 2) and F(10, 11) == F(10, 1 + 10)  # p* for (V, G) = (3, 2) and (1, 10)
    # offeror: offering trust yields V/(1-p) > 0 whatever L is; L only matters off the path
    assert all(F(3) / (1 - F(k, 10)) > 0 for k in range(1, 10))
    print("item 16 (M&R Math 5): p* = G/(G+V) in (0,1) for every G, L; L does not enter")


# ----------------------------------------------------------------------------- item 17
def item17():
    """M&R Math. 3: honest worker flagged with prob q, cheater flagged with p + (1-p) q."""
    p, q, g, N, wbar = sp.symbols("p q g N wbar", positive=True)
    flag_cheat = p + (1 - p) * q
    diff = sp.simplify(flag_cheat - q)
    assert sp.simplify(diff - p * (1 - q)) == 0
    wstar = wbar + g / (N * p * (1 - q))
    # incentive constraint holds with equality at wstar
    assert sp.simplify(p * (1 - q) * (wstar - wbar) * N - g) == 0
    assert sp.simplify(wstar.subs(q, 0) - (wbar + g / (N * p))) == 0
    assert sp.simplify(sp.diff(wstar, q)) != 0 and sp.simplify(sp.diff(wstar, q) - g / (N * p * (1 - q) ** 2)) == 0
    val = wstar.subs({p: F(1, 2), q: F(1, 5), g: 1000, N: 4, wbar: 40000})
    assert val == 40000 + F(1000, 4) * F(1, 2) ** -1 * F(5, 4)
    assert val == 40625
    # alternative reading: the cheater is flagged with probability p, the honest worker with q
    walt = wbar + g / (N * (p - q))
    assert sp.simplify(walt.subs({p: F(1, 2), q: F(1, 5), g: 1000, N: 4, wbar: 40000})) == 40000 + F(1000, 4) / F(3, 10)
    print("item 17 (M&R Math 3): w* = wbar + g/(N p (1-q)); example p=1/2, q=1/5, g=1000, N=4: w* = 40625 (q=0: 40500)")
    assert wstar.subs({p: F(1, 2), q: 0, g: 1000, N: 4, wbar: 40000}) == 40500


# ----------------------------------------------------------------------------- item 18
def item18():
    """Tadelis 10.6: regulated drug. Rows G, B; columns Buy, Not."""
    def game(price):
        firm = {("G", "B"): price - 4, ("G", "N"): -4, ("B", "B"): price, ("B", "N"): 0}
        cons = {("G", "B"): 9 - price, ("G", "N"): 0, ("B", "B"): 4 - price, ("B", "N"): 0}
        return firm, cons

    def pure_ne(firm, cons):
        out = []
        for f, c in product("GB", "BN"):
            if all(firm[(f, c)] >= firm[(f2, c)] for f2 in "GB") and all(cons[(f, c)] >= cons[(f, c2)] for c2 in "BN"):
                out.append((f, c))
        return out

    f6, c6 = game(6)
    assert pure_ne(f6, c6) == [("B", "N")]
    assert f6[("G", "B")] == 2 and c6[("G", "B")] == 3 and f6[("B", "B")] == 6 and c6[("B", "B")] == -2
    # B strictly dominates G for the firm (6 > 2, 0 > -4), so no mixed equilibrium puts weight on G
    assert f6[("B", "B")] > f6[("G", "B")] and f6[("B", "N")] > f6[("G", "N")]
    # (b) unique stage equilibrium -> unique SPE for any finite repetition: nothing to enumerate
    # (c) trigger: (p - 4)/(1 - d) >= p  <=>  d >= 4/p
    d = sp.symbols("d")
    for price, cut in [(6, F(2, 3)), (5, F(4, 5))]:
        sol = sp.solve(sp.Eq((price - 4) / (1 - d), price), d)[0]
        assert sol == cut == F(4, price)
    f5, c5 = game(5)
    assert pure_ne(f5, c5) == [("B", "N")]
    assert c5[("G", "B")] == 4 and c6[("G", "B")] == 3
    # at d in [2/3, 4/5) price 6 sustains G but price 5 does not
    dv = F(7, 10)
    assert (6 - 4) / (1 - dv) >= 6 and (5 - 4) / (1 - dv) < 5
    # consumer's surplus on the good path rises by the price cut: 4 vs 3 per period
    print("item 18 (Tadelis 10.6): unique NE (B, Not); trigger delta >= 4/p: 2/3 at p=6, 4/5 at p=5; consumer 3 -> 4 per period if G survives")


if __name__ == "__main__":
    for f in (item9, item10, item11, item13, item14, item15, item16, item17, item18):
        f()
    print("all T2 checks passed")
