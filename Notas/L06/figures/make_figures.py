"""Figures for Lecture 6 (repeated games II: collusion and relational contracts).

Run from anywhere:  python Notas/L06/figures/make_figures.py
Writes L06-*.png beside this file. Every curve is the model's exact expression; every
number is the book's own, cited by printed page (Tadelis 2013, Gibbons 1992, Cabral 2017,
Milgrom & Roberts 1992). Ends with assert checks on the plotted numbers.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt

apply()


def grim_cutoff(vc, vd, vp):
    """delta* = (v^d - v^c) / (v^d - v^p): Tadelis (10.5), p. 202."""
    return (vd - vc) / (vd - vp)


# ---------------------------------------------------------------- Tadelis 10.4
A, CST = 100.0, 10.0                         # p = 100 - q, c(q) = 10 q  (p. 201)


def profit(qi, qj):
    return (A - qi - qj - CST) * qi


def br(qj):
    return (A - CST - qj) / 2                # (10.4), p. 202


def cournot_cutoffs():
    """Tadelis's asymmetric split q1 = 22, q2 = 23 (pp. 201-202), with the correct v2^d."""
    q1, q2 = 22.0, 23.0
    vc1, vc2 = profit(q1, q2), profit(q2, q1)              # 990, 1035
    vd1, vd2 = profit(br(q2), q2), profit(br(q1), q1)       # 1122.25, 1156
    vstar = profit(30, 30)                                  # 900
    d1, d2 = grim_cutoff(vc1, vd1, vstar), grim_cutoff(vc2, vd2, vstar)
    d2_printed = (1122 - 1035) / (1122 - 900)               # p. 202 prints 0.392
    fig, ax = plt.subplots()
    d = np.linspace(0, 1, 201)
    for vc, vd, dc, col, lab in [(vc1, vd1, d1, C["main"], "firm 1 ($q_1^c=22$)"),
                                 (vc2, vd2, d2, C["hi"], "firm 2 ($q_2^c=23$)")]:
        ax.plot(d, np.full_like(d, vc), color=col, lw=2, label=f"{lab}: conform, $v_i^c$")
        ax.plot(d, (1 - d) * vd + d * vstar, color=col, lw=1.6, ls="--",
                label=f"{lab}: deviate, $(1-\\delta)v_i^d+\\delta v^*$")
        ax.plot(dc, vc, "o", color=C["good"], ms=8, zorder=5)
        ax.annotate(f"$\\delta_{{{1 if vc == vc1 else 2}}}^*={dc:.3f}$", (dc, vc),
                    xytext=(8, 10 if vc == vc2 else -18), textcoords="offset points",
                    color=C["good"], fontsize=10)
    ax.plot(d2_printed, vc2, "x", color=C["warn"], ms=9, mew=2)
    ax.annotate("printed 0.392 (uses $q_1=23$)", (d2_printed, vc2), xytext=(-40, 22),
                textcoords="offset points", color=C["warn"], fontsize=9)
    ax.axhline(vstar, color=C["ref"], lw=1, ls=":")
    ax.text(0.02, vstar + 6, "Cournot $v^*=900$", color=C["ref"], fontsize=9)
    ax.set(xlabel="discount factor $\\delta$", ylabel="average payoff per period",
           title="Tacit collusion at $q^c=(22,23)$: conform vs best deviation",
           xlim=(0, 1), ylim=(880, 1180))
    ax.legend(fontsize=8, loc="upper right")
    save(fig, "L06-cournot-cutoffs")
    return d1, d2, d2_printed, vd2


# ---------------------------------------------------------------- Gibbons 2.3.C
def q_best(delta):
    """Lowest symmetric q sustained by grim trigger, in units of a - c (Gibbons p. 104)."""
    delta = np.asarray(delta, float)
    return np.where(delta >= 9 / 17, 0.25, (9 - 5 * delta) / (3 * (9 - delta)))


