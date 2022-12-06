class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tulokset = [self.tulos]

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self.tulokset.append(self.tulos)

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self.tulokset.append(self.tulos)

    def nollaa(self):
        self.tulos = 0
        self.tulokset.append(self.tulos)

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        self.tulokset.append(self.tulos)

    def kumoa(self):
        self.tulos = self.tulokset[-2]
        self.tulokset.pop()
