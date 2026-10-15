"""Checks every number and closed form stated in items 18, 20, 21, 22, 28, 29 (group D).

Run: python check_D.py  -> prints "all D checks passed" or stops at the first failed assert.
"""
import sympy as sp

x, p, v, c, d, d1, d2, r1, r2, D, psi = sp.symbols("x p v c delta delta1 delta2 r1 r2 Delta psi", positive=True)

# ---- Item 20 (FFT 5.1): a lying cost psi in M&R's Table 5.3 example -----------------------
lo = sp.solve(sp.Eq(sp.Rational(2, 10) + sp.Rational(8, 10) * p, sp.Rational(16, 10) - psi), p)[0]
hi = sp.solve(sp.Eq(sp.Rational(26, 10) - sp.Rational(8, 10) * p, sp.Rational(16, 10) - psi), p)[0]
assert sp.simplify(lo - (sp.Rational(7, 4) - sp.Rational(5, 4) * psi)) == 0
assert sp.simplify(hi - (sp.Rational(5, 4) + sp.Rational(5, 4) * psi)) == 0
assert sp.solve(sp.Eq(lo, hi), psi) == [sp.Rational(1, 5)]
assert lo.subs(psi, sp.Rational(1, 5)) == sp.Rational(3, 2)
# Table 5.1 grab game: guilt g makes "refrain" dominant iff g > 1 (3 - g < 2 and -1 - g < -2)
assert sp.solve(sp.Eq(3 - sp.Symbol("g"), 2), sp.Symbol("g")) == [1]

# ---- Item 21 (M&R Q 5.4) ------------------------------------------------------------------
pS = {"S250": 1 - x, "S750": x}
pB = {"B500": x, "B1000": 1 - x}
assert sp.expand(1 - pB["B500"] * pS["S750"] - (1 - x**2)) == 0       # P(trade efficient)
gains = pB["B500"] * pS["S250"] * 250 + pB["B1000"] * pS["S250"] * 750 + pB["B1000"] * pS["S750"] * 250
assert sp.expand(gains - (1 - x) * (750 - 250 * x)) == 0
assert gains.subs(x, sp.Rational(1, 5)) == 560
# honest-reporting constraints with prices 500 (S250,B500), 750 (S750,B1000), p (S250,B1000)
seller_ic = x * (500 - 250) + (1 - x) * (p - 250) - (1 - x) * (750 - 250)
buyer_ic = x * (1000 - 750) + (1 - x) * (1000 - p) - (1 - x) * (1000 - 500)
k = 250 * x / (1 - x)
p_lo = sp.solve(seller_ic, p)[0]
p_hi = sp.solve(buyer_ic, p)[0]
assert sp.simplify(p_lo - (750 - k)) == 0 and sp.simplify(p_hi - (500 + k)) == 0
assert sp.solve(sp.Eq(p_lo, p_hi), x) == [sp.Rational(1, 3)]
assert p_lo.subs(x, sp.Rational(1, 3)) == 625
# the cell surplus 750 must cover both rents: 750 >= 2*(500 - k)  <=>  x >= 1/3
assert sp.solve(sp.Eq(750, 2 * (500 - k)), x) == [sp.Rational(1, 3)]
table = {sp.Rational(1, 10): (sp.Rational(2000, 3) + sp.Rational(500, 9), None),
         sp.Rational(1, 5): (sp.Rational(1375, 2), sp.Rational(1125, 2)),
         sp.Rational(1, 3): (625, 625), sp.Rational(1, 2): (500, 750), sp.Rational(4, 5): (-250, 1500)}
for xv, (lo_v, hi_v) in table.items():
    if hi_v is not None:
        assert p_lo.subs(x, xv) == lo_v and p_hi.subs(x, xv) == hi_v
assert abs(float(p_lo.subs(x, sp.Rational(1, 10))) - 722.22) < 0.01
assert abs(float(p_hi.subs(x, sp.Rational(1, 10))) - 527.78) < 0.01
assert [1 - xv**2 for xv in (sp.Rational(1, 10), sp.Rational(1, 5), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(4, 5))] == \
    [sp.Rational(99, 100), sp.Rational(24, 25), sp.Rational(8, 9), sp.Rational(3, 4), sp.Rational(9, 25)]
# low types: buyer 500 claiming 1000 and seller 750 claiming 250 are slack when the high-type ICs hold
buyer_low = 0 - (x * (500 - 750) + (1 - x) * (500 - p))     # >= 0 needed
seller_low = 0 - (x * (500 - 750) + (1 - x) * (p - 750))    # >= 0 needed
assert sp.simplify(sp.solve(buyer_low, p)[0] - (500 - k)) == 0      # p >= 500 - k, implied by p >= 750 - k
assert sp.simplify(sp.solve(seller_low, p)[0] - (750 + k)) == 0     # p <= 750 + k, implied by p <= 500 + k
# isomorphism with M&R's example: value -> (value - 250)/250 maps {250,750},{500,1000} to {0,2},{1,3}
assert p_lo.subs(x, sp.Rational(1, 5)) == 250 + 250 * sp.Rational(7, 4)
assert p_hi.subs(x, sp.Rational(1, 5)) == 250 + 250 * sp.Rational(5, 4)
assert 250 + 250 * sp.Rational(3, 2) == 625

