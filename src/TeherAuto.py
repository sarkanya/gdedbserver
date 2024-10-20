from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, max_teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self.max_teherbiras = max_teherbiras

    def get_info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij} Ft/nap, Maximum teherbírás: {self.max_teherbiras} kg"