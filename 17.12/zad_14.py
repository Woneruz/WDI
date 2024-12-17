import random
import string
import time

def generuj_losowy_ciag(dlugosc):
    """Generuje losowy ciąg o zadanej długości."""
    znaki = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(znaki) for _ in range(dlugosc))

def licz_rekurencyjnie(dane, warunek, indeks=0, liczba=0):
    """Rekurencyjnie liczy elementy spełniające warunek."""
    if indeks == len(dane):
        return liczba
    if warunek(dane[indeks]):
        liczba += 1
    return licz_rekurencyjnie(dane, warunek, indeks + 1, liczba)

def licz_iteracyjnie(dane, warunek):
    """Iteracyjnie liczy elementy spełniające warunek."""
    liczba = 0
    for znak in dane:
        if warunek(znak):
            liczba += 1
    return liczba

def czy_samogloska(znak):
    """Sprawdza, czy znak jest samogłoską."""
    return znak.lower() in 'aeiou'

def czy_spolgloska(znak):
    """Sprawdza, czy znak jest spółgłoską."""
    return znak.isalpha() and not czy_samogloska(znak)

def czy_cyfra(znak):
    """Sprawdza, czy znak jest cyfrą."""
    return znak.isdigit()

def czy_znak_specjalny(znak):
    """Sprawdza, czy znak jest znakiem specjalnym."""
    return not znak.isalnum()

def main():

    while True:
        try:
            dlugosc = int(input("Podaj długość losowego napisu: "))
            if dlugosc <= 0:
                raise ValueError("Długość musi być liczbą dodatnią.")
            break
        except ValueError as e:
            print(f"Błąd: {e}. Spróbuj ponownie.")

    typy_wyszukiwania = {
        "1": ("samogłoski", czy_samogloska),
        "2": ("spółgłoski", czy_spolgloska),
        "3": ("cyfry", czy_cyfra),
        "4": ("znaki specjalne", czy_znak_specjalny)
    }

    while True:
        print("Wybierz, co chcesz policzyć:")
        print("1 - Samogłoski")
        print("2 - Spółgłoski")
        print("3 - Cyfry")
        print("4 - Znaki specjalne")
        typ_wybor = input("Twój wybór (1/2/3/4): ").strip()
        if typ_wybor in typy_wyszukiwania:
            typ_wyszukiwania, warunek = typy_wyszukiwania[typ_wybor]
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    while True:
        metoda = input("Wybierz metodę (i - iteracyjna, r - rekurencyjna): ").strip().lower()
        if metoda in ["i", "r"]:
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    losowy_ciag = generuj_losowy_ciag(dlugosc)
    print(f"Wygenerowany napis: {losowy_ciag}")

    czas_start = time.time()
    if metoda == "r":
        liczba = licz_rekurencyjnie(losowy_ciag, warunek)
    else:
        liczba = licz_iteracyjnie(losowy_ciag, warunek)
    czas_koniec = time.time()

    print(f"Liczba {typ_wyszukiwania}: {liczba}")
    print(f"Czas wykonania: {czas_koniec - czas_start:.6f} sekund")

main()
