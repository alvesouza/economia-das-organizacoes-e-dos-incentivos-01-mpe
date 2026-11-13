"""Exact helpers shared by check_T1.py, check_T2.py, check_T3.py (Lecture 8 solutions).

Bimatrix Nash equilibria (pure, and mixed on a rational grid), and pure-strategy perfect
Bayesian equilibria of finite signaling games, all in Fractions.
"""
from fractions import Fraction as F
from itertools import product


def pure_ne(A, B):
    """Pure Nash equilibria (row, col) of the bimatrix (A, B), lists of lists."""
    R, C = len(A), len(A[0])
    return {(r, c) for r in range(R) for c in range(C)
            if A[r][c] == max(A[k][c] for k in range(R))
            and B[r][c] == max(B[r][k] for k in range(C))}


def simplex(n, k):
    """All probability vectors of length k with entries multiples of 1/n."""
    def rec(left, parts):
        if parts == 1:
            yield (left,)
            return
        for i in range(left + 1):
            for rest in rec(left - i, parts - 1):
                yield (i,) + rest
    return [tuple(F(x, n) for x in v) for v in rec(n, k)]


def is_ne(A, B, p, q):
    """Is the mixed profile (p, q) a Nash equilibrium of (A, B)?"""
    R, C = len(A), len(A[0])
    u1 = [sum(A[r][c] * q[c] for c in range(C)) for r in range(R)]
    u2 = [sum(B[r][c] * p[r] for r in range(R)) for c in range(C)]
    return (all(p[r] == 0 or u1[r] == max(u1) for r in range(R))
            and all(q[c] == 0 or u2[c] == max(u2) for c in range(C)))


def grid_ne(A, B, n):
    """All Nash equilibria whose probabilities are multiples of 1/n."""
    R, C = len(A), len(A[0])
    return [(p, q) for p in simplex(n, R) for q in simplex(n, C) if is_ne(A, B, p, q)]


def bayes_game(prior, allowed, nact, US, UR):
    """Normal form of a signaling game.

    prior[t]; allowed[t] = list of messages type t may send; nact[m] = number of replies
    after message m; US[t][m][a], UR[t][m][a] payoffs. Rows = sender strategies (tuple
    of one message per type), columns = receiver strategies (tuple of one reply per message).
    """
    T, M = len(prior), len(nact)
    rows = list(product(*[allowed[t] for t in range(T)]))
    cols = list(product(*[range(nact[m]) for m in range(M)]))
    A = [[sum(prior[t] * US[t][s[t]][c[s[t]]] for t in range(T)) for c in cols] for s in rows]
    B = [[sum(prior[t] * UR[t][s[t]][c[s[t]]] for t in range(T)) for c in cols] for s in rows]
    return rows, cols, A, B


def best_replies(mu, m, nact, UR):
    """Replies after message m that are optimal for belief mu (tuple over types)."""
    ev = [sum(mu[t] * UR[t][m][a] for t in range(len(mu))) for a in range(nact[m])]
    return {a for a in range(nact[m]) if ev[a] == max(ev)}


def pure_pbe(prior, allowed, nact, US, UR, n=60):
    """Pure-strategy PBE of a signaling game.

    Returns a list of (sender strategy, receiver strategy, off-path beliefs) where the
    off-path beliefs are, for each message nobody sends, the list of grid beliefs (multiples
    of 1/n) that make the receiver's reply a best reply. Bayes' rule fixes beliefs after the
    messages that are sent.
    """
    T, M = len(prior), len(nact)
    out = []
    for s in product(*[allowed[t] for t in range(T)]):
        for c in product(*[range(nact[m]) for m in range(M)]):
            # sender optimality
            if any(US[t][s[t]][c[s[t]]] < max(US[t][m][c[m]] for m in allowed[t])
                   for t in range(T)):
                continue
            ok, offp = True, {}
            for m in range(M):
                senders = [t for t in range(T) if s[t] == m]
                if senders:
                    tot = sum(prior[t] for t in senders)
                    mu = tuple((prior[t] / tot) if t in senders else F(0) for t in range(T))
                    ok &= c[m] in best_replies(mu, m, nact, UR)
                else:
                    good = [mu for mu in simplex(n, T)
                            if all(mu[t] == 0 or m in allowed[t] for t in range(T))
                            and c[m] in best_replies(mu, m, nact, UR)]
                    offp[m] = good
                    ok &= bool(good)
            if ok:
                out.append((s, c, offp))
    return out



def eq_dominated(t, m, utility, US, nact):
    """Message m is equilibrium-dominated for type t: U*(t) > best payoff t can get from m."""
    return utility > max(US[t][m][a] for a in range(nact[m]))


def dominated(t, m, US, nact, M):
    """Message m is dominated for type t (Gibbons Def. before Signaling Requirement 5)."""
    worst = lambda k: min(US[t][k][a] for a in range(nact[k]))
    best = max(US[t][m][a] for a in range(nact[m]))
    return any(worst(k) > best for k in range(M) if k != m)


def refine(prior, allowed, nact, US, UR, n=60, rule="eq-dominated"):
    """PBE that also satisfy Signaling Requirement 6 (rule='eq-dominated', the intuitive
    criterion) or 5 (rule='dominated'): at every off-path message the belief puts zero weight
    on the types for which it is (equilibrium-)dominated, unless it is so for all types that
    can send it. Returns (survivors, failures) as lists of (sender strategy, reply profile)."""
    T, M = len(prior), len(nact)
    keep, drop = [], []
    for s, c, offp in pure_pbe(prior, allowed, nact, US, UR, n):
        util = [US[t][s[t]][c[s[t]]] for t in range(T)]
        ok = True
        for m, good in offp.items():
            can = [t for t in range(T) if m in allowed[t]]
            if rule == "eq-dominated":
                dom = {t for t in can if eq_dominated(t, m, util[t], US, nact)}
            else:
                dom = {t for t in can if dominated(t, m, US, nact, M)}
            if len(dom) < len(can):
                good = [mu for mu in good if all(mu[t] == 0 for t in dom)]
            ok &= bool(good)
        (keep if ok else drop).append((s, c))
    return keep, drop
