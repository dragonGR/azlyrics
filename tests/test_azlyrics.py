import unittest, sys

from azlyrics import Azlyrics, Cache

class UrlTest(unittest.TestCase):

    def test_normalize_artist_music(self):
        az = Azlyrics("Artista", "MUsica")
        artist, music = az.normalize_artist_music()
        self.assertEqual("artista", artist)
        self.assertEqual("musica", music)

    def test_url_default_generate_rick_roll(self):

        expected = "http://azlyrics.com/lyrics/rickastley/nevergonnagiveyouup.html"
        az = Azlyrics("", "")
        self.assertEqual(expected, az.url())

    def test_url_uppercase(self):
        expected = "http://azlyrics.com/lyrics/molejo/cilada.html"
        az = Azlyrics("MOLEJO", "CILADA")
        self.assertEqual(expected, az.url())

    def test_url_spaces(self):
        expected = "http://azlyrics.com/lyrics/brunoetrio/garimpo.html"
        az = Azlyrics("Bruno e Trio", "Garimpo")
        self.assertEqual(expected, az.url())
    
    def test_url_with_special_chars(self):
        expected = "http://azlyrics.com/lyrics/legiaourbana/tempoperdido.html"
        az = Azlyrics("Legião Urbana", "Tempo Perdido")
        self.assertEqual(expected, az.url())


class PageTets(unittest.TestCase):

    @unittest.skip("later")
    def test_get_correct_page(self):
        import pprint
        url = "http://azlyrics.com/lyrics/threedaysgrace/goneforever.html"

class LyricTest(unittest.TestCase):
 
    def test_lyric_in_one_div(self):
        expected = ["Run, Run"]
        mock_page = "<div>Run, Run</div>"
        az = Azlyrics("", "")
        self.assertEqual(expected, az.extract_lyrics(mock_page))

    def test_lyric_in_two_divs_alone(self):
        expected = ["Run, Run", "Far Away"]
        mock_page = "<div>Run, Run</div><div>Far Away</div>"
        az = Azlyrics("", "")
        self.assertEqual(expected, az.extract_lyrics(mock_page))

    def test_lyric_in_two_divs_not_alone(self):
        expected = ["Run, Run", "Far Away"]
        mock_page = "<div>Run, Run</div><p>OKOKOK</p><div>Far Away</div>"
        az = Azlyrics("", "")
        self.assertEqual(expected, az.extract_lyrics(mock_page))

class PrintAndSaveTest(unittest.TestCase):

    def test_format_lyric(self):
        expected = "blablabla\n2bla2bla2bla"
        az = Azlyrics("", "")
        self.assertEqual(expected, az.format_lyrics(["blablabla", "2bla2bla2bla"]))

class CacheTest(unittest.TestCase):
    
    @unittest.skip
    def create_cache(self):
        return 
