from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostos_oliot_list = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return sum([_ostos.lukumaara() for _ostos in self.ostokset()])
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum(ostos_olio.hinta() for ostos_olio in self.ostokset())

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos_olio in self.ostokset():
            if ostos_olio.tuote == lisattava:
                ostos_olio.muuta_lukumaaraa(1)
                return
        self._ostos_oliot_list.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostos_oliot_list
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
