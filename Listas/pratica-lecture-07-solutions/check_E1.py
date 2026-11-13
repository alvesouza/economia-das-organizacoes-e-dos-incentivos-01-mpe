"""Lecture 7, Tier 1 (items 1-8): gibbons-3-1, munoz-garcia-7-1, gibbons-3-4, tadelis-12-1,
tadelis-13-1, munoz-garcia-8-4, munoz-garcia-8-1, tadelis-13-2.
Exact arithmetic (fractions, sympy); scipy for the continuous best-response checks.
Run: python check_E1.py -> one line per item and "all E1 checks passed", or an AssertionError."""
import random
from fractions import Fraction as F
from itertools import product

import sympy as sp
from scipy.optimize import minimize_scalar

from bayes import interim_ok, pure_bne, strategies

# --------------------------------------------------------------------- MG Ch. 7 Ex. 1 game
T_MG = [["15", "4"], ["-"]]
ACT_MG = [["A", "B"], ["C", "D"]]
PRIOR_MG = {("15", "-"): F(1, 2), ("4", "-"): F(1, 2)}
U1 = {("A", "C"): lambda x: x, ("A", "D"): lambda x: 6, ("B", "C"): lambda x: 8, ("B", "D"): lambda x: 8}
U2 = {("A", "C"): 18, ("A", "D"): 7, ("B", "C"): 0, ("B", "D"): 11}


def u_mg(i, a1, a2, t1, t2):
    return F(U1[(a1, a2)](int(t1))) if i == 0 else F(U2[(a1, a2)])


# ---- item 1 (gibbons-3-1): |S_i| = |A_i|^|T_i|; BNE = ex-ante NE = interim best replies
assert len(strategies(T_MG[0], ACT_MG[0])) == 2 ** 2
bne, U = pure_bne(T_MG, ACT_MG, PRIOR_MG, u_mg)
for s in bne:
    assert interim_ok(0, s, PRIOR_MG, T_MG, ACT_MG, u_mg)
    assert interim_ok(1, s, PRIOR_MG, T_MG, ACT_MG, u_mg)
print("gibbons-3-1: |S_i| = |A_i|^|T_i|; BNE = ex-ante NE = interim best replies (checked on the MG 7.1 game)")


# ---- item 2 (munoz-garcia-7-1)
def nash_2x2(x):
    M1 = {("A", "C"): x, ("A", "D"): 6, ("B", "C"): 8, ("B", "D"): 8}
    return [(a1, a2) for a1, a2 in product("AB", "CD")
            if M1[(a1, a2)] >= max(M1[(b, a2)] for b in "AB")
            and U2[(a1, a2)] >= max(U2[(a1, d)] for d in "CD")]


assert nash_2x2(15) == [("A", "C"), ("B", "D")]
assert nash_2x2(4) == [("B", "D")]
printed = {  # Fig. 7.5 of the book: rows A15A4, A15B4, B15A4, B15B4; columns C, D
    (("A", "A"), "C"): (F(19, 2), 18), (("A", "A"), "D"): (6, 7),
    (("A", "B"), "C"): (F(23, 2), 9), (("A", "B"), "D"): (7, 9),
    (("B", "A"), "C"): (6, 9), (("B", "A"), "D"): (7, 9),
    (("B", "B"), "C"): (8, 0), (("B", "B"), "D"): (8, 11)}
for (s1, a2), (p1, p2) in printed.items():
    assert U[(s1, (a2,))] == (F(p1), F(p2)), (s1, a2)
assert sorted(bne) == sorted([(("A", "B"), ("C",)), (("B", "B"), ("D",))])
print("munoz-garcia-7-1: x=15 NE {AC,BD}; x=4 NE {BD}; Fig. 7.5 reproduced; BNE = {(A15B4,C),(B15B4,D)}")

# ---- item 3 (gibbons-3-4)
T34 = [["G1", "G2"], ["-"]]
PRIOR34 = {("G1", "-"): F(1, 2), ("G2", "-"): F(1, 2)}
G = {"G1": {("T", "L"): (1, 1), ("T", "R"): (0, 0), ("B", "L"): (0, 0), ("B", "R"): (0, 0)},
     "G2": {("T", "L"): (0, 0), ("T", "R"): (0, 0), ("B", "L"): (0, 0), ("B", "R"): (2, 2)}}
bne3, _ = pure_bne(T34, [["T", "B"], ["L", "R"]], PRIOR34,
                   lambda i, a1, a2, t1, t2: F(G[t1][(a1, a2)][i]))
assert sorted(bne3) == sorted([(("T", "T"), ("L",)), (("T", "B"), ("R",)), (("B", "B"), ("R",))]), bne3
print("gibbons-3-4: pure BNE = {(TT,L), (TB,R), (BB,R)}")


# ---- item 4 (tadelis-12-1): chicken with parents of type L or H (cost k of an accident)
def chicken_bne(R, H, L):
    cost = {"L": L, "H": H}

    def u(i, a1, a2, t1, t2):
        ai, aj = (a1, a2)[i], (a1, a2)[1 - i]
        if ai == "C":
            return F(0)
        return F(R) if aj == "C" else F(R, 2) - cost[(t1, t2)[i]]

    T = [["L", "H"], ["L", "H"]]
    prior = {(a, b): F(1, 4) for a in "LH" for b in "LH"}
    return pure_bne(T, [["C", "D"], ["C", "D"]], prior, u)


