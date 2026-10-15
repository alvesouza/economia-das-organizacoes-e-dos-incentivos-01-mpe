"""Checks every number and closed form stated in item24.tex (M&R Math. Ex. 4.2, p. 120).

Run: python check_A.py  -> prints "all A checks passed" or fails on the first wrong claim.
"""
import sympy as sp

t, tau, eps, p = sp.symbols("t tau epsilon p", real=True)
c = {1: 3, 2: 4, 3: 5}          # marginal cost of a one-month speed-up, per department
C = sum(c.values())              # 12


def profit(t1, t2, t3):
    """Firm profit when department n is told to be ready at t_n (all t_n < 12)."""
    T = sp.Max(t1, t2, t3)       # production starts when the last department is ready
    return 144 - T**2 - sum(c[n] * (12 - tn) for n, tn in zip((1, 2, 3), (t1, t2, t3)))


# (1) coordinated date: pi(t) = 12t - t^2, t* = 6, pi* = 36
pi = sp.expand(144 - t**2 - C * (12 - t))
assert pi == 12 * t - t**2
tstar = sp.solve(sp.diff(pi, t), t)
assert tstar == [6]
assert pi.subs(t, 6) == 36
assert 144 - 6**2 == 108 and C * (12 - 6) == 72        # revenue and readiness cost at t*
assert pi.subs(t, 0) == 0 and pi.subs(t, 12) == 0      # corners (t >= 12 earns nothing)
assert sp.diff(pi, t, 2) == -2                          # strictly concave: global max
assert 2 * 6 == C                                       # MB of speed-up = sum of MCs
assert pi.subs(t, sp.Rational(59, 10)) == pi.subs(t, sp.Rational(61, 10)) == sp.Rational(3599, 100)
assert (144 - 49) - (144 - 36) == -13 and -13 + 4 == -9  # verification (b) in item24

# (2) all departments one month early / late
assert profit(5, 5, 5) == 35 and profit(7, 7, 7) == 35
assert sp.expand(pi.subs(t, 6 + eps) - 36) == -eps**2   # coordinated error: second order

# (3) department 2 alone early / late, others at t* = 6
assert profit(6, 5, 6) == 32 and profit(6, 7, 6) == 27
assert 3 * 6 + 4 * 7 + 5 * 6 == 76 and 3 * 6 + 4 * 5 + 5 * 6 == 68
assert 144 - 49 == 95 and 95 - 68 == 27 and 108 - 76 == 32
# piecewise profit of a misfit in department 2 (figure in item24)
early = sp.expand(108 - 3 * 6 - 5 * 6 - 4 * (12 - tau))   # tau <= 6
late = sp.expand(144 - tau**2 - 3 * 6 - 5 * 6 - 4 * (12 - tau))  # tau >= 6
assert early == 4 * tau + 12 and late == 48 + 4 * tau - tau**2
assert early.subs(tau, 6) == late.subs(tau, 6) == 36
assert sp.diff(early, tau) == 4                          # left slope  = c_2
assert sp.diff(late, tau).subs(tau, 6) == -8             # right slope = -(c_1 + c_3)
# general misfit losses: early c_n*eps, late (C - c_n)*eps + eps^2
for n in (1, 2, 3):
    args_e = [6 if m != n else 6 - eps for m in (1, 2, 3)]
    args_l = [6 if m != n else 6 + eps for m in (1, 2, 3)]
    loss_e = sp.simplify(36 - profit(*args_e).subs(eps, sp.Rational(1, 2)))
    loss_l = sp.simplify(36 - profit(*args_l).subs(eps, sp.Rational(1, 2)))
    assert loss_e == c[n] * sp.Rational(1, 2)
    assert loss_l == (C - c[n]) * sp.Rational(1, 2) + sp.Rational(1, 4)
# losses quoted in the comparison table (eps = 1)
assert [36 - profit(5, 5, 5), 36 - profit(7, 7, 7), 36 - profit(6, 5, 6), 36 - profit(6, 7, 6)] == [1, 1, 4, 9]

# price remark: paying p per month of earliness, department n earns (p - c_n)(12 - t_n),
# linear in t_n -> corner choice (t_n = 0 if p > c_n, t_n = 12 if p < c_n)
for n in (1, 2, 3):
    payoff = (p - c[n]) * (12 - t)
    assert sp.diff(payoff, t, 2) == 0
    assert sp.diff(payoff, t).subs(p, c[n] + 1) == -1 and sp.diff(payoff, t).subs(p, c[n] - 1) == 1

# item05 verification: Table 4.1 (M&R p. 95), error scenario. Total benefits 58, 64, 70 at
# 6, 7, 10 units; actual total costs 24, 29, 50. Quantity 6 vs price 8 (firm makes 10).
best = 64 - 29
assert (58 - 24, best, 70 - 50) == (34, 35, 20)
assert best - (58 - 24) == 1 and best - (70 - 50) == 15

print("all A checks passed")
