from Domain.Cheltuiala import getNume, getClasa, creeazaCheltuiala, getId, getPret, getCheckin


def crestereClasa(nume, lista):
    '''
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume: numele
    :param lista: lista de cheltuieli
    :return: lista noua
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNume(cheltuiala) == nume:
            if getClasa(cheltuiala) == "Economy":
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getNume(cheltuiala),
                    "EconomyPlus",
                    getPret(cheltuiala),
                    getCheckin(cheltuiala)
                )
                listaNoua.append(cheltuialaNoua)
            elif getClasa(cheltuiala) == "EconomyPlus":
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getNume(cheltuiala),
                    "Business",
                    getPret(cheltuiala),
                    getCheckin(cheltuiala)
                )
            else:
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getNume(cheltuiala),
                    getClasa(cheltuiala),
                    getPret(cheltuiala),
                    getCheckin(cheltuiala)
                )
                listaNoua.append(cheltuialaNoua)

        else:
            listaNoua.append(cheltuiala)
    return listaNoua
