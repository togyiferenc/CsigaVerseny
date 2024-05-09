import random
from csiga import Csiga
from jatekos import Jatekos


class Verseny:
    def __init__(self):
        self.csigak = [
            Csiga("Elso", "zold"),
            Csiga("Masodik", "piros"),
            Csiga("Harmadik", "kek")
        ]
        self.korok_szama = 5
        self.jatekosok = []

    def jatekos_fogadas(self):
        print("Csigák nevei:")
        for csiga in self.csigak:
            print(csiga.nev, ", színe: ", csiga.szin)
        jatekos_szama = int(input("Adja meg a játékosok számát: "))
        for _ in range(jatekos_szama):
            jatekos_nev = input("Adja meg a játékos nevét: ")
            csiga_nev = input("Erre a csigára fogad: ")
            for csiga in self.csigak:
                if csiga.nev == csiga_nev or csiga.szin == csiga_nev:
                    self.jatekosok.append(Jatekos(jatekos_nev, csiga))
                    print(f"{jatekos_nev} fogadott a(z) {csiga_nev} csigára.")
                    break
            else:
                print("Nincs ilyen nevű vagy színű csiga!")
                while True:
                    csiga_nev = input(
                        "Erre a csigára fogad: ")
                    for csiga in self.csigak:
                        if csiga.nev == csiga_nev or csiga.szin == csiga_nev:
                            self.jatekosok.append(Jatekos(jatekos_nev, csiga))
                            print(f"{jatekos_nev} fogadott a(z) {
                                  csiga_nev} csigára.")
                            break
                    else:
                        print("Nincs ilyen nevű vagy színű csiga!")
                        continue
                    break

    def versenyez(self):
        for kor in range(1, self.korok_szama + 1):
            print(f"\n--- {kor}. kör ---")
            self.kor_eredmeny(kor)

            for csiga in self.csigak:
                csiga.gyorsito = False

            kivalasztott_csiga = self.csigak[0]
            if random.random() < 0.2:
                kivalasztott_csiga.gyorsito = True

            for csiga in self.csigak:
                csiga.haladas()
        self.osszesitett_eredmeny()

    def kor_eredmeny(self, kor):
        print(f"\nKör {kor} eredménye:")
        for csiga in self.csigak:
            for jatekos in self.jatekosok:
                if jatekos.csiga == csiga:
                    break
            print(f"{csiga.nev}: Sebesség: {csiga.sebesseg}, Gyorsító: {
                  csiga.gyorsito}, Megtett táv: {csiga.megtett_tav}")
        print()

    def osszesitett_eredmeny(self):
        nyertes_csiga = max(self.csigak, key=lambda x: x.megtett_tav)
        print("\nVerseny végeredmény:")
        for csiga in self.csigak:
            print(f"{csiga.nev}: Megtett táv: {csiga.megtett_tav}")
        print(f"A versenyt a {nyertes_csiga.nev} csiga nyerte, megtett távolság: {
              nyertes_csiga.megtett_tav}")

        nyertesek = [
            jatekos for jatekos in self.jatekosok if jatekos.csiga == nyertes_csiga]
        if nyertesek:
            print("A verseny győztese(i):", ", ".join(
                jatekos.nev for jatekos in nyertesek))
        else:
            print("Nincs győztes játékos.")


if __name__ == "__main__":
    verseny = Verseny()
    verseny.jatekos_fogadas()
    verseny.versenyez()
