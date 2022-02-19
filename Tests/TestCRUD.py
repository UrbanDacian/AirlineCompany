from Domain.Cheltuiala import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaCheltuiala, getById, stergeCheltuiala, modificareCheltuiala, undo, redo


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)

    assert len(lista) == 2
    assert getId(getById(1, lista)) == 1
    assert getNume(getById(1, lista)) == "Ion"
    assert getClasa(getById(1, lista)) == "Business"
    assert getPret(getById(1, lista)) == 300
    assert getCheckin(getById("1", lista)) == "Da"


def testStergeCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)

    lista = stergeCheltuiala(1, lista)

    assert len(lista) == 1
    assert getById(1, lista) is None
    assert getById(2, lista) is not None

    try:
        lista = stergeCheltuiala(3, lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById(2, lista) is not None
    except Exception:
        assert False

def testModificaCheltuiala():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)

    lista = modificareCheltuiala(1, "Ion", "EconomyPlus", 250, "Da", lista)

    prajituraUpdatata = getById(1, lista)
    assert getId(prajituraUpdatata) == 1
    assert getNume(prajituraUpdatata) == "Ion"
    assert getClasa(prajituraUpdatata) == "EconomyPlus"
    assert getPret(prajituraUpdatata) == 250
    assert getCheckin(prajituraUpdatata) == "Da"

    prajituraNeupdatata = getById("2", lista)
    assert getId(prajituraNeupdatata) == 2
    assert getNume(prajituraNeupdatata) == "Marcel"
    assert getClasa(prajituraNeupdatata) == "Economy"
    assert getPret(prajituraNeupdatata) == 200
    assert getCheckin(prajituraNeupdatata) == "Nu"

    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, lista)

    try:
        lista = modificareCheltuiala(3, "Mihai", "Business", 300, lista)
    except ValueError:
        prajituraNeupdatata = getById(1, lista)
        assert getId(prajituraNeupdatata) == 1
        assert getNume(prajituraNeupdatata) == "Ion"
        assert getClasa(prajituraNeupdatata) == "Business"
        assert getPret(prajituraNeupdatata) == 300
        assert getCheckin(prajituraNeupdatata) == "Da"
    except Exception:
        assert False


def testGetById():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)

    assert getById(1, lista) == (1, "Ion", "Business", 300, "Da")
    assert getById(2, lista) == (2, "Marcel", "Economy", 200, "Nu")



