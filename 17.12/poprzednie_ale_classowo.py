import random

# Klasa bazowa dla figur
class Figura:
    def __init__(self, wiersz, kolumna):
        self.wiersz = wiersz
        self.kolumna = kolumna

    def pozycja(self):
        return self.wiersz, self.kolumna

class Wieza(Figura):
    def atakuje(self, inna_figura):
        return self.wiersz == inna_figura.wiersz or self.kolumna == inna_figura.kolumna

class Goniec(Figura):
    def atakuje(self, inna_figura):
        return abs(self.wiersz - inna_figura.wiersz) == abs(self.kolumna - inna_figura.kolumna)

class Hetman(Wieza, Goniec):
    def atakuje(self, inna_figura):
        return Wieza.atakuje(self, inna_figura) or Goniec.atakuje(self, inna_figura)

# Rozmiar szachownicy i lista przechowująca pozycje hetmanów
rozmiar_szachownicy = 100
hetmany = []  # Lista pozycji hetmanów [(w1, k1), (w2, k2), ...] - jak w poleceniu

# Funkcja dodająca hetmana na szachownicę
def dodaj_hetmana(wiersz, kolumna):
    if 1 <= wiersz <= rozmiar_szachownicy and 1 <= kolumna <= rozmiar_szachownicy:  # Sprawdzenie poprawności pozycji
        nowy_hetman = Hetman(wiersz, kolumna)
        if not any(h.wiersz == wiersz and h.kolumna == kolumna for h in hetmany):  # Czy pozycja nie jest zajęta
            hetmany.append(nowy_hetman)  # Dodanie pozycji hetmana do listy
        else:
            raise ValueError(f"Na pozycji ({wiersz}, {kolumna}) nie może znajdować się hetman, ponieważ jest atakowana.")
    else:
        raise ValueError("Pozycja poza zakresem szachownicy.")  # Jeśli pozycja poza plansza

# Funkcja losowo N hetmanów
def losowe_hetmany(n):
    global hetmany  # Używamy globalnej listy hetmany
    hetmany = []  # Czyścimy listę
    while len(hetmany) < n:  # Dopóki nie ustawimy N hetmanów
        wiersz = random.randint(1, rozmiar_szachownicy)
        kolumna = random.randint(1, rozmiar_szachownicy)
        try:
            dodaj_hetmana(wiersz, kolumna)  # Dodajemy hetmana
        except ValueError:
            continue

# Funkcja sprawdzająca czy hetmany się nie szachują
def czy_szach():
    for i in range(len(hetmany)):  # Pętla po każdym hetmanie
        for j in range(i + 1, len(hetmany)):  # Porównujemy go z kolejnymi hetmanami
            if hetmany[i].atakuje(hetmany[j]):
                return False  # Hetmany się szachują
    return True  # Żadne hetmany się nie szachują

# Funkcja wizualizująca szachownicę
def wizualizuj(plik="szachownica.txt"):
    # Tworzymy pustą szachownicę
    szachownica = [["." for _ in range(rozmiar_szachownicy)] for _ in range(rozmiar_szachownicy)]
    for hetman in hetmany:  # Umieszczamy hetmanów na planszy
        wiersz, kolumna = hetman.pozycja()
        szachownica[wiersz - 1][kolumna - 1] = "H"

    # Zapis szachownicy do pliku
    with open(plik, "w") as f:
        for w in szachownica:
            f.write(" ".join(w) + "\n")

    # Odczyt szachownicy z pliku i wyświetlenie w konsoli
    with open(plik, "r") as f:
        print(f.read())

# Główny program
def main():
    global hetmany  # Używamy globalnej listy `hetmany`
    print("Wybierz sposób rozmieszczenia hetmanów:")
    print("1. Losowe rozmieszczenie")
    print("2. Wprowadzenie własnych pozycji")
    wybor = input("Podaj numer opcji (1 lub 2): ")

    if wybor == "1":
        # Wybieranie czy losować liczbę hetmanów, czy podać ją ręcznie
        print("Chcesz wylosować liczbę hetmanów czy podać ją samemu?")
        print("1. Wylosuj liczbę hetmanów")
        print("2. Podaj liczbę hetmanów")
        wybor_liczby = input("Podaj numer opcji (1 lub 2): ")
        if wybor_liczby == "1":
            n = random.randint(1, 99)  # Losowa liczba od 1 do 99
            print(f"Wylosowana liczba hetmanów: {n}")
        elif wybor_liczby == "2":
            n = int(input("Podaj liczbę hetmanów (maks. 99): "))
            if n >= 100:
                print("Liczba hetmanów musi być mniejsza niż 100.")
                return
            if n <= 0:
                print("Liczba hetmanów musi być większa niż 0.")
                return
        else:
            print("Niepoprawny wybór!")
            return
        losowe_hetmany(n)  # Losowe ustawienie hetmanów

    elif wybor == "2":
        # Podawanie liczby i pozycji hetmanów
        n = int(input("Podaj liczbę hetmanów: "))
        if n < 1 or n > 100:  # Sprawdzanie, czy liczba hetmanów jest poprawna
            print("Liczba hetmanów musi być od 1 do 100.")
            return  # Przerywamy, jeśli liczba hetmanów jest niepoprawna

        for i in range(n):
            while True:
                try:
                    print(f"Podaj pozycję dla hetmana {i + 1}:")
                    wiersz = int(input("Wiersz (od 1 do 100): "))
                    kolumna = int(input("Kolumna (od 1 do 100): "))
                    dodaj_hetmana(wiersz, kolumna)  # Dodanie hetmana na podaną pozycję
                    break
                except ValueError as e:
                    print(e)
                    print("Spróbuj jeszcze raz!")
    else:
        print("Niepoprawny wybór!")
        return

    # Wizualizacja szachownicy
    print("Wizualizacja szachownicy:")
    wizualizuj()

    # Sprawdzanie czy hetmany się szachują
    if czy_szach():
        print("Żadne hetmany się nie szachują ✨")
    else:
        print("Hetmany się szachują 😯😯")

main()
