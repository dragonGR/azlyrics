# python-azlyrics
A simple CLI and *API* to fetch lyrics from azlyrics

## Install
Just do `pip install git+https://github.com/ffmarcos/python-azlyrics`

## Usage
Use with `azlyrics "Lady Gaga" "Telephone"` and it will output the lyric to the screen

if you wish to save to a file, just use the `-s path` flag

## *API*

The *API* is very simple, is composed of five (5) functions:
- `url_from_artist_music(artist, music)` (Generate a valid azlyrics url from an artist and a music title)
- `get_page_from_url(url)` (fetch the page from ~~the upper url~~ a valid url)
- `get_lyrics_from_page(page)` (extract the lyrcs from ~~the upper page~~ a valid azlyrics page)
- `print_artist_music_lyrics(artist, music, lyrics)` (output the lyric with the title being the artist and the music)
- `get_lyrics(artist, music)` does everything above

## Tests
Uses unittest, `python -m unittest -b`
