"""
Napisati kod koji za datu osnovicu a i krak b jednakokrakog trougla racuna 
površinu i zapreminu tijela koje se dobija 
rotacijom trougla oko visine spuštene na osnovicu.
"""

from math import *

def jednakokraki_se_rotira(kateta_a, kateta_b):
    poluprecnik = kateta_a / 2
    hipotenuza_izvodnica = kateta_b
    visina = sqrt(kateta_b ** 2 - (kateta_a / 2) ** 2)
    povrsina = poluprecnik ** 2 * pi + hipotenuza_izvodnica * poluprecnik * pi
    zapremina = (1 / 3) * (poluprecnik ** 2) * pi * visina
    return povrsina, zapremina

a = int(input('kateta_a = '))
b = int(input('kateta_b = '))

print('(povrsina, zapremina)', jednakokraki_se_rotira(a,b))
 