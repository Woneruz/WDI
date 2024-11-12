# MA TO BYĆ KONKRETNE ARYTMETYCZNE W SŁUPKU - SYMULACJA - NIE WIZUALIZACJA

# Funkcja do konwersji liczby na listę jej cyfr - zaczynając od najmniejszej
def liczba_na_liste_cyfr(liczba):
    cyfry = [] # pusta lista
    while liczba > 0:
        cyfry.append(liczba % 10) # to dodaje ostatnią cyfrę liczby
        liczba //= 10 # usuwa ostatnią cyfrę liczby
    return cyfry

# Funkcja do wyrównania długości dwóch list, lepsza niż ostatnio
def wyrownaj_dlugi(lista1, lista2): # jeśli któraś jest krótsza to dodaje zero na końcu, aż bedą równe
    while len(lista1) < len(lista2):
        lista1.append(0)
    while len(lista2) < len(lista1):
        lista2.append(0)

def dodawanie_w_slupku(m, n):
    m_cyfry = liczba_na_liste_cyfr(m) # konwersja liczby na listę cyfr
    n_cyfry = liczba_na_liste_cyfr(n)
    wyrownaj_dlugi(m_cyfry, n_cyfry) # to wyrównanie długości

    w_cyfry = [] # pusta lista
    przeniesienie = 0 # do przenoszenia do kolejnej kolumny
    for i in range(len(m_cyfry)):
        w = m_cyfry[i] + n_cyfry[i] + przeniesienie
        przeniesienie = w // 10 # wyciąga to co trzeba przenieść
        w_cyfry.append(w % 10) # a tu to co zostaje
    if przeniesienie:
        w_cyfry.append(przeniesienie) # dodaje to co zostało jeśli zostało

    return sum(cyfra * (10 ** i) for i, cyfra in enumerate(w_cyfry))

def odejmowanie_w_slupku(m, n):
    m_cyfry = liczba_na_liste_cyfr(m)
    n_cyfry = liczba_na_liste_cyfr(n)
    wyrownaj_dlugi(m_cyfry, n_cyfry) # to co wyżej

    w_cyfry = []
    for i in range(len(m_cyfry)):
        if m_cyfry[i] < n_cyfry[i]:
            m_cyfry[i] += 10 # pożycza od sąsiada
            j = i + 1 # do pożyczki
            while m_cyfry[j] == 0: # Gdybyśmy pożyczali od zera
                m_cyfry[j] = 9 # to będzie 9 bo zabierzemy jedno
                j += 1
            m_cyfry[j] -= 1
        w_cyfry.append(m_cyfry[i] - n_cyfry[i])

    return sum(cyfra * (10 ** i) for i, cyfra in enumerate(w_cyfry))

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Blad: prosze podac prawidlowa liczbe calkowita.")

def input_dzialanie(prompt):
    while True:
        dzialanie = input(prompt)
        if dzialanie in ["+", "-"]:
            return dzialanie
        else:
            print("Blad: prosze podac prawidlowy znak dzialania (+ lub -).")

def interakcja():
    m = input_int("Podaj liczbe m: ")
    n = input_int("Podaj liczbe n: ")
    if m < 0 or n < 0:
        print("Blad: program nie obsluguje liczb ujemnych")
        return

    dzialanie = input_dzialanie("Podaj dzialanie: ")

    if dzialanie == "+":
        wynik = dodawanie_w_slupku(m, n)
    elif dzialanie == "-":
        if m < n:
            print("Blad: wynikiem jest liczba ujemna, nie mozna obliczyc.")
            return
        wynik = odejmowanie_w_slupku(m, n)
    else:
        print("Blad: program nie obsluguje dzialan innych niz (+, -)")
        return

    print(f"Wynik: {wynik}")

interakcja()