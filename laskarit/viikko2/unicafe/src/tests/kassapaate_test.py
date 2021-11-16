import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(500)
        self.kortti2 = Maksukortti(100)

    def test_kassapaate_luodaan_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kateisella_lisaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        
    def test_edullisesti_kateisella_palauttaa_erotuksen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)

    def test_edullisesti_kateisella_kaikki_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_edullisesti_kateinen_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kateisella_palauttaa_erotuksen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maukkaasti_kateisella_palauttaa_rahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(150), 150)

    def test_maukkaasti_kateinen_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisesti_kortilla_veloittaa_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 260)

    def test_edullisesti_kortilla_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_edullisesti_kortilla_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kortilla_ei_veloita(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kortti2.saldo, 100)

    def test_edullisesti_kortilla_palauttaa_false(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti2))

    def test_edullisesti_kortilla_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaasti_kortilla_veloittaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_maukkaasti_kortilla_palauttaa_true(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_maukkaasti_kortilla_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kortilla_ei_veloita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kortti2.saldo, 100)
    
    def test_maukkaasti_kortilla_maukkaat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaat_kortilla_palauttaa_false(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti2))

    def test_edullisesti_kassa_ei_muutu_osto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kassa_ei_muutu_osto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2, 100)
        self.assertEqual(self.kortti2.saldo, 200)

    def test_kassa_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_negatiivista_summaa_ei_ladata(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti2, -100)
        self.assertEqual(self.kortti2.saldo, 100)