import pytest

def test_czy_szach():
  global hetmany
  hetmany = []
  hetmany.append(Hetman(1, 1))
  hetmany.append(Hetman(2, 2))
  assert not czy_szach()

def test2_czy_szach():
  global hetmany
  hetmany = []
  hetmany.append(Hetman(1, 1))
  hetmany.append(Hetman(2, 3))
  assert czy_szach()

def test3_dodaj_hetmana():
  global hetmany
  hetmany = []
  hetmany.append(Hetman(1, 1))
  assert any(hetman.wiersz == 1 and hetman.kolumna == 1  for hetman in hetmany)

test_czy_szach()
test2_czy_szach()
test3_dodaj_hetmana()