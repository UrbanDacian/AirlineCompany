from Domain.Cheltuiala import getClasa, getPret


def pretulMaxim(lista):
    '''
     Determinarea prețului maxim pentru fiecare clasă.
    :param lista: lista de dicitonare
    :return: pretul maxim pentru fiecare clasa
    '''
    maxBusiness = 0
    maxEconomyPlus = 0
    maxEconomy = 0
    for cheltuiala in lista:
        if getClasa(cheltuiala) == "Business":
            if getPret(cheltuiala) > maxBusiness:
                maxBusiness = getPret(cheltuiala)
        elif getClasa(cheltuiala) == "Economy":
            if getPret(cheltuiala) > maxEconomy:
                maxEconomy = getPret(cheltuiala)
        else:
            if getPret(cheltuiala) > maxEconomyPlus:
                maxEconomyPlus = getPret(cheltuiala)
    if maxEconomyPlus != 0 and maxEconomy != 0 and maxBusiness != 0:
        print("Pretul maxim pentru clasa Economy este: ", maxEconomy),
        print("Pretul maxim pentru clasa EconomyPlus este: ", maxEconomyPlus),
        print("Pretul maxim pentru clasa Business este: ", maxBusiness)

    elif maxBusiness != 0 and maxEconomy != 0 :
        print("Pretul maxim pentru clasa Business este: ", maxBusiness),
        print("Pretul maxim pentru clasa Economy este: ",maxEconomy)
    elif maxEconomy != 0  and maxEconomyPlus != 0 :
        print("Pretul maxim pentru clasa Economy este: ", maxEconomy),
        print("Pretul maxim pentru clasa EconomyPlus este: ", maxEconomyPlus )
    elif maxEconomy != 0 :
        print("Pretul maxim pentru clasa Economy este: ", maxEconomy)
    elif maxBusiness != 0 :
        print("Pretul maxim pentru clasa Business este: ", maxBusiness)
    elif maxEconomyPlus != 0 :
        print ("Pretul maxim pentru clasa EconomyPlus este: ", maxEconomyPlus)
    else:
        print("Lista este goala.Adaugati elemente.")

