"""Checks every number and equilibrium claim in the Lecture 8 solutions, Tier 3 (items 18-25):
sol-mwg-13-c-1, sol-mwg-13-c-5, sol-tadelis-15-6, sol-gibbons-4-7, sol-tadelis-16-7,
sol-munoz-garcia-11-4, sol-mwg-13-c-2, sol-mwg-13-c-4.
Exact arithmetic (fractions, sympy); floats only where a square root appears.

Run: python check_T3.py  -> one line per item and "all T3 checks passed", or an
AssertionError on the first wrong claim.
"""
import math
from fractions import Fraction as F
from itertools import product

import sympy as sp

from ne_tools import pure_pbe, simplex

h = F(1, 2)
EPS = 1e-9

# ---------------------------------------------------------------------------- mwg-13-c-1
x, a, th = sp.symbols("x a theta", positive=True)
for dens in (sp.Integer(1), 2 * th):                         # uniform and f = 2*theta on [0, 1]
    for lo in (sp.Integer(0), sp.Rational(1, 5)):
        cond_mean = sp.integrate(th * dens, (th, lo, x)) / sp.integrate(dens, (th, lo, x))
        pt = {x: sp.Rational(9, 10)}
        assert cond_mean.subs(pt) < sp.Rational(9, 10)       # E[theta | N] < sup N for a non-null N
assert sp.simplify(sp.integrate(th, (th, a, x)) / (x - a) - (a + x) / 2) == 0   # uniform: (a+x)/2 < x
print("mwg-13-c-1: E[theta | N] < sup N for every non-null N under atomless densities "
      "(uniform and 2*theta), so a non-null no-test set is impossible")

# ---------------------------------------------------------------------------- mwg-13-c-5
lam, vH, vL, p = sp.symbols("lambda v_H v_L p", positive=True)
cut = sp.solve(sp.Eq(lam * vH + (1 - lam) * vL, p), lam)[0]
assert sp.simplify(cut - (p - vL) / (vH - vL)) == 0          # buy iff lambda >= (p - v_L)/(v_H - v_L)
# discrete advertising game: v_H=10, p=6, v_L=4, c_H=3, c_L=1, A in {0,...,4}
vH_, p_, vL_, cH, cL = 10, 6, 4, 3, 1
assert vH_ > p_ > vL_ > cH > cL
ads = range(5)
US = [[[p_ - cH - A, -A] for A in ads], [[p_ - cL - A, -A] for A in ads]]     # [type][A][buy, no]
UR = [[[vH_ - p_, 0] for A in ads], [[vL_ - p_, 0] for A in ads]]
lam_ = F(1, 2)
assert lam_ * (vH_ - p_) + (1 - lam_) * (vL_ - p_) >= 0      # (a): consumer buys at the prior
res = pure_pbe([lam_, 1 - lam_], [list(ads)] * 2, [2] * 5, US, UR, n=60)
assert res and all(s[0] == s[1] for s, c, o in res)          # only pooling PBE exist
assert not [1 for s, c, o in res if s[0] != s[1]]            # no separating PBE
for A in range(0, 50):                                       # low type's mimicking profit > high's
    assert p_ - cL - A > p_ - cH - A
print("mwg-13-c-5: buy iff lambda >= (p-v_L)/(v_H-v_L); no separating PBE in the discrete "
      "advertising game (%d pooling PBE found, 0 separating)" % len(res))

# --------------------------------------------------------------------------- tadelis-15-6
# P1: A or B ; P2 (after B): C or D ; P3 (info set {x3, x4}): E or F ; mu = Pr(x3)
outcome = {("A", None, "E"): (3, 3, 2), ("A", None, "F"): (0, 0, 0),
           ("B", "C", "E"): (4, 4, 0), ("B", "C", "F"): (0, 0, 1),
           ("B", "D", None): (1, 1, 1)}


def play(a1, a2, a3):
    if a1 == "A":
        return outcome[("A", None, a3)]
    return outcome[("B", "D", None)] if a2 == "D" else outcome[("B", "C", a3)]


profiles = list(product("AB", "CD", "EF"))
ne = [s for s in profiles
      if play(*s)[0] == max(play(b, s[1], s[2])[0] for b in "AB")
      and play(*s)[1] == max(play(s[0], c, s[2])[1] for c in "CD")
      and play(*s)[2] == max(play(s[0], s[1], e)[2] for e in "EF")]
