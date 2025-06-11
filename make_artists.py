from dotenv import load_dotenv
import os, csv, spotipy

load_dotenv(".env", override=True)

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"))
)

names = ["Kneecap", "CMAT", "NewDad", "SELLÓ", "Aby Coulibaly"]

with open("artists.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["artist_name", "spotify_id"])
    for n in names:
        res = sp.search(q=n, type="artist", limit=1)["artists"]["items"]
        if res:
            w.writerow([n, res[0]["id"]])
            print(f"✓ {n}")
        else:
            print(f"✗ {n} not found")