"""Checks every number in housewives-game.tex and housewives-game-short.tex (Gorges 2021, "Of
housewives and feminists", Labour Economics 72, 102044, read as a Lecture 3 game-theory case).

Players: woman (W) and man (M); actions Career (C) or Family (F) (A/B in the Neutral frame).
Table 1 (p. 3): the player choosing Career against a Family partner gets alpha = 200 ECU, the
Family player gets beta = 100 ECU, mis-coordination pays 0. Row = woman, column = man.
Paper inputs (Table 4 col. 1, Table C1, Table 3 col. 2, Sec. 5.2) are typed in as Fractions;
everything marked "ours" in the documents (independence rates, own-payoff puzzle, signal value,
Fehr-Schmidt cut-offs, sequential game) is derived here, not taken from the paper.
Run: python "Cases/Housewive and feminists/housewives-check.py"
"""
from fractions import Fraction as F
from itertools import product

ALPHA, BETA = F(200), F(100)


def pay(w, m):
    """Payoffs (woman, man) when the woman plays w and the man plays m, each 'C' or 'F'."""
    if w == m:
        return (F(0), F(0))
    return (ALPHA, BETA) if w == "C" else (BETA, ALPHA)


def u_career(q, n=F(0)):
    """Expected payoff of Career against an opponent who plays Career with probability q.

    n is accepted for symmetry with u_family and is unused: Career carries no identity utility.
    """
    return (1 - q) * ALPHA


def u_family(q, n=F(0)):
    """Expected payoff of Family against an opponent playing Career with probability q.

    n is a lump-sum identity utility for choosing Family (our own-payoff puzzle; n = 0 is the paper).
    """
    return q * BETA + n


def show(x, d=4):
    return f"{float(x):.{d}g}"


# ---------------------------------------------------------------- (2)-(3) game, pure and mixed NE
pure_ne = [(w, m) for w, m in product("CF", repeat=2)
           if pay(w, m)[0] >= max(pay(x, m)[0] for x in "CF")
           and pay(w, m)[1] >= max(pay(w, x)[1] for x in "CF")]
assert pure_ne == [("C", "F"), ("F", "C")]
print("pure NE (woman, man):", pure_ne, "payoffs", [tuple(map(int, pay(*s))) for s in pure_ne])

# Indifference: Career pays (1-q) alpha, Family pays q beta; equal iff q = alpha / (alpha + beta).
q_star = ALPHA / (ALPHA + BETA)
assert q_star == F(2, 3) and u_career(q_star) == u_family(q_star) == F(200, 3)
assert u_career(F(1, 2)) == 100 and u_family(F(1, 2)) == 50  # Career is the best response iff q < 2/3
assert all((u_career(q) > u_family(q)) == (q < F(2, 3)) for q in [F(k, 12) for k in range(13)])
# Symmetric game: the man's indifference gives the woman's p = 2/3 in the same way.
p_star = q_star
EU = ALPHA * BETA / (ALPHA + BETA)
assert EU == F(200, 3)
cells = {(w, m): (p_star if w == "C" else 1 - p_star) * (q_star if m == "C" else 1 - q_star)
         for w, m in product("CF", repeat=2)}
assert sum(cells.values()) == 1
assert cells[("C", "F")] == cells[("F", "C")] == F(2, 9)  # progressive, traditional
assert cells[("C", "C")] == F(4, 9) and cells[("F", "F")] == F(1, 9)
coord = cells[("C", "F")] + cells[("F", "C")]
assert coord == F(4, 9) and 1 - coord == F(5, 9)
assert sum(cells[s] * pay(*s)[0] for s in cells) == EU  # expected payoff recovered from the outcomes
assert 2 * EU == F(400, 3)
print(f"mixed NE: Pr(C) = {p_star} each, EU = {EU} = {show(EU, 4)}; cells {({''.join(k): str(v) for k, v in cells.items()})};"
      f" coordination {coord} = {show(coord)}")
print(f"total payoff: pure NE {sum(pay('C', 'F'))}, mixed NE {2 * EU} = {show(2 * EU, 4)}")
assert sum(pay("C", "F")) == 300 and EU / BETA == F(2, 3)  # mixed NE gives 2/3 of the Family payoff