def best_sustainable():
    d = np.linspace(0, 1, 401)
    q = q_best(d)
    pi = (1 - 2 * q) * q                     # per-firm profit / (a-c)^2
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.0))
    a1.plot(d, q, color=C["main"])
    a1.axhline(1 / 3, color=C["warn"], lw=1, ls="--")
    a1.text(0.62, 1 / 3 + 0.002, "Cournot $q_c=1/3$", color=C["warn"], fontsize=9)
    a1.axhline(0.25, color=C["good"], lw=1, ls="--")
    a1.text(0.62, 0.25 - 0.006, "half monopoly $q_m/2=1/4$", color=C["good"], fontsize=9)
    a1.axvline(9 / 17, color=C["ref"], lw=1, ls=":")
    a1.text(9 / 17 + 0.01, 0.31, "$\\delta=9/17$", color=C["ref"])
    qh = float(q_best(0.5))
    a1.plot(0.5, qh, "o", color=C["hi"], ms=7)
    a1.annotate(f"$\\delta=1/2$: $q^*={qh:.4f}$", (0.5, qh), xytext=(-110, -24),
                textcoords="offset points", color=C["hi"])
    a1.set(xlabel="$\\delta$", ylabel="$q^*/(a-c)$", title="Most collusive quantity grim trigger sustains",
           xlim=(0, 1), ylim=(0.24, 0.34))
    a2.plot(d, pi, color=C["main"])
    a2.axhline(1 / 9, color=C["warn"], lw=1, ls="--")
    a2.text(0.62, 1 / 9 + 0.0003, "Cournot $1/9$", color=C["warn"], fontsize=9)
    a2.axhline(1 / 8, color=C["good"], lw=1, ls="--")
    a2.text(0.62, 1 / 8 - 0.0009, "half monopoly $1/8$", color=C["good"], fontsize=9)
    a2.axvline(9 / 17, color=C["ref"], lw=1, ls=":")
    a2.set(xlabel="$\\delta$", ylabel="profit per firm / $(a-c)^2$",
           title="Profit it delivers", xlim=(0, 1), ylim=(0.108, 0.127))
    save(fig, "L06-best-sustainable-q")
    return qh


# ---------------------------------------------------------------- n firms, Cabral 9.5
def cournot_threshold(n):
    """Grim-trigger cutoff for the symmetric n-firm Cournot cartel: (n+1)^2 / (n^2 + 6n + 1)."""
    n = np.asarray(n, float)
    return (n + 1) ** 2 / (n ** 2 + 6 * n + 1)


def threshold_vs_n():
    n = np.arange(2, 13)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.0))
    a1.plot(n, 1 - 1 / n, "o-", color=C["main"], label="Bertrand: $1-1/n$")
    a1.plot(n, cournot_threshold(n), "s-", color=C["hi"], label="Cournot: $(n+1)^2/(n^2+6n+1)$")
    a1.annotate("$n=2$: 1/2 vs 9/17", (2, 0.53), xytext=(14, -30), textcoords="offset points",
                color=C["ink"], fontsize=9, arrowprops=dict(arrowstyle="->", color=C["ref"]))
    a1.set(xlabel="number of firms $n$", ylabel="critical $\\delta^*$",
           title="Patience needed for the monopoly outcome", ylim=(0.45, 1.0), xticks=n)
    a1.legend(fontsize=9, loc="lower right")
    f = np.logspace(0, np.log10(365), 300)   # price changes per year
    r = 0.10                                  # Cabral's 10% annual rate, p. 221
    for H, col, ls in [(0.0, C["main"], "-"), (0.10, C["warn"], "--")]:
        h = 1 - (1 - H) ** (1 / f)            # per-period hazard from an annual one
        delta = (1 - h) / (1 + r / f)         # Cabral (9.5) with g = 0, p. 220
        a2.plot(f, 1 / (1 - delta), color=col, ls=ls,
                label=f"industry ends w.p. {H:.0%} a year")
    a2.plot(12, 1 + 12 / r, "o", color=C["good"], ms=8)
    a2.annotate("monthly prices, $r=10\\%$:\n$\\delta=0.9917$, $n\\leq121$", (12, 121),
                xytext=(10, 18), textcoords="offset points", color=C["good"], fontsize=9)
    a2.set(xscale="log", yscale="log", xlabel="pricing frequency $f$ (times per year)",
           ylabel="largest $n$ with Bertrand collusion",
           title="Cabral (9.5): frequency and cartel size")
    a2.legend(fontsize=9, loc="upper left")
    save(fig, "L06-threshold-vs-n")
    return cournot_threshold(2), 1 / (1 - 1 / (1 + r / 12))


