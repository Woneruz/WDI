# Wybrałem zadanie nr. 11
# Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.

# Funkcja do obliczania NWD dwóch liczb za pomocą algorytmu Euklidesa
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Funkcja do obliczania NWW dwóch liczb
def nww(a, b):
    return a * b // nwd(a, b)

# Funkcja do obliczania NWW trzech liczb
def nww_trzech_liczb(a, b, c):
    return nww(nww(a, b), c)

# Pobranie trzech liczb od użytkownika
print("Podaj trzy liczby całkowite:")
liczba1 = int(input("\nPodaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
liczba3 = int(input("Podaj trzecią liczbę: "))

# Obliczenie NWW dla trzech liczb
wynik = nww_trzech_liczb(liczba1, liczba2, liczba3)

# Wypisanie wyniku
print(f"\nNajmniejsza wspólna wielokrotność liczb {liczba1}, {liczba2}, {liczba3} to: {wynik}")
