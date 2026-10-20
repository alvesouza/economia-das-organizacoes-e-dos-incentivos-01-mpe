"""Figures for Lecture 2 (static games II: Nash equilibrium and mixed strategies).

Run from anywhere:  python Notas/L02/figures/make_figures.py
Writes L02-*.png beside this file. Every number is Tadelis (2013) or Gibbons (1992),
printed pages cited in each function (Tadelis PDF page = printed + 19).
Ends with assert checks on at least one plotted number per figure.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

from fractions import Fraction as Fr
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# ------------------------------------------------------------------ 1. underline method
# Tadelis Sec. 5.1.1, pp. 81-82: the 3x3 game with no dominated strategy and a unique NE.
G581 = {
    "rows": ["U", "M", "D"], "cols": ["L", "C", "R"],
    "u1": [[7, 4, 1], [2, 5, 2], [8, 3, 0]],
    "u2": [[7, 2, 8], [4, 5, 3], [1, 2, 0]],
}


def pure_br_marks(u1, u2):
    """Cells where player 1 (resp. 2) is best-responding, and the pure NE."""
    m, n = len(u1), len(u1[0])
    b1 = {(r, c) for c in range(n) for r in range(m) if u1[r][c] == max(u1[k][c] for k in range(m))}
    b2 = {(r, c) for r in range(m) for c in range(n) if u2[r][c] == max(u2[r][k] for k in range(n))}
    return b1, b2, b1 & b2


def underline_method():
    g = G581
    b1, b2, ne = pure_br_marks(g["u1"], g["u2"])
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    ax.set_xlim(-0.9, 3.05)
    ax.set_ylim(-0.2, 3.85)
    ax.axis("off")
    ax.text(1.5, 3.62, "Player 2", ha="center", fontsize=11, color=C["ink"])
    ax.text(-0.75, 1.5, "Player 1", ha="center", va="center", rotation=90, fontsize=11)
    for c, name in enumerate(g["cols"]):
        ax.text(c + 0.5, 3.22, name, ha="center", fontsize=11, weight="semibold")
    for r, name in enumerate(g["rows"]):
        y = 2.5 - r
        ax.text(-0.25, y, name, ha="center", va="center", fontsize=11, weight="semibold")
        for c in range(3):
            fc = "#e3efe8" if (r, c) in ne else "white"
            ax.add_patch(Rectangle((c, y - 0.5), 1, 1, fc=fc, ec=C["ref"], lw=1))
            s1, s2 = str(g["u1"][r][c]), str(g["u2"][r][c])
            ax.text(c + 0.36, y, s1, ha="center", va="center", fontsize=13,
                    color=C["main"] if (r, c) in b1 else C["ink"])
            ax.text(c + 0.5, y, ",", ha="center", va="center", fontsize=13)
            ax.text(c + 0.64, y, s2, ha="center", va="center", fontsize=13,
                    color=C["hi"] if (r, c) in b2 else C["ink"])
            if (r, c) in b1:   # underline: player 1's best response to this column
                ax.plot([c + 0.29, c + 0.43], [y - 0.17, y - 0.17], color=C["main"], lw=2)
            if (r, c) in b2:   # overline: player 2's best response to this row
                ax.plot([c + 0.57, c + 0.71], [y + 0.17, y + 0.17], color=C["hi"], lw=2)
    ax.text(1.5, -0.12, "underline = BR of player 1 to the column; overline = BR of player 2 to the row;"
            "\nshaded cell carries both marks: the unique pure-strategy Nash equilibrium (M, C)",
            ha="center", va="top", fontsize=9, color=C["ref"])
    save(fig, "L02-underline-method")
    return b1, b2, ne


# ------------------------------------------------------------------ 2. Cournot
# Tadelis Sec. 4.3.4 (pp. 73-74) and Sec. 5.2.3 (pp. 87-88, Fig. 5.2): P = 100 - q, c = 10.
A, B, CC = 100.0, 1.0, 10.0


def cournot_br(qj, a=A, b=B, ci=CC):
    """Eq. (5.2): BR_i(q_j) = max{0, (a - b q_j - c_i) / (2b)}."""
    return np.maximum(0.0, (a - b * np.asarray(qj, float) - ci) / (2 * b))


def cournot():
    fig, ax = plt.subplots(figsize=(6.2, 5.4))
    q = np.linspace(0, 95, 400)
    # rationalizability rounds of Sec. 4.3.4: [0,45] then [22.5,45]
    ax.add_patch(Rectangle((0, 0), 45, 45, fc=C["grid"], ec="none", alpha=0.55, zorder=0))
    ax.add_patch(Rectangle((22.5, 22.5), 22.5, 22.5, fc="#cfdbe4", ec="none", alpha=0.8, zorder=0))
    ax.text(1.5, 1.5, "round 1: $[0,45]^2$", color=C["ref"], fontsize=9)
    ax.text(23.5, 41.5, "round 2: $[22.5,45]^2$", color=C["ref"], fontsize=9)
    ax.plot(cournot_br(q), q, color=C["main"], label="$BR_1(q_2)=(90-q_2)/2$")
    ax.plot(q, cournot_br(q), color=C["hi"], label="$BR_2(q_1)=(90-q_1)/2$")
    qn = 30.0
    ax.plot(qn, qn, "o", color=C["good"], ms=9, zorder=5)
    ax.annotate("Nash equilibrium (30, 30)", (qn, qn), xytext=(14, 14), textcoords="offset points",
                color=C["good"], weight="semibold")
    qm2 = 22.5                                     # half the monopoly output 45
    dev = float(cournot_br(qm2))                   # 33.75
    ax.plot(qm2, qm2, "o", mfc="white", mec=C["warn"], ms=8, zorder=5)
    ax.annotate("", (dev, qm2), (qm2, qm2), arrowprops=dict(arrowstyle="->", color=C["warn"], lw=1.6))
    ax.annotate("collusive split (22.5, 22.5):\nfirm 1's best reply is 33.75", (dev, qm2),
                xytext=(40, -60), textcoords="offset points", color=C["warn"], fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=C["warn"], lw=0.8))
    ax.plot([0, 45], [45, 0], ls="--", color=C["ref"], lw=1)
    ax.annotate("$q_1+q_2=45$ (monopoly output)", (8, 37), xytext=(30, 70), textcoords="offset points",
                color=C["ref"], fontsize=9, arrowprops=dict(arrowstyle="-", color=C["ref"], lw=0.8))
    ax.set(xlabel="$q_1$", ylabel="$q_2$", xlim=(0, 92), ylim=(0, 92),
           title="Cournot duopoly: best responses cross once")
    ax.set_aspect("equal")
    ax.legend(loc="upper right")
    save(fig, "L02-cournot-best-responses")
    return qn, dev


# ------------------------------------------------------------------ 3. Bertrand
# Tadelis Sec. 5.2.4 (pp. 88-93): p = 100 - q, c = 10, prices in cents; asymmetric c1=1, c2=2.
def bertrand_profit(pi, pj, c=10.0):
    """v_i(p_i, p_j) of p. 88 with ties split equally."""
    pi = np.asarray(pi, float)
    full = (100 - pi) * (pi - c)
    return np.where(pi < pj - 1e-9, full, np.where(np.abs(pi - pj) <= 1e-9, full / 2, 0.0))


def bertrand_br_grid(lo=0.0, hi=60.0):
    """Brute-force BR on the cent grid (the book's Delta = 0.01)."""
    grid = np.round(np.arange(round(lo * 100), round(hi * 100) + 1) / 100, 2)
    br = []
    for pj in grid:
        v = bertrand_profit(grid, pj)
        best = v.max()
        br.append(grid[np.abs(v - best) <= 1e-9])
    return grid, br


def bertrand():
    grid, br = bertrand_br_grid()
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4))
    sel = (grid >= 10.01) & (grid <= 60)
    a1.plot(grid[sel], [b.min() for b, s in zip(br, sel) if s], color=C["main"],
            label="$BR_i(p_j)$, cent grid")
    a1.plot([0, 60], [0, 60], ls=":", color=C["ref"], lw=1, label="45° line")
    a1.vlines(10, 10, 60, color=C["main"], lw=4, alpha=0.35)
    a1.text(11, 44,"$BR_i(10)=\\{10, 10.01, \\dots\\}$", color=C["main"], fontsize=9)
    a1.axhline(55, color=C["ref"], lw=1, ls="--")
    a1.text(35, 56.2, "monopoly price 55", color=C["ref"], fontsize=9)
    a1.plot([10, 10.01], [10, 10.01], "o", color=C["good"], ms=8)
    a1.annotate("NE: (10, 10) and (10.01, 10.01)", (10, 10), xytext=(16, -4),
                textcoords="offset points", color=C["good"], weight="semibold")
    a1.set(xlabel="rival's price $p_j$", ylabel="best-response price $p_i$", xlim=(0, 60), ylim=(0, 60),
           title="Symmetric Bertrand ($c=10$): undercut by one cent")
    a1.legend(loc="center right")
    # Fig. 5.3 with the book's numbers: firm 1 (c1 = 1) facing p2 = 2
    p = np.linspace(0, 6, 1201)
    hump = (100 - p) * (p - 1)
    a2.plot(p, hump, ls="--", color=C["ref"], lw=1.2, label="monopoly profit $(100-p_1)(p_1-1)$")
    lo = p < 2
    a2.plot(p[lo], hump[lo], color=C["main"], lw=2.4, label="$v_1(p_1, 2)$")
    a2.plot(p[p > 2], 0 * p[p > 2], color=C["main"], lw=2.4)
    a2.plot(2, 98, "o", mfc="white", mec=C["warn"], ms=7)
    a2.plot(2, 49, "o", color=C["warn"], ms=7)
    a2.annotate("$p_1\\uparrow 2$: profit $\\to 98$, never reached", (2, 98), xytext=(16, 22),
                textcoords="offset points", color=C["warn"], fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=C["warn"], lw=0.8))
    a2.annotate("$p_1=2$: split market, 49", (2, 49), xytext=(14, -4), textcoords="offset points",
                color=C["warn"], fontsize=9.5)
    a2.annotate("$p_1>2$: no customers, 0", (4, 0), xytext=(0, -20), textcoords="offset points",
                color=C["main"], fontsize=9.5)
    a2.set(xlabel="$p_1$ (monopoly price $p_1^M=50.5$ lies far to the right)", ylabel="profit of firm 1",
           xlim=(0, 6), ylim=(-110, 420), title="Asymmetric Bertrand: no best response to $p_2=2$")
    a2.legend(loc="upper right")
    save(fig, "L02-bertrand")
    return grid, br