# ---- Item 22 (M&R Q 5.5) ------------------------------------------------------------------
# gain 10: one price 10, trade always; check every participation and honesty condition
P = 10
assert P - 0 >= 0 and P - 10 >= 0                 # seller types participate
assert (0 + 10) - P >= 0 and (10 + 10) - P >= 0   # buyer gains ex post in both states
assert sp.simplify(x * (10 - p) + (1 - x) * (20 - p)) == sp.simplify(20 - 10 * x - p)
# gain g, trade always: honesty forces one price P, needs 10 <= P <= 0 + g  <=>  g >= 10
g = sp.Symbol("g")
assert sp.solve(sp.Eq(10, 0 + g), g) == [10]
# gain 5: best honest scheme sells for sure at 5 after report 0, with prob q at 10 after report 10
q = sp.Symbol("q")
assert sp.solve(sp.Eq(5, q * 10), q) == [sp.Rational(1, 2)]   # seller-0 honesty: 5 >= q * 10
assert 15 - 10 >= 0 and 5 - 5 >= 0 and 0 >= 5 - 10            # buyer IR in both states; seller-10 does not mimic
lost = (1 - x) * (1 - sp.Rational(1, 2)) * 5
assert sp.simplify(lost - sp.Rational(5, 2) * (1 - x)) == 0
# interim buyer, single price P in [10, 15 - 10x]: nonempty iff x <= 1/2
assert sp.solve(sp.Eq(x * (5 - 10) + (1 - x) * (15 - 10), 0), x) == [sp.Rational(1, 2)]


# ---- Item 28 (MWG 9.B.7 and 9.B.13): offer cost c, no discounting --------------------------
def cost_game(T, vv, cc):
    """Backward induction; returns (net payoff of player 1, net payoff of player 2, gross offer)."""
    a = 0                         # net payoff of the proposer with k periods left; a_0 = 0
    for _ in range(T):
        a_prev, a = a, vv - cc - a   # responder must get a_prev (her value as next proposer)
    resp = a_prev
    return a, resp, (vv - resp, resp)


for T in range(1, 12):
    u1, u2, offer = cost_game(T, 10, 3)
    if T % 2:
        assert (u1, u2, offer) == (7, 0, (10, 0))
    else:
        assert (u1, u2, offer) == (0, 7, (3, 7))
    assert u1 == (10 - 3) * (1 - (-1) ** T) // 2
# discounted formula of Example 9.AA.1 at delta = 1 has the same parity pattern
vT = lambda T, dd: v * (1 - (-dd) ** T) / (1 + dd)
assert sp.simplify(vT(5, 1) - v) == 0 and sp.simplify(vT(6, 1)) == 0
assert all(abs(float(vT(T, 0.6).subs(v, 1)) - 0.625) < 1e-9 for T in (200, 201))
# infinite horizon: stationary profiles (a, b) with b = v - c - a and a = v - c - b
a_, b_ = sp.symbols("a b")
assert sp.expand((b_ - (v - c - a_)) - (a_ - (v - c - b_))) == 0     # the same equation: a continuum
# Shaked-Sutton map has slope 1 (identity) with costs, slope delta1*delta2 < 1 with discounting
M1 = sp.Symbol("M1")
assert sp.simplify((v - c - (v - c - M1)) - M1) == 0
assert sp.simplify(sp.diff(v - d2 * (v - d1 * M1), M1) - d1 * d2) == 0
# delay equilibrium: on-path (v - 2c, 0); player 1's best deviation gives at most 0
vv, cc = 10, 3
assert vv - 2 * cc >= 0 and vv - (vv - cc) - cc == 0 and -cc < 0
assert (vv - 2 * cc) + 0 == (vv - cc) - cc

# ---- Item 29 (MWG 9.B.12): Rubinstein with delta1 != delta2 --------------------------------
x1 = v * (1 - d2) / (1 - d1 * d2)
x2 = v * (1 - d1) / (1 - d1 * d2)
assert sp.simplify(v - x1 - d2 * x2) == 0           # 1 offers 2 exactly delta2 * x2
assert sp.simplify(v - x2 - d1 * x1) == 0           # 2 offers 1 exactly delta1 * x1
Mx = sp.Symbol("Mx")
assert sp.simplify(sp.solve(sp.Eq(Mx, v - d2 * (v - d1 * Mx)), Mx)[0] - x1) == 0
assert sp.simplify(x1.subs(d2, d) .subs(d1, d) - v / (1 + d)) == 0
assert sp.limit(x1, d1, 1) == v                      # delta2 < 1 fixed
assert sp.limit(x1, d2, 1) == 0
assert sp.simplify(sp.limit(x1.subs({d1: sp.exp(-r1 * D), d2: sp.exp(-r2 * D)}), D, 0) - v * r2 / (r1 + r2)) == 0
num = x1.subs({v: 1, d1: sp.Rational(9, 10), d2: sp.Rational(4, 5)})
assert num == sp.Rational(5, 7) and 1 - num == sp.Rational(2, 7)
assert x2.subs({v: 1, d1: sp.Rational(9, 10), d2: sp.Rational(4, 5)}) == sp.Rational(5, 14)
assert (v * r2 / (r1 + r2)).subs({v: 1, r1: 1, r2: 2}) == sp.Rational(2, 3)
assert sp.simplify(sp.diff(x1, d1)) != 0 and sp.simplify(sp.diff(x1, d1) - v * d2 * (1 - d2) / (1 - d1 * d2) ** 2) == 0


def proposer_share(T, e1, e2):
    """Finite-horizon share of player 1 (pie 1), player 1 proposes first (as in the notes)."""
    share, who = 1.0, (T - 1) % 2
    for _ in range(T - 1):
        e = e1 if who == 0 else e2
        share = 1 - e * share
        who = 1 - who
    return share


assert abs(proposer_share(401, 0.9, 0.8) - 5 / 7) < 1e-12
assert abs(proposer_share(400, 0.9, 0.8) - 5 / 7) < 1e-12
assert abs(proposer_share(3, 0.6, 0.6) - (1 + 0.6**3) / 1.6) < 1e-12

print("all D checks passed")
