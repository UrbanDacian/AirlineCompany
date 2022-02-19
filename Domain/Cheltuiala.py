def creeazaCheltuiala(id, nume, clasa, pret, checkin):
    '''
    Creaza un dictionar care retine o cheltuiala
    :param id: id-ul cheltuielii - int
    :param nume: numele cheltuielii - string
    :param clasa: tipul de clasa (business/ economy plus/ economy) - string
    :param pret: pretul - float
    :param checkin: (da/nu) - string
    :return:
    '''
    return{
        'id': id,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin': checkin
    }


def getId(cheltuiala):
    '''
    Getter pentru id
    :param cheltuiala: Libraria de dictionare
    :return: id-ul unui dicitonar
    '''
    return cheltuiala['id']


def getNume(cheltuiala):
    '''
    Getter pentru nume
    :param cheltuiala: Libraria de dictionare
    :return: numele unui dicitonar
    '''
    return cheltuiala['nume']


def getClasa(cheltuiala):
    '''
    Getter pentru clasa
    :param cheltuiala: Libraria de dictionare
    :return: clasa unui dicitonar
    '''
    return cheltuiala['clasa']


def getPret(cheltuiala):
    '''
    Getter pentru pret
    :param cheltuiala: Libraria de dictionare
    :return: pretul unui dicitonar
    '''
    return cheltuiala['pret']


def getCheckin(cheltuiala):
    '''
    Getter pentru checkin
    :param cheltuiala: Libraria de dictionare
    :return: Da/Nu
    '''
    return cheltuiala['checkin']


def toString(cheltuiala):
    return "{}, {}, {}, {}, {}" .format(
        getId(cheltuiala),
        getNume(cheltuiala),
        getClasa(cheltuiala),
        getPret(cheltuiala),
        getCheckin(cheltuiala)
    )