# ------------------------------------------------------------------ 4. commons
# Tadelis Sec. 5.2.2 (pp. 84-87, Fig. 5.1): v_i = ln k_i + ln(K - k_1 - k_2); K normalised to 1.
def commons():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
    k = np.linspace(0, 1, 300)
    a1.plot((1 - k) / 2, k, color=C["main"], label="$k_1(k_2)=(K-k_2)/2$")
    a1.plot(k, (1 - k) / 2, color=C["hi"], label="$k_2(k_1)=(K-k_1)/2$")
    a1.plot(1 / 3, 1 / 3, "o", color=C["good"], ms=9)
    a1.annotate("Nash: $K/3$ each", (1 / 3, 1 / 3), xytext=(12, 8), textcoords="offset points",
                color=C["good"], weight="semibold")
    a1.plot(1 / 4, 1 / 4, "o", mfc="white", mec=C["warn"], ms=8)
    a1.annotate("Pareto optimum: $K/4$ each", (1 / 4, 1 / 4), xytext=(-70, -24),
                textcoords="offset points", color=C["warn"])
    a1.set(xlabel="$k_1$ (share of $K$)", ylabel="$k_2$ (share of $K$)", xlim=(0, 1), ylim=(0, 1),
           title="Best responses (Fig. 5.1), $K=1$")
    a1.set_aspect("equal")
    a1.legend(loc="upper right")
    ks = np.linspace(0.02, 0.48, 300)
    v = np.log(ks) + np.log(1 - 2 * ks)            # each player's payoff at the symmetric profile
    a2.plot(ks, v, color=C["main"], label="$v_i(k,k)=\\ln k+\\ln(K-2k)$")
    for x, col, lab in [(1 / 4, C["warn"], "$K/4$"), (1 / 3, C["good"], "$K/3$")]:
        y = math.log(x) + math.log(1 - 2 * x)
        a2.plot(x, y, "o", color=col, ms=8)
        a2.annotate(f"{lab}: {y:.3f}", (x, y), xytext=(-20, -26), textcoords="offset points", color=col)
    a2.set(xlabel="common consumption $k$", ylabel="payoff of each player", ylim=(-4.2, -1.8),
           title="Everyone gains $\\ln(9/8)\\approx0.118$ at $K/4$")
    a2.legend(loc="lower center")
    save(fig, "L02-commons")
    v_opt = math.log(1 / 4) + math.log(1 / 2)
    v_ne = 2 * math.log(1 / 3)
    return v_opt - v_ne


