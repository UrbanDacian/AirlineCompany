from Logic.CRUD import adaugaCheltuiala, modificareCheltuiala, stergeCheltuiala
from UserInterface.Console import showAll


def help():
    print("Daca doriti sa adaugati o rezervare, tastati in primul rand 'add', iar mai apoi "
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numele, clasa, pretul si checkin-ul")
    print("Daca doriti sa stergeti o rezervare, tastati in primul rand 'delete', iar mai apoi "
          "id-ul rezervarii pe care doriti sa o stergeti")
    print("Daca doriti sa modificati o rezervare, tastati in primul rand 'modify', iar mai apoi, "
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numele, clasa, pretul si checkin-ul")
    print("Daca doriti sa efectuati mai multe comenzi deodata, dati valorile asa cum este specificat mai sus, "
          "iar intre doua comenzi,tastati ';'")
    print("Daca doriti sa afisati lista tastati 'a'")
    print("Daca doriti sa va opriti tastati 'x'")


def new_menu(lista):
    ajutor = input("Daca vreti sa afisati meniul, tastati 'Da',altfel tastati orice altceva: ")
    if ajutor == 'Da':
        help()
    while True:
        comanda = input("Ce comenzi doriti sa efectuati despartite prin ';' ?")
        categorii = comanda.split(";")
        if categorii[0] == "exit":
            break
        else:
            for optiune in categorii:
                camp = optiune.split(",")
                if camp[0] == "add":
                    try:
                        lista = adaugaCheltuiala(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                    except IndexError as ie:
                        print("Eroare: {}".format(ie))
                elif camp[0] == "a":
                    showAll(lista)
                elif camp[0] == "modify":
                    try:
                        lista = modificareCheltuiala(camp[1], camp[2], camp[3], camp[4], camp[5], lista)
                    except IndexError as ie:
                        print("Eroare: {}".format(ie))
                elif camp[0] == "delete":
                    lista = stergeCheltuiala(camp[1], lista)
                elif camp[0] == "x":
                    break
                else:
                    print("Optiune gresita! Reincercati!")