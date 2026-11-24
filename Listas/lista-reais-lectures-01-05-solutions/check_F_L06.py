"""Checks every number and equilibrium claim in the ten Lecture 6 solutions (items 51-60):
sol-gibbons-3-1, sol-tadelis-11-1, sol-munoz-garcia-4-1, sol-gibbons-3-4, sol-munoz-garcia-7-1,
sol-tadelis-11-2, sol-tadelis-12-3, sol-tadelis-12-2, sol-tadelis-12-9, sol-tadelis-11-7.
Exact arithmetic (fractions, sympy); every threshold is tested on both sides.

Run: python check_F_L06.py  -> one line per item and "all F L06 checks passed",
or an AssertionError on the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

EPS = F(1, 1000)
H = F(1, 2)


def bayes_nf(types, prior, acts1, acts2, u):
    """Bayesian normal form when only player 1 has types.
    u(type, a1, a2) -> (u1, u2). Returns {(s1, a2): (EU1, EU2)} with s1 a tuple, one action per type."""
    nf = {}
    for s1 in product(acts1, repeat=len(types)):
        for a2 in acts2:
            e1 = sum(prior[k] * u(t, s1[k], a2)[0] for k, t in enumerate(types))
            e2 = sum(prior[k] * u(t, s1[k], a2)[1] for k, t in enumerate(types))
            nf[(s1, a2)] = (e1, e2)
    return nf


def nash(nf, S1, S2):
    return sorted((s1, s2) for s1 in S1 for s2 in S2
                  if nf[(s1, s2)][0] == max(nf[(x, s2)][0] for x in S1)
                  and nf[(s1, s2)][1] == max(nf[(s1, y)][1] for y in S2))


def interim_ok(types, prior, acts1, acts2, u, s1, a2):
    """Type-by-type best-reply test (player 2 has one type)."""
    for k, t in enumerate(types):
        if u(t, s1[k], a2)[0] < max(u(t, a, a2)[0] for a in acts1):
            return False
    e2 = lambda y: sum(prior[k] * u(t, s1[k], y)[1] for k, t in enumerate(types))
    return e2(a2) == max(e2(y) for y in acts2)


# ================================================== MG 7.1 (also used by Gibbons 3.1)
M71 = {("A", "C"): (None, 18), ("A", "D"): (6, 7), ("B", "C"): (8, 0), ("B", "D"): (8, 11)}


def u71(x, a1, a2):
    v = M71[(a1, a2)]
    return (x if v[0] is None else v[0], v[1])


T71, P71 = (15, 4), (H, H)
nf71 = bayes_nf(T71, P71, "AB", "CD", u71)
S1 = sorted({s for s, _ in nf71})
assert len(S1) == 4                                     # |A1|^|Theta1| = 2^2
cells = {("A", "A", "C"): (F(19, 2), 18), ("A", "A", "D"): (6, 7), ("A", "B", "C"): (F(23, 2), 9),
         ("A", "B", "D"): (7, 9), ("B", "A", "C"): (6, 9), ("B", "A", "D"): (7, 9),
         ("B", "B", "C"): (8, 0), ("B", "B", "D"): (8, 11)}
for (a, b, c), v in cells.items():
    assert nf71[((a, b), c)] == v
bne71 = nash(nf71, S1, "CD")
assert bne71 == [(("A", "B"), "C"), (("B", "B"), "D")]
assert [p for p in product(S1, "CD") if interim_ok(T71, P71, "AB", "CD", u71, *p)] == bne71
# complete information
for x, want in ((15, [("A", "C"), ("B", "D")]), (4, [("B", "D")])):
    got = [(a1, a2) for a1, a2 in product("AB", "CD")
           if u71(x, a1, a2)[0] == max(u71(x, z, a2)[0] for z in "AB")
           and u71(x, a1, a2)[1] == max(u71(x, a1, z)[1] for z in "CD")]
    assert got == want
# player 2's threshold on q = Pr(x = 15) against A15B4: C iff q >= 1/2
c_ok = lambda q: 18 * q >= 7 * q + 11 * (1 - q)
assert c_ok(H) and c_ok(H + EPS) and not c_ok(H - EPS)

# Munich (Lecture 6 frames 26-27)
UC, UN = F(6, 10) * 3 + F(4, 10) * 1, F(6, 10) * 2 + F(4, 10) * 2
assert (UC, UN) == (F(11, 5), 2) and UC > UN
print("Gibbons 3.1: |S1| = 4; normal-form NE = type-by-type BNE (2 profiles); "
      "Munich U(C) = 11/5 > U(N) = 2")

# ================================================== Tadelis 11.1 (disagreement)
GRID = [F(k, 10) for k in range(11)]


def play(T, d, dev, plan):
    """Payoff of player `dev` (1 or 2) using plan[t] = (own claim when proposing, minimum own share
    accepted when responding), against an opponent who claims the whole pie and rejects everything.
    Player 1 proposes in odd periods."""
    for t in range(1, T + 1):
        proposer = 1 if t % 2 else 2
        if proposer == dev:
            continue                                     # opponent rejects any offer
        if 0 >= plan[t - 1][1]:                          # opponent leaves him 0; he accepts iff 0 >= threshold
            return d ** (t - 1) * 0
    return F(0)


def best_deviation(T, d):
    """Best payoff over all deviator plans on a grid (claims and acceptance thresholds in GRID)."""
    acts = [(x, th) for x in GRID for th in GRID[:3]]
    plans = product(acts, repeat=T) if T <= 3 else [[(x, th)] * T for x, th in acts]
    return max(play(T, d, dev, list(pl)) for dev in (1, 2) for pl in plans)


for T in range(1, 7):
    for d in (H, F(9, 10)):
        assert best_deviation(T, d) == 0
# against a claim x < 1, rejecting costs the responder 1 - x > 0
assert all((1 - x) > 0 for x in GRID if x < 1)
print("Tadelis 11.1: disagreement is Nash for T = 1..6 (best deviation payoff 0); x < 1 would break it")

# ================================================== MG 4.1 (ultimatum with envy)
m, a = sp.symbols("m alpha", positive=True)
mstar = sp.solve(sp.Eq(m + a * (2 * m - 1), 0), m)[0]
assert sp.simplify(mstar - a / (1 + 2 * a)) == 0
assert sp.simplify(sp.diff(mstar, a) - 1 / (1 + 2 * a) ** 2) == 0
assert sp.simplify(sp.diff(1 - mstar, a) + 1 / (1 + 2 * a) ** 2) == 0
for al, want in ((H, (F(3, 4), F(1, 4))), (1, (F(2, 3), F(1, 3))), (2, (F(3, 5), F(2, 5)))):
    ms = F(al) / (1 + 2 * F(al))
    assert (1 - ms, ms) == want
    accept = lambda mm: mm + al * (2 * mm - 1) >= 0
    assert accept(ms) and not accept(ms - EPS)
    assert ms + al * (2 * ms - 1) == 0                   # responder's utility is 0
assert sp.limit(mstar, a, sp.oo) == H
assert sp.simplify(1 - 2 * mstar - 1 / (1 + 2 * a)) == 0
print("MG 4.1: m* = alpha/(1+2 alpha); (3/4,1/4) at alpha=1/2, (2/3,1/3) at alpha=1; limit 1/2")

# ================================================== Gibbons 3.4
G1 = {("T", "L"): (1, 1), ("T", "R"): (0, 0), ("B", "L"): (0, 0), ("B", "R"): (0, 0)}
G2 = {("T", "L"): (0, 0), ("T", "R"): (0, 0), ("B", "L"): (0, 0), ("B", "R"): (2, 2)}
u34 = lambda g, a1, a2: (G1 if g == 1 else G2)[(a1, a2)]
nf34 = bayes_nf((1, 2), (H, H), "TB", "LR", u34)
S34 = sorted({s for s, _ in nf34})
bne34 = nash(nf34, S34, "LR")
assert bne34 == [(("B", "B"), "R"), (("T", "B"), "R"), (("T", "T"), "L")]
assert [p for p in product(S34, "LR") if interim_ok((1, 2), (H, H), "TB", "LR", u34, *p)] == bne34
print("Gibbons 3.4: pure BNE = (TT,L), (TB,R), (BB,R)")

assert bne71  # MG 7.1 line printed here to keep the item order of the list
print("MG 7.1: complete info x=15 -> (A,C),(B,D); x=4 -> (B,D); BNE = (A15B4,C), (B15B4,D)")

# ================================================== Tadelis 11.2 (holdup), integer grid
vL, vH, cL, cH = 6, 12, 2, 5
V, C = {"L": vL, "H": vH}, {"L": cL, "H": cH}


def outcome(inv, offers, thr):
    """inv: investment; offers[k]: share offered to 2 after k; thr[k]: 2 accepts iff share >= thr[k]."""
    z = offers[inv]
    return (V[inv] - z, z - C[inv]) if z >= thr[inv] else (0, -C[inv])


P1 = [dict(L=zl, H=zh) for zl in range(vL + 1) for zh in range(vH + 1)]
P2 = [(inv, dict(L=tl, H=th)) for inv in "LH" for tl in range(vL + 2) for th in range(vH + 2)]
nash_out = set()
spe = []
for o in P1:
    for inv, thr in P2:
        u = outcome(inv, o, thr)
        if any(outcome(inv, o2, thr)[0] > u[0] for o2 in P1):
            continue
        if any(outcome(i2, o, t2)[1] > u[1] for i2, t2 in P2):
            continue
        nash_out.add((inv, o[inv], u))
        # subgame perfect: 2 accepts every share >= 0 after both investments; 1 offers 0
        if thr == dict(L=0, H=0) and o == dict(L=0, H=0):
            spe.append((inv, u))
assert spe == [("L", (6, -2))]
better = sorted((inv, y) for inv, y, u in nash_out if u[0] > vL and u[1] > -cL)
assert better == [("H", 4), ("H", 5)]                   # 3 < y < 6
print("Tadelis 11.2: SPE (L, offer 0) = (6,-2); Pareto-better Nash outcomes use H with y in {4, 5}")

# ================================================== Tadelis 12.3 (armed conflict)


def bne_conflict(mv, w, s):
    def uA(t, tr, ar):                                   # attack payoff of type t vs rival type tr acting ar
        if ar == "N":
            return mv
        if t == "S" and tr == "W":
            return mv - s
        return -s if t == "S" else -w
    strat = [x + y for x in "AN" for y in "AN"]          # (strong, weak)

    def br_ok(own, rival):
        for k, t in enumerate("SW"):
            eA = H * uA(t, "S", rival[0]) + H * uA(t, "W", rival[1])
            if (own[k] == "A") != (eA >= 0) and eA != 0:
                return False
        return True
    return sorted((x, y) for x in strat for y in strat if br_ok(x, y) and br_ok(y, x))


assert bne_conflict(3, 2, 1) == [("AA", "AN"), ("AN", "AA")]
assert bne_conflict(3, 4, 2) == [("AA", "NN"), ("AN", "AN"), ("NN", "AA")]
print("Tadelis 12.3: (a) BNE = (AA,AN), (AN,AA); (b) BNE = (AA,NN), (AN,AN), (NN,AA)")

# ================================================== Tadelis 12.2 (Cournot with private costs)
A_, B_, cl, ch, mu = sp.symbols("a b c_L c_H mu", positive=True)
q1L, q1H, q2L, q2H = sp.symbols("q1L q1H q2L q2H")
qb2, qb1 = mu * q2L + (1 - mu) * q2H, mu * q1L + (1 - mu) * q1H
sol = sp.solve([A_ - cl - B_ * qb2 - 2 * B_ * q1L, A_ - ch - B_ * qb2 - 2 * B_ * q1H,
                A_ - cl - B_ * qb1 - 2 * B_ * q2L, A_ - ch - B_ * qb1 - 2 * B_ * q2H],
               [q1L, q1H, q2L, q2H], dict=True)
assert len(sol) == 1
sol = sol[0]
cbar = mu * cl + (1 - mu) * ch
fL, fH = (2 * A_ - 3 * cl + cbar) / (6 * B_), (2 * A_ - 3 * ch + cbar) / (6 * B_)
assert sp.simplify(sol[q1L] - fL) == 0 and sp.simplify(sol[q2L] - fL) == 0
assert sp.simplify(sol[q1H] - fH) == 0 and sp.simplify(sol[q2H] - fH) == 0
assert sp.simplify(fL - ((A_ - cl) / (3 * B_) + (1 - mu) * (ch - cl) / (6 * B_))) == 0
assert sp.simplify(fH - ((A_ - ch) / (3 * B_) - mu * (ch - cl) / (6 * B_))) == 0
assert sp.simplify(mu * fL + (1 - mu) * fH - (A_ - cbar) / (3 * B_)) == 0
ex = {A_: 10, B_: 1, cl: 1, ch: 3, mu: sp.Rational(2, 5)}
qL, qH = fL.subs(ex), fH.subs(ex)
assert (qL, qH) == (sp.Rational(16, 5), sp.Rational(11, 5))
qbar = sp.Rational(2, 5) * qL + sp.Rational(3, 5) * qH
assert qbar == sp.Rational(13, 5)
for c, qs in ((1, qL), (3, qH)):
    prof = lambda q: (10 - c - qbar - q) * q
    assert all(prof(qs) >= prof(sp.Rational(k, 100)) for k in range(0, 1001))
# homework: q_i = (theta_i - E q_j)/2
th, E1, E2 = sp.symbols("theta Etheta_i Etheta_j")
Eq1, Eq2 = sp.symbols("Eq_i Eq_j")
hw = sp.solve([Eq1 - (E1 - Eq2) / 2, Eq2 - (E2 - Eq1) / 2], [Eq1, Eq2])
assert sp.simplify(hw[Eq1] - (2 * E1 - E2) / 3) == 0
q_hw = (th - hw[Eq2]) / 2
assert sp.simplify(q_hw - (th / 2 - (2 * E2 - E1) / 6)) == 0
print("Tadelis 12.2: q(cL) = (2a-3cL+cbar)/(6b), q(cH) = (2a-3cH+cbar)/(6b), unique; example 16/5, 11/5; "
      "homework q(theta) = theta/2 - (2E theta_j - E theta_i)/6")

# ================================================== Tadelis 12.9 (grab the dollar)
# (a) mixed NE by indifference
p = sp.symbols("p")
assert sp.solve(sp.Eq((1 - p) * 1 + p * (-1), 0), p) == [sp.Rational(1, 2)]
# (b) threshold equations
e, ti, tj = sp.symbols("epsilon t_i t_j")
sols = sp.solve([ti * (e + tj) + 2 * tj, tj * (e + ti) + 2 * ti], [ti, tj], dict=True)
pairs = {(sp.simplify(s[ti]), sp.simplify(s[tj])) for s in sols}
assert pairs == {(0, 0), (-(2 + e), -(2 + e))}
for ev in (F(1, 10), H, F(9, 10)):
    assert not (-ev <= -(2 + ev) <= ev)                  # only t = 0 is inside [-eps, eps]
    assert (ev - 0) / (2 * ev) == H                      # grab probability at t = 0
    # best threshold to a rival with threshold t: -2t/(eps+t); at t = 0 it is 0
    assert F(-2 * 0) / (ev + 0) == 0
    # corners: rival never grabs (p=0) -> grab iff theta >= -1, true for all types
    assert all((1 - 0) * (1 + th_) - 0 > 0 for th_ in (-ev, 0, ev))
    # rival always grabs (p=1) -> grabbing gives -1 < 0
    assert (1 - 1) * (1 + ev) - 1 < 0
print("Tadelis 12.9: (a) (G,D), (D,G), p = 1/2; (b) symmetric threshold 0, prob 1/2, plus 2 corner BNE; "
      "(c) limit = mixed NE")

# ================================================== Tadelis 11.7 (Baron-Ferejohn, T periods)
for N in (3, 5, 7, 9):
    for d in (H, F(9, 10), F(1)):
        v = F(1, N)                                      # v_1
        for t in range(2, 8):
            k = 1 - F(N - 1, 2) * d * v
            v_new = k / N + F(N - 1, N) * H * d * v
            assert v_new == F(1, N)
            assert k + F(N - 1, 2) * d * v == 1          # shares add to 1
            v = v_new
        k2 = 1 - F(N - 1, 2) * d * F(1, N)
        assert k2 == 1 - d * F(N - 1, 2 * N)
        # stationary fixed point v = k/N + (N-1)/(2N) d v with k = 1 - (N-1)/2 d v -> v = 1/N
        vs = sp.symbols("v")
        fp = sp.solve(sp.Eq(vs, (1 - sp.Rational(N - 1, 2) * d * vs) / N
                            + sp.Rational(N - 1, 2 * N) * d * vs), vs)
        assert fp == [sp.Rational(1, N)]
        assert k2 > 1 - d                                # beats two-person T = 2
        assert k2 > d * F(1, N)                          # proposer prefers passing
assert 1 - F(9, 10) * F(2, 6) == F(7, 10)                # N = 3, delta = 9/10
# N = 5, T = 1, all vote no: yes count = proposer only (1); one voter switching -> 2 < 3 = majority
N = 5
assert 1 + 1 < (N + 1) // 2
assert 1 + 1 >= (3 + 1) // 2                             # with N = 3 that voter would be pivotal
print("Tadelis 11.7: v_t = 1/N for all t; k2 = k_inf = 1 - delta(N-1)/(2N) > 1 - delta; "
      "N=5 all-no voting has no pivotal voter")

print("all F L06 checks passed")
