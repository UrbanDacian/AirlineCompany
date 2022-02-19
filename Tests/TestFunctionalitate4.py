from Domain.Cheltuiala import getId
from Logic.CRUD import adaugaCheltuiala
from Logic.Functionalitate4 import ordonarePreturi


def testOrdonarePreturi():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    ordonarePreturi(lista)
    assert len(lista) == 2
    assert getId(lista.pop) == 2