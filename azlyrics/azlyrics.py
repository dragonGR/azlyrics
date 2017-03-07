from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import argparse, sys

def url_from_artist_music(artist, music):
    if artist and music:
        artist = artist.lower().replace(" ", "")
        music = music.lower().replace(" ", "")
    else:
        artist = "rickastley"
        music = "nevergonnagiveyouup"

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

def print_artist_music_lyric(artist, music, lyrics):    
    print("{} by {}".format(music, artist), end="\n")
    for line in lyrics:
        print(line, end="\n\n")

def save_lyrics_to_file(path):
    with open(path, "w") as f:
        f.write("\n".join(lyrics).strip())

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
    lyrics = get_lyrics(args.artist, args.music)
    if args.path:
        save_lyrics_to_file(args.path)
    else:
        print_artist_music_lyric(args.artist, args.music, lyrics)