# ---------------------------------------------------------------- Gibbons carrot and stick
def carrot_stick(delta=0.5):
    """Slack in (2.3.3) and (2.3.4) at delta = 1/2, x in units of a - c (pp. 104-106)."""
    x = np.linspace(0, 0.6, 601)
    pm2, pd = 1 / 8, 9 / 64
    pix = (1 - 2 * x) * x
    pidp = (1 - x) ** 2 / 4
    s3 = delta * (pm2 - pix) - (pd - pm2)     # (2.3.3) rewritten, p. 105
    s4 = delta * (pm2 - pix) - (pidp - pix)   # (2.3.4) rewritten, p. 106
    fig, ax = plt.subplots()
    ax.axhline(0, color=C["ink"], lw=0.8)
    ax.plot(x, s3, color=C["main"], label="(2.3.3) collusive phase: no deviation")
    ax.plot(x, s4, color=C["hi"], label="(2.3.4) punishment phase: no deviation")
    ok = (s3 >= -1e-12) & (s4 >= -1e-12)
    ax.fill_between(x, -0.06, 0.06, where=ok, color=C["good"], alpha=0.15)
    ax.text(0.385, 0.045, "both hold:\n$3/8\\leq x/(a-c)\\leq 1/2$", color=C["good"], fontsize=9.5)
    for r_ in (1 / 8, 3 / 8, 3 / 10, 1 / 2):
        ax.axvline(r_, color=C["ref"], lw=0.8, ls=":")
    ax.set(xlabel="punishment output $x/(a-c)$", ylabel="slack (≥ 0 means the constraint holds)",
           title="Abreu's two-phase strategy at $\\delta=1/2$", xlim=(0, 0.6), ylim=(-0.06, 0.06))
    ax.set_xticks([0, 1 / 8, 0.2, 3 / 10, 3 / 8, 1 / 2, 0.6])
    ax.set_xticklabels(["0", "1/8", "0.2", "3/10", "3/8", "1/2", "0.6"])
    ax.legend(fontsize=9, loc="lower left")
    save(fig, "L06-carrot-stick")
    return x[ok].min(), x[ok].max()


