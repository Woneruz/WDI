import pandas as pd

# Wczytywanie dane z pliku iris.csv do ramki danych (dataframe)
plik = pd.read_csv('iris.csv')

# Obliczanie średnią dla kolumny 'petallength'
srednia = plik['petallength'].mean()
print(f"Średnia dla 'petallength': {srednia}")

# Obliczanie mediany dla kolumny 'petallength'
mediana = plik['petallength'].median()
print(f"Mediana dla 'petallength': {mediana}")

#  Podawanie wartości progowej do filtrowania
user_value = float(input("Podaj wartość minimalną dla 'petallength': "))

# FIltruje wiersze które mają petallength >= podanej
przefiltrowana = plik[plik['petallength'] >= user_value]

# Pokazywanie 5 wierszy przefiltrowanej ramki danych
print("\nPierwsze 5 wierszy (head):")
print(przefiltrowana.head())

# 5 wierszy przefiltrowanej ramki danych
print("\nOstatnie 5 wierszy (tail):")
print(przefiltrowana.tail())

# Opis statystyczny tej przefiltrowanej ramki
print("\nOpis statystyczny (funkcja describe()):")
print(przefiltrowana.describe())
