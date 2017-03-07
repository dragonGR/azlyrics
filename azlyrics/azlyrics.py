from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

def url_from_artist_music(artist, music):
        if artist and music:
            artist = artist.lower().replace(" ", "")
            music = music.lower().replace(" ", "")
        else:
            artist = "rickastley"
            music = "nevergonnagiveyouup"

        url = "https://azlyrics.com/lyrics/{}/{}.html".format(artist, music)
        return url
        
def processing(generate_url, artist, title, save):
    response = urllib.request.urlopen(generate_url)
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics)
    lyrics = soup.find_all("div", attrs={"class": None, "id": None})
    lyrics = [x.getText() for x in lyrics]
    printing(artist, title, save, lyrics)
    
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
