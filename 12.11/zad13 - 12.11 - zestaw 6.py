# Sortowanie słownika zagnieżdżonego po wartościach - sortowanie cen rzeczy w sklepach

def wprowadz_zagniezdzony_slownik():
    zagniezdzony_slownik = {} # słownik sklepów customowych
    while True:
        sklep = input("Podaj nazwę sklepu (lub 'stop' aby zakończyć): ")
        if sklep.lower() == 'stop':
            break
        zagniezdzony_slownik[sklep] = {} # słownik w słowniku, ceny dla poszczególnych sklepów
        while True:
            owoc = input(f"Podaj nazwę owocu dla sklepu {sklep} (lub 'stop' aby zakończyć): ")
            if owoc.lower() == 'stop':
                break
            cena = wprowadz_int(f"Podaj cenę dla {owoc} w sklepie {sklep}: ")
            zagniezdzony_slownik[sklep][owoc] = cena # Dodajemy owoc jako w słowniku sklepu i przypisujemy mu cenę
    return zagniezdzony_slownik


def wprowadz_int(liczba):
    while True:
        try:
            return int(input(liczba)) # konwersja na int
        except ValueError:
            print("Błąd: nie można przekonwertować na liczbę.")


def sortuj_zagniezdzony_slownik_po_wartosciach(zagniezdzony_slownik, rosnaco=True):
    posortowany_slownik = {}
    for sklepik, wartosc in zagniezdzony_slownik.items():
        posortowany_slownik[sklepik] = dict(sorted(wartosc.items(), key=lambda item: item[1], reverse=not rosnaco)) # jeśli rosnaco jest true to z not bedzie false, czyli od najmniejszej i na odwrót
    return posortowany_slownik #


def interakcja():
    wybor = input("Czy chcesz posortować wartości testowe czy własne? (test/wlasne): ").strip().lower()
    if wybor == 'test':
        testowy_slownik = {'Lidl': {'Jabłka': 5, 'Pomarańcze': 2, 'Gruszki': 14},
                           'Kaufland': {'Jabłka': 15, 'Pomarańcze': 7, 'Gruszki': 2},
                           'Aldi': {'Jabłka': 5, 'Pomarańcze': 50, 'Gruszki': 20}}
    elif wybor == 'wlasne':
        testowy_slownik = wprowadz_zagniezdzony_slownik()
    else:
        print("Nieprawidłowy wybór.")
        return

    kierunek = input("Czy chcesz posortować rosnąco czy malejąco? (rosnaco/malejaco): ").strip().lower()
    if kierunek == 'rosnaco':
        rosnaco = True
    elif kierunek == 'malejaco':
        rosnaco = False
    else:
        print("Nieprawidłowy wybór.")
        return

    posortowany_slownik = sortuj_zagniezdzony_slownik_po_wartosciach(testowy_slownik, rosnaco)

    for sklep, owoce in posortowany_slownik.items():
        print(f"{sklep}: {owoce}")



interakcja()