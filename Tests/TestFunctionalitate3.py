from Logic.CRUD import adaugaCheltuiala
from Logic.Functionalitate3 import pretulMaxim


def testPretulMaxim():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    rezultat = pretulMaxim(lista)

    assert rezultat["EconomyPlus"] is None
    assert rezultat["Economy"] == 200
    assert rezultat["Business"] == 300
    assert rezultat is not None