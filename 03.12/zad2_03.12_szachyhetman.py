import random

# Rozmiar szachownicy i lista przechowująca pozycje hetmanów
rozmiar_szachownicy = 100
hetmany = []  # Lista pozycji hetmanów [(w1, k1), (w2, k2), ...] - jak w poleceniu

# Funkcja dodająca hetmana na szachownicę
def dodaj_hetmana(wiersz, kolumna):
    if 1 <= wiersz <= rozmiar_szachownicy and 1 <= kolumna <= rozmiar_szachownicy:  # Sprawdzenie poprawności pozycji
        if (wiersz, kolumna) not in hetmany:  # Czy pozycja nie jest zajęta
            hetmany.append((wiersz, kolumna))  # Dodanie pozycji hetmana do listy
        else:
            raise ValueError(f"Na pozycji ({wiersz}, {kolumna}) już znajduje się hetman.")  # Jeśli pozycja zajęta
    else:
        raise ValueError("Pozycja poza zakresem szachownicy.")  # Jeśli pozycja poza plansza

# Funkcja losowo N hetmanów
def losowe_hetmany(n):
    global hetmany  # Używamy globalnej listy hetmany
    hetmany = []  # Czyścimy listę
    pozycje = set()  # Zbiór przechowujący zajęte pozycje
    while len(pozycje) < n:  # Dopóki nie ustawimy N hetmanów
        wiersz = random.randint(1, rozmiar_szachownicy)
        kolumna = random.randint(1, rozmiar_szachownicy)
        if (wiersz, kolumna) not in pozycje:  # Sprawdzamy, czy pozycja jest wolna
            dodaj_hetmana(wiersz, kolumna)  # Dodajemy hetmana
            pozycje.add((wiersz, kolumna))  # Zapisujemy pozycję jako zajętą

# Funkcja sprawdzająca czy hetany się nie szachują
def czy_szach():
    for i in range(len(hetmany)):  # Pętla po każdym hetmanie
        for j in range(i + 1, len(hetmany)):  # Porównujemy go z kloejnymi hetmanami
            h1 = hetmany[i]
            h2 = hetmany[j]
            if (h1[0] == h2[0] or  # Ten sam wiersz
                h1[1] == h2[1] or  # Ta sama kolumna
                abs(h1[0] - h2[0]) == abs(h1[1] - h2[1])):  # Ta sama przekątna
                return False  # Hetmany się szachują
    return True  # Żadne dwa hetmany się nie szachują

# Funkcja wizualizująca szachownicę
def wizualizuj(plik="szachownica.txt"):
    # Tworzymy pustą szachownicę
    szachownica = [["." for _ in range(rozmiar_szachownicy)] for _ in range(rozmiar_szachownicy)]
    for wiersz, kolumna in hetmany:  # Umieszczamy hetmanów na planszy
        szachownica[wiersz - 1][kolumna - 1] = "H"

    # Wyświetlenie szachownicy w konsoli
    #for w in szachownica:
    #    print(" ".join(w))

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
        else:
            print("Niepoprawny wybór!")
            return
        losowe_hetmany(n)  # Losowe ustawienie hetmanów

    elif wybor == "2":
        # Podawanie liczbę i pozycje hetmanów
        n = int(input("Podaj liczbę hetmanów: "))
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

    # Wizualizacja szachownicy (nie symulacja 😘)
    print("Wizualizacja szachownicy:")
    wizualizuj()

    # Sprawdzanie czy hetmany się szachują
    if czy_szach():
        print("Żadne hetmany się nie szachują ✨")
    else:
        print("Hetmany się szachują 😯😯")

main()
