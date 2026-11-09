"""Checks every number in deterrence-game.tex and deterrence-game-short.tex.

Case: Maheshri & Mastrobuoni (2021), "The race between deterrence and displacement", REStat
103(3), 547-562, read as a game (Lecture 5). Banks choose a guard g_i in {0, 1}; the robbery
probability is linear, p(g, x) = 0.07 + b1 g + b2 x + b3 g x, with x the share of the other
banks that are guarded; bank i's expected cost is p L_i + c_i g_i (euros). Pure Nash equilibria
are found by enumerating all 2^N profiles and testing every unilateral deviation, never from the
threshold formulas (those are asserted separately as cross-checks).
Run: python "Cases/the race between deterrence and displacement/deterrence-check.py"
"""
from fractions import Fraction as F
from itertools import product
import random

BASE = F(7, 100)                                              # mean robbery risk (Table 1)
B1, B2, B3 = F(-318, 10000), F(169, 10000), F(-336, 10000)    # Table 3 col. 7 = Table 4 col. 1
C = F(40000)                                                  # guard cost per year (p. 557)


def p(g, x):
    """Robbery probability of a bank with guard g facing a guarded share x of its neighbours."""
    return BASE + B1 * g + B2 * x + B3 * g * x


def delta(x):
    """Guard premium p(0, x) - p(1, x) = -b1 - b3 x (eq. 5, left-hand side)."""
    return p(0, x) - p(1, x)


def cost(i, prof, L, c):
    """Expected cost of bank i (robbery loss plus guard cost) in the profile prof."""
    x = F(sum(prof) - prof[i], len(prof) - 1)
    return p(prof[i], x) * L[i] + c[i] * prof[i]


def pure_ne(L, c):
    """All pure NE by brute force over the 2^N profiles (no unilateral deviation lowers cost)."""
    out = []
    for prof in product((0, 1), repeat=len(L)):
        if all(cost(i, prof[:i] + (1 - prof[i],) + prof[i + 1:], L, c) >= cost(i, prof, L, c)
               for i in range(len(L))):
            out.append(prof)
    return out


def total(prof, L, c):
    """Sum of all banks' expected costs."""
    return sum(cost(i, prof, L, c) for i in range(len(prof)))


def label(prof):
    """Set notation of the guarded banks, e.g. (1,1,1,0) -> {1,2,3}."""
    return "{" + ",".join(str(i + 1) for i, g in enumerate(prof) if g) + "}"


def chk(name, got, want, tol=0):
    """Assert |got - want| <= tol (tol=0: exact) and print the line."""
    ok = abs(F(got) - F(want)) <= F(tol)
    print(f"{'ok ' if ok else 'BAD'} {name}: {float(got):.6g}")
    assert ok, (name, got, want)


# 1. Calibration ----------------------------------------------------------------------------
print("== Calibration (Table 3 col. 7 = Table 4 col. 1, 500 m) ==")
D0, D1 = delta(F(0)), delta(F(1))
chk("Delta(0) = -b1", D0, F(318, 10000))
chk("Delta(1) = -(b1+b3)", D1, F(654, 10000))
chk("displaced share b2/|b1|", B2 / -B1, F(531, 1000), F(5, 10000))
chk("b2 vs -b3/2 (0.0169 vs 0.0168)", B2, -B3 / 2, F(1, 10000))
for k in range(4):
    print(f"   Delta({k}/3) = {float(delta(F(k, 3))):.5f}")

# 2. Two-bank thresholds (Prop. 3 with N = 2) -----------------------------------------------
print("== Two-bank thresholds, c = 40,000 ==")
chk("NN is a NE iff L <= c/Delta(0)", C / D0, 1257862, F(1, 2))
chk("GG is a NE iff L >= c/Delta(1)", C / D1, 611621, F(1, 2))
chk("paper p.557 (c=44,000, Table 4 col.2): c/0.0321", F(44000) / F(321, 10000), 1370717, F(1, 2))
chk("Table 4 col.2: Delta(1) = 0.0321 + 0.0343 - ... = -(b1+b3)", F(321 + 343, 10000), F(664, 10000))
chk("paper p.557 (c=44,000, Table 4 col.2): c/0.0664", F(44000) / F(664, 10000), 662651, F(1, 2))
S = -(B1 + B2 + B3)                                            # per-bank gross gain of GG vs NN
chk("social: GG beats NN iff c < S L, S", S, F(485, 10000))
chk("social cutoff L = c/S", C / S, 824742, F(1, 2))
chk("risk dominance: GG iff theta < (D0+D1)/2", (D0 + D1) / 2, F(486, 10000))
chk("risk-dominance cutoff L = 2c/(D0+D1)", 2 * C / (D0 + D1), 823045, F(1, 2))
chk("(D0+D1)/2 - S = b2 + b3/2", (D0 + D1) / 2 - S, B2 + B3 / 2)

