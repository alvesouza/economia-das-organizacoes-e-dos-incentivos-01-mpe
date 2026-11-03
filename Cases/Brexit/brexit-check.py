"""Checks every number in Cases/Brexit/brexit-game.tex (the Brexit negotiation as a game).

Costs in GBP bn (payoff = -cost). UK chooses Prepare/Not, the EU offers a Favourable,
Neutral or Unfavourable soft deal, the UK presents it to Parliament or rejects it, and
Parliament (Nature) passes a presented deal with probability p; a failed vote or an outright
rejection means hard Brexit, and rejection adds the political cost r to the UK.
Run: python Cases/Brexit/brexit-check.py
"""
from fractions import Fraction as F
from itertools import product

HARD_UK, HARD_EU = F(35), F(18)
PREP, MITIGATION = F(5), F(25, 2)  # all-or-nothing preparation, 2.5 saved per pound spent
DEALS = {"F": (F(19), F(13)), "Nt": (F(23), F(9)), "U": (F(27), F(5))}  # (UK cost, EU cost)
P_PASS = F(4, 5)
OFFERS = list(DEALS)


def leaf(prep, deal, event, r=F(0), k=F(0)):
    """Payoffs (UK, EU) at a terminal node.

    prep: "P" or "N"; deal: key of DEALS; event: "pass", "fail" or "reject".
    r: UK political cost of rejecting outright; k: EU deterrence premium, added to the EU's
    cost when a favourable deal is implemented.
    """
    sunk = PREP if prep == "P" else F(0)
    if event == "pass":
        uk, eu = DEALS[deal]
        return (-(uk + sunk), -(eu + (k if deal == "F" else 0)))
    hard_uk = HARD_UK - (MITIGATION if prep == "P" else 0) + sunk
    return (-(hard_uk + (r if event == "reject" else 0)), -HARD_EU)


def tree(r=F(0), p=None, k=F(0)):
    """Extensive form as nested tuples.

    Decision node: ("D", player, label, {action: child}); chance: ("C", label, [(prob, child)]);
    terminal: ("T", (uk, eu)). p maps a deal to its pass probability (default 0.8 for all).
    """
    p = p or {d: P_PASS for d in OFFERS}

    def uk_node(prep, d):
        nature = ("C", f"Nature|{prep},{d}", [(p[d], ("T", leaf(prep, d, "pass", r, k))),
                                               (1 - p[d], ("T", leaf(prep, d, "fail", r, k)))])
        return ("D", 0, f"UK|{prep},{d}",
                {"present": nature, "reject": ("T", leaf(prep, d, "reject", r, k))})

    eu = {prep: ("D", 1, f"EU|{prep}", {d: uk_node(prep, d) for d in OFFERS}) for prep in "PN"}
    return ("D", 0, "UK|root", {"P": eu["P"], "N": eu["N"]})


def backward_induction(node):
    """Zermelo's algorithm. Returns (value, strategy {label: action}); asserts no ties."""
    kind = node[0]
    if kind == "T":
        return node[1], {}
    if kind == "C":
        strat, val = {}, [F(0), F(0)]
        for prob, child in node[2]:
            v, s = backward_induction(child)
            strat.update(s)
            val = [val[i] + prob * v[i] for i in range(2)]
        return tuple(val), strat
    _, player, label, children = node
    strat, vals = {}, {}
    for a, child in children.items():
        vals[a], s = backward_induction(child)
        strat.update(s)
    best = max(v[player] for v in vals.values())
    argmax = [a for a, v in vals.items() if v[player] == best]
    assert len(argmax) == 1, f"tie at {label}: {argmax}"
    strat[label] = argmax[0]
    return vals[argmax[0]], strat


def evaluate(node, profile):
    """Expected payoffs when every player follows the pure strategy profile {label: action}."""
    kind = node[0]
    if kind == "T":
        return node[1]
    if kind == "C":
        out = [F(0), F(0)]
        for prob, child in node[2]:
            v = evaluate(child, profile)
            out = [out[i] + prob * v[i] for i in range(2)]
        return tuple(out)
    return evaluate(node[3][profile[node[2]]], profile)


def show(x):
    return f"{float(x):.4g}"


