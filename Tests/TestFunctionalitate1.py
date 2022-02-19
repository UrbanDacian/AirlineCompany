from Domain.Cheltuiala import getClasa
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.Functionalitate1 import crestereClasa


def testCrestereClase():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    crestereClasa("Marcel", lista)
    assert len(lista) == 2
    assert getClasa(getById(2, lista)) == "EconomyPlus"