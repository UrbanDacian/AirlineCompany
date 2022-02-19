from Domain.Cheltuiala import getCheckin, getPret, creeazaCheltuiala, getId, getNume, getClasa


def ieftinireCheltuiala(procent, lista):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param procent: procentul de ieftinire
    :param lista: lista de dicitonare
    :return: o lista cu preturile ieftinite
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getCheckin(cheltuiala) == "Da":
            pret = getPret(cheltuiala) - (procent/100)*getPret(cheltuiala)
            cheltuialaNoua = creeazaCheltuiala(
                getId(cheltuiala),
                getNume(cheltuiala),
                getClasa(cheltuiala),
                pret,
                "Da"
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua