"""Figures for Lecture 5 (repeated games I: cooperation). Estimated unit.

Run from anywhere:  python Notas/L05/figures/make_figures.py
Writes L05-*.png beside this file. Book numbers are Tadelis (2013), printed pages
(PDF 1-based = printed + 19); Gibbons (1992) and Cabral (2017) cited where used.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from _figstyle import C, apply, save

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

# Tadelis's Prisoner's Dilemma (pp. 197, 209): (M,m)=(4,4), (M,f)=(-1,5), (F,m)=(5,-1), (F,f)=(1,1).
# Labels: temptation T=5, reward R=4, punishment P=1, sucker S=-1.
TT, RR, PP, SS = 5.0, 4.0, 1.0, -1.0
PD = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("F", "m"): (5, -1), ("F", "f"): (1, 1)}
# Tadelis's two-stage game (p. 191): two stage NE, (F,f) and (R,r).
G3_ROWS, G3_COLS = ["M", "F", "R"], ["m", "f", "r"]
G3 = {("M", "m"): (4, 4), ("M", "f"): (-1, 5), ("M", "r"): (0, 0),
      ("F", "m"): (5, -1), ("F", "f"): (1, 1), ("F", "r"): (0, 0),
      ("R", "m"): (0, 0), ("R", "f"): (0, 0), ("R", "r"): (3, 3)}


def pure_ne(rows, cols, pay, tol=1e-12):
    """Pure-strategy Nash equilibria of a bimatrix given as {(row, col): (u1, u2)} (weak BR)."""
    out = []
    for r in rows:
        for c in cols:
            u1, u2 = pay[(r, c)]
            if all(u1 >= pay[(r2, c)][0] - tol for r2 in rows) and \
               all(u2 >= pay[(r, c2)][1] - tol for c2 in cols):
                out.append((r, c))
    return out


def draw_matrix(ax, rows, cols, pay, title, mark=(), fmt="{:g}"):
    """A payoff matrix drawn as a table; cells in `mark` are filled with the 'good' role."""
    ax.set_xlim(0, len(cols) + 0.6); ax.set_ylim(0, len(rows) + 0.7)
    ax.axis("off"); ax.set_title(title)
    for j, c in enumerate(cols):
        ax.text(0.6 + j + 0.5, len(rows) + 0.3, c, ha="center", va="center", fontsize=12,
                color=C["main"], style="italic")
    for i, r in enumerate(rows):
        y = len(rows) - 1 - i
        ax.text(0.3, y + 0.5, r, ha="center", va="center", fontsize=12, color=C["main"])
        for j, c in enumerate(cols):
            on = (r, c) in mark
            ax.add_patch(Rectangle((0.6 + j, y), 1, 1, fc=C["good"] if on else "white",
                                   alpha=0.18 if on else 1, ec=C["ref"], lw=1))
            u1, u2 = pay[(r, c)]
            ax.text(0.6 + j + 0.5, y + 0.5, (fmt + ", " + fmt).format(u1, u2), ha="center",
                    va="center", fontsize=11, color=C["good"] if on else C["ink"],
                    weight="bold" if on else "normal")


def unraveling():
    """Prop. 10.1 (p. 192): fold the last stage back; the reduced game is again a PD."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.4))
    rows, cols = ["M", "F"], ["m", "f"]
    ne_T = pure_ne(rows, cols, PD)
    draw_matrix(a1, rows, cols, PD, "Stage $T$: the stage game $G$", ne_T)
    # Stage T-1 with the continuation (F,f) forever after: add delta*1 to every cell (delta=1 shown,
    # the no-discounting case of Gibbons Fig. 2.3.2, p. 83).
    red = {k: (v[0] + 1, v[1] + 1) for k, v in PD.items()}
    ne_T1 = pure_ne(rows, cols, red)
    draw_matrix(a2, rows, cols, red, "Stage $T-1$: $G$ + continuation $(1,1)$", ne_T1)
    save(fig, "L05-unraveling")
    return ne_T, ne_T1


