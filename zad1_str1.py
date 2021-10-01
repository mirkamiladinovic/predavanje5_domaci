"""
Napisati kod koji za date katete a i b (a<b) pravouglog trougla racuna površinu i
zapreminu tijela koje se dobija rotacijom trougla oko manje katete.
"""

from math import *

def rotacija_trougla_oko_manje_katete(kateta_a, kateta_b):
    if kateta_a < kateta_b:
        poluprecnik = kateta_b
        hipotenuza_izvodnica = sqrt(kateta_a ** 2 + kateta_b ** 2)
        visina = kateta_a
        povrsina = kateta_b * pi * (kateta_b + hipotenuza_izvodnica)
        zapremina = (1 / 3) * (kateta_b ** 2) * pi * kateta_a
        return povrsina, zapremina
    elif kateta_b < kateta_a:
        poluprecnik = kateta_a
        hipotenuza_izvodnica = sqrt(kateta_a ** 2 + kateta_b ** 2)
        visina = kateta_b
        povrsina = kateta_a * pi * (kateta_a + hipotenuza_izvodnica)
        zapremina = (1 / 3) * (kateta_a ** 2) * pi * kateta_b
        return povrsina, zapremina
    else:
        povrsina = print('nepravilan unos')
        zapremina = print('nepravilan unos')
        return povrsina, zapremina

a = int(input('kateta_a = '))
b = int(input('kateta_b = '))

print(rotacija_trougla_oko_manje_katete(a,b))


