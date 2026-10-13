"""Reference implementation of the 'Two Coherent Systems' companion (M&R 1992, Fig. 4.3, p. 111).

pi(n, b, theta) = m Q + A ln n - S_theta Q / b - h n b / 2 - dc_theta Q,  n >= 1, b > 0,
theta in {specialized (S_s, no premium), flexible (S_f, premium dc per unit)}.

Used to calibrate two_systems.html and to check its read-outs independently
(`python model_two_systems.py`). Fails with AssertionError if a calibration claim breaks.
"""
import math

M = 2.0    # contribution margin per unit before setup, inventory and the flexible premium
S_S = 50.0  # changeover cost of specialized equipment
DEFAULTS = dict(A=20.0, h=1.0, Sf=2.0, dc=1.0, Q=100.0)


def system(A, h, S, Q, dc):
    """Optimum of one equipment regime; returns (n, b, profit, corner?)."""
    n = 2 * A * A / (h * S * Q)
    if n <= 1:
        b = math.sqrt(2 * S * Q / h)
        return 1.0, b, M * Q - S * Q / b - h * b / 2 - dc * Q, True
    b = S * Q / A
    return n, b, M * Q + A * math.log(n) - 2 * A - dc * Q, False


def switch_n(h, Sf, Q, dc):
    """Variety above which flexible equipment gives lower manufacturing cost."""
    return (dc * Q) ** 2 / (2 * Q * h * (math.sqrt(S_S) - math.sqrt(Sf)) ** 2)


def ridge(n, A, h, Sf, dc, Q):
    """Profit along manufacturing's best response (batch and equipment chosen given n)."""
    cs = math.sqrt(2 * S_S * Q * h * n)
    cf = math.sqrt(2 * Sf * Q * h * n) + dc * Q
    return M * Q + A * math.log(n) - min(cs, cf)


def report(A, h, Sf, dc, Q):
    F = system(A, h, S_S, Q, 0.0)
    T = system(A, h, Sf, Q, dc)
    nh = switch_n(h, Sf, Q, dc)
    out = dict(F=F, T=T, nhat=nh, F_coh=F[0] <= nh, T_coh=T[0] >= nh)
    if out["F_coh"] and out["T_coh"]:
        grid = [F[0] * (T[0] / F[0]) ** (k / 4000) for k in range(4001)]
        out["valley"] = min(ridge(n, A, h, Sf, dc, Q) for n in grid)
    return out


def fmt(r):
    f = lambda t: tuple(round(x, 3) if isinstance(x, float) else x for x in t)
    return {k: f(v) if isinstance(v, tuple) else round(v, 3) if isinstance(v, float) else v
            for k, v in r.items()}


if __name__ == "__main__":
    vectors = {
        "default": DEFAULTS,
        "low end": dict(A=5.0, h=0.2, Sf=0.5, dc=0.0, Q=20.0),
        "high end": dict(A=60.0, h=3.0, Sf=20.0, dc=2.0, Q=400.0),
        "A=30 flips": dict(DEFAULTS, A=30.0),
        "dc=0.85 flips": dict(DEFAULTS, dc=0.85),
    }
    for name, v in vectors.items():
        print(f"{name:14s}", v, fmt(report(**v)))
    r = report(**DEFAULTS)
    assert r["F_coh"] and r["T_coh"] and r["F"][2] > r["T"][2] and r["valley"] < r["T"][2]
    r = report(**dict(DEFAULTS, A=30.0))
    assert r["F_coh"] and r["T_coh"] and r["T"][2] > r["F"][2]
    print("calibration claims hold")