# ---------------------------------------------------------------- (iv) leaf payoffs
expected_leaves = {
    ("N", "F", "pass"): (-19, -13), ("N", "Nt", "pass"): (-23, -9), ("N", "U", "pass"): (-27, -5),
    ("P", "F", "pass"): (-24, -13), ("P", "Nt", "pass"): (-28, -9), ("P", "U", "pass"): (-32, -5),
}
for (prep, d, ev), val in expected_leaves.items():
    assert leaf(prep, d, ev) == val
for d in OFFERS:
    assert leaf("N", d, "fail") == leaf("N", d, "reject") == (-35, -18)
    assert leaf("P", d, "fail") == leaf("P", d, "reject") == (F(-55, 2), -18)
    assert leaf("N", d, "reject", r=F(2)) == (-37, -18)
assert HARD_UK - MITIGATION == F(45, 2)  # 22.5 hard-Brexit cost to a prepared UK, before the 5
print("(iv) leaves, prepared hard Brexit UK cost:", show(HARD_UK - MITIGATION + PREP))
# Every soft deal splits the same joint cost: the deal type is a pure transfer.
assert {sum(v) for v in DEALS.values()} == {32}
assert HARD_UK + HARD_EU == 53 and HARD_UK - MITIGATION + HARD_EU == F(81, 2)

# ---------------------------------------------------------------- (vi) step by step, r = 0
p = P_PASS


def present_cost(prep, d, pp=p):
    """UK expected cost of presenting deal d (Parliament passes with prob. pp)."""
    return -(pp * leaf(prep, d, "pass")[0] + (1 - pp) * leaf(prep, d, "fail")[0])


def eu_cost_if_presented(d, pp=p, k=F(0)):
    return -pp * leaf("N", d, "pass", k=k)[1] + (1 - pp) * HARD_EU


assert [present_cost("N", d) for d in OFFERS] == [F(111, 5), F(127, 5), F(143, 5)]  # 22.2 25.4 28.6
assert [present_cost("P", d) for d in OFFERS] == [F(247, 10), F(279, 10), F(311, 10)]  # 24.7 27.9 31.1
assert [eu_cost_if_presented(d) for d in OFFERS] == [14, F(54, 5), F(38, 5)]  # 14 10.8 7.6
print("step 1, UK present cost after N:", [show(present_cost("N", d)) for d in OFFERS], "reject 35")
print("step 1, UK present cost after P:", [show(present_cost("P", d)) for d in OFFERS], "reject 27.5")
print("step 2, EU cost if presented:", [show(eu_cost_if_presented(d)) for d in OFFERS], "rejected 18")

# Present/reject rule after P: p c + (1-p) 22.5 + 5 <= 27.5 + r  <=>  c <= 22.5 + r/p
for r in [F(0), F(1, 5), F(2, 5), F(1), F(18, 5), F(4), F(10)]:
    for pp in [F(1, 2), F(3, 5), F(4, 5), F(9, 10), F(1)]:
        for c in [F(19), F(45, 2), F(23), F(27)]:
            lhs = PREP + pp * c + (1 - pp) * (HARD_UK - MITIGATION)
            assert (lhs <= HARD_UK - MITIGATION + PREP + r) == (c <= F(45, 2) + r / pp)
        # after N the UK presents every listed deal: p c + (1-p) 35 <= 35 + r  <=>  c <= 35 + r/p
        assert all(pp * c + (1 - pp) * HARD_UK <= HARD_UK + r for c, _ in DEALS.values())

# Programmatic backward induction at r = 0
val, spe = backward_induction(tree())
assert spe == {
    "UK|root": "P", "EU|P": "F", "EU|N": "U",
    "UK|P,F": "present", "UK|P,Nt": "reject", "UK|P,U": "reject",
    "UK|N,F": "present", "UK|N,Nt": "present", "UK|N,U": "present",
}, spe
assert val == (F(-247, 10), -14)
val_N, _ = backward_induction(tree()[3]["N"])
assert val_N == (F(-143, 5), F(-38, 5))
print("SPE (r=0):", spe)
print("SPE payoffs (UK, EU):", show(val[0]), show(val[1]), "; after N:", show(val_N[0]), show(val_N[1]))
assert -val_N[0] - (-val[0]) == F(39, 10)  # UK gains 3.9 by preparing
assert -val[1] - (-val_N[1]) == F(32, 5)  # EU loses 6.4

