# Pobranie dwóch liczb od użytkownika
poczatek_zakresu = int(input("Podaj początek zakresu (liczba całkowita): "))
koniec_zakresu = int(input("Podaj koniec zakresu (liczba całkowita): "))

# Sprawdzenie, która liczba jest większa, aby prawidłowo zdefiniować zakres
if poczatek_zakresu > koniec_zakresu:
    poczatek_zakresu, koniec_zakresu = koniec_zakresu, poczatek_zakresu  # Zamiana liczb, jeśli początek jest większy

# Tworzenie listy liczb w zadanym zakresie
zakres = list(range(poczatek_zakresu, koniec_zakresu + 1))  # +1 aby uwzględnić koniec zakresu

# Sprawdzenie, czy zakres liczb jest większy niż 20
if len(zakres) > 20:
    # Obliczenie średniej zakresu
    srednia = sum(zakres) / len(zakres)

    # Sortowanie liczb według ich odległości od średniej
    odleglosci = {}
    for liczba in zakres:
        odleglosci[liczba] = abs(liczba - srednia)
    liczby_najblizej_sredniej = sorted(odleglosci, key=odleglosci.get)

    # Wypisanie pierwszych 6 liczb najbliższych średniej (bez samej średniej)
    print("6 liczb najbliższych średniej zakresu (bez samej średniej):")
    i = 1  # Pętla while dla wypisywania 6 liczb
    while i < 7:
        print(liczby_najblizej_sredniej[i])
        i += 1
else:
    # Wypisanie wszystkich liczb w zakresie za pomocą pętli for, gdy zakres ma 20 lub mniej liczb
    print("Liczby w zakresie:")
    for liczba in zakres:
        print(liczba)
