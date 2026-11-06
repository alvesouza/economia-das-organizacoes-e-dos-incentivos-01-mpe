"""Checks every number and equilibrium claim in the four Lecture 4 solutions written by agent D:
sol-tadelis-7-6, sol-munoz-garcia-4-11, sol-tadelis-8-11, sol-tadelis-8-7.
Exact arithmetic (fractions, sympy). Backward induction, Nash equilibria and subgame-perfect
equilibria of the finite trees are computed by enumeration, not typed in.

Run: python check_D.py  -> one line per item and "all D checks passed", or an AssertionError on
the first wrong claim.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp


# ----------------------------------------------------------------------------- finite trees
# A decision node is (player, label, {action: child}); a leaf is a tuple of payoffs.
def is_leaf(t):
    return not (len(t) == 3 and isinstance(t[2], dict))


def nodes(t):
    """All decision nodes of the tree t (pre-order)."""
    if is_leaf(t):
        return []
    return [t] + [n for c in t[2].values() for n in nodes(c)]


def play(t, prof):
    """Terminal payoffs when the pure profile prof = {label: action} is played from t."""
    while not is_leaf(t):
        t = t[2][prof[t[1]]]
    return t


def strategies(t, player):
    """All pure strategies of `player` in t, as dicts {label: action} over all its nodes."""
    own = [n for n in nodes(t) if n[0] == player]
    return [dict(zip([n[1] for n in own], acts)) for acts in product(*[list(n[2]) for n in own])]


def is_ne(t, prof, players):
    """Pure Nash equilibrium test of prof in the (sub)tree t."""
    base = play(t, prof)
    return all(play(t, {**prof, **dev})[i] <= base[i]
               for i in players for dev in strategies(t, i))


def is_spe(t, prof, players):
    """Subgame perfection by definition: the restriction is a NE in every subgame. In these
    perfect-information trees every decision node starts a subgame."""
    return all(is_ne(n, prof, players) for n in nodes(t))


def pure_profiles(t, players):
    for parts in product(*[strategies(t, i) for i in players]):
        yield {k: v for p in parts for k, v in p.items()}


def backward_induction(t):
    """(payoffs, plan) by backward induction; asserts no ties at any node (so it is unique)."""
    if is_leaf(t):
        return t, {}
    player, label, kids = t
    res = {a: backward_induction(c) for a, c in kids.items()}
    vals = sorted((r[0][player] for r in res.values()), reverse=True)
    assert len(vals) == 1 or vals[0] > vals[1], f"tie at {label}"
    best = max(res, key=lambda a: res[a][0][player])
    plan = {label: best}
    for r in res.values():
        plan.update(r[1])
    return res[best][0], plan


# ============================================================ Tadelis 7.6 (Entering an Industry)
# payoffs (u1, u2); 1: In,A = 2 > Out = 1 > In,F = 0; 2: Out = 2 > In,A = 1 > In,F = 0
T76 = (0, "1", {"Out": (1, 2), "In": (1, "2", {"A": (2, 1), "F": (0, 0)})})
assert [len(strategies(T76, i)) for i in (0, 1)] == [2, 2]
ne76 = [p for p in pure_profiles(T76, (0, 1)) if is_ne(T76, p, (0, 1))]
assert sorted(tuple(sorted(p.items())) for p in ne76) == [
    (("1", "In"), ("2", "A")), (("1", "Out"), ("2", "F"))]
spe76 = [p for p in ne76 if is_spe(T76, p, (0, 1))]
assert spe76 == [{"1": "In", "2": "A"}]
assert backward_induction(T76) == ((2, 1), {"1": "In", "2": "A"})
# mixed: p = Pr(In), f = Pr(F); exact NE test on a grid of step 1/100 (includes 1/2)
def ne76_mixed(p, f):
    u1_in, u1_out = 2 * (1 - f), F(1)
    u2_a, u2_f = p * 1 + (1 - p) * 2, p * 0 + (1 - p) * 2
    u1 = p * u1_in + (1 - p) * u1_out
    u2 = (1 - f) * u2_a + f * u2_f
    return u1 >= max(u1_in, u1_out) and u2 >= max(u2_a, u2_f)
grid = [F(k, 100) for k in range(101)]
found = {(p, f) for p in grid for f in grid if ne76_mixed(p, f)}
assert found == {(F(1), F(0))} | {(F(0), f) for f in grid if f >= F(1, 2)}
print("Tadelis 7.6: 2 strategies each; pure NE (In,A), (Out,F); all NE = (In,A) and "
      "Out with Pr(F) >= 1/2; SPE (In,A) only")


# ============================================================ Muñoz-Garcia Ch. 4 Ex. 11 (Stackelberg)
qL, qF, cL, cF, c = sp.symbols("q_L q_F c_L c_F c", real=True)
piF = (1 - qL - qF) * qF - cF * qF
brF = sp.solve(sp.diff(piF, qF), qF)[0]
assert sp.simplify(brF - ((1 - cF) / 2 - qL / 2)) == 0
assert sp.diff(piF, qF, 2) == -2
piL = sp.expand(((1 - qL - brF) - cL) * qL)
qLs = sp.solve(sp.diff(piL, qL), qL)[0]
qFs = sp.simplify(brF.subs(qL, qLs))
assert sp.simplify(qLs - (1 + cF - 2 * cL) / 2) == 0
assert sp.simplify(qFs - (1 - 3 * cF + 2 * cL) / 4) == 0
pS = sp.simplify(1 - qLs - qFs)
assert sp.simplify(pS - (1 + cF + 2 * cL) / 4) == 0
# interior iff cL > (3cF - 1)/2; qL* > 0 always on 0 < cL <= cF < 1
assert sp.simplify(sp.solve(sp.Eq(qFs, 0), cL)[0] - (3 * cF - 1) / 2) == 0
assert sp.simplify(qLs.subs(cL, cF) - (1 - cF) / 2) == 0      # qL* >= (1 - cF)/2 > 0


def leader_regime(cl, cf):
    """Exact SPE (qL, qF) with the follower's nonnegativity constraint (three regimes)."""
    if cl > (3 * cf - 1) / 2:
        return (1 + cf - 2 * cl) / 2, (1 - 3 * cf + 2 * cl) / 4
    if cl > 2 * cf - 1:
        return 1 - cf, F(0)                                       # limit output
    return (1 - cl) / 2, F(0)                                     # blockaded: monopoly


