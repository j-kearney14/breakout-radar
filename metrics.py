import pandas as pd, glob

snapshots = sorted(glob.glob("snapshots/snapshot_*.csv"))
if len(snapshots) < 2:
    raise SystemExit("Need at least 2 snapshots")

latest, prev = snapshots[-1], snapshots[-2]

now  = pd.read_csv(latest)
prev = pd.read_csv(prev)

m = now.merge(prev, on="artist", suffixes=("_now", "_prev"))
m["followers_delta_%"] = 100 * (m["followers_now"] - m["followers_prev"]) / m["followers_prev"]
m.to_csv("latest_metrics.csv", index=False)
print("✓ Wrote latest_metrics.csv")
