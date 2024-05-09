import random


class Csiga:
    def __init__(self, nev, szin):
        self.nev = nev
        self.szin = szin
        self.sebesseg = 0
        self.gyorsito = False
        self.megtett_tav = 0

    def haladas(self):
        # Generálunk egy véletlenszerű sebességet 0 és 3 között
        self.sebesseg = random.randint(0, 3)

        if self.gyorsito:
            self.megtett_tav += self.sebesseg * 2
        else:
            self.megtett_tav += self.sebesseg
