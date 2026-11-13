"""Lecture 7, Tier 2 (items 9-18): tadelis-12-2, gibbons-3-3, tadelis-12-3, tadelis-12-9,
tadelis-12-5, tadelis-12-6, gibbons-3-6, tadelis-13-9, tadelis-13-3, tadelis-12-8.
Exact arithmetic (fractions, sympy); scipy for continuous best replies.
Run: python check_E2.py -> one line per item and "all E2 checks passed", or an AssertionError."""
from fractions import Fraction as F
from itertools import product

import sympy as sp
from scipy.optimize import minimize_scalar

from bayes import pure_bne

R_ = sp.Rational

# ---- item 9 (tadelis-12-2): Cournot with private costs
a, b, mu, cL, cH, qL, qH = sp.symbols("a b mu c_L c_H q_L q_H", positive=True)
Eq = mu * qL + (1 - mu) * qH
foc = [sp.Eq(a - cL - b * Eq - 2 * b * qL, 0), sp.Eq(a - cH - b * Eq - 2 * b * qH, 0)]
sol = sp.solve(foc, [qL, qH], dict=True)[0]
cbar = mu * cL + (1 - mu) * cH
assert sp.simplify(sol[qL] - (2 * a - 3 * cL + cbar) / (6 * b)) == 0
assert sp.simplify(sol[qH] - (2 * a - 3 * cH + cbar) / (6 * b)) == 0
assert sp.simplify(sol[qL] - ((a - cL) / (3 * b) + (1 - mu) * (cH - cL) / (6 * b))) == 0
assert sp.simplify(sol[qH] - ((a - cH) / (3 * b) - mu * (cH - cL) / (6 * b))) == 0
assert sp.simplify(mu * sol[qL] + (1 - mu) * sol[qH] - (a - cbar) / (3 * b)) == 0
# asymmetric profiles: the 4 FOCs (two firms, two types) are linear with a unique solution
q1L, q1H, q2L, q2H = sp.symbols("q1L q1H q2L q2H")
E1 = mu * q1L + (1 - mu) * q1H
E2 = mu * q2L + (1 - mu) * q2H
full = sp.solve([a - cL - b * E2 - 2 * b * q1L, a - cH - b * E2 - 2 * b * q1H,
                 a - cL - b * E1 - 2 * b * q2L, a - cH - b * E1 - 2 * b * q2H], [q1L, q1H, q2L, q2H], dict=True)
assert len(full) == 1 and sp.simplify(full[0][q1L] - sol[qL]) == 0 and sp.simplify(full[0][q2H] - sol[qH]) == 0
# numeric best reply against the equilibrium (a=10, b=1, cL=1, cH=3, mu=2/5), scipy
num = {a: 10, b: 1, cL: 1, cH: 3, mu: R_(2, 5)}
qLn, qHn = float(sol[qL].subs(num)), float(sol[qH].subs(num))
for c, qstar in ((1, qLn), (3, qHn)):
    Eqo = 0.4 * qLn + 0.6 * qHn
    r = minimize_scalar(lambda q: -((10 - (q + Eqo) - c) * q), bounds=(0, 10), method="bounded",
                        options={"xatol": 1e-10})
    assert abs(r.x - qstar) < 1e-5
print("tadelis-12-2: q_L = (a-c_L)/(3b) + (1-mu)(c_H-c_L)/(6b), q_H = (a-c_H)/(3b) - mu(c_H-c_L)/(6b); unique, best reply checked")

