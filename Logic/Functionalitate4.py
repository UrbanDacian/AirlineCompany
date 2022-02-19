from Domain.Cheltuiala import getPret, getId


def obtinerePret(cheltuiala):
    return getPret(cheltuiala)

def ordonarePreturi(lista):
    '''
    Ordonarea rezervărilor descrescător după preț.
    :param lista: lista de dictionare
    :return: lista ordonata descrescator
    '''
    return sorted(lista, key=obtinerePret, reverse=True)