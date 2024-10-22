# Pobranie liczby od użytkownika
wysokosc = int(input("Podaj wysokość choinki (liczba całkowita nieujemna): "))

# Pobranie wyboru wzoru od użytkownika
print("Wybierz wzór choinki:")
print("1 - Klasyczny")
print("2 - Z bombkami i gwiazdką")
wybor = int(input("Wybierz 1 lub 2: "))

# Funkcja do rysowania klasycznej choinki
def klasyczna_choinka(wysokosc):
    for i in range(wysokosc):
        # Liczba spacji maleje, liczba gwiazdek rośnie
        spacje = ' ' * (wysokosc - i - 1)
        gwiazdki = '*' * (2 * i + 1)
        print(spacje + gwiazdki)

# Funkcja do rysowania choinki z bombkami i gwiazdką
def choinka_z_bombkami(wysokosc):
    for i in range(wysokosc):
        spacje = ' ' * (wysokosc - i - 1)
        # Budowanie rzędu choinki z bombkami
        rzad = ''
        for j in range(2 * i + 1):
            if i == 0 and j == 0:
                rzad += 'X'  # Górna gwiazdka/szpic
            elif (i + j) % 3 == 0:
                rzad += 'o'  # Bombka
            else:
                rzad += '*'  # Gałązka
        print(spacje + rzad)

# Funkcja do rysowania pnia choinki
def pien_choinki(wysokosc):
    # Wysokość pnia to 1/4 wysokości choinki (zaokrąglone w dół), przynajmniej 1
    wysokosc_pnia = max(1, wysokosc // 4)
    szerokosc_pnia = 3  # Szerokość pnia to zawsze 3
    for i in range(wysokosc_pnia):
        spacje = ' ' * (wysokosc - szerokosc_pnia // 2 - 1)
        print(spacje + 'U' * szerokosc_pnia)

# Wybór wzoru choinki
if wybor == 1:
    klasyczna_choinka(wysokosc)
elif wybor == 2:
    choinka_z_bombkami(wysokosc)

# Rysowanie pnia choinki dla obu wzorów
pien_choinki(wysokosc)