# ---- item 10 (gibbons-3-3): Bertrand with private demand sensitivity
a, th, bH, bL, pH, pL = sp.symbols("a theta b_H b_L p_H p_L", positive=True)
pbar = th * pH + (1 - th) * pL
sol10 = sp.solve([sp.Eq(a - 2 * pH - bH * pbar, 0), sp.Eq(a - 2 * pL - bL * pbar, 0)], [pH, pL], dict=True)[0]
bbar = th * bH + (1 - th) * bL
assert sp.simplify(sol10[pH] - a * (2 + bbar - bH) / (2 * (2 + bbar))) == 0
assert sp.simplify(sol10[pL] - a * (2 + bbar - bL) / (2 * (2 + bbar))) == 0
assert sp.simplify(th * sol10[pH] + (1 - th) * sol10[pL] - a / (2 + bbar)) == 0
p_ = sp.symbols("p")
pj = sp.symbols('p_j')
assert sp.diff(p_ * (a - p_ - bH * pj), p_, 2) == -2  # profit is strictly concave in own price
num = {a: 10, bH: R_(3, 2), bL: R_(1, 2), th: R_(1, 3)}
pHn, pLn = float(sol10[pH].subs(num)), float(sol10[pL].subs(num))
pb = pHn / 3 + 2 * pLn / 3
for bi, pstar in ((1.5, pHn), (0.5, pLn)):
    r = minimize_scalar(lambda p: -(p * (10 - p - bi * pb)), bounds=(0, 10), method="bounded",
                        options={"xatol": 1e-10})
    assert abs(r.x - pstar) < 1e-5
print("gibbons-3-3: p_i(b) = a(2 + bbar - b)/(2(2 + bbar)), bbar = theta b_H + (1-theta) b_L; best reply checked")

# ---- item 11 (tadelis-12-3): armed conflict, all pure BNE
def conflict(m, w, s):
    cost = {"S": s, "W": w}

    def u(i, a1, a2, t1, t2):
        ai, aj = (a1, a2)[i], (a1, a2)[1 - i]
        ti, tj = (t1, t2)[i], (t1, t2)[1 - i]
        if ai == "N":
            return F(0)
        if aj == "N":
            return F(m)
        return F(m - cost[ti]) if (ti == "S" and tj == "W") else F(-cost[ti])

    T = [["S", "W"], ["S", "W"]]
    prior = {(x, y): F(1, 4) for x in "SW" for y in "SW"}
    return pure_bne(T, [["A", "N"], ["A", "N"]], prior, u)


bA, _ = conflict(3, 2, 1)
assert sorted(bA) == sorted([(("A", "A"), ("A", "N")), (("A", "N"), ("A", "A"))]), bA
bB, _ = conflict(3, 4, 2)
assert sorted(bB) == sorted([(('A', 'A'), ('N', 'N')), (('A', 'N'), ('A', 'N')), (('N', 'N'), ('A', 'A'))])
print("tadelis-12-3 case a:", bA)
print("tadelis-12-3 case b:", bB)
# expected payoffs of attack against each rival strategy (rival: action of S-type, action of W-type)
for case, (m, w, s) in (("a", (3, 2, 1)), ("b", (3, 4, 2))):
    cost = {"S": s, "W": w}
    for own in "SW":
        row = []
        for rival in product("AN", repeat=2):  # (action if S, action if W)
            tot = F(0)
            for tj, aj in zip("SW", rival):
                if aj == "N":
                    tot += F(1, 2) * m
                else:
                    tot += F(1, 2) * (F(m - cost[own]) if (own == "S" and tj == "W") else F(-cost[own]))
            row.append((rival, tot))
        print(f"  case {case}, own {own}: ", ", ".join(f"vs {''.join(r)}: {t}" for r, t in row))

