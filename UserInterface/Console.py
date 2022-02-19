from Domain.Cheltuiala import getNume, getClasa, getPret, getCheckin, toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, getById, modificareCheltuiala
from Logic.Functionalitate1 import crestereClasa
from Logic.Functionalitate2 import ieftinireCheltuiala
from Logic.Functionalitate3 import pretulMaxim
from Logic.Functionalitate4 import ordonarePreturi
from Logic.Functionalitate5 import suma


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare chelutuiala")
    print("4. Crestere clasa ")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def runMenu(lista):
    undoOperations = []
    redoOperations = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareCheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "2":
            lista = uiStergeCheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "4":
            lista = uiCrestereClasa(lista)
        elif optiune == "5":
            lista = uiIeftinireCheltuiala(lista)
        elif optiune == "6":
            uiPretulMaxim(lista)
        elif optiune == "7":
            lista = uiOrdonareCheltuieli(lista)
        elif optiune == "8":
            print(uiSuma(lista))
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                redoOperations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOperations) > 0:
                operations = redoOperations.pop()
                undoOperations.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


def uiAdaugareCheltuiala(lista, undoOperations, redoOperations):
    try:
        id = int(input("Dati id-ul: "))
        nume = input("Dati numele: ")
        clasa = input("Dati clasa(Business/EconomyPlus/Economy: ")
        pret = float(input('Dati pretul: '))
        checkin = input("Dati tipul de checkin(Da/Nu): ")

        rezultat = adaugaCheltuiala(id, nume, clasa, pret, checkin, lista)
        undoOperations.append([
            lambda: stergeCheltuiala(id, rezultat),
            lambda: adaugaCheltuiala(id, nume, clasa, pret, checkin, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeCheltuiala(lista, undoOperations, redoOperations):
    try:
        id = int(input("Dati id-ul cheltuielii de sters: "))

        rezultat = stergeCheltuiala(id, lista)
        prajituraDeSters = getById(id, lista)
        undoOperations.append([
            lambda: adaugaCheltuiala(
                id,
                getNume(prajituraDeSters),
                getClasa(prajituraDeSters),
                getPret(prajituraDeSters),
                getCheckin(prajituraDeSters),
                rezultat),
            lambda: stergeCheltuiala(id, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaCheltuiala(lista, undoOperations, redoOperations):
    try:
        id = int(input("Dati id-ul cheltuielii de modificat: "))
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa(Business/EconomyPlus/Economy): ")
        pret = float(input('Dati noul pret: '))
        checkin = input("Dati noul tip de checkin(Da/Nu): ")

        rezultat = modificareCheltuiala(id, nume, clasa, pret, checkin, lista)
        prajituraVeche = getById(id, lista)
        undoOperations.append([
            lambda: modificareCheltuiala(
                id,
                getNume(prajituraVeche),
                getClasa(prajituraVeche),
                getPret(prajituraVeche),
                getCheckin(prajituraVeche),
                rezultat),
            lambda: modificareCheltuiala(id, nume, clasa, pret, checkin, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiCrestereClasa(lista):
    try:
        nume = input("Dati numele pentru care se vor creste clasele")
        return crestereClasa(nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinireCheltuiala(lista):
    try:
        procent = int(input("Dati procentul cu care sa se ieftineasca cheltuielile (format - a): "))
        return ieftinireCheltuiala(procent, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiPretulMaxim(lista):
    return pretulMaxim(lista)


def uiOrdonareCheltuieli(lista):
    return ordonarePreturi(lista)


def uiSuma(lista):
    return suma(lista)