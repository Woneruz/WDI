import unittest
class test_szachownica(unittest.TestCase):
  def test_czy_szach(self):
    global hetmany
    hetmany = []
    hetmany.append(Hetman(1, 1))
    hetmany.append(Hetman(2, 2))
    self.assertNotEqual(True, czy_szach())

  def test2_czy_szach(self):
    global hetmany
    hetmany = []
    hetmany.append(Hetman(1, 1))
    hetmany.append(Hetman(2, 3))
    self.assertEqual(True, czy_szach())

  def test3_dodaj_hetmana(self):
    global hetmany
    hetmany = []
    hetmany.append(Hetman(1, 1))
    self.assertRaises(ValueError, dodaj_hetmana, 1,1)





unittest.main(argv=[''], verbosity=2, exit=False)