# 3. Two-bank games: matrices, NE, mixed NE -------------------------------------------------
for Lv, mix, nn, gn, gg in [(1000000, "0.244", 70000, (78200, 86900), 61500),
                            (700000, "0.754", 49000, (66740, 60830), 55050)]:
    print(f"== Two banks, L = {Lv:,} (theta = {float(C / Lv):.4f}) ==")
    L, c = (F(Lv),) * 2, (C,) * 2
    chk("NN cost", cost(0, (0, 0), L, c), nn)
    chk("GN cost, guarded", cost(0, (1, 0), L, c), gn[0])
    chk("GN cost, unguarded", cost(1, (1, 0), L, c), gn[1])
    chk("GG cost", cost(0, (1, 1), L, c), gg)
    ne = pure_ne(L, c)
    print("   pure NE:", [label(s) for s in ne])
    assert set(ne) == {(0, 0), (1, 1)}
    q = (C / Lv - D0) / (D1 - D0)                             # opponent's Pr(G) that makes i indifferent
    chk("mixed NE Pr(G)", q, F(mix), F(5, 10000))
    ev_g = q * cost(0, (1, 1), L, c) + (1 - q) * cost(0, (1, 0), L, c)
    ev_n = q * cost(0, (0, 1), L, c) + (1 - q) * cost(0, (0, 0), L, c)
    chk("indifference G vs N (expected cost)", ev_g, ev_n)
    print(f"   social totals: NN {float(total((0, 0), L, c)):,.0f}, GG {float(total((1, 1), L, c)):,.0f}")
    print(f"   expected cost per bank in the mixed NE: {float(ev_g):,.0f}")
assert total((1, 1), (F(10**6),) * 2, (C,) * 2) < total((0, 0), (F(10**6),) * 2, (C,) * 2)
assert total((1, 1), (F(7 * 10**5),) * 2, (C,) * 2) > total((0, 0), (F(7 * 10**5),) * 2, (C,) * 2)
print("   L=1,000,000: GG is the efficient NE (too few guards possible); L=700,000: NN is (too many).")

# 4. Four banks -----------------------------------------------------------------------------
print("== Four banks, c = 40,000, theta = (0.020, 0.044, 0.050, 0.068) ==")
TH = (F(20, 1000), F(44, 1000), F(50, 1000), F(68, 1000))
L4 = tuple(C / t for t in TH)
c4 = (C,) * 4
print("   L =", [round(float(x)) for x in L4])
assert [round(float(x)) for x in L4] == [2000000, 909091, 800000, 588235]
chk("Delta(1/3)", delta(F(1, 3)), F(430, 10000))
ne4 = pure_ne(L4, c4)
print("   pure NE:", [label(s) for s in ne4])
assert set(ne4) == {(1, 0, 0, 0), (1, 1, 1, 0)}
chk("total, NE {1}", total((1, 0, 0, 0), L4, c4), 290154, 1)
chk("total, NE {1,2,3}", total((1, 1, 1, 0), L4, c4), 271510, 1)
best = min(product((0, 1), repeat=4), key=lambda s: total(s, L4, c4))
print("   social optimum:", label(best))
assert best == (1, 1, 1, 1) and best not in ne4
chk("total, all four", total(best, L4, c4), 252393, 1)
chk("total, ban (all zero)", total((0,) * 4, L4, c4), 300813, 1)
cA, cN1, cN2 = (cost(3, s, L4, c4) for s in ((1, 1, 1, 1), (1, 0, 0, 0), (1, 1, 1, 0)))
chk("bank 4 cost, all four", cA, 52647, 1)
chk("bank 4 cost, NE {1,2,3} (it fires)", cN2, 51118, 1)
chk("bank 4 cost, NE {1}", cN1, 44490, 1)
chk("bank 4 gain from firing at all four (subsidy threshold)", cA - cN2, F(15294, 10), F(1, 2))
chk("requirement vs NE {1}: total saving", total((1, 0, 0, 0), L4, c4) - total(best, L4, c4), 37762, F(1, 2))
chk("requirement vs NE {1,2,3}: total saving", total((1, 1, 1, 0), L4, c4) - total(best, L4, c4), 19118, F(1, 2))
chk("subsidy bill, 4 guards x 1,600", 4 * 1600, 6400)
chk("c = 44,000 with baseline: c/Delta(0)", F(44000) / D0, 1383648, F(1, 2))
chk("c = 44,000 with baseline: c/Delta(1)", F(44000) / D1, 672783, F(1, 2))
for s in (F(1529), F(1529, 1) + F(1, 2), F(1600)):
    print(f"   subsidy s = {float(s):,.1f}: pure NE", [label(x) for x in pure_ne(L4, (C - s,) * 4)])
