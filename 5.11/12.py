def liczba_na_liste_cyfr(n):  # Definiujemy funkcję która przekształca liczbę na listę cyfr
    return list(str(n))  # Rozbijamy liczbę na cyfry i zwracamy jako listę


def wyswietl_w_slupku(M, N, wynik, operacja): # Funkcja do wyświetlania liczb w słupku
    # Konwertujemy liczby na listy cyfr
    lista_M = liczba_na_liste_cyfr(M)
    lista_N = liczba_na_liste_cyfr(N)
    lista_wynik = liczba_na_liste_cyfr(wynik)

    # Ustalamy maksymalną długość z liczb a, b i wyniku - potrzebne do wyrównania, żeby jednosći były pod sobą
    max_len = max(len(lista_M), len(lista_N), len(lista_wynik))

    # Dodajemy spacje z lewej strony, aby wyrównać długość (na podstawie maksymalnej długości)
    lista_M = [' '] * (max_len - len(lista_M)) + lista_M
    lista_N = [' '] * (max_len - len(lista_N)) + lista_N
    lista_wynik = [' '] * (max_len - len(lista_wynik)) + lista_wynik

    # Wyświetlamy liczby w "słupku"
    print("  " + ''.join(lista_M))
    print(f"{operacja} " + ''.join(lista_N))
    print("-" * (max_len + 2))  # Linia dostosowana do szerokości wsns długosci liczb
    print("  " + ''.join(lista_wynik))

# Definiujemy customowe klasy - aspekt wizualny
class DzieloneZero(Exception): # Aby customowa klasa poprawnie działała jako wyjątek musi być dziedziczona po klasie Exception
    pass
class BladWartosci(Exception):
    pass

def oblicz(M, N, D): # Definiujemy funkcję liczącą
    try:
        # Sprawdzamy, czy M i N są mniejsze niż 10^10 tylko dla dodawania i odejmowania - jak w poleceniu
        if D in ('+', '-') and (abs(M) >= 10 ** 10 or abs(N) >= 10 ** 10):
            raise BladWartosci("Liczby muszą być mniejsze niż 10^10 dla dodawania i odejmowania.")

        # Wykonujemy odpowiednią operację w zależności od wartości D
        if D == '+':
            wynik = M + N
            wyswietl_w_slupku(M, N, wynik, '+')

        elif D == '-':
            wynik = M - N
            wyswietl_w_slupku(M, N, wynik, '-')

        elif D == '*':
            wynik = M * N
            wyswietl_w_slupku(M, N, wynik, '*')

        elif D == '/':
            if N == 0:
                raise DzieloneZero("Nie można dzielić przez zero.")
            wynik = M // N  # Używamy dzielenia całkowitego
            wyswietl_w_slupku(M, N, wynik, '/')

        else:
            raise BladWartosci("Nieprawidłowy znak działania. Dozwolone znaki: +, -, *, /")

    except BladWartosci as e:
        print("Błąd:", e)
    except DzieloneZero as e:
        print("Błąd:", e)


# Pobieramy dane od użytkownika
try: # Używamy "try" bo jest to operacja która może zakończyć się błędem, użytkownik może podać nieprawidłowe dane.
    M = int(input("Podaj pierwszą liczbę (M): "))
    N = int(input("Podaj drugą liczbę (N): "))
    D = input("Podaj znak działania (+, -, *, /): ")

    # Uruchamiamy obliczenia
    oblicz(M, N, D)

# definiujemy błąd jeśli "try" się nie powiedzie
except ValueError: # tu już użyłem wbudowanej klasy ValueError do obsługi błędu
    print("Błąd: Nieprawidłowe dane. Progam kończy działanie.")
