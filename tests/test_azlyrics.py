import unittest, sys

import azlyrics 

class UrlTest(unittest.TestCase):

    def test_normalize_artist_music(self):
        artist, music = azlyrics.normalize_artist_music("ARTISTA", "muSICA")
        self.assertEqual("artista", artist)
        self.assertEqual("musica", music)

    def test_url_default_generate_rick_roll(self):
        expected = "http://azlyrics.com/lyrics/rickastley/nevergonnagiveyouup.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("", ""))

    def test_url_uppercase(self):
        expected = "http://azlyrics.com/lyrics/molejo/cilada.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("Molejo", "CiLada"))

    def test_url_spaces(self):
        expected = "http://azlyrics.com/lyrics/brunoetrio/garimpo.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("Bruno e Trio", "Garimpo"))
    
    @unittest.skip
    def test_url_with_special_chars(self):
        url = ""


class PageTets(unittest.TestCase):

    @unittest.skip("later")
    def test_get_correct_page(self):
        import pprint
        url = "http://azlyrics.com/lyrics/threedaysgrace/goneforever.html"

class LyricTest(unittest.TestCase):
 
    def test_lyric_in_one_div(self):
        expected = ["Run, Run"]
        mock_page = "<div>Run, Run</div>"
        self.assertEqual(expected, azlyrics.get_lyrics_from_page(mock_page));

    def test_lyric_in_two_divs_alone(self):
        expected = ["Run, Run", "Far Away"]
        mock_page = "<div>Run, Run</div><div>Far Away</div>"
        self.assertEqual(expected, azlyrics.get_lyrics_from_page(mock_page));

    def test_lyric_in_two_divs_not_alone(self):
        expected = ["Run, Run", "Far Away"]
        mock_page = "<div>Run, Run</div><p>OKOKOK</p><div>Far Away</div>"
        self.assertEqual(expected, azlyrics.get_lyrics_from_page(mock_page));

class PrintAndSaveTest(unittest.TestCase):

    def test_format_lyric(self):
        expected = "blablabla\n2bla2bla2bla"
        self.assertEqual(expected, azlyrics.format_lyrics(["blablabla", "2bla2bla2bla"]))
