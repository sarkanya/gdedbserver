from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, max_utasok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.max_utasok_szama = max_utasok_szama

    def get_info(self) -> str:
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Utasok maximum száma: {self.max_utasok_szama}"