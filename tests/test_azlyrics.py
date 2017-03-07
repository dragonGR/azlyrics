import unittest

from azlyrics import azlyrics 

class UrlTest(unittest.TestCase):

    def test_url_default_generate_rick_roll(self):
        expected = "https://azlyrics.com/lyrics/rickastley/nevergonnagiveyouup.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("", ""))

    def test_url_uppercase(self):
        expected = "https://azlyrics.com/lyrics/molejo/cilada.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("Molejo", "CiLada"))

    def test_url_spaces(self):
        expected = "https://azlyrics.com/lyrics/brunoetrio/garimpo.html"
        self.assertEqual(expected, azlyrics.url_from_artist_music("Bruno e Trio", "Garimpo"))

