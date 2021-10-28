import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

secrets_file = "../../../../secrets/spotify.json"

with open(secrets_file) as f:
    data = json.load(f)

CLIENT_ID = data.get("CLIENT_ID")
CLIENT_SECRET = data.get("CLIENT_SECRET")
PLAYLIST_ID = data.get("PLAYLIST_ID")
REDIRECT_URI = data.get("REDIRECT_URI")
RANK = "rank"
SONG = "song"
ARTIST = "artist"


def get_date():
    pattern = re.compile(r"[1-2]\d{3}-[0-1]\d-[0-3]\d")
    date_input = input("Which year do you want to travel to? Type date in format YYYY-MM-DD: ")
    while not pattern.match(date_input):
        date_input = input("This doesn't look like real date! Enter correct format YYYY-MM-DD: ")
        if date_input in ["exit", "quit", "abort", "break"]:
            break
    return date_input


def create_url(selected_date):
    return f"https://www.billboard.com/charts/hot-100/{selected_date}"


def get_page_content(web_url):
    return requests.get(web_url).text


def parse_page(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    song_names = [song_name.getText() for song_name in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]
    artists = [artist.getText() for artist in soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")]
    ranks = [rank.getText() for rank in soup.find_all(name="span", class_="chart-element__rank__number")]
    songs = []
    if len(song_names) == len(artists) == len(ranks):
        for index in range(len(ranks)):
            songs.append({RANK: ranks[index], SONG: song_names[index], ARTIST: artists[index]})
    return songs


def create_lines(songs):
    lines = []
    for song in songs:
        lines.append(f"#{song.get(RANK)}\nsong: {song.get(SONG)}\nartist: {song.get(ARTIST)}\n")
    return lines


def run_spotipy(date, tracks):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=REDIRECT_URI,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    track_ids = []
    for track in tracks:
        query = f"track: {track.get(SONG)} artist: {track.get(ARTIST)}"
        result = sp.search(query)
        if len(result.get("tracks").get("items")) > 0:
            track_ids.append(result.get("tracks").get("items")[0].get("id"))

    sp.playlist_replace_items(PLAYLIST_ID, track_ids)


def print_in_file(lines, day):
    with open(f"top_100_on_{day}", "w") as output_file:
        for line in lines:
            output_file.write(line)


if __name__ == '__main__':
    input_date = get_date()
    url = create_url(input_date)
    page_content = get_page_content(url)
    tracks = parse_page(page_content)
    lines = create_lines(tracks)
    print_in_file(lines, input_date)
    run_spotipy(input_date, tracks)
