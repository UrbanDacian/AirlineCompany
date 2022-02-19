from Domain.Cheltuiala import getPret
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.Functionalitate2 import ieftinireCheltuiala


def testIeftinireCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    ieftinireCheltuiala(1/2, lista)
    assert len(lista) == 2
    assert getPret(getById(1, lista)) == 150
    assert getPret(getById(2, lista)) == 100