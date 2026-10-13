"""Check every closed form and number quoted in part2.tex (Bargaining).

Run: python check_part2.py  -> prints each value and fails on the first mismatch.
"""
import math

import numpy as np
import sympy as sp


def close(a, b, tol=1e-9):
    assert abs(float(a) - float(b)) < tol, (a, b)


# --- Wealth effects: WTP vs WTA with u = ln x + a*y, w = 100, a = 0.5 ----------------
w, a = 100, 0.5
wtp, wta = w * (1 - math.exp(-a)), w * (math.exp(a) - 1)
print(f"WTP {wtp:.2f}  WTA {wta:.2f}")
close(round(wtp, 2), 39.35)
close(round(wta, 2), 64.87)
assert wtp < 50 < wta  # plant's gain 50 sits between: rights decide the allocation

# --- Nash bargaining under transferable utility -------------------------------------
u1, V, d1, d2, al = sp.symbols("u1 V d1 d2 alpha", positive=True)
nash = sp.solve(sp.diff((u1 - d1) ** al * (V - u1 - d2) ** (1 - al), u1), u1)[0]
assert sp.simplify(nash - (d1 + al * (V - d1 - d2))) == 0
print("Nash split u1 =", sp.simplify(nash))
close((d1 + sp.Rational(1, 2) * (V - d1 - d2)).subs({V: 100, d1: 0, d2: 60}), 20)
# Coase example: plant gains 100, residents lose 60; residents hold the right -> price 80
close(60 + sp.Rational(1, 2) * (100 - 60), 80)


# --- Alternating offers -------------------------------------------------------------
def proposer_share(T, d_first, d_second):
    """Share of the period-1 proposer in a T-period alternating-offer game (pie 1)."""
    share = 1.0  # last proposer takes everything
    who = (T - 1) % 2  # 0 = first mover proposes in period T
    for _ in range(T - 1):
        # the earlier proposer gives the responder (next period's proposer, `who`) the
        # discounted value of proposing next
        d_resp = d_first if who == 0 else d_second
        share = 1 - d_resp * share
        who = 1 - who
    return share


d = sp.symbols("delta", positive=True)
for T in range(1, 9):
    closed = (1 - (-d) ** T) / (1 + d)
    close(proposer_share(T, 0.6, 0.6), closed.subs(d, 0.6))
print("finite horizon (1-(-d)^T)/(1+d) ok; T=3, d=.6 ->", proposer_share(3, 0.6, 0.6))
close(proposer_share(3, 0.6, 0.6), 1 - 0.6 + 0.36)
# Varian three-day game: Alice discounts at alpha, Bob at beta
alpha, beta = 0.9, 0.7
close(proposer_share(3, alpha, beta), 1 - beta * (1 - alpha))
# Rubinstein limit with different discount factors
rub = (1 - beta) / (1 - alpha * beta)
close(proposer_share(401, alpha, beta), rub, 1e-6)
print(f"Rubinstein share (a=.9, b=.7) {rub:.4f}")
close(proposer_share(401, 0.6, 0.6), 1 / 1.6, 1e-9)
r1, r2, h = sp.symbols("r1 r2 Delta", positive=True)
lim = sp.limit((1 - sp.exp(-r2 * h)) / (1 - sp.exp(-(r1 + r2) * h)), h, 0)
assert sp.simplify(lim - r2 / (r1 + r2)) == 0
print("Delta -> 0 share:", lim)

# --- M&R Table 5.2/5.3 --------------------------------------------------------------
p = sp.symbols("p")
seller_p = sp.solve(sp.Eq(sp.Rational(2, 10) * 1 + sp.Rational(8, 10) * p, sp.Rational(8, 10) * 2), p)[0]
buyer_p = sp.solve(sp.Eq(sp.Rational(2, 10) * (3 - 2) + sp.Rational(8, 10) * (3 - p),
                         sp.Rational(8, 10) * (3 - 1)), p)[0]
close(seller_p, 1.75)
close(buyer_p, 1.25)
print("original: seller needs p >=", seller_p, " buyer needs p <=", buyer_p)
# reversed probabilities, p = 1.5
close(0.8 * 1 + 0.2 * 1.5, 1.10)
close(0.2 * 2, 0.40)
close(0.8 * (3 - 2) + 0.2 * (3 - 1.5), 1.10)  # high buyer honest
close(0.2 * (3 - 1), 0.40)  # high buyer claims 1
# feasible p in reversed case: seller .8 + .2p >= .4 always; buyer .8 + .2(3-p) >= .4 -> p <= 5
close(sp.solve(sp.Eq(0.8 + 0.2 * (3 - p), 0.4), p)[0], 5)

