from Auto import Auto
from datetime import date

class Berles:
    def __init__(self, auto: Auto, datum: date):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Autó típus: {self.auto.tipus}, Autó rendszám: {self.auto.rendszam}, Dátum: {self.datum}"