# ---------------------------------------------------------------- non-SPE Nash equilibria
uk_labels = ["UK|root"] + [f"UK|{a},{d}" for a in "PN" for d in OFFERS]
eu_labels = ["EU|P", "EU|N"]
G = tree()
uk_strats = [dict(zip(uk_labels, s)) for s in
             product("PN", *[["present", "reject"]] * 6)]
eu_strats = [dict(zip(eu_labels, s)) for s in product(OFFERS, OFFERS)]
pay = {(i, j): evaluate(G, {**u, **e}) for i, u in enumerate(uk_strats) for j, e in enumerate(eu_strats)}
best_uk = {j: max(pay[i, j][0] for i in range(len(uk_strats))) for j in range(len(eu_strats))}
best_eu = {i: max(pay[i, j][1] for j in range(len(eu_strats))) for i in range(len(uk_strats))}
ne = [(i, j) for (i, j), v in pay.items() if v[0] == best_uk[j] and v[1] == best_eu[i]]
ne_spe = [(i, j) for i, j in ne if {**uk_strats[i], **eu_strats[j]} == spe]
outcomes = sorted({(show(pay[n][0]), show(pay[n][1])) for n in ne})
assert len(uk_strats) == 128 and len(eu_strats) == 9 and len(ne_spe) == 1
print(f"pure NE of the 128x9 normal form: {len(ne)}; subgame perfect: {len(ne_spe)}")
print("NE payoff pairs:", outcomes)
threat = {"UK|root": "N", "UK|N,F": "present", "UK|N,Nt": "reject", "UK|N,U": "reject",
          "UK|P,F": "present", "UK|P,Nt": "reject", "UK|P,U": "reject"}
threat_eu = {"EU|P": "F", "EU|N": "F"}
idx = (uk_strats.index(threat), eu_strats.index(threat_eu))
assert idx in ne and pay[idx] == (F(-111, 5), -14)  # (-22.2, -14): N, F offered, presented
assert present_cost("N", "U") < HARD_UK  # 28.6 < 35: the threat to reject U after N is not credible
assert F(247, 10) - F(111, 5) == PREP - (1 - p) * MITIGATION == F(5, 2)  # UK's price of credibility
print("non-credible-threat NE (N; reject Nt,U after N; EU offers F):", show(pay[idx][0]), show(pay[idx][1]))

# ---------------------------------------------------------------- sensitivity: r regimes
assert F(23) <= F(45, 2) + F(2, 5) / p and F(27) <= F(45, 2) + F(18, 5) / p
assert (F(23) - F(45, 2)) * p == F(2, 5) and (F(27) - F(45, 2)) * p == F(18, 5)
regimes = {F(0): ("P", "F", F(-247, 10)), F(1, 5): ("P", "F", F(-247, 10)),
           F(1): ("P", "Nt", F(-279, 10)), F(3): ("P", "Nt", F(-279, 10)),
           F(4): ("N", "U", F(-143, 5)), F(10): ("N", "U", F(-143, 5))}
for r, (a, d, uk) in regimes.items():
    v, s = backward_induction(tree(r=r))
    assert (s["UK|root"], s[f"EU|{s['UK|root']}"], v[0]) == (a, d, uk), (r, s, v)
print("r regimes: r<0.4 -> (P,F) UK -24.7; 0.4<r<3.6 -> (P,Nt) UK -27.9; r>3.6 -> (N,U) UK -28.6")
assert backward_induction(tree(r=F(1)))[0][1] == F(-54, 5)  # EU -10.8 in the middle regime
assert F(143, 5) - F(279, 10) == F(7, 10)  # middle regime: preparing gains the UK only 0.7

# EU unsure about r after observing P: q = Pr(r >= 0.4), q2 = Pr(r >= 3.6)
q, q2 = F(5, 9), F(5, 13)
assert q * F(54, 5) + (1 - q) * HARD_EU == 14 and q2 * F(38, 5) + (1 - q2) * HARD_EU == 14
print("EU under uncertainty about r: Nt beats F iff Pr(r>=0.4) > 5/9; U beats F iff Pr(r>=3.6) > 5/13")
# Negative r (walking away is rewarded): an unprepared UK rejects U iff r < -6.4
assert present_cost("N", "U") - HARD_UK == F(-32, 5)
for r, act in [(F(-7), "reject"), (F(-6), "present")]:
    assert backward_induction(tree(r=r)[3]["N"][3]["U"])[1]["UK|N,U"] == act
print("r < 0: unprepared UK rejects U iff r < -6.4")