assert ne == [("A", "D", "E"), ("B", "D", "F")]


def pbe_with(s, mu):
    a1, a2, a3 = s
    eu3 = {"E": 2 * mu + 0 * (1 - mu), "F": 0 * mu + 1 * (1 - mu)}
    ok3 = eu3[a3] == max(eu3.values())
    # P2 at x2 (singleton): best reply to P3's strategy a3, on or off the path
    ok2 = play("B", a2, a3)[1] == max(play("B", c, a3)[1] for c in "CD")
    ok1 = play(*s)[0] == max(play(b, a2, a3)[0] for b in "AB")
    bayes = (a1 == "A" and mu == 1) or (a1 == "B" and a2 == "D") or (a1 == "B" and a2 == "C" and mu == 0)
    return ok1 and ok2 and ok3 and bayes


pbe = {(s, mu) for s in ne for mu in [F(k, 60) for k in range(61)] if pbe_with(s, mu)}
assert {s for s, mu in pbe} == {("B", "D", "F")}             # (A,D,E) fails at x2: C pays 4 > 1
assert sorted(mu for s, mu in pbe)[-1] == F(1, 3)            # F optimal iff mu <= 1/3
assert play("B", "C", "E")[1] == 4 > play("B", "D", "E")[1] == 1


def tremble_belief(eA, eC):
    return eA / (eA + (1 - eA) * eC)                         # Pr(x3 | info set) with Pr(A)=eA, Pr(C|B)=eC


for target in (F(0), F(1, 4), F(1, 3)):                      # any mu <= 1/3 is a limit of Bayes beliefs
    k = 10 ** 7
    eA = F(1, k) if target > 0 else F(1, k * k)
    eC = eA * (1 - target) / target if target > 0 else F(1, k)
    assert abs(float(tremble_belief(eA, eC)) - float(target)) < 1e-6
print("tadelis-15-6: pure BNE (A,D,E), (B,D,F); PBE only (B,D,F) with mu<=1/3 ((A,D,E) fails at x2); "
      "(B,D,F) is also sequential: any mu<=1/3 is a limit of trembles")

# ---------------------------------------------------------------------------- gibbons-4-7
# types eta_L=1, eta_H=2, Pr(H)=2/3; cost e^2/eta; y = eta; w(e) = E[eta | e]
q_, r_, estar = F(2, 3), F(1, 2), F(1)
mu0 = q_ * (1 - r_) / (q_ * (1 - r_) + (1 - q_))             # Bayes at e=0 (H plays 0 w.p. 1-r)
assert mu0 == h
w0 = 1 * (1 - mu0) + 2 * mu0
assert w0 == F(3, 2)
cost = lambda eta, e: e * e / eta
assert w0 - cost(2, 0) == 2 - cost(2, estar)                 # H indifferent: 3/2 = 2 - 1/2
assert w0 - cost(1, 0) > 2 - cost(1, estar)                  # L strictly prefers 0: 3/2 > 1


def wage(e):
    return w0 if e == 0 else (F(2) if e == estar else F(1))  # off-path belief: low type


for eta in (1, 2):
    eqpay = w0 - cost(eta, 0)
    for e in [F(k, 20) for k in range(0, 101)]:
        assert wage(e) - cost(eta, e) <= eqpay
for e in [F(k, 20) for k in range(0, 101)]:                  # even wage 2 (best case) deters L,H beyond e*
    if e >= estar:
        assert 2 - cost(1, e) < w0 and 2 - cost(2, e) <= w0
print("gibbons-4-7: hybrid PBE, L plays 0; H plays e*=1 w.p. 1/2 and 0 w.p. 1/2; "
      "mu(0)=1/2, w(0)=3/2, w(1)=2, off-path belief low type")

