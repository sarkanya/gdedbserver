from datetime import date
from Berles import Berles
from Auto import Auto

class Autokolcsonzo:
    def __init__(self, nev: str):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadasa(self, auto : Auto):
        self.autok.append(auto)

    def auto_berlese(self, rendszam: str, datum : date) -> int | None:
        auto = self.get_auto_by_rendszam(rendszam)
        if not auto:
            print("Nincs autó ilyen rendszámmal a rendszerben.")
            return None

        if not self.is_auto_berelheto(auto, datum):
            print("Az autó már foglalt a megadott napon.")
            return None

        uj_berles = Berles(auto, datum)
        self.berlesek.append(uj_berles)
        print(f"Sikeres bérlés! Bérleti díj: {auto.berleti_dij} Ft")
        return auto.berleti_dij

    def berles_lemondasa(self, rendszam: str, datum: date):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print("A bérlés sikeresen lemondva.")
                return
        print("Nincs ilyen bérlés.")

    def berlesek_listazasa(self):
        if not self.berlesek:
            print("Nincsenek aktív bérlések.")
            return
        for berles in self.berlesek:
            print(berles)

    def auto_informacio(self, rendszam: str) -> str | None:
        auto = self.get_auto_by_rendszam(rendszam)
        if not auto:
            print("Nincs autó ilyen rendszámmal a rendszerben.")
            return None

        return auto.get_info()

    def get_auto_by_rendszam(self, rendszam: str) -> Auto:
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto
        return None

    def is_auto_berelheto(self, auto:Auto, datum: date) -> bool:
        for berles in self.berlesek:
            if berles.auto.rendszam == auto.rendszam and berles.datum == datum:
                return False
        return True