# ---------------------------------------------------------------- (5) data
men_neutral, women_neutral = F("0.536"), F("0.563")  # Table 4 col. 1: intercept, + Female
men_norm, women_norm = F("0.625"), F("0.250")
assert men_neutral + F("0.027") == women_neutral  # 0.536 + 0.027
assert men_neutral + F("0.089") == men_norm  # + Norm
assert men_neutral + F("0.089") + F("0.027") + F("-0.402") == women_norm  # + Norm x Female
assert women_neutral - women_norm == F("0.313") and women_norm / women_neutral < F(1, 2)  # "falls by more than half"
assert men_norm - men_neutral == F("0.089")
print("Table 4 col. 1 Career rates: men Neutral", men_neutral, "women Neutral", women_neutral,
      "men Norm", men_norm, "women Norm", women_norm)


def independence(p, q):
    """Outcome rates if the woman plays Career w.p. p and the man w.p. q, independently (ours).

    Returns (progressive = W Career & M Family, traditional = W Family & M Career, coordination).
    """
    prog, trad = p * (1 - q), (1 - p) * q
    return prog, trad, prog + trad


for name, (p, q) in {"Neutral": (women_neutral, men_neutral), "Norm": (women_norm, men_norm)}.items():
    prog, trad, co = independence(p, q)
    print(f"independence, {name}: progressive {show(prog)}, traditional {show(trad)}, coordination {show(co)}")
pn, tn, cn = independence(women_neutral, men_neutral)
pm, tm, cm = independence(women_norm, men_norm)
assert (round(float(pn), 3), round(float(tn), 3), round(float(cn), 3)) == (0.261, 0.234, 0.495)
assert (pm, tm, cm) == (F(3, 32), F(15, 32), F(9, 16))  # 0.09375, 0.46875, 0.5625
assert float(cn) > float(coord) and cm - cn > 0  # both above 4/9; Norm above Neutral under independence

# Expected earnings under independence (man earns ALPHA in the traditional cell, BETA in progressive).
exp_men_norm, exp_women_norm = tm * ALPHA + pm * BETA, tm * BETA + pm * ALPHA
assert exp_men_norm == F(825, 8) and exp_women_norm == F(525, 8)  # 103.125, 65.625
exp_men_neu, exp_women_neu = tn * ALPHA + pn * BETA, tn * BETA + pn * ALPHA
print(f"expected earnings under independence: Norm men {show(exp_men_norm, 4)}, women {show(exp_women_norm, 3)};"
      f" Neutral men {show(exp_men_neu, 3)}, women {show(exp_women_neu, 3)}")
assert (round(float(exp_men_neu), 1), round(float(exp_women_neu), 1)) == (73.0, 75.7)

# Table C1 means (ECU per subject and game).
C1 = {("Norm", "men"): F("112.50"), ("Norm", "women"): F("75.00"),
      ("Neutral", "men"): F("80.36"), ("Neutral", "women"): F("83.04")}
assert C1["Norm", "women"] / C1["Norm", "men"] == F(2, 3)  # "women earn 67% of men"
assert round(float(C1["Neutral", "men"] / C1["Norm", "men"]), 2) == 0.71  # "around 70%"
assert round(float(C1["Neutral", "women"] / C1["Norm", "men"]), 2) == 0.74
tot_norm = C1["Norm", "men"] + C1["Norm", "women"]
tot_neu = C1["Neutral", "men"] + C1["Neutral", "women"]
assert tot_norm == F("187.50") and tot_neu == F("163.40") and tot_norm - tot_neu == F("24.10")
# Each coordinated pair pays 300 in total and each miscoordinated pair 0, so total/300 is the
# coordination rate implied by Table C1 (ours).
co_norm, co_neu = tot_norm / 300, tot_neu / 300
assert co_norm == F(5, 8) and round(float(co_neu), 4) == 0.5447
assert round(float(co_norm - co_neu), 4) == 0.0803  # versus the AME of -0.085 on non-coordination
assert co_norm > cm and co_neu > cn  # observed coordination beats independence in both frames
assert C1["Norm", "men"] - C1["Norm", "women"] == F("37.50")
assert C1["Neutral", "women"] - C1["Neutral", "men"] == F("2.68")
assert C1["Norm", "men"] - C1["Neutral", "men"] == F("32.14")
assert C1["Neutral", "women"] - C1["Norm", "women"] == F("8.04")
assert C1["Norm", "women"] - exp_women_norm == F(75) - F(525, 8) == F(75, 8)  # 9.375
assert C1["Norm", "men"] - exp_men_norm == F(75, 8)  # same gap for men
assert round(float(C1["Neutral", "men"] - exp_men_neu), 1) == round(float(C1["Neutral", "women"] - exp_women_neu), 1) == 7.4
print(f"Table C1: totals Norm {float(tot_norm)}, Neutral {float(tot_neu)}; implied coordination Norm {show(co_norm)},"
      f" Neutral {show(co_neu, 4)}; Norm gap {float(C1['Norm', 'men'] - C1['Norm', 'women'])}")
