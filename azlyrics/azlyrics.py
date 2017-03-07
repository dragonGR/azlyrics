from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

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
    page = urllib.request.urlopen(url)
    return page.read() 

def get_lyrics_from_page(page):
    soup = BeautifulSoup(page, "html.parser")
    lyrics_tags = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [tag.getText() for tag in lyrics_tags]
    return lyrics

def printing(artist, title, save, lyrics):    
    for x in lyrics:
        print(x, end="\n\n")
    if save == True:
        saving(artist, title, lyrics)
    elif save == False:
        pass
            
def saving(artist, title, lyrics):
        f = open(artist + '_' + title + '.txt', 'w')
        f.write("\n".join(lyrics).strip())
        f.close()