# ------------------------------------------------------------------ 5. Hotelling voting
# Tadelis Sec. 5.2.5 (pp. 93-95, Fig. 5.4): 101 citizens -50..50, platforms in the same set.
PLAT = list(range(-50, 51))


def vote_payoff(ai, aj):
    """1 win, 1/2 tie, 0 lose; citizens equidistant from both platforms abstain (fn. 9, p. 94)."""
    if ai == aj:
        return 0.5
    mine = sum(1 for x in PLAT if abs(x - ai) < abs(x - aj))
    theirs = sum(1 for x in PLAT if abs(x - aj) < abs(x - ai))
    return 1.0 if mine > theirs else 0.5 if mine == theirs else 0.0


def voting_br():
    pay = {(ai, aj): vote_payoff(ai, aj) for ai in PLAT for aj in PLAT}
    br = {}
    for aj in PLAT:
        best = max(pay[(ai, aj)] for ai in PLAT)
        br[aj] = [ai for ai in PLAT if pay[(ai, aj)] == best]
    return br


def hotelling():
    br = voting_br()
    fig, ax = plt.subplots(figsize=(5.8, 5.6))
    x1 = [aj for aj in PLAT for ai in br[aj]]
    y1 = [ai for aj in PLAT for ai in br[aj]]
    ax.scatter(x1, y1, s=1.6, color=C["main"], alpha=0.55, label="$BR_1(a_2)$: $a_1$ against $a_2$")
    ax.scatter(y1, x1, s=1.6, color=C["hi"], alpha=0.35, label="$BR_2(a_1)$ (transposed)")
    ne = [(a1, a2) for a2 in PLAT for a1 in br[a2] if a2 in br[a1]]
    for a1, a2 in ne:
        ax.plot(a2, a1, "o", color=C["good"], ms=9)
    ax.annotate("unique NE $a_1=a_2=0$\n(the median citizen)", (0, 0), xytext=(14, -40),
                textcoords="offset points", color=C["good"], weight="semibold",
                bbox=dict(fc="white", ec=C["good"], lw=0.8, pad=3))
    ax.set(xlabel="$a_2$ (horizontal) / rival's platform", ylabel="$a_1$ / own platform",
           xlim=(-52, 52), ylim=(-52, 52), title="Hotelling voting: best responses")
    ax.set_aspect("equal")
    ax.legend(loc="upper left", markerscale=6, fontsize=9)
    save(fig, "L02-hotelling-voting")
    return br, ne