# ---------------------------------------------------------------- sensitivity: general p
def uk_cost_spe(pp, r=F(0)):
    v, s = backward_induction(tree(r=r, p={d: pp for d in OFFERS}))
    return -v[0], s


for pp in [F(1, 10), F(1, 2), F(3, 5), F(4, 5), F(9, 10), F(1)]:
    gain = (pp * 27 + (1 - pp) * 35) - (PREP + pp * 19 + (1 - pp) * F(45, 2))
    assert gain == 3 * pp + F(15, 2) * (1 - pp) == F(15, 2) - F(9, 2) * pp > 0
    if pp < 1:
        c, s = uk_cost_spe(pp)
        assert s["UK|root"] == "P" and s["EU|P"] == "F" and s["EU|N"] == "U"
        assert c == PREP + pp * 19 + (1 - pp) * F(45, 2)
assert F(15, 2) - F(9, 2) * F(4, 5) == F(39, 10)
# thresholds for general p: Nt presented after P iff r >= p/2, U iff r >= 9p/2
# middle regime: prepare iff 27.5 + p/2 < 35 - 8p iff p < 15/17; high regime iff p < 3/5
for pp in [F(1, 2), F(7, 10), F(4, 5), F(9, 10)]:
    _, s = uk_cost_spe(pp, r=pp)  # middle regime: p/2 < r = p < 9p/2
    assert (s["UK|root"] == "P") == (pp < F(15, 17)), pp
    _, s = uk_cost_spe(pp, r=5 * pp)  # high regime
    assert (s["UK|root"] == "P") == (pp < F(3, 5)), pp
print("general p: gain from preparing (r=0) = 3p + 7.5(1-p) = 7.5 - 4.5p; at p=0.8:", show(F(39, 10)))
print("general p: middle regime prepares iff p < 15/17; high regime iff p < 3/5")

# ---------------------------------------------------------------- deterrence premium k
for k in [F(0), F(4), F(5) - F(1, 100), F(5) + F(1, 100), F(6)]:
    assert (eu_cost_if_presented("F", k=k) <= HARD_EU) == (k <= 5)
for k, offer_after_P in [(F(0), "F"), (F(4), "F")]:
    _, s = backward_induction(tree(k=k))
    assert s["EU|P"] == offer_after_P and s["UK|root"] == "P"
G6 = tree(k=F(6))  # k > 5: EU indifferent between Nt and U (both rejected); fix Nt, check payoffs
for d in ["Nt", "U"]:
    prof = {**spe, "EU|P": d}
    assert evaluate(G6, prof) == (F(-55, 2), -18)
assert eu_cost_if_presented("F", k=F(6)) == F(76, 5) + F(18, 5) == F(94, 5)  # 18.8 > 18
assert F(-55, 2) > F(-143, 5)  # UK still prepares: -27.5 > -28.6
# variant: premium paid when F is offered (not when implemented): 14 + k <= 18 iff k <= 4
assert all((14 + k <= 18) == (k <= 4) for k in [F(3), F(4), F(5)])
print("k: F offered after P iff 0.8(13+k)+3.6 <= 18 iff k <= 5; k>5 -> hard Brexit, UK -27.5, EU -18")

# ---------------------------------------------------------------- deal-specific pass probabilities
pd = {"F": F(9, 10), "Nt": F(4, 5), "U": F(1, 2)}
assert [pd[d] * (HARD_EU - DEALS[d][1]) for d in OFFERS] == [F(9, 2), F(36, 5), F(13, 2)]
v, s = backward_induction(tree(p=pd))
assert s["EU|N"] == "Nt" and s["EU|P"] == "F" and s["UK|root"] == "P"
assert v == (F(-487, 20), F(-27, 2))  # UK -24.35, EU -13.5
assert backward_induction(tree(p=pd)[3]["N"])[0] == (F(-127, 5), F(-54, 5))  # UK -25.4, EU -10.8
assert F(127, 5) - F(487, 20) == F(21, 20)  # UK gain from preparing falls to 1.05
print("p by deal (0.9, 0.8, 0.5): EU offers Nt after N, F after P; UK prepares; UK -24.35, EU -13.5")

# ---------------------------------------------------------------- unobservable preparation
# Reduced 2x3 normal form after the UK's optimal present/reject choices (UK knows its own move).
red = {}
for a in "PN":
    for d in OFFERS:
        sub = tree()[3][a][3][d]
        red[a, d] = backward_induction(sub)[0]