def two_stage():
    """Tadelis p. 191 and fn. 2: (R,r) after (M,m), (F,f) otherwise; M is a BR iff delta >= 1/2."""
    d = 0.5
    red = {k: (v[0] + d * (3 if k == ("M", "m") else 1), v[1] + d * (3 if k == ("M", "m") else 1))
           for k, v in G3.items()}
    fig = plt.figure(figsize=(12.6, 3.7))
    a1, a2, a3 = fig.add_subplot(131), fig.add_subplot(132), fig.add_subplot(133)
    draw_matrix(a1, G3_ROWS, G3_COLS, G3, "Stage game: two NE, Pareto ranked",
                pure_ne(G3_ROWS, G3_COLS, G3))
    ne_red = pure_ne(G3_ROWS, G3_COLS, red)
    draw_matrix(a2, G3_ROWS, G3_COLS, red, "Stage 1 folded back, $\\delta=1/2$", ne_red, fmt="{:g}")
    x = np.linspace(0, 1, 200)
    a3.plot(x, np.ones_like(x), color=C["warn"], label="gain from F today: $5-4=1$")
    a3.plot(x, 2 * x, color=C["main"], label="loss tomorrow: $\\delta(3-1)=2\\delta$")
    a3.axvline(0.5, color=C["good"], ls="--", lw=1.2)
    a3.text(0.52, 1.6, "$\\delta=1/2$", color=C["good"])
    a3.set(xlabel="discount factor $\\delta$", ylabel="payoff units", xlim=(0, 1), ylim=(0, 2.1),
           title="Carrot vs stick")
    a3.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    save(fig, "L05-two-stage-carrot-stick")
    return red, ne_red


def coop_rounds(d, T, b=5.0, a=4.0, r=3.0, p=1.0):
    """Most (M,m) rounds n in a T-period repetition of the p. 191 game when the path is
    (M,m) x n then (R,r) x (T-n), any deviation -> (F,f) to the end. Checks every
    cooperative period by the one-stage deviation principle (Prop. 10.3 / Thm 9.1)."""
    best = 0
    for n in range(0, T):
        ok = True
        for t in range(1, n + 1):
            loss = sum(d ** (s - t) * ((a if s <= n else r) - p) for s in range(t + 1, T + 1))
            if b - a > loss + 1e-12:
                ok = False
                break
        if ok:
            best = n
    return best


def finite_rounds():
    """T = 10 repetitions of the p. 191 game: cooperative rounds that survive, against delta."""
    T = 10
    ds = np.linspace(0.2, 0.99, 800)
    n = [coop_rounds(d, T) for d in ds]
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    ax.step(ds, n, where="post", color=C["main"])
    ax.axvline(1 / 3, color=C["warn"], ls=":", lw=1.2)
    ax.text(0.205, 1.0, "$\\delta\\leq 1/3$: no reward\nphase is long enough", color=C["warn"], fontsize=8.5)
    ax.axvline(0.5, color=C["good"], ls="--", lw=1.2)
    ax.text(0.51, 4.6, "$\\delta\\geq 1/2$: one reward\nround suffices", color=C["good"], fontsize=9)
    ax.set(xlabel="discount factor $\\delta$", ylabel="rounds of $(M,m)$ in an SPE",
           title="$T=10$: cooperation survives in the early rounds", xlim=(0.2, 1), ylim=(-0.3, 10))
    save(fig, "L05-finite-coop-rounds")
    return {d: coop_rounds(d, T) for d in (0.3, 0.34, 0.4, 0.5, 0.9)}


