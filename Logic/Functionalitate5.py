from Domain.Cheltuiala import getNume, getId, getPret


def suma(lista):
    """
    Functia returneaza suma preturilor penru fiecare Nume
    :param lista: lista cu rezervari
    :return: o lista cu suma preturilor pentru fiecare nume
    """
    rezultat = {}
    for cheltuiala in lista:
        nume = getNume(cheltuiala)
        pret = getPret(cheltuiala)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat

        