import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        self.pankki_mock = pankki_mock
        self.viitegeneraattori_mock = viitegeneraattori_mock

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "voi", 7)
            if tuote_id == 3:
                return Tuote(3, "pulla", 1)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test1(self):
        """Aloitetaan asiointi, koriin lisätään tuote, jota varastossa on ja
        suoritetaan ostos, eli kutsutaan metodia kaupan tilimaksu, varmista
        että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla,
        tilinumeroilla ja summalla

        Tämä siis on muuten copypaste esimerkistä, mutta assert_called_with-
        metodia käytettävä, jotta voidaan tarkastaa, että parametreilla on
        oikeat arvot
        """
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test2(self):
        """Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta, joita
        varastossa on ja suoritetaan ostos, varmista että kutsutaan pankin
        metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja
        summalla
        """
        kauppa = self.kauppa
        pankki_mock = self.pankki_mock
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 12)

    def test3(self):
        """Aloitetaan asiointi, koriin lisätään kaksi samaa tuotetta, jota on
        varastossa tarpeeksi ja suoritetaan ostos, varmista että kutsutaan
        pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja
        summalla
        """

        kauppa = self.kauppa
        pankki_mock = self.pankki_mock
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 10)

    def test4(self):
        """Aloitetaan asiointi, koriin lisätään tuote, jota on varastossa
        tarpeeksi ja tuote joka on loppu ja suoritetaan ostos, varmista
        että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla,
        tilinumerolla ja summalla
        """

        kauppa = self.kauppa
        pankki_mock = self.pankki_mock
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        # tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)