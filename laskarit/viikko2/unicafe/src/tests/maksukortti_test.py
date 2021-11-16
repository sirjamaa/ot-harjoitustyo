import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertIs(self.maksukortti.saldo, 10)

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_laskee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(15)
        self.assertIs(self.maksukortti.saldo, 10)

    def test_true_jos_rahat_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(1))
        self.assertFalse(self.maksukortti.ota_rahaa(11))