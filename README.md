# python-azlyrics
A simple CLI and *API* to fetch lyrics from azlyrics

## Install
Just do `pip install git+https://github.com/ffmarcos/python-azlyrics`

## Usage
Use with `azlyrics "Lady Gaga" "Telephone"` and it will output the lyric to the screen

if you wish to save to a file, just use the `-s path` flag

## *API*

The *[API](azlyrics/azlyrics.py)* is very simple, first you import with `import azlyrics` 

`azlyrics.` package is composed of six (6) functions:
- `normalize_artist_music` (Translate the artist and the music to be valid in the url below)
- `url_from_artist_music(artist, music)` (Generate a valid azlyrics url from an artist and a music title)
- `get_page_from_url(url)` (fetch the page from ~~the upper url~~ a valid url)
- `get_lyrics_from_page(page)` (extract the lyrcs from ~~the upper page~~ a valid azlyrics page)
- `get_lyrics(artist, music)` does everything above
- `format_lyrics(lyrics)` (return the lyric formated to print)

and a *[cache](azlyrics/cache.py)* class `azlyrics.Cache` which upon instatiation creates the folder `~/.cache/azlyrics` 
`c = azlyrics.Cache()`

and is composed of four (4) functions:
- `c.add(key, content)`
- `c.get(key)`
- `c.exists(key)`
- `c.destroy()` (Removes the cache folder)

the format of the *cache* is a file with the name being the key, with the content supplied

## Tests
Uses unittest, `python -m unittest`