ame = {"progressive": F("-0.171"), "traditional": F("0.255"), "not coordinated": F("-0.085")}
assert sum(ame.values()) == F("-0.001")  # rounding: the three AMEs sum to zero up to rounding
print("Table 3 col. 2 AMEs:", {k: float(v) for k, v in ame.items()})

# Best responses against the actual rates (Norm).
assert u_career(men_norm) == F(75) and u_family(men_norm) == F("62.5")  # woman vs men's 0.625
assert u_career(women_norm) == F(150) and u_family(women_norm) == F(25)
assert u_career(men_neutral) == F("92.8") and u_family(men_neutral) == F("53.6")  # woman, Neutral
assert u_career(women_neutral) == F("87.4") and u_family(women_neutral) == F("56.3")  # man, Neutral
# Women's own mix against the men's real 0.625, if independent: p*75 + (1-p)*62.5 at p = 0.25.
assert women_norm * F(75) + (1 - women_norm) * F("62.5") == exp_women_norm  # 65.625
print("BR woman in Norm vs men 0.625: Career", u_career(men_norm), "Family", float(u_family(men_norm)),
      "; man vs women 0.25: Career", u_career(women_norm), "Family", u_family(women_norm))
print("Neutral: woman vs 0.536 Career", show(u_career(men_neutral)), "Family", show(u_family(men_neutral)),
      "; man vs 0.563 Career", show(u_career(women_neutral)), "Family", show(u_family(women_neutral)))
# Beliefs: any belief q > 2/3 about the man makes Family the woman's best response (fn. 27 overshoot).
assert u_family(F("0.7")) > u_career(F("0.7")) and u_career(F("0.65")) > u_family(F("0.65"))
assert q_star - men_norm == F(1, 24)  # the men's real rate is only 1/24 below the indifference point

# ---------------------------------------------------------------- (6) own-payoff puzzle (ours)
for n in [F(0), F(50), F(100), F(150)]:
    # Woman's indifference 200 (1-q) = 100 q + n fixes the MAN's mix; the man's indifference
    # (no identity utility for him) leaves the WOMAN's mix at 2/3.
    q_n = (ALPHA - n) / (ALPHA + BETA)
    assert u_career(q_n) == u_family(q_n, n) and q_n == (200 - n) / 300
    assert (u_career(F(1, 2)) > u_family(F(1, 2), n)) == (F(1, 2) < q_n)
assert [(ALPHA - n) / 300 for n in (0, 50, 100, 150)] == [F(2, 3), F(1, 2), F(1, 3), F(1, 6)]
# n >= alpha: Family is strictly dominant for the woman (0 < n), unique NE (F, C).
assert all(u_family(q, F(200)) >= u_career(q) for q in [F(k, 10) for k in range(11)])
# Woman's expected payoff in the identity-utility mixed NE (she is indifferent): 100 q_n + n.
assert u_family(F(1, 2), F(50)) == F(100)
print("own-payoff puzzle: Pr_man(C) = (200 - n)/300 =", [str((ALPHA - n) / 300) for n in (0, 50, 100, 150)],
      "for n = 0, 50, 100, 150; Pr_woman(C) stays 2/3")

# ---------------------------------------------------------------- (7) signalling value (ours)
belief = F("0.33")
c_belief, f_belief = u_career(belief), u_family(belief)
assert c_belief == F(134) and f_belief == F(33) and c_belief - f_belief == F(101)
assert u_career(women_norm) - u_family(women_norm) == F(125)  # at the women's actual rate 0.25
print(f"man in Norm, partner Career belief 0.33: Career {c_belief}, Family {f_belief}, "
      f"signal must be worth > {c_belief - f_belief} ECU (= EUR 1.01); at 0.25: 125")