assert red["N", "F"] == (F(-111, 5), -14) and red["N", "Nt"] == (F(-127, 5), F(-54, 5))
assert red["N", "U"] == (F(-143, 5), F(-38, 5)) and red["P", "F"] == (F(-247, 10), -14)
assert red["P", "Nt"] == red["P", "U"] == (F(-55, 2), -18)
pure = [(a, d) for a in "PN" for d in OFFERS
        if red[a, d][0] == max(red[b, d][0] for b in "PN")
        and red[a, d][1] == max(red[a, e][1] for e in OFFERS)]
assert pure == []
# Mixed: sigma = Pr(P), tau = Pr(F), 1 - tau = Pr(U). EU indifferent F vs U; UK indifferent P vs N.
sigma = (red["N", "U"][1] - red["N", "F"][1]) / (
    (red["N", "U"][1] - red["N", "F"][1]) + (red["P", "F"][1] - red["P", "U"][1]))
dP = red["P", "U"][0] - red["N", "U"][0]  # UK gain from P when EU plays U: 1.1
dN = red["N", "F"][0] - red["P", "F"][0]  # UK gain from N when EU plays F: 2.5
tau = dP / (dP + dN)
assert sigma == F(8, 13) and tau == F(11, 36)


def eu_pay(d, s):
    return s * red["P", d][1] + (1 - s) * red["N", d][1]


def uk_pay(a, t):
    return t * red[a, "F"][0] + (1 - t) * red[a, "U"][0]


assert eu_pay("F", sigma) == eu_pay("U", sigma) == -14 and eu_pay("Nt", sigma) == F(-198, 13)
assert uk_pay("P", tau) == uk_pay("N", tau) == F(-1199, 45)
# Nt is weakly dominated by U and strictly worse at any sigma < 1: no equilibrium uses it.
assert red["P", "Nt"][1] <= red["P", "U"][1] and red["N", "Nt"][1] < red["N", "U"][1]
# Any equilibrium mixes both UK actions (no pure NE); EU support must then be {F, U}.
uk_mixed = uk_pay("P", tau)
p_breakdown = sigma * (1 - tau)  # prepared UK meets U and rejects
p_hard = p_breakdown + (1 - p_breakdown) * (1 - p)
assert p_breakdown == F(50, 117) and p_hard == F(317, 585)
assert -uk_mixed - F(247, 10) == F(35, 18)  # value of observability to the UK
print(f"unobservable: no pure NE; sigma=Pr(P)={sigma}, tau=Pr(F)={tau}; "
      f"UK {show(uk_mixed)}, EU -14; Pr(reject)={show(p_breakdown)}, Pr(hard)={show(p_hard)}")

# ---------------------------------------------------------------- efficiency
joint = {"(P,F)": F(247, 10) + 14, "(N,U)": F(143, 5) + F(38, 5),
         "(P,Nt)": F(279, 10) + F(54, 5), "k>5": F(55, 2) + 18, "mixed": -uk_mixed + 14}
assert joint["(P,F)"] == F(387, 10) and joint["(N,U)"] == F(181, 5)
assert joint["(P,F)"] - joint["(N,U)"] == PREP - (1 - p) * MITIGATION == F(5, 2)
assert joint["(P,Nt)"] == F(387, 10) and joint["k>5"] == F(91, 2) and joint["mixed"] == F(1829, 45)
assert ((1 - F(3, 5)) * MITIGATION == PREP)  # preparation is efficient iff p <= 0.6
print("joint costs:", {k_: show(v_) for k_, v_ in joint.items()})
# Coasean bargain on the frontier c + e = 32: deal that makes an unprepared UK as well off as (P,F)
c_star = (F(247, 10) - (1 - p) * HARD_UK) / p
assert c_star == F(177, 8) and p * (32 - c_star) + (1 - p) * HARD_EU == F(23, 2)
print("frontier deal c* =", show(c_star), "-> UK -24.7, EU -11.5 without preparation")
# share of the deal surplus (53 - 32 = 21) each deal gives the UK, for the ultimatum comparison
assert [(HARD_UK - c) / 21 for c, _ in DEALS.values()] == [F(16, 21), F(12, 21), F(8, 21)]
print("UK share of the 21bn deal surplus: F 76%, Nt 57%, U 38%")
print("all checks passed")