assert pure_ne(L4, (C - 1600,) * 4) == [(1, 1, 1, 1)]
assert (1, 1, 1, 1) not in pure_ne(L4, (C - 1529,) * 4)
assert (1, 1, 1, 1) in pure_ne(L4, (C - F(15295, 10),) * 4)

print("== Lemma (ordering): every NE is a prefix of the sorted banks ==")
rng = random.Random(1)
for _ in range(300):
    th = sorted(F(rng.randint(10, 90), 1000) for _ in range(5))
    for prof in pure_ne(tuple(C / t for t in th), (C,) * 5):
        assert list(prof) == sorted(prof, reverse=True), (th, prof)
print("ok  300 random 5-bank markets: all pure NE are prefixes")

print("== Figure-1-style example, theta = (0.025, 0.035, 0.058, 0.060) ==")
LF = tuple(C / t for t in (F(25, 1000), F(35, 1000), F(58, 1000), F(60, 1000)))
neF = pure_ne(LF, c4)
print("   pure NE:", [label(s) for s in neF])
assert set(neF) == {(1, 1, 0, 0), (1, 1, 1, 1)}
print("   social optimum:", label(min(product((0, 1), repeat=4), key=lambda s: total(s, LF, c4))))

# 5. Repeated game (Lecture 5) --------------------------------------------------------------
print("== Repeated game, four-bank example ==")
# Two periods, undiscounted sum (same cutoff as the (1-d)-normalised form). t=1 all four; t=2 NE
# {1} after compliance, NE {1,2,3} after any deviation. Bank 4 complies iff
# cA + d*cN1 <= cN2 + d*cN2.
d_star = (cA - cN2) / (cN2 - cN1)
chk("delta* = 1,529/6,628", d_star, F(1529, 6628), F(1, 10**4))
chk("delta* decimal", d_star, F(2307, 10000), F(1, 10**4))
print(f"   bank 4 stage costs: all four {float(cA):,.0f}, NE {{1,2,3}} {float(cN2):,.0f}, NE {{1}} {float(cN1):,.0f}")
assert cN1 < cA and cN2 < cA          # Nash reversion cannot sustain all four forever
for d in (F(1, 10), F(1, 2), F(99, 100)):
    for v in (cN1, cN2):              # infinite horizon: deviate once, then revert to a stage NE
        assert (1 - d) * cN2 + d * v < cA
print("   both stage NE cost bank 4 less than all four: Nash reversion cannot sustain it forever")
for i in range(3):                    # banks 1-3 at t=1 under the same two-period strategies
    dev = (1, 1, 1, 1)[:i] + (0,) + (1, 1, 1, 1)[i + 1:]
    now = cost(i, dev, L4, c4) - cost(i, (1, 1, 1, 1), L4, c4)
    later = cost(i, (1, 1, 1, 0), L4, c4) - cost(i, (1, 0, 0, 0), L4, c4)
    print(f"   bank {i + 1}: t=1 cost rise from firing {float(now):+,.0f}, t=2 change {float(later):+,.0f}")
    assert now + later > 0            # holds for every delta in [0, 1]
print("all checks passed")