# ---- item 12 (tadelis-12-9): grab the dollar
p_, e, t1, t2 = sp.symbols("p epsilon t1 t2")
assert sp.solve(sp.Eq((1 - p_) * 1 + p_ * (-1), 0), p_) == [R_(1, 2)]  # mixed NE of the complete-information game
pr = lambda t: (e - t) / (2 * e)  # prob. a player with threshold t grabs
thr = lambda pj: (2 * pj - 1) / (1 - pj)  # grab iff theta >= (2p_j - 1)/(1 - p_j)
sols = sp.solve([sp.Eq(t1, thr(pr(t2))), sp.Eq(t2, thr(pr(t1)))], [t1, t2], dict=True)
interior = [s for s in sols if all(-0.5 < float(s[t].subs(e, R_(1, 2))) < 0.5 for t in (t1, t2))]
assert interior == [{t1: 0, t2: 0}], sols
assert sp.simplify(pr(0)) == R_(1, 2)  # grab probability 1/2 for every epsilon: converges to the mixed NE
# corner (asymmetric) pure BNE: player 2 always grabs (1+theta_2 > 0 since epsilon < 1), player 1 never does
for eps in (R_(1, 10), R_(1, 2), R_(9, 10)):
    assert 1 - eps > 0  # lowest 1 + theta_2
    assert (1 - 1) * 1 - 1 < 0  # player 1 facing p_2 = 1: grabbing gives -1 < 0
print("tadelis-12-9: mixed NE p = 1/2; unique interior symmetric BNE threshold 0 (grab prob 1/2 for all eps); corner BNEs exist")

# ---- item 13 (tadelis-12-5): the gold mine
x, p = sp.symbols("x p", positive=True)
cond = sp.integrate(4 * x - p, (x, 0, p / 3)) / (p / 3)  # owner's payoff given types x <= p/3
assert sp.simplify(cond + p / 3) == 0
assert sp.simplify(sp.integrate(x, (x, 0, p / 3)) / (p / 3) - p / 6) == 0
cond_big = sp.integrate(4 * x - p, (x, 0, 1))  # p >= 3: all types sell
assert sp.simplify(cond_big - (2 - p)) == 0 and (2 - 3) < 0
assert sp.integrate(3 * x, (x, 0, 1)) == R_(3, 2)  # prospector's expected payoff in equilibrium
print("tadelis-12-5: owner's expected net at price p is -p/3 < 0; no trade; payoffs 3x and 0 (prospector avg 3/2)")

# ---- item 14 (tadelis-12-6): reap and weep
th, w = sp.symbols("theta w", positive=True)
assert sp.simplify(sp.integrate(R_(3, 2) * th - w, (th, 0, w)) / w + w / 4) == 0  # (a): -w/4
assert sp.integrate(th, (th, 0, 1)) == R_(1, 2)  # (b): surplus 1/2
# (c): outside option theta/2: type sells iff w >= theta/2 <=> theta <= 2w
low = sp.integrate(R_(3, 2) * th - w, (th, 0, 2 * w)) / (2 * w)  # w <= 1/2
assert sp.simplify(low - w / 2) == 0
high = sp.integrate(R_(3, 2) * th - w, (th, 0, 1))  # w >= 1/2: everyone sells
assert sp.simplify(high - (R_(3, 4) - w)) == 0 and sp.solve(sp.Eq(high, 0), w) == [R_(3, 4)]
surplus_low = sp.integrate(R_(3, 2) * th, (th, 0, 2 * w)) + sp.integrate(th / 2, (th, 2 * w, 1))
assert sp.simplify(surplus_low - (R_(1, 4) + 2 * w ** 2)) == 0
assert surplus_low.subs(w, R_(1, 2)) == R_(3, 4) == sp.integrate(R_(3, 2) * th, (th, 0, 1))
assert sp.integrate(th / 2, (th, 0, 1)) == R_(1, 4)  # no-trade surplus after the policy
assert sp.solve(sp.Eq(R_(1, 4) + 2 * w ** 2, R_(1, 2)), w) == [sp.sqrt(2) / 4]  # break-even wage vs 1/2
print("tadelis-12-6: (a) -w/4 <0, no trade; (b) surplus 1/2; (c) after the policy trade at w in (0,3/4], "
      "surplus 1/4 + 2w^2 (w<=1/2) or 3/4, best 3/4 > 1/2")

