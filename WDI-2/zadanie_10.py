import math  # Dla pierwiastkowania
import random  # Dla losowania liczby

# Funkcja do dodawania
def dodawanie(a, b):
    return a + b


# Funkcja do odejmowania
def odejmowanie(a, b):
    return a - b


# Funkcja do mnożenia
def mnozenie(a, b):
    return a * b


# Funkcja do dzielenia
def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: nie można dzielić przez zero!"


# Funkcja do potęgowania
def potegowanie(a, b):
    return a ** b


# Funkcja do pierwiastkowania
def pierwiastkowanie(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Błąd: nie można pierwiastkować liczby ujemnej!"


# Funkcja do losowania liczby z zakresu
def losowanie_zakresu(a, b):
    return random.randint(a, b)


# Funkcja obsługująca kalkulator
def kalkulator():
    while True:
        # Pobieranie pierwszej liczby
        liczba1 = float(input("Podaj pierwszą liczbę: "))

        # Pobieranie operatora
        operator = input("\n + dodawanie | - odejmowanie | * mnożenie | / dzielenie "
                         "\n # pierwiastkowanie | ^ potęgowanie | x losowanie z zakresu"
                         "\n\n Podaj symbol operacji: ")


        if operator in ['+', '-', '*', '/', '^']:
            # Pobieranie drugiej liczby
            liczba2 = float(input("\nPodaj drugą liczbę: "))

            if operator == '+':
                wynik = dodawanie(liczba1, liczba2)
            elif operator == '-':
                wynik = odejmowanie(liczba1, liczba2)
            elif operator == '*':
                wynik = mnozenie(liczba1, liczba2)
            elif operator == '/':
                wynik = dzielenie(liczba1, liczba2)
            elif operator == '^':
                wynik = potegowanie(liczba1, liczba2)
            print(f"Wynik: {wynik}")

        elif operator == '#':
            # Pierwiastkowanie pierwszej liczby
            wynik = pierwiastkowanie(liczba1)
            print(f"Wynik pierwiastkowania: {wynik}")

        elif operator == 'x':
            # Losowanie liczby z zakresu między liczba1 a liczba2
            liczba2 = int(input("Podaj drugą liczbę (zakres do losowania): "))
            wynik = losowanie_zakresu(int(liczba1), liczba2)
            print(f"Wylosowana liczba z zakresu {int(liczba1)} do {liczba2}: {wynik}")

        else:
            print("Nieprawidłowy operator!")

        # Zapytanie, czy kontynuować
        kontynuacja = input("Czy chcesz wprowadzić nowe dane? (T/N): ").upper()
        if kontynuacja != 'T':
            print("Dziękujemy za skorzystanie z kalkulatora!")
            break


# Uruchomienie kalkulatora
kalkulator()
