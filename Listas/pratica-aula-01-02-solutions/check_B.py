"""Check every number and closed form stated in the group-B solutions (Cabral items).

Items: 09 (Cabral 5.1, front yards), 10 (7.6, Cortez), 19 (7.14, centipede),
30 (13.10, asset specificity). Run: python check_B.py -> "all B checks passed".
"""
import sympy as sp

# ---- Item 09: two neighbours, private benefit a*x, spillover s*x to the other, cost x^2/2.
a, s, x1, x2 = sp.symbols("a s x1 x2", positive=True)
u1 = a * x1 + s * x2 - x1**2 / 2
u2 = a * x2 + s * x1 - x2**2 / 2
nash = sp.solve([sp.diff(u1, x1), sp.diff(u2, x2)], [x1, x2], dict=True)[0]
assert nash == {x1: a, x2: a}
eff = sp.solve([sp.diff(u1 + u2, x1), sp.diff(u1 + u2, x2)], [x1, x2], dict=True)[0]
assert eff == {x1: a + s, x2: a + s}
gain_each = sp.simplify(u1.subs(eff) - u1.subs(nash))
assert sp.simplify(gain_each - s**2 / 2) == 0
# Deviation from the reciprocal deal (x2 = a+s fixed): best reply is a, gain s^2/2 (needs enforcement).
dev = sp.simplify(u1.subs({x1: a, x2: a + s}) - u1.subs({x1: a + s, x2: a + s}))
assert sp.simplify(dev - s**2 / 2) == 0
num = {a: 1, s: sp.Rational(1, 2)}
assert (u1 + u2).subs(eff).subs(num) - (u1 + u2).subs(nash).subs(num) == sp.Rational(1, 4)

# ---- Item 10: Cortez tree. Payoffs (natives, Spaniards).
NOT, RES_LEAVE, RES_FIGHT = (0, 10), (5, 2), (-5, 1)
def spe(can_leave):
    sp_reply = max([RES_FIGHT] + ([RES_LEAVE] if can_leave else []), key=lambda p: p[1])
    return max([NOT, sp_reply], key=lambda p: p[0])
assert spe(True) == (5, 2)      # ships kept: natives resist, Spaniards leave
assert spe(False) == (0, 10)    # ships sunk: natives do not resist
assert spe(False)[1] - spe(True)[1] == 8   # value of commitment

# ---- Item 19: centipede, 100 decision nodes (Cabral Figure 7.13).
N = 100
def stop(k):  # payoff (P1, P2) if the mover at node k plays d
    j = (k + 1) // 2
    return (2 * j, 2 * j - 2) if k % 2 else (2 * j - 1, 2 * j + 1)
assert [stop(k) for k in (1, 2, 3, 4, 5)] == [(2, 0), (1, 3), (4, 2), (3, 5), (6, 4)]
assert [stop(k) for k in (98, 99, 100)] == [(97, 99), (100, 98), (99, 101)]
cont = (100, 100)          # value after r at the last node
choices = {}
for k in range(N, 0, -1):  # backward induction
    mover = 0 if k % 2 else 1
    if stop(k)[mover] > cont[mover]:
        choices[k], cont = "d", stop(k)
    else:
        choices[k] = "r"
assert set(choices.values()) == {"d"} and cont == (2, 0)
# Stopping beats being stopped on next node by exactly 1, at every node.
for k in range(1, N):
    m = 0 if k % 2 else 1
    assert stop(k)[m] - stop(k + 1)[m] == 1
assert sum(cont) == 2 and sum((100, 100)) == 200

# ---- Item 30: v = sqrt(eM) + sqrt(eR), 50/50 ex-post split.
eM, eR, sh = sp.symbols("e_M e_R s", positive=True)
v = sp.sqrt(eM) + sp.sqrt(eR)
eM_sep = sp.solve(sp.diff(v / 2 - eM, eM), eM)[0]
eR_sep = sp.solve(sp.diff(v / 2 - eR, eR), eR)[0]
assert eM_sep == eR_sep == sp.Rational(1, 16)
sep = {eM: eM_sep, eR: eR_sep}
payoff_each = (v / 2 - eM).subs(sep)
assert payoff_each == sp.Rational(3, 16)
W_sep = (v - eM - eR).subs(sep)
assert W_sep == sp.Rational(3, 8)
eM_int = sp.solve(sp.diff(v - eM - eR, eM), eM)[0]
assert eM_int == sp.Rational(1, 4)
W_int = (v - eM - eR).subs({eM: eM_int, eR: eM_int})
assert W_int == sp.Rational(1, 2)
assert W_int - W_sep == sp.Rational(1, 8) and (W_int - W_sep) / W_sep == sp.Rational(1, 3)
assert v.subs(sep) == sp.Rational(1, 2) and v.subs({eM: eM_int, eR: eM_int}) == 1
# General share s to M: eM = s^2/4, eR = (1-s)^2/4, W(s) = 1/2 - (s^2 + (1-s)^2)/4.
eMs = sp.solve(sp.diff(sh * v - eM, eM), eM)[0]
eRs = sp.solve(sp.diff((1 - sh) * v - eR, eR), eR)[0]
assert sp.simplify(eMs - sh**2 / 4) == 0 and sp.simplify(eRs - (1 - sh) ** 2 / 4) == 0
Ws = sp.Rational(1, 2) - (sh**2 + (1 - sh) ** 2) / 4
for q in (sp.Rational(1, 10), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(9, 10)):
    assert (v - eM - eR).subs({eM: eMs, eR: eRs}).subs(sh, q) == Ws.subs(sh, q)
assert sp.solve(sp.diff(Ws, sh), sh) == [sp.Rational(1, 2)]
assert Ws.subs(sh, 1) == sp.Rational(1, 4) and Ws.subs(sh, sp.Rational(1, 2)) == W_sep
# One-sided investment (only M invests, eR fixed at 0): giving M everything is efficient.
assert sp.solve(sp.diff(sp.sqrt(eM) - eM, eM), eM)[0] == sp.Rational(1, 4)

# ---- Item 25: TFP script output (synthetic data) and the noise-only 90/10 ratio.
import math, os, subprocess, sys
noise_sd = math.sqrt(0.05**2 + (0.3 * 0.05) ** 2 + (0.5 * 0.05) ** 2)
assert round(noise_sd, 3) == 0.058 and round(math.exp(2 * 1.2816 * noise_sd), 2) == 1.16
out = subprocess.run([sys.executable, "-B", "tfp_example.py"], capture_output=True, text=True,
                     cwd=os.path.dirname(os.path.abspath(__file__)), check=True).stdout
for s_ in ("alpha=0.300  beta=0.502", "90/10 TFP ratio=2.02", "OLS of ln q on ln K, ln L: alpha=0.491",
           "log TFP) = 0.057", "90/10 ratio=2.01", "corr(estimated, true)=0.983"):
    assert s_ in out, s_

print("all B checks passed")