# ---- item 15 (gibbons-3-6): first price, n uniform bidders
v, bid = sp.symbols("v b", positive=True)
for n in range(2, 8):
    EU = (n * bid / (n - 1)) ** (n - 1) * (v - bid)
    s = sp.solve(sp.diff(EU, bid), bid)
    assert s == [(n - 1) * v / n], (n, s)
    vv = 0.7
    r = minimize_scalar(lambda z: -((n * z / (n - 1)) ** (n - 1) * (vv - z)) if z <= (n - 1) / n else -(vv - z),
                        bounds=(0, 1), method="bounded", options={"xatol": 1e-10})
    assert abs(r.x - (n - 1) * vv / n) < 1e-5
    t = sp.symbols("t")
    rev = sp.integrate((n - 1) / sp.Integer(n) * t * n * t ** (n - 1), (t, 0, 1))
    sec = sp.integrate(t * n * (n - 1) * t ** (n - 2) * (1 - t), (t, 0, 1))  # E[second highest value]
    assert rev == sec == sp.Rational(n - 1, n + 1)
print("gibbons-3-6: b = (n-1)v/n is a best reply to itself for n = 2..7; revenue (n-1)/(n+1) = second-price revenue")

# ---- item 16 (tadelis-13-9): private values 0.5 + theta, linear bidding
th, xx, aa, bb = sp.symbols("theta x a b", positive=True)
EU = ((xx - aa) / bb) * (R_(1, 2) + th - xx)
xs = sp.solve(sp.diff(EU, xx), xx)[0]
assert sp.simplify(xs - (R_(1, 2) + th + aa) / 2) == 0
ab = sp.solve([sp.Eq(bb, R_(1, 2)), sp.Eq(aa, (R_(1, 2) + aa) / 2)], [aa, bb], dict=True)
assert ab == [{aa: R_(1, 2), bb: R_(1, 2)}]
bidfun = lambda z: 0.5 + 0.5 * z
for tt in (0.0, 0.2, 0.5, 0.9, 1.0):
    f = lambda x_: -(max(0.0, min(1.0, (x_ - 0.5) / 0.5)) * (0.5 + tt - x_))
    r = minimize_scalar(f, bounds=(0, 1.5), method="bounded", options={"xatol": 1e-10})
    assert abs(r.x - bidfun(tt)) < 1e-4 or tt == 0.0  # at theta=0 any bid <= 0.5 gives 0 and 0.5 is a best reply
    assert abs(-f(bidfun(tt)) - tt ** 2 / 2) < 1e-12
assert sp.simplify(EU.subs({aa: R_(1, 2), bb: R_(1, 2)}).subs(xx, R_(1, 2) + th / 2) - th ** 2 / 2) == 0
print("tadelis-13-9: s(theta) = 1/2 + theta/2 (a = b = 1/2); expected payoff theta^2/2; best reply checked")

# ---- item 17 (tadelis-13-3): reserve prices, values {0,1,2}
vals3 = [F(0), F(1), F(2)]


def revenue(r):
    tot = F(0)
    for v1, v2 in product(vals3, repeat=2):  # bids = values (weakly dominant)
        hi, lo = max(v1, v2), min(v1, v2)
        if hi < r:
            pay = F(0)
        elif lo < r:
            pay = r
        else:
            pay = lo
        tot += pay / 9
    return tot


assert revenue(F(0)) == F(5, 9)
assert revenue(F(1)) == F(1)
assert revenue(F(2)) == F(10, 9)
for r in [F(k, 10) for k in range(1, 11)]:
    assert revenue(r) == F(5, 9) + F(4, 9) * r, r
for r in [F(k, 10) for k in range(11, 21)]:
    assert revenue(r) == (4 * r + 2) / 9, r
assert max(revenue(F(k, 10)) for k in range(0, 31)) == F(10, 9)
assert all(revenue(F(k, 10)) < F(10, 9) for k in range(0, 20)) and revenue(F(21, 10)) == 0


