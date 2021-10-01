"""
Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i 
datu godinu štampa broja dana u datom mjesecu.
"""

def prestupna(godina):
    if godina % 4 == 0:
        if godina % 100 == 0:
            if godina % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

"""
ako je godina prestupna -> februar ima 29 dana, u suprotnom 28
"""

def broj_dana_u_mjesecu(broj_mjeseca, god):
    mjeseci_sa_31_danom = [1,3,5,7,8,10,12]
    mjeseci_sa_30_dana = [4,6,9,11]
    if god == True and broj_mjeseca == 2:
        print('29 dana')
    elif god == False and broj_mjeseca == 2:
        print('28 dana')
    elif broj_mjeseca in mjeseci_sa_31_danom:
        print('31 dan')
    elif broj_mjeseca in mjeseci_sa_30_dana:
        print('30 dana')
    else:
        print('Netacan unos')

br_m = int(input('Unesite redni broj mjeseca: '))
br_g = int(input('Unesite godinu: '))
broj_dana_u_mjesecu(br_m, prestupna(br_g))