def discounting():
    """Sec. 10.2.1 (pp. 193-195): delta as continuation probability; s(v, delta, T) -> v/(1-delta)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.4, 3.9))
    t = np.arange(0, 501)
    a1.semilogy(t, 0.97 ** t, color=C["main"])
    for k in (100, 500):
        a1.plot(k, 0.97 ** k, "o", color=C["warn"])
        a1.annotate(f"$0.97^{{{k}}}=$ {0.97 ** k:.4g}".replace("e-07", "e-7"), (k, 0.97 ** k), xytext=(-20, 12),
                    textcoords="offset points", color=C["warn"], ha="right" if k == 500 else "left")
    a1.set(xlabel="periods $t$", ylabel="Pr(play at least $t$ periods)", xlim=(0, 520),
           title="$\\delta=0.97$ read as a continuation probability")
    v = 4.0
    TT_ = np.arange(1, 61)
    for d, col in ((0.9, C["main"]), (0.75, C["hi"])):
        s = v * (1 - d ** TT_) / (1 - d)
        a2.plot(TT_, s, color=col, label=f"$\\delta={d}$")
        a2.axhline(v / (1 - d), color=col, ls="--", lw=1)
        a2.text(30, v / (1 - d) + 0.6, f"$v/(1-\\delta)={v / (1 - d):g}$", color=col, va="bottom", fontsize=9)
    a2.set(xlabel="horizon $T$", ylabel="$s(v,\\delta,T)$", xlim=(0, 61), ylim=(0, 45),
           title="Present value of $v=4$ for $T$ periods")
    a2.legend(loc="center right")
    save(fig, "L05-discounting")
    return 0.97 ** 100, 0.97 ** 500


def grim_threshold():
    """(10.3), p. 200 in average-payoff form: cooperate R vs deviate (1-d)T + dP."""
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    d = np.linspace(0, 1, 300)
    cases = [("Tadelis p. 197: $T,R,P=5,4,1$", 5, 4, 1, C["main"]),
             ("Cabral p. 173: $6,5,4$", 6, 5, 4, C["hi"])]
    out = []
    for lab, T, R, P, col in cases:
        ax.plot(d, (1 - d) * T + d * P, color=col, label=lab + ": deviate")
        ax.plot(d, np.full_like(d, R), color=col, ls="--", lw=1.4, label="cooperate forever")
        ds = (T - R) / (T - P)
        ax.plot(ds, R, "o", color=C["good"], ms=8, zorder=5)
        ax.annotate(f"$\\delta^*={ds:g}$", (ds, R), xytext=(8, 8), textcoords="offset points",
                    color=C["good"], weight="bold")
        out.append(ds)
    ax.set(xlabel="discount factor $\\delta$", ylabel="average payoff $(1-\\delta)\\sum\\delta^{t-1}v_t$",
           title="Grim trigger: cooperation is sustained right of $\\delta^*=(T-R)/(T-P)$",
           xlim=(0, 1), ylim=(0, 6.5))
    ax.legend(fontsize=8.5, loc="lower left")
    save(fig, "L05-grim-threshold")
    return out


def deviation_stream():
    """One-stage deviation on the path (p. 200): +1 today, then -3 every period forever."""
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    t = np.arange(1, 41)
    diff = np.where(t == 1, TT - RR, PP - RR)  # deviate minus cooperate, period by period
    finals = {}
    for d, col in ((0.15, C["warn"]), (0.25, C["ref"]), (0.5, C["good"])):
        cum = np.cumsum(d ** (t - 1) * diff)
        ax.plot(t, cum, "o-", ms=3, color=col, label=f"$\\delta={d}$")
        finals[d] = (TT - RR) - d * (RR - PP) / (1 - d)
        ax.axhline(finals[d], color=col, ls=":", lw=1)
    ax.axhline(0, color=C["ink"], lw=0.8)
    ax.set(xlabel="period $t$ (deviation at $t=1$)", ylabel="cumulative PV of deviating $-$ cooperating",
           title="The gain is paid once, the loss forever", xlim=(0, 41))
    ax.legend()
    save(fig, "L05-deviation-stream")
    return finals


def folk():
    """Defs. 10.6-10.7 and Thm 10.1 (pp. 209-214): feasible set, IR region, alternating path."""
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    hull = np.array([(SS, TT), (RR, RR), (TT, SS), (PP, PP)])  # convex hull of the four payoffs
    ax.add_patch(Polygon(hull, closed=True, fc=C["ref"], alpha=0.18, ec=C["ref"], label="feasible (convex hull)"))
    # Feasible and v_i > 1: the edge (S,T)-(R,R) meets v1 = P at v2 = T - (P-S)(T-R)/(R-S) = 4.6.
    top = TT - (PP - SS) * (TT - RR) / (RR - SS)
    ir = np.array([(PP, PP), (PP, top), (RR, RR), (top, PP)])
    ax.add_patch(Polygon(ir, closed=True, fc=C["good"], alpha=0.30, ec=C["good"], lw=1.5,
                         label="feasible and $v_i>1$: folk-theorem region"))
    for (x, y), lab, off in [((RR, RR), "(4,4) = (M,m)", (6, 6)), ((PP, PP), "(1,1) = (F,f)", (-30, -18)),
                             ((TT, SS), "(5,-1)", (6, -4)), ((SS, TT), "(-1,5)", (6, 0))]:
        ax.plot(x, y, "o", color=C["ink"])
        ax.annotate(lab, (x, y), xytext=off, textcoords="offset points")
    ax.plot(4.4, 2, "s", color=C["hi"])
    ax.annotate("(4.4, 2)", (4.4, 2), xytext=(-8, -4), textcoords="offset points",
                color=C["hi"], fontsize=9, ha="right")
    d = np.linspace(0.5, 0.999, 200)
    v1, v2 = (5 - d) / (1 + d), (-1 + 5 * d) / (1 + d)
    ax.plot(v1, v2, color=C["warn"], lw=2.4, label="alternating path, $\\delta\\in[1/2,1)$")
    ax.plot(2, 2, "o", color=C["good"], ms=8)
    ax.annotate("(2,2): limit as $\\delta\\to1$", (2, 2), xytext=(-110, 14), textcoords="offset points",
                color=C["good"])
    ax.plot((5 - 0.9) / 1.9, (-1 + 4.5) / 1.9, "o", color=C["warn"])
    ax.annotate("$\\delta=0.9$: (2.158, 1.842)", ((5 - 0.9) / 1.9, (-1 + 4.5) / 1.9), xytext=(-8, -4),
                textcoords="offset points", color=C["warn"], fontsize=9, ha="right")
    ax.plot(3, 1, "o", color=C["warn"], mfc="white")
    ax.axhline(PP, color=C["ref"], ls="--", lw=1); ax.axvline(PP, color=C["ref"], ls="--", lw=1)
    ax.set(xlabel="average payoff $\\bar v_1$", ylabel="average payoff $\\bar v_2$", xlim=(-1.5, 5.7),
           ylim=(-1.5, 5.7), title="Folk theorem for Tadelis's Prisoner's Dilemma", aspect="equal")
    ax.legend(loc="upper right", fontsize=8.5)
    save(fig, "L05-folk-theorem")
    return top, (v1[0], v2[0])


if __name__ == "__main__":
    apply()
    ne_T, ne_T1 = unraveling()
    assert ne_T == [("F", "f")] and ne_T1 == [("F", "f")]          # unique NE in both stages
    red, ne_red = two_stage()
    assert red[("M", "m")] == (5.5, 5.5) and red[("F", "m")] == (5.5, -0.5)
    assert set(ne_red) == {("M", "m"), ("F", "f"), ("R", "r")}       # three NE at delta = 1/2
    rounds = finite_rounds()
    assert rounds[0.5] == 9 and rounds[0.4] == 8 and rounds[0.34] == 6 and rounds[0.3] == 0
    p100, p500 = discounting()
    assert abs(p100 - 0.0475) < 1e-4 and abs(p500 - 2.4315e-7) < 1e-10   # p. 194
    ds = grim_threshold()
    assert ds == [0.25, 0.5]                                           # (10.3) p. 200; Cabral p. 173
    finals = deviation_stream()
    assert abs(finals[0.25]) < 1e-12 and finals[0.15] > 0 > finals[0.5]
    top, start = folk()
    assert abs(top - 4.6) < 1e-12
    assert abs(start[0] - 3) < 1e-12 and abs(start[1] - 1) < 1e-12    # delta = 1/2: bad period at P
    print("all L05 figures written; checks pass")
