# python-azlyrics
A simple CLI and *API* to fetch lyrics from azlyrics

## Install
Just do `pip install git+https://github.com/ffmarcos/python-azlyrics`

## Usage
Use with `azlyrics "Lady Gaga" "Telephone"` and it will output the lyric to the screen

if you wish to save to a file, just use the `-s path` flag

## *API*

The *[API](azlyrics/azlyrics.py)* is very simple, is composed of the `Azlyrics` class with the following usage

`az = Azlyrics("ARTISTA", "MUSIC")`

`az` is composed of seven (7) methods:
- `az.normalize_str(str)` (Make the str valid (no special chars, spaces, lowercase)
- `az.normalize_artist_music()` (Translate the artist and the music to be valid in the url below)
- `az.url()` (Generate a valid azlyrics url from the artist and music suplied in the creation)
- `az.get_page()` (fetch the page from the upper url)
- `az.extract_lyrics(page)` (extract the lyrcs from ~~the upper page~~ a valid azlyrics page)
- `az.get_lyrics()` does everything above
- `az.format_lyrics(lyrics)` (return the lyric formated to print)

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