assert round(float(F("0.54") - F("0.33")), 2) == 0.21 and round(float(F("0.78") - F("0.33")), 2) == 0.45
assert round(float(F("0.78") / F("0.33")), 1) == 2.4  # "more than twice as high"

# ---------------------------------------------------------------- (8) sequential BoS (ours)
# Woman moves first and the man sees her action; man's strategy = (action after C, action after F).
man_strats = list(product("CF", repeat=2))


def seq_pay(w, ms):
    """Payoffs when the woman plays w and the man plays the contingent plan ms = (after C, after F)."""
    return pay(w, ms[0] if w == "C" else ms[1])


ne_seq = [(w, ms) for w in "CF" for ms in man_strats
          if seq_pay(w, ms)[0] >= max(seq_pay(x, ms)[0] for x in "CF")
          and seq_pay(w, ms)[1] >= max(seq_pay(w, mm)[1] for mm in man_strats)]
best_after = {w: max("CF", key=lambda m: pay(w, m)[1]) for w in "CF"}  # backward induction, man
spe_w = max("CF", key=lambda w: pay(w, best_after[w])[0])
assert best_after == {"C": "F", "F": "C"} and spe_w == "C"
spe = (spe_w, (best_after["C"], best_after["F"]))
assert spe == ("C", ("F", "C")) and seq_pay(*spe) == (200, 100)
assert sorted(ne_seq) == [("C", ("F", "C")), ("C", ("F", "F")), ("F", ("C", "C"))]
assert len(ne_seq) == 3
non_spe = [s for s in ne_seq if s != spe]
assert ("F", ("C", "C")) in non_spe and seq_pay("F", ("C", "C")) == (100, 200)
# The threat "C whatever you do": after C the man would get 0 instead of 100.
assert pay("C", "C")[1] == 0 and pay("C", "F")[1] == 100
print("sequential BoS, woman first: NE", sorted(ne_seq), "; SPE", spe, "payoffs", tuple(map(int, seq_pay(*spe))))
assert seq_pay(*spe)[0] - EU == F(400, 3) and seq_pay(*spe)[0] - BETA == 100  # first-mover gain 133.3
assert seq_pay(*spe)[0] - EU == ALPHA - F(200, 3) == F(400, 3)

# ---------------------------------------------------------------- Lecture 5 preview (ours)
alt = (pay("C", "F")[0] + pay("F", "C")[0]) / 2
assert alt == F(150) and alt > EU and alt * 2 == 300
print("alternation (C,F), (F,C), ...: average per period", alt, "each vs mixed NE", show(EU, 4))

# ---------------------------------------------------------------- (9) Fehr-Schmidt (ours)
def fs(x_i, x_j, a, b):
    """Fehr-Schmidt utility: a weighs disadvantageous, b advantageous inequality (a_FS, b_FS)."""
    return x_i - a * max(x_j - x_i, 0) - b * max(x_i - x_j, 0)


def strict_ne_fs(w, m, a, b):
    """True iff (w, m) is a strict Nash equilibrium when both players have FS parameters (a, b)."""
    uw = fs(*pay(w, m), a, b)
    um = fs(*pay(w, m)[::-1], a, b)
    dw = fs(*pay("F" if w == "C" else "C", m), a, b)
    dm = fs(*pay(w, "F" if m == "C" else "C")[::-1], a, b)
    return uw > dw and um > dm


grid = [F(k, 4) for k in range(0, 13)]
for a, b in product(grid, repeat=2):
    expected = (b < 2) and (a < 1)
    assert strict_ne_fs("C", "F", a, b) == strict_ne_fs("F", "C", a, b) == expected, (a, b)
# The two inequalities in closed form: advantaged player: 200 - 100 b > 0; disadvantaged: 100 - 100 a > 0.
assert fs(ALPHA, BETA, 0, F(2)) == 0 and fs(BETA, ALPHA, F(1), 0) == 0
print("Fehr-Schmidt: coordination is a strict NE iff b_FS < 2 and a_FS < 1 (grid 0..3 step 1/4 checked)")

print("all checks passed")
