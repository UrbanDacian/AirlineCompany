from Domain.Cheltuiala import getPret
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.Functionalitate5 import suma


def testSuma():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)

    suma(lista)
    
    assert getPret(getById(2, lista)) == 200