def leader_profit(ql, cl, cf):
    qf = max(F(0), (1 - cf - ql) / 2)
    return (1 - ql - qf - cl) * ql


N = 2000
for cl, cf in [(F(1, 10), F(1, 5)), (F(1, 5), F(1, 5)), (F(1, 4), F(1, 2)),
               (F(3, 10), F(7, 10)), (F(1, 10), F(7, 10)), (F(1, 2), F(3, 5))]:
    ql_star, qf_star = leader_regime(cl, cf)
    best = max((F(k, N) for k in range(N + 1)), key=lambda q: leader_profit(q, cl, cf))
    assert best == ql_star and leader_profit(best, cl, cf) > leader_profit(best + F(1, N), cl, cf)
    assert qf_star == max(F(0), (1 - cf - ql_star) / 2)
assert leader_regime(F(1, 4), F(1, 2)) == (F(1, 2), F(0))                 # limit output
assert leader_regime(F(1, 10), F(7, 10)) == (F(9, 20), F(0))             # blockaded
# symmetric costs: Stackelberg, monopoly, Cournot, Bertrand
QS = sp.simplify((qLs + qFs).subs({cL: c, cF: c}))
assert sp.simplify(qLs.subs({cL: c, cF: c}) - (1 - c) / 2) == 0
assert sp.simplify(qFs.subs({cL: c, cF: c}) - (1 - c) / 4) == 0
assert sp.simplify(QS - 3 * (1 - c) / 4) == 0
q1, q2, Q = sp.symbols("q1 q2 Q")
cour = sp.solve([sp.diff((1 - q1 - q2 - c) * q1, q1), sp.diff((1 - q1 - q2 - c) * q2, q2)], [q1, q2])
QC = sp.simplify(cour[q1] + cour[q2])
QM = sp.solve(sp.diff((1 - Q - c) * Q, Q), Q)[0]
QB = 1 - c
assert sp.simplify(QC - 2 * (1 - c) / 3) == 0 and sp.simplify(QM - (1 - c) / 2) == 0
for cc in (F(0), F(1, 5), F(1, 2), F(9, 10)):
    qs = [sp.Rational(e.subs(c, cc)) for e in (QM, QC, QS, QB)]
    assert qs[0] < qs[1] < qs[2] < qs[3]
    assert [1 - x for x in qs] == sorted([1 - x for x in qs], reverse=True)
assert [sp.simplify(1 - e) for e in (QM, QC, QS, QB)] == [
    sp.simplify(e) for e in ((1 + c) / 2, (1 + 2 * c) / 3, (1 + 3 * c) / 4, c)]
