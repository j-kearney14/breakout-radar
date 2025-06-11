from dotenv import load_dotenv
import os, csv, pandas as pd, spotipy, pathlib

# 1️⃣  load keys
load_dotenv(".env", override=True)

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
)

# 2️⃣  read the artist list
rows = []
with open("artists.csv") as f:
    for name, sp_id in csv.reader(f):
        if name == "artist_name":          # skip header
            continue
        a = sp.artist(sp_id)
        rows.append({
            "timestamp": pd.Timestamp.utcnow(),
            "artist": a["name"],
            "followers": a["followers"]["total"],
            "popularity": a["popularity"]
        })

df = pd.DataFrame(rows)

# 3️⃣  write to snapshots/
snap_dir = pathlib.Path("snapshots")
snap_dir.mkdir(exist_ok=True)

outfile = snap_dir / f"snapshot_{pd.Timestamp.utcnow():%Y%m%d_%H%M%S}.csv"
df.to_csv(outfile, index=False)
print(f"✓ Saved {outfile}")
