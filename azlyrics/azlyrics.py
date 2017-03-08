import argparse, sys, re
import urllib.request, urllib.error
from bs4 import BeautifulSoup

from azlyrics.cache import Cache

def normalize_artist_music(artist, music):
    if artist and music:
        artist = re.sub(r'\W+', '', artist.lower())
        music = re.sub(r'\W+', '', music.lower())
    else:
        artist = "rickastley"
        music = "nevergonnagiveyouup"
    return artist, music

def url_from_artist_music(artist, music):
    artist, music = normalize_artist_music(artist, music)
    url = "http://azlyrics.com/lyrics/{}/{}.html".format(artist, music)
    return url

def get_page_from_url(url):
    try:
        page = urllib.request.urlopen(url)
        return page.read() 
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Music not found")
            sys.exit(1)

def get_lyrics_from_page(page):
    soup = BeautifulSoup(page, "html.parser")
    lyrics_tags = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [tag.getText() for tag in lyrics_tags]
    return lyrics

def format_lyrics(lyrics):    
    formated_lyrics = "\n".join(lyrics)
    return formated_lyrics

def save_lyrics_to_file(path, lyrics):
    with open(path, "w") as f:
        f.write(lyrcs)

def get_lyrics(artist, music):
    url = url_from_artist_music(artist, music)
    page = get_page_from_url(url)
    lyrics = get_lyrics_from_page(page)
    return lyrics

def get_args():
    parser = argparse.ArgumentParser(description="Fetch lyric from azlyric")
    parser.add_argument("artist", metavar="Artist", type=str)
    parser.add_argument("music", metavar="Music", type=str)
    parser.add_argument("-s", "--save", metavar="path", help="Save to the file", default=False, dest="path")
    args = parser.parse_args()
    return args

def run():
    args = get_args()
    c = Cache()
    cache_key = '_'.join(normalize_artist_music(args.artist, args.music))
    lyrics = c.get(cache_key)
    if lyrics is None:
        lyrics = format_lyrics(get_lyrics(args.artist, args.music))
        c.add(cache_key, lyrics)
    if args.path:
        save_lyrics_to_file(args.path, lyrics)
    else:
        print("{} by {}".format(args.music, args.artist))
        print(lyrics)