# leader's profit: Stackelberg (1-c)^2/8 > Cournot (1-c)^2/9; follower (1-c)^2/16
assert sp.simplify(((1 - QS - c) * (1 - c) / 2) - (1 - c) ** 2 / 8) == 0
assert sp.simplify(((1 - QC - c) * cour[q1]) - (1 - c) ** 2 / 9) == 0
assert sp.simplify(((1 - QS - c) * (1 - c) / 4) - (1 - c) ** 2 / 16) == 0
# the Cournot outcome is a NE of the sequential game (qF = (1-c)/3 for every qL) but not an SPE
cc = F(1, 5)
qcour = (1 - cc) / 3
assert max((F(k, 300) for k in range(301)), key=lambda q: (1 - q - qcour - cc) * q) == qcour
assert (1 - cc - F(1, 2)) / 2 != qcour                     # off-path qL = 1/2: not a best reply
print("Munoz-Garcia 4.11: BR_F = (1-cF-qL)/2; qL* = (1+cF-2cL)/2, qF* = (1-3cF+2cL)/4; both > 0 "
      "iff cL > (3cF-1)/2; Q: monopoly (1-c)/2 < Cournot 2(1-c)/3 < Stackelberg 3(1-c)/4 < "
      "Bertrand 1-c (book: same)")


# ============================================================ Tadelis 8.11 (RA selection)
U1 = {"a": 2, "b": 1, "c": 0}
U2 = {"b": 2, "a": 1, "c": 0}
def leaf(x):
    return (U1[x], U2[x])


def veto_game(pool, who=0):
    """Player `who` vetoes one candidate of pool; with two left, the other player vetoes next."""
    kids = {"v" + v: veto_game(rest, 1 - who) if len(rest) == 2 else leaf(rest[0])
            for v in pool for rest in [[x for x in pool if x != v]]}
    return (who, "".join(pool) + str(who), kids)


T811 = veto_game(["a", "b", "c"])
assert [len(strategies(T811, i)) for i in (0, 1)] == [3, 8]
bi_pay, bi_plan = backward_induction(T811)
assert bi_pay == (2, 1) and bi_plan == {"abc0": "vb", "bc1": "vc", "ac1": "vc", "ab1": "va"}
ne811 = [p for p in pure_profiles(T811, (0, 1)) if is_ne(T811, p, (0, 1))]
spe811 = [p for p in ne811 if is_spe(T811, p, (0, 1))]
assert spe811 == [bi_plan]
outcomes = sorted({play(T811, p) for p in ne811})
assert outcomes == [(1, 2), (2, 1)]
ne_b = [p for p in ne811 if play(T811, p) == (1, 2)]
# every NE with outcome b uses player 2's threat to veto a after b is vetoed (outcome c)
assert all(p["ac1"] == "va" for p in ne_b)
assert {"abc0": "vc", "bc1": "vc", "ac1": "va", "ab1": "va"} in ne_b
n_a = len([p for p in ne811 if play(T811, p) == (2, 1)])
print(f"Tadelis 8.11: SPE veto b, then (bc: veto c, ac: veto c, ab: veto a), outcome a (2,1), "
      f"unique; {len(ne811)} pure NE ({n_a} with outcome a, {len(ne_b)} with outcome b), "
      f"{len(ne811) - 1} not SPE")
# (d) player 2 may first eliminate one candidate (or none); with two left only player 1 vetoes
def p1_vetoes(pool):
    return (0, "".join(pool) + "0", {"v" + v: leaf([x for x in pool if x != v][0]) for v in pool})


T811d = (1, "email", {"none": T811, **{"e" + x: p1_vetoes([y for y in "abc" if y != x])
                                        for x in "abc"}})
pay_d, plan_d = backward_induction(T811d)
assert pay_d == (1, 2) and plan_d["email"] == "ea" and plan_d["bc0"] == "vc"
assert [backward_induction(T811d[2][k])[0] for k in ("none", "ea", "eb", "ec")] == [
    (2, 1), (1, 2), (2, 1), (2, 1)]
print("Tadelis 8.11 (d): player 2 e-mails candidate a; player 1 then vetoes c; outcome b (1,2)")


# ============================================================ Tadelis 8.7 (Debt and Repayment)
# x on the grid k/8, 0..110 (contains 0, 100, 105, 110 and points just below 105 and above 0)
X = [F(k, 8) for k in range(0, 8 * 110 + 1)]
LOAN, RET, DUE, FINE, FEE = 100, 110, 105, 5, 105


def payoffs(case, offer, x, sue):
    """(lender, debtor) payoffs. case: 'a' no courts, 'b' free courts, 'd' fee 105 paid by the
    lender, 'f' fee 105 paid by the debtor (no fine)."""
    if not offer:
        return (0, 0)
    if x >= DUE or case == "a" or not sue:
        return (x - LOAN, RET - x)
    lender = DUE - LOAN - (FEE if case == "d" else 0)
    debtor = RET - DUE - (FINE if case in "bd" else FEE)
    return (lender, debtor)