def pay_rule(v, bid, rho, r):
    """Payoff to a bidder of value v with bid `bid` against a single rival bid rho (tie = coin)."""
    def win_price():
        return r if rho < r else rho
    if bid < r:
        return F(0)
    if rho < r or bid > rho:
        return v - win_price()
    if bid == rho:
        return F(1, 2) * (v - rho)
    return F(0)


rgrid = [F(k, 4) for k in range(0, 11)]
for r in (F(1, 2), F(1), F(3, 2), F(2)):
    for v in (F(0), F(1), F(2), F(1, 2), F(3, 2)):
        for bid in rgrid:
            for rho in rgrid:
                assert pay_rule(v, v, rho, r) >= pay_rule(v, bid, rho, r), (r, v, bid, rho)
print("tadelis-13-3: b = v still weakly dominant for r > 0; revenue r=0: 5/9, r=1: 1, r=2: 10/9 (optimal)")


# ---- item 18 (tadelis-12-8): jury voting
def jury(q, p, n, k):
    """Pure BNE (symmetric or not) of the n-juror game with conviction iff >= k votes C.
    Strategy xy: x on signal G, y on signal I. Common payoff = probability of a correct verdict."""
    strat = list(product("AC", repeat=2))

    def correct(prof):
        tot = F(0)
        for sig in product("GI", repeat=n):
            pg = q * F(1)
            pi = (1 - q)
            for sg in sig:
                pg *= p if sg == "G" else 1 - p
                pi *= (1 - p) if sg == "G" else p
            votes = sum(1 for j in range(n) if prof[j][0 if sig[j] == "G" else 1] == "C")
            conv = votes >= k
            tot += pg if conv else pi
        return tot

    out = []
    for prof in product(strat, repeat=n):
        base = correct(prof)
        if all(correct(prof[:j] + (s2,) + prof[j + 1:]) <= base for j in range(n) for s2 in strat):
            out.append("".join("".join(s) + "," for s in prof)[:-1])
    return out, correct


cases = {"p>q": (F(3, 5), F(4, 5)), "p<q": (F(4, 5), F(3, 5)), "p=q": (F(3, 5), F(3, 5))}
for name, (q, p) in cases.items():
    out2, corr2 = jury(q, p, 2, 2)
    print(f"  two jurors, unanimity, {name} (q={q}, p={p}): pure BNE = {out2}")
    if p > q:
        assert "CC,CC" not in out2 and "AA,AA" in out2 and "CA,CA" not in out2
    else:
        assert "CC,CC" in out2 and "AA,AA" in out2 and "CA,CA" not in out2
        assert corr2((("C", "C"),) * 2) == q
# (b) single decider: voting by signal gives p, always convicting gives q
for name, (q, p) in cases.items():
    out1, corr1 = jury(q, p, 1, 1)
    assert corr1((("C", "A"),)) == p and corr1((("C", "C"),)) == q
    assert ("CA" in out1) == (p >= q) and ("CC" in out1) == (p <= q)
    out2, corr2 = jury(q, p, 2, 2)
    best2 = max(corr2(tuple(tuple(s) for s in [x[:2], x[3:]])) for x in out2)
    assert max(p, q) >= best2
# (c) three jurors, majority: voting by signal is a BNE iff p >= q (grid of q, p)
for q in [F(k, 20) for k in range(11, 20)]:
    for p in [F(k, 20) for k in range(11, 20)]:
        out3, _ = jury(q, p, 3, 2)
        assert ("CA,CA,CA" in out3) == (p >= q), (q, p, out3)
print("tadelis-12-8: CC,CC is a BNE iff p <= q (not for p > q, contrary to the book text); AA,AA always; "
      "single juror gets max(p,q); 3 jurors majority: CA,CA,CA iff p >= q")
print("all E2 checks passed")
