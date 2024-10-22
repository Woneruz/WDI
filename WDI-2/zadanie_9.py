# Stała wartość PIN
PIN = "1234"

# Zmienna do przechowywania salda (zaczynamy z saldem początkowym 1000)
saldo = 1000

# Funkcja do sprawdzenia poprawności PIN-u
def sprawdz_pin():
    podany_pin = input("Podaj PIN: ")
    if podany_pin == PIN:
        return True
    else:
        print("Niepoprawny PIN!")
        return False

# Funkcja do wpłaty pieniędzy
def wplata():
    global saldo
    kwota = float(input("Podaj kwotę do wpłaty: "))
    if kwota > 0:
        saldo += kwota
        print(f"Dokonano wpłaty {kwota:.2f}. Nowe saldo: {saldo:.2f}")
    else:
        print("Nie można wpłacić kwoty mniejszej lub równej 0!")

# Funkcja do wypłaty pieniędzy
def wyplata():
    global saldo
    kwota = float(input("Podaj kwotę do wypłaty: "))
    if kwota > saldo:
        print("Nie masz wystarczających środków na koncie!")
    elif kwota <= 0:
        print("Nie można wypłacić kwoty mniejszej lub równej 0!")
    else:
        saldo -= kwota
        print(f"Dokonano wypłaty {kwota:.2f}. Nowe saldo: {saldo:.2f}")

# Funkcja do sprawdzania salda
def sprawdz_saldo():
    print(f"Twoje aktualne saldo wynosi: {saldo:.2f}")

# Funkcja główna symulująca działanie bankomatu
def bankomat():
    while True:
        print("Wybierz operację:")
        print("1 - Wpłata")
        print("2 - Wypłata")
        print("3 - Sprawdź saldo")
        print("4 - Zakończ")

        wybor = input("Twój wybór: ")

        if wybor == '1':  # Wpłata
            if sprawdz_pin():
                wplata()

        elif wybor == '2':  # Wypłata
            if sprawdz_pin():
                wyplata()

        elif wybor == '3':  # Sprawdzenie salda
            if sprawdz_pin():
                sprawdz_saldo()

        elif wybor == '4':  # Zakończenie programu
            print("Dziękujemy za skorzystanie z usług!")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

        # Pytanie co dalej
        print("Co chcesz zrobić w kolejnym kroku?")

# Wywołanie programu bankomatu
bankomat()