# --- Split-the-difference double auction, uniform values ----------------------------
S, B, s, b, b1, b2, s1, s2 = sp.symbols("S B s b beta1 beta2 sigma1 sigma2")
seller_payoff = sp.integrate(((s + b1 + b2 * B) / 2 - S), (B, (s - b1) / b2, 1))
s_best = sp.solve(sp.diff(seller_payoff, s), s)[0]
buyer_payoff = sp.integrate((B - (b + s1 + s2 * S) / 2), (S, 0, (b - s1) / s2))
b_best = sp.solve(sp.diff(buyer_payoff, b), b)[0]
sol = sp.solve([sp.Eq(s2, sp.diff(s_best, S)), sp.Eq(s1, s_best.subs(S, 0)),
                sp.Eq(b2, sp.diff(b_best, B)), sp.Eq(b1, b_best.subs(B, 0))],
               [s1, s2, b1, b2], dict=True)[0]
assert sol == {s1: sp.Rational(1, 4), s2: sp.Rational(2, 3), b1: sp.Rational(1, 12), b2: sp.Rational(2, 3)}
print("linear equilibrium:", sol)
gap = sp.solve(sp.Eq(sol[b1] + sol[b2] * B, sol[s1] + sol[s2] * S), B)[0] - S
assert sp.simplify(gap - sp.Rational(1, 4)) == 0
D = sp.symbols("D")
p_trade = sp.integrate(1 - D, (D, sp.Rational(1, 4), 1))
eff_gain = sp.integrate(D * (1 - D), (D, 0, 1))
real_gain = sp.integrate(D * (1 - D), (D, sp.Rational(1, 4), 1))
assert p_trade == sp.Rational(9, 32) and eff_gain == sp.Rational(1, 6)
assert real_gain == sp.Rational(9, 64) and real_gain / eff_gain == sp.Rational(27, 32)
print("P(trade) 9/32, gains 9/64 of 1/6 = 27/32")
rng = np.random.default_rng(0)
Bs, Ss = rng.random((2, 2_000_000))
close((Bs > Ss + 0.25).mean(), 9 / 32, 2e-3)
# a seller with S = .5 who asks .52 against an honest buyer (M&R p. 144)
close(0.48 * 0.01, 0.0048)
close(0.02 * 0.005, 0.0001)

# --- Public project, many participants ----------------------------------------------
pr, q = sp.symbols("p q", positive=True)
n2 = sp.solve(sp.Eq(pr * (2 - sp.Rational(1, 2)) + (1 - pr) * (2 - 1), 2 * pr), pr)[0]
assert n2 == sp.Rational(2, 3)
q_max = sp.solve(sp.Eq(pr * sp.Rational(3, 2) + (1 - pr) * q, 2 * pr * q), q)[0]
assert sp.limit(q_max, pr, 1) == sp.Rational(3, 4)
print("N=2: p <= 2/3; q_max(p) =", sp.simplify(q_max), "-> 3/4")
lhs3 = pr**2 * (2 - sp.Rational(1, 3)) + 2 * pr * (1 - pr) * (2 - sp.Rational(1, 2)) + (1 - pr) ** 2 * (2 - 1)
rhs3 = 2 * (1 - (1 - pr) ** 2)
n3 = [r for r in sp.solve(sp.Eq(lhs3, rhs3), pr) if 0 < r < 1][0]
print(f"N=3 threshold p = {float(n3):.4f}")
assert 0.43 < float(n3) < 0.45
q3 = sp.solve(sp.Eq(
    sp.Rational(1, 4) * sp.Rational(5, 3) + sp.Rational(1, 2) * sp.Rational(3, 2) + sp.Rational(1, 4) * q,
    sp.Rational(1, 4) * 2 + sp.Rational(1, 2) * 2 * q), q)[0]
assert q3 == sp.Rational(8, 9)
print("N=3, p=1/2: q <= 8/9")

# --- Hold-up preview: value a*e, cost e^2/2, ex-post 50/50 split ---------------------
av, e = sp.symbols("a e", positive=True)
e_eff = sp.solve(sp.diff(av * e - e**2 / 2, e), e)[0]
e_hold = sp.solve(sp.diff(av * e / 2 - e**2 / 2, e), e)[0]
surplus = lambda x: av * x - x**2 / 2  # noqa: E731
assert e_eff == av and e_hold == av / 2
assert sp.simplify(surplus(e_hold) / surplus(e_eff)) == sp.Rational(3, 4)
print("hold-up: e = a/2, surplus 3/4 of efficient")
print("all Part II checks passed")
