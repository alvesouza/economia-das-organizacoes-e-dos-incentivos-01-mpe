"""TFP and its dispersion by Cabral's cost-share method (Section 3.1, eqs. 3.1-3.2, pp. 39-40).

SYNTHETIC DATA by default: the firms below are simulated (seeded), not real evidence.
To use a real firm-level dataset, pass a CSV with columns q, K, L, p, r, w (one row per firm,
same industry and year; q = output quantity or deflated revenue, p = output price, r = user
cost of capital, w = wage):   python tfp_example.py firms.csv
"""
import sys
import numpy as np


def estimate_tfp(q, K, L, p, r, w):
    """Cabral's method: alpha, beta = mean revenue shares of capital and labour costs;
    ln(omega_i) = ln q_i - alpha ln K_i - beta ln L_i. Arrays of equal length; returns
    (alpha, beta, ln_omega). Valid under price taking, profit maximization and a common
    Cobb-Douglas technology (assumptions a-c, p. 39)."""
    alpha = np.mean(r * K / (p * q))
    beta = np.mean(w * L / (p * q))
    return alpha, beta, np.log(q) - alpha * np.log(K) - beta * np.log(L)


def synthetic(n=500, alpha=0.3, beta=0.5, sd_tfp=0.27, seed=2017):
    """Price-taking, profit-maximizing firms with TFP dispersion sd_tfp (log points), input
    prices that vary by firm, input-choice errors and output measurement error."""
    g = np.random.default_rng(seed)
    ln_omega = g.normal(0.0, sd_tfp, n)
    p = np.ones(n)                                  # assumption (a): common output price
    r = np.exp(g.normal(np.log(0.10), 0.10, n))
    w = np.exp(g.normal(np.log(1.00), 0.10, n))
    # Optimal output: q = [omega (alpha p/r)^alpha (beta p/w)^beta]^(1/(1-alpha-beta)).
    ln_q = (ln_omega + alpha * np.log(alpha * p / r) + beta * np.log(beta * p / w)) / (1 - alpha - beta)
    K = alpha * p * np.exp(ln_q) / r * np.exp(g.normal(0, 0.05, n))   # input-choice error
    L = beta * p * np.exp(ln_q) / w * np.exp(g.normal(0, 0.05, n))
    q = np.exp(alpha * np.log(K) + beta * np.log(L) + ln_omega + g.normal(0, 0.05, n))
    return q, K, L, p, r, w, ln_omega


def summary(ln_omega):
    d = ln_omega - ln_omega.mean()
    p90, p10 = np.percentile(d, [90, 10])
    return d.std(), np.exp(p90 - p10)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = np.genfromtxt(sys.argv[1], delimiter=",", names=True)
        q, K, L, p, r, w = (data[c] for c in ("q", "K", "L", "p", "r", "w"))
        true = None
        print(f"CSV DATA from {sys.argv[1]}: {len(q)} firms")
    else:
        q, K, L, p, r, w, true = synthetic()
        print("SYNTHETIC DATA (seed 2017), 500 simulated firms; true alpha=0.30, beta=0.50")
    a, b, ln_om = estimate_tfp(q, K, L, p, r, w)
    sd, r9010 = summary(ln_om)
    print(f"cost-share estimates: alpha={a:.3f}  beta={b:.3f}")
    print(f"log TFP: sd={sd:.3f}   90/10 TFP ratio={r9010:.2f}")
    X = np.column_stack([np.ones(len(q)), np.log(K), np.log(L)])
    coef = np.linalg.lstsq(X, np.log(q), rcond=None)[0]
    print(f"naive OLS of ln q on ln K, ln L: alpha={coef[1]:.3f}  beta={coef[2]:.3f}")
    lp = np.log(p * q / L)
    print(f"corr(log labour productivity, log TFP) = {np.corrcoef(lp, ln_om)[0, 1]:.3f}")
    if true is not None:
        sd0, r0 = summary(true)
        print(f"true log TFP: sd={sd0:.3f}   90/10 ratio={r0:.2f}   "
              f"corr(estimated, true)={np.corrcoef(ln_om, true)[0, 1]:.3f}")
        assert abs(a - 0.3) < 0.02 and abs(b - 0.5) < 0.02 and np.corrcoef(ln_om, true)[0, 1] > 0.9
