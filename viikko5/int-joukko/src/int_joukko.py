class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            return True
        False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm >= len(self.ljono):
                self.ljono = self.ljono + [0]*self.kasvatuskoko

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.ljono[i] for i in range(self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            x.lisaa(a)

        for b in b_taulu:
            x.lisaa(b)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            for b in b_taulu:
                if a == b:
                    y.lisaa(b)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a in a_taulu:
            z.lisaa(a)

        for b in b_taulu:
            z.poista(b)
        return z

    def __str__(self):
        ljono_str = [str(_) for _ in self.ljono[:self.alkioiden_lkm]]
        return "{" + ", ".join(ljono_str) + "}"