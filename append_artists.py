from dotenv import load_dotenv
import os, csv, spotipy

load_dotenv(".env", override=True)

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
)

new_names = ["Inhaler", "MOIO", "Monjola", "Fizzy Orange", "Annie-Dog", "Kojaque"]

# build a set of artists already in the CSV (first column)
with open("artists.csv") as f:
    existing = {row.split(",")[0] for row in f.read().splitlines()[1:]}  # skip header

with open("artists.csv", "a", newline="") as f:
    w = csv.writer(f)
    for name in new_names:
        if name in existing:
            print(f"• {name} already listed – skipped")
            continue
        res = sp.search(q=name, type="artist", limit=1)["artists"]["items"]
        if res:
            w.writerow([name, res[0]["id"]])
            print(f"✓ added {name}")
        else:
            print(f"✗ {name} not found – check spelling")
