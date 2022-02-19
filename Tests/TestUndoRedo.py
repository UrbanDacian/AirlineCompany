from Domain.Cheltuiala import getId
from Logic.CRUD import adaugaCheltuiala


def operatii(undo_list, redo_list, lista):
    undo_list.append(lista)
    redo_list.clear()


def test_ui_undo_redo():
    undo_list = []
    redo_list = []

    lista = []

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(3, "Ilie", "Business", 300, "Nu", lista)
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
        assert getId(lista[1]) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    assert getId(lista[0]) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 0

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    assert len(lista) == 2

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(3, "Ilie", "Business", 300, "Nu", lista)
    assert len(lista) == 3

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
        assert len(lista) == 3

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 2
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    operatii(undo_list, redo_list, lista)
    lista = adaugaCheltuiala(4, "Mihai", "Business", 250, "Da", lista)
    assert len(lista) == 2

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 1

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
        assert len(lista) == 0

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 1
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2

    assert getId(lista[0]) == 1
    assert getId(lista[1]) == 4

    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2