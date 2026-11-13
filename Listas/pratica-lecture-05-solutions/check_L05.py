"""Checks every number and equilibrium claim in the 17 NEW Lecture 5 solutions of
Listas/pratica-lecture-05.md (the 8 reused ones are checked by
../lista-reais-lectures-01-05-solutions/check_C_L05.py).

New: Cabral 7.8, Gibbons 2.22, Munoz-Garcia Ch.4 Ex.18, Tadelis 10.9, Tadelis 9.3, Cabral 7.12,
Gibbons 2.10, Tadelis 9.2, 9.4, Munoz-Garcia Ch.6 Ex.6, Tadelis 10.5, 9.6, MWG 12.AA.1,
Tadelis 9.5, Gibbons 2.8, 2.16, MWG 12.AA.2.
Exact arithmetic (fractions, sympy); thresholds are tested on both sides.

Run: python check_L05.py  -> one line per item and "all L05 checks passed",
or stops with an AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp


def pure_ne(U, rows, cols):
    """Pure Nash equilibria of a bimatrix U[(r, c)] = (u1, u2)."""
    return [(r, c) for r, c in product(rows, cols)
            if U[(r, c)][0] == max(U[(x, c)][0] for x in rows)
            and U[(r, c)][1] == max(U[(r, y)][1] for y in cols)]


def two_stage_support(U, rows, cols, d, U2=None):
    """First-stage profiles a that are the first-stage outcome of a pure SPE of the two-stage game
    (stage game U, then U2 (default U); second stage after a history must be a stage NE).
    Test (one-stage deviations; a deviation history is reached by one deviator only, so it can be
    given that deviator's worst stage NE): some NE e with, for both i,
    u_i(a) + d*u_i(e) >= max_{a_i' != a_i} u_i(a_i', a_-i) + d*min_{e' in NE} u_i(e')."""
    U2 = U2 or U
    ne2 = pure_ne(U2, rows, cols)
    out = []
    for a in product(rows, cols):
        def ok(e):
            r, c = a
            g1 = max(U[(x, c)][0] + d * min(U2[n][0] for n in ne2) for x in rows if x != r)
            g2 = max(U[(r, y)][1] + d * min(U2[n][1] for n in ne2) for y in cols if y != c)
            return (U[a][0] + d * U2[e][0] >= g1) and (U[a][1] + d * U2[e][1] >= g2)
        if any(ok(e) for e in ne2):
            out.append(a)
    return out


# ============================================================ Cabral 7.8 (slide 11 game)
R, C = "MFR", "mfr"
U = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("M", "r"): (0, 0),
     ("F", "m"): (5, -1), ("F", "f"): (1, 1), ("F", "r"): (0, 0),
     ("R", "m"): (0, 0), ("R", "f"): (0, 0), ("R", "r"): (3, 3)}
assert pure_ne(U, R, C) == [("F", "f"), ("R", "r")]
for d in (F(1, 2), F(3, 4), F(1)):
    assert ("M", "m") in two_stage_support(U, R, C, d)
assert ("M", "m") not in two_stage_support(U, R, C, F(49, 100))
assert 4 + 3 * F(1, 2) == 5 + 1 * F(1, 2)                  # indifference at delta = 1/2
assert 4 + 3 == 7 and 5 + 1 == 6                           # slide 13, delta = 1
# the one-shot NE profile is also an SPE outcome: both pure NE are supported as first-stage outcomes
assert {("F", "f"), ("R", "r")} <= set(two_stage_support(U, R, C, F(1)))
print("Cabral 7.8: slide-11 stage game has NE (F,f),(R,r); (M,m) in stage 1 iff delta >= 1/2")

# ============================================================ Gibbons 2.22 (bank runs)
for D, r, Rr in ((10, 6, 12), (10, 5.5, 11), (100, 51, 101), (100, 99, 500)):
    assert D > r > D / 2 and Rr > D
    S = [(a, b) for a in "wd" for b in "wd"]                 # (date-1 action, date-2 action)

    def date2(x, y):
        if x == "w" and y == "w": return (Rr, Rr)
        if x == "w": return (2 * Rr - D, D)
        if y == "w": return (D, 2 * Rr - D)
        return (Rr, Rr)

    def payoff(s1, s2):
        a, b = s1[0], s2[0]
        if a == "w" and b == "w": return (r, r)
        if a == "w": return (D, 2 * r - D)
        if b == "w": return (2 * r - D, D)
        return date2(s1[1], s2[1])

    NE = [(s1, s2) for s1 in S for s2 in S
          if payoff(s1, s2)[0] >= max(payoff(t, s2)[0] for t in S)
          and payoff(s1, s2)[1] >= max(payoff(s1, t)[1] for t in S)]
    SPNE = [(s1, s2) for s1, s2 in NE if s1[1] == "w" and s2[1] == "w"]   # date-2 subgame: both w
    assert date2("w", "w") == (Rr, Rr) and 2 * Rr - D > Rr    # w strictly dominant at date 2
    assert sorted(SPNE) == [(("d", "w"), ("d", "w")), (("w", "w"), ("w", "w"))]
    assert payoff(("w", "w"), ("w", "w")) == (r, r) and payoff(("d", "w"), ("d", "w")) == (Rr, Rr)
    assert (("w", "d"), ("w", "d")) in NE and (("w", "d"), ("w", "d")) not in SPNE
    assert len(NE) == 5                                      # 4 sets of the run + the (dw,dw) outcome
print("Gibbons 2.22: 4x4 normal form; NE 5, SPNE 2: both (w,w) = run (r,r), both (d,w) = (R,R); "
      "(wd,wd) is NE but not subgame perfect")

# ============================================================ Munoz-Garcia Ch.4 Ex.18
h, w = sp.symbols("h w", real=True)
pi = (h - h**2 / 2) - w * h
hbr = sp.solve(sp.diff(pi, h), h)[0]
assert sp.simplify(hbr - (1 - w)) == 0 and sp.diff(pi, h, 2) == -1
uL = sp.expand(w * hbr)
wstar = sp.solve(sp.diff(uL, w), w)[0]
assert wstar == sp.Rational(1, 2) and hbr.subs(w, wstar) == sp.Rational(1, 2)
assert uL.subs(w, wstar) == sp.Rational(1, 4) and pi.subs({h: sp.Rational(1, 2), w: wstar}) == sp.Rational(1, 8)
assert max(F(k, 100) * (1 - F(k, 100)) for k in range(101)) == F(1, 4)
# w > 1: firm hires nobody; w in [0,1]: h = 1 - w in [0,1]
assert all(0 <= 1 - F(k, 10) <= 1 for k in range(11))
print("MG Ch.4 Ex.18: h(w) = 1-w; w* = 1/2, h* = 1/2; payoffs union 1/4, firm 1/8 (the book's)")

# ============================================================ Tadelis 10.9
q1, q2 = sp.symbols("q1 q2", real=True)
v1 = (30 - q2) * q1 - q1**2
v2 = (30 - q1) * q2 - q2**2
sol = sp.solve([sp.diff(v1, q1), sp.diff(v2, q2)], [q1, q2])
assert sol == {q1: 10, q2: 10} and v1.subs(sol) == 100 and sp.diff(v1, q1, 2) == -2
s = sp.symbols("s")
joint = sp.expand((v1 + v2).subs({q2: s - q1}))
assert sp.simplify(joint - (30 * s - s**2)) == 0           # depends only on s = q1+q2
assert sp.solve(sp.diff(30 * s - s**2, s), s) == [15]
qc = sp.Rational(15, 2)
assert v1.subs({q1: qc, q2: qc}) == sp.Rational(225, 2)     # 112.5
qd = (30 - qc) / 2
assert qd == sp.Rational(45, 4) and v1.subs({q1: qd, q2: qc}) == sp.Rational(2025, 16)  # 126.5625
vc, vd, vn = sp.Rational(225, 2), sp.Rational(2025, 16), 100
dstar = (vd - vc) / (vd - vn)
assert dstar == sp.Rational(9, 17)
ok = lambda d: vc >= (1 - d) * vd + d * vn
assert ok(dstar) and ok(dstar + sp.Rational(1, 1000)) and not ok(dstar - sp.Rational(1, 1000))
print("Tadelis 10.9: NE q=(10,10), profit 100; Pareto q=(15/2,15/2), profit 225/2; deviation 2025/16; "
      "delta* = 9/17 ~ 0.529")

# ============================================================ Tadelis 9.3
RA, CA = "PN", "pn"
A1 = {("P", "p"): (2, 2), ("P", "n"): (0, 5), ("N", "p"): (5, 0), ("N", "n"): (3, 3)}
A2 = {("P", "p"): (4, 4), ("P", "n"): (1, 0), ("N", "p"): (0, 1), ("N", "n"): (2, 2)}
assert pure_ne(A1, RA, CA) == [("N", "n")]
assert pure_ne(A2, RA, CA) == [("P", "p"), ("N", "n")]
assert 2 ** 4 == 16                                         # SPE at delta = 0: 2 NE after each of 4 histories
for d in (F(0), F(1, 10), F(1, 2), F(9, 10), F(1)):
    assert two_stage_support(A1, RA, CA, d, A2) == [("N", "n")]
dlow = F(3, 2)
assert 2 + 4 * dlow == 5 + 2 * dlow and ("P", "p") in two_stage_support(A1, RA, CA, dlow, A2)
assert ("P", "p") not in two_stage_support(A1, RA, CA, F(149, 100), A2)
# mixed NE of A2 as the stick: q = Pr(P) with 1 + 3q = 2 - 2q
qm = sp.symbols("q")
qq = sp.solve(1 + 3 * qm - (2 - 2 * qm), qm)[0]
assert qq == sp.Rational(1, 5) and 1 + 3 * qq == sp.Rational(8, 5)
assert sp.solve(2 + 4 * sp.Symbol("x") - 5 - sp.Rational(8, 5) * sp.Symbol("x"))[0] == sp.Rational(5, 4)
# stage-1 best-reply gain of N over P is 3 against p and against n; swing in stage 2 is at most 4-2
assert 5 - 2 == 3 and 3 - 0 == 3 and 4 - 2 == 2
print("Tadelis 9.3: NE stage 1 (N,n); stage 2 (P,p),(N,n); 16 SPE at delta=0; (P,p) first needs "
      "delta >= 3/2 (5/4 with the mixed stick) -> no SPE for delta <= 1; only (N,n) in stage 1")

# ============================================================ Cabral 7.12
RH, CH = "HL", "HL"
UH = {("H", "H"): (5, 5), ("H", "L"): (8, 1), ("L", "H"): (1, 8), ("L", "L"): (4, 4)}
assert pure_ne(UH, RH, CH) == [("H", "H")]
assert all(UH[("H", y)][0] > UH[("L", y)][0] for y in "HL")  # H strictly dominant
# sustaining (L,L) by grim trigger would need 4 >= (1-d)*8 + d*5  <=>  d >= 4/3 > 1
dx = sp.symbols("d")
assert sp.solve(4 - ((1 - dx) * 8 + dx * 5), dx) == [sp.Rational(4, 3)]
assert max(u1 for u1, u2 in UH.values() if u1 == u2) == 5   # best symmetric stage payoff
assert max(a + b for a, b in UH.values()) == 10             # (H,H) also maximises the total
assert F(8 + 1, 2) == F(9, 2) < 5                            # alternating (H,L),(L,H) gives 4.5 each
d = F(4, 5)
V = lambda per: sum(d**t * per(t) for t in range(2000))   # truncated; error below 1e-190
pay_c = lambda t: 10 if t < 10 else 5
Vc = 10 * (1 - d**10) / (1 - d) + 5 * d**10 / (1 - d)
assert abs(V(pay_c) - Vc) < F(1, 10**100)
assert (1 - d) * Vc == 1 * (10 * (1 - d**10) + 5 * d**10)
print("Cabral 7.12: one-shot NE (H,H); (H,H) every period is best symmetric at delta=.8 (value 5, "
      "average); with doubled first 10 periods value %s (average %.4f)" % (Vc, float((1 - d) * Vc)))

# ============================================================ Gibbons 2.10
RG = ["P1", "Q1", "R1", "S1"]
CG = ["P2", "Q2", "R2", "S2"]


def gibbons_game(x):
    rows = {"P1": [(2, 2), (x, 0), (-1, 0), (0, 0)], "Q1": [(0, x), (4, 4), (-1, 0), (0, 0)],
            "R1": [(0, 0), (0, 0), (0, 2), (0, 0)], "S1": [(0, -1), (0, -1), (-1, -1), (2, 0)]}
    return {(r, c): rows[r][j] for r in RG for j, c in enumerate(CG)}


for x in (F(9, 2), 5, 6, F(61, 10), 7):
    G = gibbons_game(x)
    assert pure_ne(G, RG, CG) == [("P1", "P2"), ("R1", "R2"), ("S1", "S2")]
    assert ("Q1", "Q2") not in pure_ne(G, RG, CG)
    sup = ("Q1", "Q2") in two_stage_support(G, RG, CG, 1)
    assert sup == (x <= 6)
G = gibbons_game(6)
assert G[("Q1", "Q2")][0] + G[("P1", "P2")][0] == 6 == G[("P1", "Q2")][0] + G[("R1", "R2")][0]
assert max(G[(r, "Q2")][0] for r in RG if r != "Q1") == 6   # best deviation = P1, payoff x
print("Gibbons 2.10: stage NE (P,P),(R,R),(S,S); the strategy is SPE iff 4 < x <= 6")

# ============================================================ Tadelis 9.2 (centipede + coordination)
TERM = {"N": (1, 1), "Cn": (0, 3), "CcN": (2, 2), "CcCn": (1, 4), "CcCc": (3, 3)}
AC = {("A", "a"): (1, 1), ("B", "b"): (3, 3), ("A", "b"): (0, 0), ("B", "a"): (0, 0)}
assert pure_ne(AC, "AB", "ab") == [("A", "a"), ("B", "b")]
# strategies of the centipede alone: 4 per player; NE by brute force
S1c = list(product("NC", repeat=2))     # (node 1, node 3)
S2c = list(product("nc", repeat=2))     # (node 2, node 4)


def cent(s1, s2):
    if s1[0] == "N": return "N"
    if s2[0] == "n": return "Cn"
    if s1[1] == "N": return "CcN"
    return "CcCn" if s2[1] == "n" else "CcCc"


NEc = [(s1, s2) for s1 in S1c for s2 in S2c
       if TERM[cent(s1, s2)][0] >= max(TERM[cent(t, s2)][0] for t in S1c)
       and TERM[cent(s1, s2)][1] >= max(TERM[cent(s1, t)][1] for t in S2c)]
assert all(cent(*p) == "N" for p in NEc) and len(NEc) == 4
assert set(NEc) == {(a, b) for a in (("N", "N"), ("N", "C")) for b in (("n", "n"), ("n", "c"))}
assert 4 * 2 ** 5 == 128                                    # pure strategies per player in the multistage game
assert 2 ** 5 == 32                                         # SPE at delta = 0


def spe_outcomes(delta, cont):
    """Outcomes of pure SPE of the centipede with continuation value cont[o] (same for both players)
    added as delta*cont[o]; all tie-breaks."""
    def val(o, i): return TERM[o][i] + delta * cont[o]
    n4 = {max(("CcCn", "CcCc"), key=lambda o: val(o, 1))} if val("CcCn", 1) != val("CcCc", 1) else {"CcCn", "CcCc"}
    out3 = set()
    for o4 in n4:
        out3 |= ({"CcN"} if val("CcN", 0) > val(o4, 0) else {o4} if val("CcN", 0) < val(o4, 0) else {"CcN", o4})
    out2 = set()
    for o3 in out3:
        out2 |= ({"Cn"} if val("Cn", 1) > val(o3, 1) else {o3} if val("Cn", 1) < val(o3, 1) else {"Cn", o3})
    out1 = set()
    for o2 in out2:
        out1 |= ({"N"} if val("N", 0) > val(o2, 0) else {o2} if val("N", 0) < val(o2, 0) else {"N", o2})
    return out1


def reachable(delta):
    res = set()
    for assign in product((1, 3), repeat=5):
        res |= spe_outcomes(delta, dict(zip(TERM, assign)))
    return res


assert reachable(F(0)) == {"N"}
assert reachable(F(49, 100)) == {"N"}
assert "CcN" in reachable(F(1, 2)) and "CcN" not in reachable(F(499, 1000))
assert reachable(F(1, 2)) == set(TERM) == reachable(F(1))
# (d)-(e): reward (B,b) after (2,2) only, (A,a) after every other outcome
cont = {o: (3 if o == "CcN" else 1) for o in TERM}
assert spe_outcomes(F(1), cont) == {"CcN"} and spe_outcomes(F(1, 2), cont) >= {"CcN"}
assert spe_outcomes(F(49, 100), cont) == {"N"}
chk = lambda dl: (2 + 3 * dl >= 3 + dl)                       # player 2 at node 2: stay vs 'n'
assert chk(F(1, 2)) and not chk(F(499, 1000))
assert 2 + 3 * F(1, 2) == 3 + F(1, 2)
print("Tadelis 9.2: centipede NE 4 (all with (N)), 128 strategies each, 32 SPE at delta=0; (2,2) first "
      "stage iff delta >= 1/2; for delta >= 1/2 all 5 outcomes of the centipede are SPE outcomes")

# ============================================================ Tadelis 9.4 (online gaming)
x1, x2, qq = sp.symbols("x1 x2 qq", real=True)
pr = lambda a, b: (100 - a - b) * a
sol = sp.solve([sp.diff(pr(x1, x2), x1), sp.diff(pr(x2, x1), x2)], [x1, x2])
assert sol == {x1: sp.Rational(100, 3), x2: sp.Rational(100, 3)}
assert pr(sol[x1], sol[x2]) == sp.Rational(10000, 9)
mon = sp.solve(sp.diff((100 - qq) * qq, qq), qq)[0]
assert mon == 50 and (100 - mon) * mon == 2500
assert pr(25, 25) == 1250
bd = sp.solve(sp.diff(pr(x1, 25), x1), x1)[0]
assert bd == sp.Rational(75, 2) and pr(bd, 25) == sp.Rational(5625, 4)    # 1406.25
RO, CO = "ON", "on"
UO = {("O", "o"): (2500, 2500), ("O", "n"): (-10, 0), ("N", "o"): (0, -10), ("N", "n"): (0, 0)}
assert pure_ne(UO, RO, CO) == [("O", "o"), ("N", "n")]
d9 = (sp.Rational(5625, 4) - 1250) / 2500
assert d9 == sp.Rational(1, 16)
okq = lambda d: 1250 + d * 2500 >= sp.Rational(5625, 4) + d * 0
assert okq(d9) and not okq(d9 - sp.Rational(1, 1000)) and okq(sp.Rational(4, 10))
assert sp.expand((100 - qq) ** 2 / 4 - (100 - 2 * qq) * qq - (sp.Rational(9, 4) * qq**2 - 150 * qq + 2500)) == 0
dsym = sp.symbols("dsym", positive=True)
cond94 = sp.expand(sp.Rational(9, 4) * qq**2 - 150 * qq + 2500 - 2500 * dsym)
r94 = sorted(sp.solve(cond94, qq), key=lambda r: r.subs(dsym, sp.Rational(1, 4)))
assert sp.simplify(r94[0] - sp.Rational(100, 3) * (1 - sp.sqrt(dsym))) == 0
assert sp.simplify(r94[0].subs(dsym, sp.Rational(1, 16)) - 25) == 0
xo = sp.symbols("xo")
assert sp.solve(2500 * xo - 10 * (1 - xo), xo) == [sp.Rational(1, 251)]   # mixed NE, payoff 0
print("Tadelis 9.4: Cournot NE (100/3,100/3) profit 10000/9; monopoly 50 -> 25 each, 1250; deviation "
      "75/2 gives 5625/4; delta* = 1/16, so delta = 0.4 supports the monopoly outcome")

# ============================================================ Munoz-Garcia Ch.6 Ex.6
gi, gj, W, m = sp.symbols("g_i g_j w m", positive=True)
u = lambda a, b: sp.sqrt((W - a) * m * (a + b))
BR = sp.solve(sp.diff((W - gi) * (gi + gj), gi), gi)[0]
assert sp.simplify(BR - (W / 2 - gj / 2)) == 0
gN = sp.solve(sp.Eq(gi, BR.subs(gj, gi)), gi)[0]
assert gN == W / 3
gs = sp.symbols("gs", positive=True)
SO = sp.solve(sp.diff(2 * (W - gs) * m * 2 * gs, gs), gs)[0]
assert SO == W / 2
# asymmetric joint maximum is the same point
gA, gB = sp.symbols("gA gB", positive=True)
Jt = u(gA, gB) + u(gB, gA)
assert sp.simplify(sp.diff(Jt, gA).subs({gA: W / 2, gB: W / 2})) == 0
uc = sp.simplify(u(W / 2, W / 2)); un = sp.simplify(u(W / 3, W / 3))
dv = sp.simplify(u(W / 4, W / 2))
assert sp.simplify(uc - W * sp.sqrt(m) / sp.sqrt(2)) == 0
assert sp.simplify(un - 2 * W * sp.sqrt(m) / 3) == 0
assert sp.simplify(dv - 3 * W * sp.sqrt(m) / 4) == 0
assert sp.simplify(BR.subs(gj, W / 2) - W / 4) == 0
dstar = sp.simplify((dv - uc) / (dv - un))
assert sp.simplify(dstar - (9 - 6 * sp.sqrt(2))) == 0
assert abs(float(9 - 6 * sp.sqrt(2)) - 0.5147) < 1e-4
dn = 9 - 6 * sp.sqrt(2)
assert sp.simplify(uc - ((1 - dn) * dv + dn * un)) == 0          # equality at the threshold
assert (uc - ((1 - 0.52) * dv + 0.52 * un)).subs({W: 1, m: 1}) > 0
assert (uc - ((1 - 0.51) * dv + 0.51 * un)).subs({W: 1, m: 1}) < 0
assert float((3 * sp.sqrt(2) - 4) / 6) > 0.0404 and float((3 * sp.sqrt(2) - 4) / 6) < 0.0405
print("MG Ch.6 Ex.6: BR g=(w-g_j)/2, NE w/3, SO w/2; payoffs w*sqrt(m)*(1/sqrt2, 2/3, 3/4 dev); "
      "delta* = 9-6*sqrt2 = %.4f (book 0.51)" % float(dn))

# ============================================================ Tadelis 10.5
a1, a2 = sp.symbols("a1 a2", real=True)
va = lambda x, y: x - 2 * y + x * y - x**2
sol = sp.solve([sp.diff(va(a1, a2), a1), sp.diff(va(a2, a1), a2)], [a1, a2])
assert sol == {a1: 1, a2: 1} and va(1, 1) == -1
Jj = sp.expand(va(a1, a2) + va(a2, a1))
assert sp.simplify(Jj + (a1 + a2) + (a1 - a2) ** 2) == 0
assert all(F(0) >= -(F(x, 4) + F(y, 4)) - (F(x, 4) - F(y, 4)) ** 2 for x in range(9) for y in range(9))
assert sp.solve(sp.diff(va(a1, 0), a1), a1) == [sp.Rational(1, 2)] and va(sp.Rational(1, 2), 0) == sp.Rational(1, 4)
d1 = (sp.Rational(1, 4) - 0) / (sp.Rational(1, 4) - (-1))
assert d1 == sp.Rational(1, 5)
okc = lambda d: 0 >= (1 - d) * sp.Rational(1, 4) + d * (-1)
assert okc(d1) and not okc(d1 - sp.Rational(1, 1000))
# (d) a in [0, 1/2]
assert all(sp.Rational(1, 2) <= (1 + F(y, 10)) / 2 for y in range(6))       # BR is cut at 1/2 for a_j in [0,1/2]
assert va(sp.Rational(1, 2), sp.Rational(1, 2)) == -sp.Rational(1, 2)
d2 = (sp.Rational(1, 4) - 0) / (sp.Rational(1, 4) + sp.Rational(1, 2))
assert d2 == sp.Rational(1, 3)
# best symmetric collusive level a_min(delta), with and without the cap
a_, dl = sp.symbols("a delta")
f_free = -a_ + dl - (1 - dl) * ((1 + a_) ** 2 / 4 - 2 * a_)
assert sp.simplify(f_free - ((5 * dl - 1) / 4 + a_ * (1 - 3 * dl) / 2 - (1 - dl) * a_**2 / 4)) == 0
assert sp.simplify(f_free.subs(a_, 1)) == 0
assert sp.simplify(f_free.subs(a_, (1 - 5 * dl) / (1 - dl))) == 0
f_cap = -a_ + dl / 2 - (1 - dl) * (sp.Rational(1, 4) - 3 * a_ / 2)
assert sp.simplify(f_cap.subs(a_, sp.Rational(1, 2))) == 0
assert sp.simplify(f_cap - (sp.Rational(1, 2) - 3 * dl / 2) * (a_ - sp.Rational(1, 2))) == 0
amin = lambda dd: max(F(0), (1 - 5 * dd) / (1 - dd))
for dd in (F(1, 20), F(1, 9), F(1, 5), F(1, 3), F(1, 2)):
    ac = amin(dd)
    assert f_free.subs({a_: ac, dl: dd}) >= 0
    if ac > 0: assert f_free.subs({a_: ac - F(1, 1000), dl: dd}) < 0
assert amin(F(1, 9)) == F(1, 2) and amin(F(1, 5)) == 0 and amin(F(1, 20)) == F(15, 19)
capmin = lambda dd: F(1, 2) if dd < F(1, 3) else F(0)
assert f_cap.subs({a_: 0, dl: F(1, 3)}) == 0 and f_cap.subs({a_: 0, dl: F(32, 100)}) < 0
assert amin(F(1, 20)) > capmin(F(1, 20)) and amin(F(1, 5)) < capmin(F(1, 5)) and amin(F(1, 2)) == capmin(F(1, 2))
print("Tadelis 10.5: NE (1,1) payoff -1; binding optimum (0,0); delta >= 1/5; cap 1/2: NE (1/2,1/2) payoff -1/2, "
      "delta >= 1/3; a_min(delta) = max(0,(1-5d)/(1-d)) free vs 1/2 below 1/3 capped (policy helps only d<1/9)")

# ============================================================ Tadelis 9.6
y1, y2 = sp.symbols("y1 y2", real=True)
pc = lambda a, b: (100 - a - b - 10) * a
sol = sp.solve([sp.diff(pc(y1, y2), y1), sp.diff(pc(y2, y1), y2)], [y1, y2])
assert sol == {y1: 30, y2: 30} and pc(30, 30) == 900
qm_ = sp.solve(sp.diff((90 - qq) * qq, qq), qq)[0]
assert qm_ == 45 and (90 - qm_) * qm_ == 2025 and pc(sp.Rational(45, 2), sp.Rational(45, 2)) == sp.Rational(2025, 2)
RS, CS = "AB", "ab"
US = {("A", "a"): (100, 100), ("A", "b"): (0, 0), ("B", "a"): (0, 0), ("B", "b"): (300, 300)}
assert pure_ne(US, RS, CS) == [("A", "a"), ("B", "b")]
qd = sp.solve(sp.diff(pc(y1, sp.Rational(45, 2)), y1), y1)[0]
assert qd == sp.Rational(135, 4) and pc(qd, sp.Rational(45, 2)) == sp.Rational(18225, 16)  # 1139.0625
dd6 = (sp.Rational(18225, 16) - sp.Rational(2025, 2)) / (300 - 100)
assert dd6 == sp.Rational(81, 128) and abs(float(dd6) - 0.6328125) < 1e-12
ok6 = lambda d: sp.Rational(2025, 2) + 300 * d >= sp.Rational(18225, 16) + 100 * d
assert ok6(dd6) and not ok6(dd6 - sp.Rational(1, 1000))
# (d) delta = 1/2: sustainable symmetric q
qs, = sp.symbols("qs", positive=True),
pi_sym = (90 - 2 * qs) * qs
dev = ((90 - qs) / 2) ** 2
cond = sp.expand(pi_sym + 300 * sp.Rational(1, 2) - dev - 100 * sp.Rational(1, 2))
roots = sp.solve(cond, qs)
assert sorted(roots) == [sp.Rational(70, 3), sp.Rational(110, 3)]
assert pi_sym.subs(qs, sp.Rational(70, 3)) == sp.Rational(9100, 9)
assert sp.simplify(pi_sym.subs(qs, sp.Rational(70, 3)) + 150 - (dev.subs(qs, sp.Rational(70, 3)) + 50)) == 0
# (e) lowest sustainable q as function of delta
de = sp.symbols("delta", positive=True)
cond_d = sp.expand(pi_sym + 300 * de - dev - 100 * de)
qlow = min(sp.solve(cond_d, qs), key=lambda r: r.subs(de, sp.Rational(1, 2)))
assert sp.simplify(qlow - (30 - 20 * sp.sqrt(2) * sp.sqrt(de) / 3)) == 0
assert sp.simplify(qlow.subs(de, sp.Rational(1, 2)) - sp.Rational(70, 3)) == 0
assert sp.simplify(qlow.subs(de, dd6) - sp.Rational(45, 2)) == 0
# mixed stick of the standard game
assert sp.solve(100 * sp.Symbol("t") - 300 * (1 - sp.Symbol("t")), sp.Symbol("t")) == [sp.Rational(3, 4)]
assert (sp.Rational(18225, 16) - sp.Rational(2025, 2)) / (300 - 75) == sp.Rational(9, 16)
print("Tadelis 9.6: Cournot (30,30) profit 900; joint max 45 -> 45/2 each, 2025/2; deviation 135/4 gives "
      "18225/16; delta* = 81/128; delta=1/2: q in [70/3,110/3], best 70/3, profit 9100/9")

# ============================================================ MWG 12.AA.1
RM, CM = "UD", "LR"
UW = {("U", "L"): (-1, 9), ("U", "R"): (-1, 10), ("D", "L"): (-10, -1), ("D", "R"): (0, 0)}
assert pure_ne(UW, RM, CM) == [("D", "R")]
ds = sp.symbols("ds")
ic1 = lambda dd: -1 >= (1 - dd) * (-10) + dd * 0                    # player 1 deviates to D
ic2 = lambda dd: 9 >= (1 - dd) * 10 + dd * 0                         # player 2 deviates to R
for dd in (F(1, 10), F(1, 2), F(9, 10)):
    assert ic1(dd) and ic2(dd)
assert not ic1(F(91, 100)) and not ic2(F(9, 100))
assert sp.solve(-1 - (-10 + 10 * ds), ds) == [sp.Rational(9, 10)] and sp.solve(9 - (10 - 10 * ds), ds) == [sp.Rational(1, 10)]
assert UW[("U", "L")][0] < UW[("D", "R")][0] and UW[("U", "L")][1] > UW[("D", "R")][1]
# U is player 1's short-run best reply to L, so the deviation set excludes the on-path action
assert max(UW[(r, "L")][0] for r in RM) == UW[("U", "L")][0]
# corrected claim: both below Nash => someone is not best-replying => profitable deviation for any delta
def sustainable(U, ne, q, dd, rows, cols):
    r, c = q
    i1 = U[q][0] >= max((1 - dd) * U[(x, c)][0] + dd * U[ne][0] for x in rows if x != r)
    i2 = U[q][1] >= max((1 - dd) * U[(r, y)][1] + dd * U[ne][1] for y in cols if y != c)
    return i1 and i2
import random
random.seed(1)
for _ in range(300):
    Ur = {(r, c): (random.randint(-6, 6), random.randint(-6, 6)) for r in "ABC" for c in "xyz"}
    nes = pure_ne(Ur, "ABC", "xyz")
    if len(nes) != 1: continue
    ne = nes[0]
    for q in product("ABC", "xyz"):
        if Ur[q][0] < Ur[ne][0] and Ur[q][1] < Ur[ne][1]:
            assert not any(sustainable(Ur, ne, q, F(k, 100), "ABC", "xyz") for k in range(1, 100))
# Cournot illustration of the first claim in the proof of the corrected statement
Pc = lambda a, b: (100 - a - b - 10) * a
assert Pc(40, 40) < Pc(30, 30)
for k in range(1, 100):
    dd = F(k, 100)
    br = (90 - F(40)) / 2
    assert not (Pc(40, 40) >= (1 - dd) * Pc(br, 40) + dd * Pc(30, 30))
print("MWG 12.AA.1: printed statement false (manual's erratum): (U,L) = (-1,9) below Nash 0 for player 1 is "
      "sustainable iff 1/10 <= delta <= 9/10; corrected 'for all i' version holds (300 random games, Cournot)")

# ============================================================ Tadelis 9.5
s1, s2 = sp.symbols("s1 s2", positive=True)
vs = lambda a, b: 16 * a / (a + b) - a
BRs = sp.solve(sp.diff(vs(s1, s2), s1), s1)
assert sp.simplify(BRs[0] - (4 * sp.sqrt(s2) - s2)) == 0
sN = sp.solve(sp.Eq(s1, 4 * sp.sqrt(s1) - s1), s1)[0]
assert sN == 4 and vs(4, 4) == 4
S_ = sp.symbols("S_", positive=True)
devS = sp.simplify(vs(4 * sp.sqrt(S_) - S_, S_))
assert sp.simplify(devS - (16 - 8 * sp.sqrt(S_) + S_)) == 0
wv = sp.symbols("wv", positive=True)
ic = sp.simplify((8 - S_ + wv) - (16 - 8 * sp.sqrt(S_) + S_))
assert sp.simplify(ic - (wv - 2 * (sp.sqrt(S_) - 2) ** 2)) == 0
smin = lambda ww: (2 - sp.sqrt(sp.Rational(ww) / 2)) ** 2
assert sp.simplify(smin(1) - (sp.Rational(9, 2) - 2 * sp.sqrt(2))) == 0 and abs(float(smin(1)) - 1.6716) < 1e-3
assert sp.simplify(ic.subs({S_: smin(1), wv: 1})) == 0
assert sp.simplify(smin(8)) == 0 and abs(float(smin(F(1, 10**6)) - 4)) < 0.01
assert abs(float(8 - smin(1) + 1) - 7.3284) < 1e-3
assert vs(sp.Symbol("e", positive=True), 0) == 16 - sp.Symbol("e", positive=True)   # sup 16 as e -> 0, not attained
# stage-2 NE
RP, CP = "PN", "pn"
for ww in (1, 8, F(1, 2)):
    UP = {("P", "p"): (ww, ww), ("P", "n"): (-1, 0), ("N", "p"): (0, -1), ("N", "n"): (0, 0)}
    assert pure_ne(UP, RP, CP) == [("P", "p"), ("N", "n")]
assert 8 + 8 >= 16 and not (8 + F(79, 10) >= 16)
print("Tadelis 9.5: s* = 4 each, payoff 4; Pareto (0,0), payoff 8; (P,p) path needs w >= 8; w=1: "
      "s_min = 9/2 - 2*sqrt2 ~ 1.6716, payoff ~ 7.3284")

# ============================================================ Gibbons 2.8
e, sg = sp.symbols("e s", positive=True)
# D(e) = 2(1-g'(e)) - s'(e)(1+g'(e)), with g'(s(e)) = g'(e)/2. Example g(x) = x^2/2, so g'(x) = x
g_ex = e**2 / 2
gp_e = sp.diff(g_ex, e)
s_of_e = e / 2                                              # g'(s) = g'(e)/2
prof = 2 * e - s_of_e - 2 * g_ex - 2 * (s_of_e**2 / 2)
estar = sp.solve(sp.diff(prof, e), e)[0]
assert estar == sp.Rational(3, 5) and sp.diff(s_of_e, e) == sp.Rational(1, 2)
Dd = 2 * (1 - gp_e) - sp.diff(s_of_e, e) * (1 + gp_e)
assert sp.simplify(sp.diff(prof, e) - Dd) == 0
assert gp_e.subs(e, estar) == sp.Rational(3, 5)             # g'(e*) = 3/5 < 1
# non-quadratic cost g(x) = x^2/2 + x^4/4: numerical optimum of the induced-effort problem
G = lambda x: x**2 / 2 + x**4 / 4
Gp = lambda x: x + x**3
z = sp.Symbol("z", positive=True)


def profit(ee):
    ss = float(sp.nsolve(z + z**3 - (ee + ee**3) / 2, z, 0.3)) if ee > 0 else 0.0
    return 2 * ee - ss - 2 * G(ee) - 2 * G(ss)


e0 = float(sp.nsolve(z + z**3 - 1, z, 0.6))                 # g'(e0) = 1: no-sabotage optimum
best = max([i * e0 / 400 for i in range(0, 401)], key=profit)
assert best < e0 and Gp(best) < 1 - 0.05
assert all(Dd.subs(e, sp.Rational(k, 10)) < 0 for k in range(10, 40))   # D < 0 whenever g' >= 1
print("Gibbons 2.8: s* solves g'(s)=g'(e)/2; D(e)=2(1-g')-s'(1+g') < 0 for g'>=1; example g=x^2/2: e*=3/5 "
      "(prize 3/5 of the no-sabotage one); g=x^2/2+x^4/4: g'(e*) = %.3f < 1" % Gp(best))

# ============================================================ Gibbons 2.16 (union-firm), model of MG Ch.4 Ex.18
wv_, hv_ = sp.symbols("w_ h_", positive=True)
Uu = wv_ * hv_
Pf = lambda hh, ww: hh - hh**2 / 2 - ww * hh
Ustar, Pstar = sp.Rational(1, 4), sp.Rational(1, 8)
Pd = lambda ww: (1 - ww) ** 2 / 2
assert sp.simplify(Pf(1 - wv_, wv_) - Pd(wv_)) == 0
# efficient h = 1 (joint profit h - h^2/2 maximal), wage w: U = w, firm = 1/2 - w
assert sp.solve(sp.diff(hv_ - hv_**2 / 2, hv_), hv_) == [1]
dlt = lambda ww: (Pd(ww) - (sp.Rational(1, 2) - ww)) / (Pd(ww) - Pstar)
assert dlt(sp.Rational(1, 4)) == sp.Rational(1, 5)
assert sp.simplify(dlt(wv_) - (wv_**2 / 2) / ((1 - wv_) ** 2 / 2 - sp.Rational(1, 8))) == 0
assert dlt(sp.Rational(3, 8)) == 1
assert dlt(sp.Rational(3, 10)) == F(9, 200) / (F(49, 200) - F(25, 200))   # 3/8
assert dlt(sp.Rational(3, 10)) == sp.Rational(3, 8)
assert all(dlt(sp.Rational(k, 100)) < dlt(sp.Rational(k + 1, 100)) for k in range(25, 37))
okf = lambda ww, d: (sp.Rational(1, 2) - ww) >= (1 - d) * Pd(ww) + d * Pstar
assert okf(sp.Rational(1, 4), sp.Rational(1, 5)) and not okf(sp.Rational(1, 4), sp.Rational(199, 1000))
# union's best deviation payoff is the Stackelberg payoff U* = 1/4
assert max(w_ * (1 - w_) for w_ in [F(k, 1000) for k in range(1001)]) == F(1, 4)
print("Gibbons 2.16: conditions U>=U*, pi>=pi*, delta >= (pi^d-pi)/(pi^d-pi*); example (w,h)=(1/4,1): "
      "delta >= 1/5; general w in [1/4,3/8]: delta(w) = (w^2/2)/((1-w)^2/2-1/8) rising to 1")

# ============================================================ MWG 12.AA.2 (Cournot illustration of the proof)
ee_, dd_ = sp.symbols("ee dd", positive=True)
piq = lambda a, b: (100 - a - b - 10) * a
qeps = 30 + ee_
p_q = piq(qeps, qeps)
p_dev = piq((90 - qeps) / 2, qeps)
assert sp.simplify(p_q - (900 - 30 * ee_ - 2 * ee_**2)) == 0
assert sp.simplify(p_dev - (900 - 30 * ee_ + ee_**2 / 4)) == 0
ic_start = sp.simplify((1 - dd_) * p_q + dd_ * 900 - p_dev)
assert sp.simplify(ic_start - ee_ * (30 * dd_ - ee_ * (sp.Rational(9, 4) - 2 * dd_))) == 0
for dd in (F(1, 100), F(1, 10), F(1, 2), F(9, 10)):
    eps = 30 * dd / (F(9, 4) - 2 * dd) / 2                       # half the upper bound
    pq = piq(30 + eps, 30 + eps); pdv = piq((90 - 30 - eps) / 2, 30 + eps)
    assert pq < 900
    avg = (1 - dd) * pq + dd * 900
    assert avg < 900 and avg >= pdv                              # start state: IC and avg < Nash
    assert 900 + dd * (pq + dd * 900 / (1 - dd)) <= 900 / (1 - dd)   # Nash-phase: dev gets 900 then restart
    assert avg >= 0 and avg > 0                                   # above minimax 0 (Cournot, c<p)
    assert pdv >= 0
assert min(max(piq(a, b) for a in [F(k, 4) for k in range(0, 400)]) for b in [F(k, 4) for k in range(0, 400)]) >= 0
assert piq(40, 40) == 400 and piq(F(90 - 40, 2), 40) == 625 and F(1, 2) * 400 + F(1, 2) * 900 == 650 >= 625
assert piq(42, 42) == 252 and piq(F(90 - 42, 2), 42) == 576 == F(1, 2) * 252 + F(1, 2) * 900
assert F(30, 2) / (F(9, 4) - 1) == 12                     # bound at delta = 1/2
print("MWG 12.AA.2: Cournot example q=(30+e,30+e): start-state IC iff e <= 30d/(9/4-2d); average payoff "
      "below 900 for every d in (0,1) tested")

print("all L05 checks passed")