# ------------------------------------------------------------------ 6. mixed 2x2
# Tadelis Sec. 6.2.3 (pp. 113-114, Fig. 6.4): M/D vs C/R, (0,0) (3,5) / (4,4) (0,3).
def mixed_2x2():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.6))
    q = np.linspace(0, 1, 301)
    vm, vd = 3 * (1 - q), 4 * q                    # v1(M,q), v1(D,q)
    a1.plot(q, vm, color=C["main"], label="$v_1(M,q)=3(1-q)$")
    a1.plot(q, vd, color=C["hi"], label="$v_1(D,q)=4q$")
    a1.plot(q, np.maximum(vm, vd), color=C["ink"], lw=5, alpha=0.12, label="upper envelope = best reply")
    qs = Fr(3, 7)
    a1.plot(float(qs), 12 / 7, "o", color=C["good"], ms=8)
    a1.annotate("$q=3/7$: indifferent, payoff $12/7$", (float(qs), 12 / 7), xytext=(14, -30),
                textcoords="offset points", color=C["good"])
    a1.set(xlabel="$q=\\sigma_2(C)$", ylabel="player 1's expected payoff", xlim=(0, 1), ylim=(0, 4.2),
           title="Player 1 mixes only when player 2 plays $q=3/7$")
    a1.legend(loc="upper center")
    # best-response correspondences, p = sigma_1(M) on the vertical axis as in Fig. 6.4
    a2.plot([0, 3 / 7, 3 / 7, 1], [1, 1, 0, 0], color=C["main"], lw=2.4, label="$BR_1(q)$")
    a2.plot([1, 1, 0, 0], [0, 1 / 6, 1 / 6, 1], color=C["hi"], lw=2.4, ls="--", label="$BR_2(p)$")
    for (qq, pp, lab, off) in [(0, 1, "(M, R): $(p,q)=(1,0)$", (8, -16)),
                               (1, 0, "(D, C): $(p,q)=(0,1)$", (-128, 10)),
                               (3 / 7, 1 / 6, "mixed: $(1/6,\\,3/7)$", (8, 8))]:
        a2.plot(qq, pp, "o", color=C["good"], ms=9, zorder=5)
        a2.annotate(lab, (qq, pp), xytext=off, textcoords="offset points", color=C["good"])
    a2.set(xlabel="$q=\\sigma_2(C)$", ylabel="$p=\\sigma_1(M)$", xlim=(-0.03, 1.03), ylim=(-0.03, 1.03),
           title="Three crossings, three Nash equilibria (Fig. 6.4)")
    a2.set_aspect("equal")
    a2.legend(loc="center right")
    save(fig, "L02-mixed-2x2")
    return qs