# ---------------------------------------------------------------- trust game, guarantor
def trust_game():
    """Tadelis Fig. 10.1 (p. 205) as a tree; thresholds 1/2 (p. 205) and 0.95 (p. 207)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 4.2), gridspec_kw=dict(width_ratios=[1, 1.25]))
    a1.axis("off")
    a1.set(xlim=(0, 10), ylim=(0, 10))
    n1, n2 = (5, 9), (7, 5.5)
    leaves = {"N": (2.5, 5.5), "C": (5.5, 2), "D": (8.5, 2)}
    pay = {"N": "(0, 0)", "C": "(1, 1)", "D": "(−1, 2)"}
    a1.plot(*zip(n1, leaves["N"]), color=C["ref"], lw=2)
    a1.plot(*zip(n1, n2), color=C["good"], lw=2.6)
    a1.plot(*zip(n2, leaves["C"]), color=C["good"], lw=2.6)
    a1.plot(*zip(n2, leaves["D"]), color=C["warn"], lw=2)
    for (x, y), lab in [(n1, "1"), (n2, "2")]:
        a1.add_patch(plt.Circle((x, y), 0.42, color=C["main"]))
        a1.text(x, y, lab, color="white", ha="center", va="center", fontweight="bold")
    a1.text(3.4, 7.6, "N", fontsize=11)
    a1.text(6.2, 7.6, "T", fontsize=11)
    a1.text(5.6, 3.9, "C", fontsize=11)
    a1.text(8.0, 3.9, "D", fontsize=11)
    for k, (x, y) in leaves.items():
        a1.text(x, y - 0.8, pay[k], ha="center", fontsize=11,
                color=C["warn"] if k == "D" else C["ink"])
    a1.text(5, 0.2, "payoffs (player 1, player 2); green = cooperative path",
            ha="center", fontsize=8.5, color=C["ref"])
    a1.set_title("One-shot trust game (Tadelis Fig. 10.1)")
    d = np.linspace(0, 1, 201)
    a2.plot(d, np.ones_like(d), color=C["main"], label="player 2 honours: average 1")
    a2.plot(d, 2 * (1 - d), color=C["warn"], ls="--",
            label="either cheats: 2 now, 0 after = $(1-\\delta)\\,2$")
    a2.plot(d, np.full_like(d, 0.1), color=C["hi"], label="guarantor keeps contract: fee 0.1")
    a2.plot(0.5, 1, "o", color=C["good"], ms=8)
    a2.annotate("$\\delta\\geq 1/2$", (0.5, 1), xytext=(8, 8), textcoords="offset points", color=C["good"])
    a2.plot(0.95, 0.1, "o", color=C["good"], ms=8)
    a2.annotate("guarantor: $\\delta\\geq 0.95$", (0.95, 0.1), xytext=(-150, -22),
                textcoords="offset points", color=C["good"])
    a2.set(xlabel="$\\delta$", ylabel="average payoff per period", xlim=(0, 1), ylim=(0, 2.05),
           title="Honour vs cheat, as average payoffs")
    a2.legend(fontsize=8.5, loc="upper right")
    save(fig, "L06-trust-game")


# ---------------------------------------------------------------- efficiency wage
def w_star(w0, e, p, delta):
    """Gibbons (2.3.5), p. 110: w* = w0 + e + (1 - delta) e / (delta (1 - p))."""
    return w0 + e + (1 - delta) * e / (delta * (1 - p))


def efficiency_wage():
    # M&R p. 251: outside wage 40 ($000), gain from cheating 1, detection 0.05.
    # Mapped into Gibbons: e = 1, w0 + e = 40 (so w0 = 39), p = 1 - 0.05.
    w0, e, p = 39.0, 1.0, 0.95
    d = np.linspace(0.05, 0.99, 400)
    fig, ax = plt.subplots()
    for pp, col, lab in [(0.95, C["main"], "$p=0.95$ (M&R: 5% detection)"),
                         (0.5, C["hi"], "$p=0.5$"), (0.0, C["good"], "$p=0$ (perfect monitoring)")]:
        ax.plot(d, w_star(w0, e, pp, d), color=col, label=lab)
    ax.axhline(w0 + e, color=C["ref"], lw=1, ls=":")
    ax.text(0.06, w0 + e - 1.6, "$w_0+e=40$ (static floor)", color=C["ref"], fontsize=9)
    ax.axhline(50, color=C["warn"], lw=1, ls="--")
    ax.text(0.06, 50.5, "M&R's current wage 50", color=C["warn"], fontsize=9)
    for dd, lab, off in [(0.5, "$N=1$: 60", (8, 4)), (2 / 3, "$N=2$: 50", (8, 6))]:
        w = w_star(w0, e, p, dd)
        ax.plot(dd, w, "o", color=C["main"], ms=7)
        ax.annotate(lab, (dd, w), xytext=off, textcoords="offset points", color=C["main"])
    ax.set(xlabel="discount factor $\\delta$  (M&R multiplier $N=\\delta/(1-\\delta)$)",
           ylabel="minimum no-shirking wage $w^*$ (\\$000/yr)",
           title="Efficiency wage: the premium falls with patience and detection",
           xlim=(0, 1), ylim=(35, 80))
    ax.legend(fontsize=9, loc="upper right")
    save(fig, "L06-efficiency-wage")
    return w_star(w0, e, p, 0.5), w_star(w0, e, p, 2 / 3)


if __name__ == "__main__":
    d1, d2, d2p, vd2 = cournot_cutoffs()
    assert abs(d1 - 0.595) < 5e-4 and abs(d2p - 0.392) < 5e-4      # Tadelis p. 202
    assert vd2 == 1156 and abs(d2 - 121 / 256) < 1e-12              # corrected firm-2 values
    qh = best_sustainable()
    assert abs(qh - 6.5 / 25.5) < 1e-12 and abs(float(q_best(0)) - 1 / 3) < 1e-12
    c2, nmax = threshold_vs_n()
    assert abs(c2 - 9 / 17) < 1e-12 and abs(nmax - 121) < 1e-9     # Gibbons p. 103; Cabral p. 221
    lo, hi = carrot_stick()
    assert abs(lo - 0.375) < 1e-3 and abs(hi - 0.5) < 1e-3          # Gibbons p. 106
    trust_game()
    w_half, w_two_thirds = efficiency_wage()
    assert abs(w_half - 60) < 1e-12 and abs(w_two_thirds - 50) < 1e-9  # M&R pp. 251-252
    print("L06 figures written; all checks pass")