# ---------------------------------------------------------------------------- tadelis-16-7
q = sp.symbols("q", real=True)
lo_roots = sp.solve(sp.Eq((3 - q) * q + sp.Rational(9, 4), sp.Rational(13, 4)), q)
hi_roots = sp.solve(sp.Eq((4 - q) * q + 4, sp.Rational(25, 4)), q)
qmin, qmax = (3 + math.sqrt(5)) / 2, 2 + math.sqrt(1.75)
assert abs(max(float(r) for r in lo_roots) - qmin) < EPS and abs(float(max(hi_roots)) - qmax) < EPS
assert abs(qmin - 2.618) < 1e-3 and abs(qmax - 3.323) < 1e-3
H_eq = 3.25
H_dev = lambda qq: (3 - qq) * qq + 2.25                      # H's best payoff from output qq (entry deterred)
L_dev = lambda qq: (4 - qq) * qq + 4                         # L's best payoff from qq (entry deterred)
grid = [i / 1000 for i in range(0, 6001)]


def survives(qs):
    """Intuitive criterion for the separating PBE with q_1^{1L} = qs."""
    L_eq = L_dev(qs)
    for qq in grid:
        domH = H_eq > H_dev(qq) + EPS
        domL = L_eq > L_dev(qq) + EPS
        if domH and not domL and L_dev(qq) > L_eq + EPS:     # belief must be 'low cost': L deviates
            return False
    return True


assert survives(qmin)
for qs in [qmin + t * (qmax - qmin) / 20 for t in range(1, 21)]:
    assert not survives(qs)
assert not survives(qmin + 0.01) and not survives(qmax)
print("tadelis-16-7: separating set [%.4f, %.4f]; only q_1^{1L}=(3+sqrt5)/2=%.4f survives the "
      "intuitive criterion" % (qmin, qmax, qmin))

# -------------------------------------------------------------------------- munoz-garcia-11-4
lo_, hi_ = 1.0, 2 ** (1 / 3)
# separating (e1=0, e2=eb): IC1: 1 >= 2 - eb^3 ; IC2: 2 - eb^3/2 >= 1
assert abs(sp.solve(sp.Eq(1, 2 - q ** 3), q)[0] - 1) < EPS
assert abs(float(sp.real_root(2, 3)) - hi_) < EPS


def sep_ok(eb):
    u1_eq, u2_eq = 1.0, 2 - eb ** 3 / 2
    for e in [i / 500 for i in range(0, 2001)]:
        w = 1.0                                              # worst off-path belief: low type
        if e == eb:
            continue
        if w - e ** 3 / 1 > u1_eq + EPS or w - e ** 3 / 2 > u2_eq + EPS:
            return False
    return 1 >= 2 - eb ** 3 - EPS and u2_eq >= 1 - EPS


for eb in [i / 100 for i in range(0, 201)]:
    assert sep_ok(eb) == (lo_ - EPS <= eb <= hi_ + EPS)


def ic_survives(eb):
    u2_eq = 2 - eb ** 3 / 2
    for e in [i / 1000 for i in range(0, 2001)]:
        dom1 = 1.0 > 2 - e ** 3 + EPS                        # theta=1: best case wage 2
        dom2 = u2_eq > 2 - e ** 3 / 2 + EPS
        if dom1 and not dom2 and 2 - e ** 3 / 2 > u2_eq + EPS:
            return False
    return True


assert ic_survives(1.0)
for eb in [1.01, 1.1, 1.2, hi_]:
    assert not ic_survives(eb)
print("munoz-garcia-11-4: separating e_2 in [1, 2^(1/3)] = [1, %.4f] (e_1 = 0); only e_2 = 1 "
      "survives the intuitive criterion" % hi_)