# ------------------------------------------------------------------ 7. mixed dominance
# Gibbons Sec. 1.3.A, Figs. 1.3.1-1.3.2 (pp. 32-33): T = (3, 0), M = (0, 3), B = (1, 1) or (2, 2).
def mixed_dominance():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.3), sharey=True)
    q = np.linspace(0, 1, 301)
    for ax, bval, title in [(axs[0], 1, "B = (1, 1): dominated by $T/2+M/2$"),
                            (axs[1], 2, "B = (2, 2): best reply for $1/3<q<2/3$")]:
        t, m = 3 * q, 3 * (1 - q)
        env = np.maximum(t, m)
        ax.plot(q, t, color=C["main"], label="T: $3q$")
        ax.plot(q, m, color=C["hi"], label="M: $3(1-q)$")
        ax.plot(q, 0 * q + bval, color=C["warn"], label=f"B: {bval}")
        ax.plot(q, 0 * q + 1.5, ls=":", color=C["ref"], label="mix $T/2+M/2$: 3/2")
        ax.fill_between(q, bval, env, where=bval > env, color=C["good"], alpha=0.25)
        ax.set(xlabel="$q$ = player 2's probability of L", xlim=(0, 1), ylim=(0, 4.4), title=title)
        ax.legend(loc="upper center", fontsize=9, ncol=2)
    axs[0].set_ylabel("player 1's expected payoff")
    save(fig, "L02-mixed-dominance")


