imie = "Arkadiusz"
nazwisko = "Baran"
wiek = 19
potrawa = "pizza"
zwierze = "pies"
dzielenie = 5/7
# w kilku wywołaniach
print(imie)
print(nazwisko)
print(wiek)
print(potrawa)
print(zwierze)
print(5/7)
# w jednym wywołaniu
print(imie, nazwisko, wiek, potrawa, zwierze, dzielenie)
# zaokrąglanie
zmienna = round(dzielenie, 1)
print (f"zaokrąglenie do 1: {zmienna}")
zmienna = round(dzielenie, 3)
print (f"zaokrąglenie do 3: {zmienna}")
zmienna = round(dzielenie, 5)
print (f"zaokrąglenie do 5: {zmienna}")
zmienna = round(dzielenie, 10)
print (f"zaokrąglenie do 10: {zmienna}")
print (f"zaokrąglenie do 10 bez zmiennej:")
print(round(5/7, 1))
print(round(5/7, 3))
print(round(5/7, 5))
print(round(5/7, 10))
