"""Joint-speed graph of a rig shot (role 05 §2).

usage: /root/.venvs/motion/bin/python -I joint_speed.py joints.json out.png [joint ...] [--lag parent:child ...]
joints.json: {"fps": 30, "joints": {"name": [[x, y], ...]}} — screen px, one point per frame.
Prints per joint: max speed, dead holds (< HOLD_V px/f for >= HOLD_F frames), pops (|accel| > POP_K x median
and > POP_MIN), fast frames (> FAST_V px/f: smear candidates); per --lag pair: frames by which the child trails
the parent (peak of the cross-correlation of their speeds within +-12 frames — read it together with the graph).
Thresholds are starting values; tune them on probes the owner approved.
"""
import json
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HOLD_V, HOLD_F, POP_K, POP_MIN, FAST_V, MAX_LAG = 0.3, 8, 6.0, 4.0, 30.0, 12


def runs(mask):
    out, start = [], None
    for i, m in enumerate(list(mask) + [False]):
        if m and start is None:
            start = i
        elif not m and start is not None:
            out.append((start, i - 1))
            start = None
    return out


def speed(points):
    p = np.asarray(points, float)
    return np.r_[0.0, np.linalg.norm(np.diff(p, axis=0), axis=1)]


def main():
    src, dst, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
    cut = rest.index("--lag") if "--lag" in rest else len(rest)
    pick, lags = rest[:cut], [a.split(":") for a in rest[cut + 1 :]]
    data = json.load(open(src))
    joints = data["joints"]
    fig, ax = plt.subplots(figsize=(14, 6), dpi=110)
    for name in pick or list(joints):
        v = speed(joints[name])
        acc = np.abs(np.r_[0.0, np.diff(v)])
        med = np.median(acc[acc > 0]) if np.any(acc > 0) else 0.0
        holds = [(s, e) for s, e in runs(v < HOLD_V) if e - s + 1 >= HOLD_F and s > 0]
        pops = [int(i) for i in np.where((acc > POP_K * med) & (acc > POP_MIN))[0]]
        fast = [(s, e) for s, e in runs(v > FAST_V)]
        print(f"{name:12s} max {v.max():6.1f} px/f  holds {holds or '-'}  pops {pops or '-'}  fast {fast or '-'}")
        ax.plot(v, lw=1.2, label=name)
    for a, b in lags:
        x, y = speed(joints[a]), speed(joints[b])
        x, y = x - x.mean(), y - y.mean()
        n = len(x)
        lag = max(
            range(-MAX_LAG, MAX_LAG + 1),
            key=lambda s: float(np.dot(x[max(0, -s) : n - max(0, s)], y[max(0, s) : n - max(0, -s)])),
        )
        print(f"lag {a} -> {b}: {lag} f")
    ax.set_xlabel(f"frame ({data.get('fps', 30)} fps)")
    ax.set_ylabel("speed, px/frame")
    ax.grid(alpha=0.3)
    ax.legend(ncol=6, fontsize=8)
    fig.tight_layout()
    fig.savefig(dst)


if __name__ == "__main__":
    main()