if __name__ == "__main__":
    apply()
    b1, b2, ne = underline_method()
    qn, dev = cournot()
    grid, br = bertrand()
    gain = commons()
    vbr, vne = hotelling()
    qs = mixed_2x2()
    mixed_dominance()

    # p. 82: player 1 best-responds at (D,L), (M,C), (M,R); player 2 at (D,C), (M,C), (U,R)
    R, Cn = G581["rows"], G581["cols"]
    nm = lambda s: {(R[r], Cn[c]) for r, c in s}
    assert nm(b1) == {("D", "L"), ("M", "C"), ("M", "R")}
    assert nm(b2) == {("D", "C"), ("M", "C"), ("U", "R")}
    assert nm(ne) == {("M", "C")}
    # pp. 87-88: NE 30; Gibbons p. 17: q_m/2 is not a best reply to q_m/2
    assert qn == 30 and float(cournot_br(30)) == 30 and dev == 33.75
    # p. 90: BR(p_j) = p_j - 0.01 on [10.02, 55]; BR(10.01) = {10.01}; BR(10) = [10, ...)
    idx = {round(g, 2): i for i, g in enumerate(grid)}
    assert list(br[idx[30.0]]) == [29.99] and list(br[idx[55.0]]) == [54.99]
    assert list(br[idx[57.0]]) == [55.0] and list(br[idx[10.01]]) == [10.01]
    assert br[idx[10.0]].min() == 10.0 and len(br[idx[10.0]]) == len(grid) - 1000
    # every NE on the grid: p2 in BR(p1) and p1 in BR(p2)
    brs = [set(np.round(b, 2).tolist()) for b in br]
    ne_b = {(round(p1, 2), p2) for i, p1 in enumerate(grid) for p2 in brs[i]
            if round(p1, 2) in brs[idx[p2]]}
    assert sorted(ne_b) == [(10.0, 10.0), (10.01, 10.01)]
    # p. 89: Delta v = 55.02 p - 0.5 p^2 - 501.1 equals 0.0002 at p_j = 10.02
    assert abs(55.02 * 10.02 - 0.5 * 10.02 ** 2 - 501.1 - 0.0002) < 1e-9
    # pp. 86-87: the per-player gain from K/4 over K/3 is 2ln3 - ln2 - ln4 = ln(9/8)
    assert abs(gain - math.log(9 / 8)) < 1e-12 and abs(gain - 0.1178) < 1e-4
    # pp. 94-95: BR(a_j) = [-a_j+1, a_j-1] for a_j > 1, {0} for |a_j| <= 1, unique NE (0, 0)
    assert vbr[22] == list(range(-21, 22)) and vbr[-15] == list(range(-14, 15))
    assert vbr[0] == [0] and vbr[1] == [0] and vbr[-1] == [0] and vne == [(0, 0)]
    # p. 113: q = 3/7 makes player 1 indifferent; p = 1/6 makes player 2 indifferent
    assert 3 * (1 - qs) == 4 * qs and 4 * (1 - Fr(1, 6)) == 5 * Fr(1, 6) + 3 * (1 - Fr(1, 6))
    # Gibbons p. 33: with B = 2, B beats max(3q, 3(1-q)) exactly for 1/3 < q < 2/3
    qq = np.linspace(0, 1, 3001)
    beats = qq[2 > np.maximum(3 * qq, 3 * (1 - qq))]
    assert abs(beats.min() - 1 / 3) < 1e-3 and abs(beats.max() - 2 / 3) < 1e-3
    print("L02 figures written; all checks pass")