b1, U1c = chicken_bne(8, 16, 0)
assert b1 == [(("D", "C"), ("D", "C"))], b1  # (DC, dc): L-types drive, H-types swerve
assert U1c[(("C", "D"), ("D", "D"))] == (F(-6), F(2))  # printed matrix entry (CD, dd)
assert U1c[(("D", "C"), ("D", "C"))] == (F(3), F(3))
b2, _ = chicken_bne(8, 0, 16)
assert b2 == [(("C", "D"), ("C", "D"))], b2  # L-types swerve, H-types drive
assert F(8, 2) - 0 > 0  # all-lenient society, case 1 (k = 0): D strictly dominant (8 > 0 and 4 > 0)
q = sp.symbols("q")
assert sp.solve(sp.Eq(8 * (1 - q) + q * (4 - 16), 0), q) == [sp.Rational(2, 5)]  # case 2, all lenient (k = 16)
assert sp.Rational(2, 5) ** 2 == sp.Rational(4, 25) < sp.Rational(1, 4)
print("tadelis-12-1: R=8,H=16,L=0 -> unique BNE (DC,dc); R=8,H=0,L=16 -> unique BNE (CD,cd); all-lenient cases checked")


# ---- item 5 (tadelis-13-1): weak dominance of b = v in the second-price auction
def spa_payoff(v, b, r, ut=lambda z: z):
    """Payoff of a bidder with bid b against highest rival bid r; a tie is a fair coin."""
    if b > r:
        return ut(v - r)
    if b == r:
        return F(1, 2) * ut(v - r) + F(1, 2) * ut(0)
    return ut(0)


grid = [F(k, 2) for k in range(0, 13)]
for v in grid:
    for b in grid:
        diffs = [spa_payoff(v, v, r) - spa_payoff(v, b, r) for r in grid]
        assert all(d >= 0 for d in diffs), (v, b)
        if b != v:
            assert any(d > 0 for d in diffs), (v, b)  # strict for some rival bid
print("tadelis-13-1: b = v weakly dominates every b != v on a 13x13x13 grid")

# ---- item 6 (munoz-garcia-8-4): independence of correlation, N and risk attitude
utils = {"linear": lambda z: z, "concave": lambda z: z / 2 if z >= 0 else 2 * z,
         "convex": lambda z: z * z if z >= 0 else -z * z}  # all with u(0) = 0, strictly increasing
for name, ut in utils.items():
    for v in grid:
        for b in grid:
            for r in grid:
                assert spa_payoff(v, v, r, ut) >= spa_payoff(v, b, r, ut), (name, v, b, r)
random.seed(7)  # arbitrary joint laws of the rivals' bids: dominance holds pointwise, hence on average
for N in (2, 3, 5):
    for _ in range(200):
        v = random.choice(grid)
        draws = [[random.choice(grid) for _ in range(N - 1)] for _ in range(30)]
        ev = sum(spa_payoff(v, v, max(d)) for d in draws)
        for b in grid:
            assert ev >= sum(spa_payoff(v, b, max(d)) for d in draws)
print("munoz-garcia-8-4: b = v dominant for linear/concave/convex u, N = 2,3,5, arbitrary joint laws of rival bids")

# ---- item 7 (munoz-garcia-8-1): first price, two uniform bidders
v, x, a, t = sp.symbols("v x a t", positive=True)
EU = (x / a) * (v - x)
sol = sp.solve(sp.diff(EU, x), x)
assert sol == [v / 2]  # FOC does not depend on the shading factor a
assert sp.solve(sp.Eq(sol[0], a * v), a) == [sp.Rational(1, 2)]  # x = a v consistency -> a = 1/2
for vv in [0.1, 1 / 3, 2 / 3, 0.9, 1.0]:
    r = minimize_scalar(lambda b: -(min(2 * b, 1.0) * (vv - b)), bounds=(0, 1), method="bounded",
                        options={"xatol": 1e-10})
    assert abs(r.x - vv / 2) < 1e-5, (vv, r.x)
    assert abs(-r.fun - vv ** 2 / 2) < 1e-8  # EU* = 2b(v-b) at b = v/2 = v^2/2
rev_fpa = sp.integrate(sp.Rational(1, 2) * t * 2 * t, (t, 0, 1))  # E[max v / 2], max has density 2t
rev_spa = sp.integrate(t * 2 * (1 - t), (t, 0, 1))  # E[min v], min has density 2(1-t)
assert rev_fpa == rev_spa == sp.Rational(1, 3)
print("munoz-garcia-8-1: FOC gives b = v/2; scipy confirms the best reply; EU*(v) = v^2/2; "
      "revenue 1/3 = second-price revenue")

# ---- item 8 (tadelis-13-2): complete-information second-price auction, N = 3
vals = [F(3), F(2), F(1)]
bids = [F(k) for k in range(0, 5)]


def spa_N(i, prof):
    mx = max(prof)
    winners = [k for k, bb in enumerate(prof) if bb == mx]
    if i not in winners:
        return F(0)
    return (vals[i] - sorted(prof, reverse=True)[1]) / len(winners)


ne = [p for p in product(bids, repeat=3)
      if all(spa_N(i, p) >= spa_N(i, p[:i] + (bb,) + p[i + 1:]) for i in range(3) for bb in bids)]
assert (F(3), F(2), F(1)) in ne  # truthful bidding is a NE
assert (F(0), F(3), F(0)) in ne  # player 2 (value 2) wins by bidding the highest rival value
assert (F(0), F(0), F(3)) in ne  # even player 3 (value 1) can win in equilibrium
for i in range(3):  # weak dominance of the true value against every profile of rivals
    for bb in bids:
        for others in product(bids, repeat=2):
            def pay(z, i=i, others=others):
                prof = list(others)
                prof.insert(i, z)
                return spa_N(i, tuple(prof))
            assert pay(vals[i]) >= pay(bb)
assert {i for p in ne for i in range(3) if spa_N(i, p) > 0} == {0, 1, 2}
print(f"tadelis-13-2: truthful is weakly dominant; {len(ne)} pure NE on the integer grid, every player can win")
print("all E1 checks passed")
