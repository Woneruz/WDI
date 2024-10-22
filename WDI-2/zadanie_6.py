# Pobranie dwóch liczb od usera
# input() pobiera dane jako ciąg znaków i musimy użyć float() do konwersji na liczby
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

# Sprawdzenie, czy obie liczby są mniejsze od 0
if liczba1 < 0 and liczba2 < 0:
    # Zakończenie programu gdy obie liczby są mniejsze od 0
    print("Uwaga! Obie liczby są mniejsze od 0 - Program kończy swoje działanie!")
else:
    # Sprawdzenie, czy tylko jedna liczba jest mniejsza od 0
    if liczba1 < 0:
        liczba1 = abs(liczba1)  # Użycie wartości bezwzględnej dla liczby1
    if liczba2 < 0:
        liczba2 = abs(liczba2)  # Użycie wartości bezwzględnej dla liczby2

    # Obliczenia podstawowych działań matematycznych
    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    iloczyn = liczba1 * liczba2
    if liczba2 != 0:  # Sprawdzamy, czy liczba2 nie jest zerem przed wykonaniem dzielenia
        iloraz = liczba1 / liczba2
    else:
        iloraz = "Nie można dzielić przez 0!"  # Informacja, jeśli liczba2 to 0

    # Obliczenia kwadratów obu liczb
    kwadrat1 = liczba1 ** 2
    kwadrat2 = liczba2 ** 2

    # Obliczenia pierwiastka drugiego stopnia obu liczb
    pierwiastek1 = liczba1 ** 0.5
    pierwiastek2 = liczba2 ** 0.5

    # Wypisanie wyników obliczeń z odpowiednimi informacjami
    print(f"Suma liczb: {suma}")
    print(f"Różnica liczb: {roznica}")
    print(f"Iloczyn liczb: {iloczyn}")
    print(f"Iloraz liczb: {iloraz}")
    print(f"Kwadrat pierwszej liczby: {kwadrat1}")
    print(f"Kwadrat drugiej liczby: {kwadrat2}")
    print(f"Pierwiastek drugiego stopnia z pierwszej liczby: {pierwiastek1}")
    print(f"Pierwiastek drugiego stopnia z drugiej liczby: {pierwiastek2}")

    # komunikat "Yay!" jeśli iloczyn wynosi 10
    if iloczyn == 10:
        print("Yay!")