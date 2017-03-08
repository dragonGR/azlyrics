import argparse, sys, re
import urllib.request, urllib.error
from bs4 import BeautifulSoup

from azlyrics.cache import Cache

class Azlyrics(object):

    def __init__(self, artist, music):
        self.artist = artist
        self.music = music

    def normalize_str(self, str):
        return re.sub(r'\W+', '', str.lower())

    def normalize_artist_music(self):
        return self.normalize_str(self.artist), self.normalize_str(self.music)


    def url(self):
        if not self.artist and not self.music:
            self.artist = "rickastley"
            self.music = "nevergonnagiveyouup"
        return "http://azlyrics.com/lyrics/{}/{}.html".format(*self.normalize_artist_music())

    def get_page(self):
        try:
            page = urllib.request.urlopen(self.url())
            return page.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("Music not found")
                sys.exit(1)

    def extract_lyrics(self, page):
        soup = BeautifulSoup(page, "html.parser")
        lyrics_tags = soup.find_all("div", attrs={"class": None, "id": None})
        lyrics = [tag.getText() for tag in lyrics_tags]
        return lyrics

    def format_lyrics(self, lyrics):
        formated_lyrics = "\n".join(lyrics)
        return formated_lyrics

    def get_lyrics(self):
        page = self.get_page()
        lyrics = self.extract_lyrics(page)
        return lyrics



def run():
    parser = argparse.ArgumentParser(description="Fetch lyric from azlyric")
    parser.add_argument("artist", metavar="Artist", type=str)
    parser.add_argument("music", metavar="Music", type=str)
    parser.add_argument("-s", "--save", metavar="path", help="Save to the file", default=False, dest="path")
    args = parser.parse_args()

    c = Cache()
    az = Azlyrics(args.artist, args.music)
    cache_key = '_'.join(az.normalize_artist_music())

    lyrics = c.get(cache_key)
    if lyrics is None:
        lyrics = az.format_lyrics(az.get_lyrics())
        c.add(cache_key, lyrics)
    if args.path:
        save_lyrics_to_file(args.path, lyrics)
    else:
        print("{} by {}".format(args.music, args.artist))
        print(lyrics)