# ---------------------------------------------------------------------------- mwg-13-c-2
e = sp.symbols("e", positive=True)
muu, tL, tH, lm = sp.Rational(1, 2), sp.Integer(1), sp.Integer(2), sp.Rational(1, 2)
c = lambda ee, t: ee ** 2 / t
prodv = lambda ee, t: t * (1 + muu * ee)
star = lambda t: sp.solve(sp.diff(prodv(e, t) - c(e, t), e), e)[0]
eL, eH = star(tL), star(tH)
assert (eL, eH) == (sp.Rational(1, 4), 1)
uL = (prodv(e, tL) - c(e, tL)).subs(e, eL)
uH = (prodv(e, tH) - c(e, tH)).subs(e, eH)
assert (uL, uH) == (sp.Rational(17, 16), sp.Rational(5, 2))
DH = (prodv(e, tL) - c(e, tH)).subs(e, sp.solve(sp.diff(prodv(e, tL) - c(e, tH), e), e)[0])
assert DH == sp.Rational(9, 8)
# separating: L at eL, H at e in [e1, e2]
ic_L = sp.solve(sp.Eq(prodv(e, tH) - c(e, tL), uL), e)
ic_H = sp.solve(sp.Eq(prodv(e, tH) - c(e, tH), DH), e)
e1 = max(ic_L)
e2 = max(ic_H)
assert sp.simplify(e1 - (2 + sp.sqrt(19)) / 4) == 0 and sp.simplify(e2 - (1 + sp.sqrt(11) / 2)) == 0
assert float(e1) > float(eH)                                 # full-information outcome not sustainable
assert prodv(eH, tH) - c(eH, tL) > uL                        # L would mimic H's efficient level
assert uH >= DH                                              # ... while H's constraint is slack
# pooling at e: wage (lam*tH + (1-lam)*tL)(1+mu e)
tbar = lm * tH + (1 - lm) * tL
pL_ = sp.solve(sp.Eq(prodv(e, tbar) - c(e, tL), uL), e)
pH_ = sp.solve(sp.Eq(prodv(e, tbar) - c(e, tH), DH), e)
assert sp.simplify(max(pL_) - (3 + sp.sqrt(37)) / 8) == 0 and sp.simplify(max(pH_) - (3 + sp.sqrt(21)) / 4) == 0
assert float(max(pL_)) < float(max(pH_))                     # L's constraint binds: pooling for e in [0, 1.135]
assert float(max(pL_)) > 0 and prodv(0, tbar) - c(0, tL) >= uL and prodv(0, tbar) - c(0, tH) >= DH
# a second parameter set in which the full-information outcome IS a separating PBE
tH2 = sp.Integer(4)
eH2 = star(tH2)
assert eH2 == 4
assert prodv(eH2, tH2) - c(eH2, tL) == -4 <= uL              # L does not mimic: IC_L holds at e_H^*
print("mwg-13-c-2: example c=e^2/theta, theta=(1,2), mu=1/2, lambda=1/2: e*=(1/4,1), u*=(17/16,5/2); "
      "separating e_H in [%.4f, %.4f]; pooling e in [0, %.4f]; full information sustainable for "
      "theta_H=4" % (float(e1), float(e2), float(max(pL_))))

# ---------------------------------------------------------------------------- mwg-13-c-4
Lw, thS, ee, wf = sp.symbols("theta_low theta e w", positive=True)
wfun = sp.Function("w")
sol = sp.dsolve(sp.Eq(wfun(ee) * wfun(ee).diff(ee), 2 * ee), wfun(ee))
assert any(sp.simplify(s.rhs ** 2 - (2 * ee ** 2 + sp.Symbol("C1"))) == 0 for s in sol)
W = sp.sqrt(2 * ee ** 2 + Lw ** 2)                           # boundary: w(0) = theta_low
assert sp.simplify(W * sp.diff(W, ee) - 2 * ee) == 0
assert W.subs(ee, 0) == Lw
etheta = sp.sqrt((thS ** 2 - Lw ** 2) / 2)
assert sp.simplify(W.subs(ee, etheta) - thS) == 0            # zero profit: w(e(theta)) = theta
assert sp.simplify(etheta.subs(thS, Lw)) == 0                # lowest type chooses e = 0
assert sp.simplify(sp.diff(W, ee) - 2 * ee / W) == 0 and sp.simplify(sp.diff(W - ee ** 2 / thS, ee).subs(ee, etheta)) == 0
for Lv, tv in [(1, 2), (1, 5), (sp.Rational(1, 2), 3)]:      # global optimality of e(theta)
    ut = lambda x: float((W - x ** 2 / tv).subs({Lw: Lv, ee: x}))
    ev = float(etheta.subs({Lw: Lv, thS: tv}))
    assert all(ut(i / 200) <= ut(ev) + 1e-12 for i in range(0, 2000))
    assert abs(ut(ev) - (float(tv) - ev ** 2 / float(tv))) < 1e-12
# the manual's w = sqrt(2) e is the special case theta_low = 0
assert sp.simplify(W.subs(Lw, 0) - sp.sqrt(2) * ee) == 0
print("mwg-13-c-4: w(e)=sqrt(2e^2+theta_low^2), e(theta)=sqrt((theta^2-theta_low^2)/2); "
      "the manual's w=sqrt2 e is the case theta_low=0")

print("all T3 checks passed")