def sue_best(case, x):
    """Lender's sequentially rational choice(s) after default x < 105, as a set."""
    s, n = payoffs(case, True, x, True)[0], payoffs(case, True, x, False)[0]
    return {True} if s > n else {False} if n > s else {True, False}


def spe(case):
    """SPE (offer, x, sue rule) with the debtor's best x computed on the grid."""
    rule = {x: max(sue_best(case, x)) if case != "d" else min(sue_best(case, x))
            for x in X if x < DUE}
    xbest = max(X, key=lambda x: payoffs(case, True, x, rule.get(x, False))[1])
    offer = payoffs(case, True, xbest, rule.get(xbest, False))[0] > 0
    return offer, xbest, rule, payoffs(case, offer, xbest, rule.get(xbest, False))


assert spe("a")[:2] == (False, 0) and spe("a")[3] == (0, 0)
assert payoffs("a", True, F(0), False) == (-100, 110)
assert all(sue_best("b", x) == {True} for x in X if x < DUE)
assert spe("b")[:2] == (True, 105) and spe("b")[3] == (5, 5)
# (d): suing is strictly worse for x > 0, a tie at x = 0
assert sue_best("d", F(0)) == {True, False}
assert all(sue_best("d", x) == {False} for x in X if 0 < x < DUE)
assert spe("d")[:2] == (False, 0) and spe("d")[3] == (0, 0)
# if the lender sued at x = 0, the debtor's payoff 110 - x on (0, 105) has no maximum
assert payoffs("d", True, F(0), True)[1] == 0
assert all(payoffs("d", True, x / 2, False)[1] > payoffs("d", True, x, False)[1] > 0
           for x in X if 0 < x < DUE)                               # x/2 always beats x
assert spe("f")[:2] == (True, 105) and spe("f")[3] == (5, 5)
assert all(sue_best("f", x) == {True} for x in X if x < DUE)
assert payoffs("f", True, F(0), True) == (5, -100)


def ne(case, offer, x, rule):
    """NE test of (offer, x, rule) on the grid: lender deviates in offer (and in the sue choice
    at the on-path x), debtor deviates to any grid x'."""
    u = payoffs(case, offer, x, rule(x))
    lender_ok = all(payoffs(case, o, x, s)[0] <= u[0] for o in (True, False) for s in (True, False))
    debtor_ok = all(payoffs(case, True, y, rule(y))[1] <= payoffs(case, True, x, rule(x))[1]
                    for y in X)
    return lender_ok and (debtor_ok or not offer)


always, never = (lambda y: True), (lambda y: False)
# (c) in (b): no pure NE other than the SPE. Not lending is never a NE (offering and suing
# after any x < 105 gives the lender 5 > 0); lending forces x = 105 and a suit after every x < 105.
assert not any(ne("b", False, x, r) for x in X for r in (never, always))
assert ne("b", True, F(105), always)
assert not any(ne("b", True, x, always) for x in X if x != 105)
assert not ne("b", True, F(105), lambda y: y != F(1045, 10))   # one gap in the suit rule breaks it
# behavioural NE that is not SPE: sue with probability s after x' < 105, s >= 1 - 5/(110 - x')
s_min = lambda y: 1 - F(RET - DUE, RET - y)
assert s_min(F(104)) == F(1, 6) and s_min(F(0)) == F(21, 22)
assert all((1 - s_min(y)) * (RET - y) == RET - DUE and 0 < s_min(y) < 1 for y in X if y < DUE)
# (e) in (d): the non-credible threat to sue supports lending at x = 105, payoffs (5, 5)
assert ne("d", True, F(105), always) and payoffs("d", True, F(105), True) == (5, 5)
assert not ne("d", True, F(105), lambda y: y != F(1045, 10))
assert not any(ne("d", True, x, always) for x in X if x != 105)
assert all(ne("d", False, x, r) for x in X if x <= 100 for r in (never, always))
assert not any(ne("d", False, x, r) for x in X if x > 100 for r in (never, always))
# (f)-(g): lender gains 5 - 0, debtor 5 - 0, surplus 10 - 0
assert spe("f")[3][0] - spe("d")[3][0] == 5
assert sum(spe("f")[3]) - sum(spe("d")[3]) == RET - LOAN == 10
print("Tadelis 8.7: (a) no loan, x = 0, (0,0); (b) loan, x = 105, sue every x < 105, (5,5); "
      "(c) pure NE = SPE; (d) no loan, x = 0, never sue (tie at x = 0), (0,0); "
      "(e) NE with loan and threat to sue, (5,5), and no-loan NE with x <= 100; (f) lender pays up to 5; (g) surplus +10")

print("all D checks passed")
