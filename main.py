from Logic.CRUD import adaugaCheltuiala
from UserInterface.Console import runMenu
from UserInterface.command_line_console import new_menu


def main():
    lista = []
    lista = adaugaCheltuiala(1, "Ion", "Business", 300, "Da", lista)
    lista = adaugaCheltuiala(2, "Marcel", "Economy", 200, "Nu", lista)
    while True:
        print("1.Meniu principal")
        print("2.Meniu secundar")
        print("x.Inchidere")
        menu = input("Alegeti meniul: ")
        if menu == "1":
            runMenu(lista)
        elif menu == "2":
            new_menu(lista)
        elif menu == "x":
            break
        else:
            print("Optiune gresita.Reincercati!")


main()
