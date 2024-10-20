from datetime import datetime, timedelta
from SzemelyAuto import Szemelyauto
from TeherAuto import Teherauto
from AutoKolcsonzo import Autokolcsonzo
from Berles import Berles

def menu():
    print("\n--- Autókölcsönző Rendszer ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Autó információ")
    print("5. Kilépés")

def main():
    kolcsonzo = Autokolcsonzo("Test Rent")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5)
    auto2 = Teherauto("DEF-456", "Ford Transit", 15000, 1000)
    auto3 = Szemelyauto("GHI-789", "Honda Civic", 12000, 5)

    kolcsonzo.auto_hozzaadasa(auto1)
    kolcsonzo.auto_hozzaadasa(auto2)
    kolcsonzo.auto_hozzaadasa(auto3)

    datum1 = datetime.today().date() + timedelta(days=1)
    datum2 = datetime.today().date() + timedelta(days=2)

    kolcsonzo.berlesek.append(Berles(auto1, datum1))
    kolcsonzo.berlesek.append(Berles(auto2, datum1))
    kolcsonzo.berlesek.append(Berles(auto3, datum2))
    kolcsonzo.berlesek.append(Berles(auto1, datum2))

    while True:
        menu()
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            rendszam = input("Add meg az autó rendszámát: ")
            datum = datum_input()
            kolcsonzo.auto_berlese(rendszam, datum)
        elif valasztas == "2":
            rendszam = input("Add meg a lemondani kívánt autó rendszámát: ")
            datum = datum_input()
            kolcsonzo.berles_lemondasa(rendszam, datum)
        elif valasztas == "3":
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "4":
            rendszam = input("Add meg az autó rendszámát: ")
            info = kolcsonzo.auto_informacio(rendszam)
            if info:
                print(info)
        elif valasztas == "5":
            print("Köszönjük, hogy használtad a rendszert!")
            break
        else:
            print("Érvénytelen választás. Próbáld újra.")

def datum_input():
    while True:
        datum_str = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            if datum < datetime.today().date():
                print("Nem adhatsz meg múltbéli dátumot.")
                continue
            return datum
        except ValueError:
            print("Hibás dátum formátum. Próbáld újra.")

if __name__ == "__main__":
    main()