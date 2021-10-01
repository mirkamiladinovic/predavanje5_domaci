from math import *
"""
Program koji racuna povrsinu i zapreminu tijela 
koje nastaje rotacijom oko hipotenuze pravouglog trougla.
"""
def povrsina_zapremina_tijela(kateta_a, kateta_b):
    hipotenuza = sqrt(kateta_a ** 2 + kateta_b ** 2)
    povrsina = (kateta_a * kateta_b) / hipotenuza * pi * (kateta_a + kateta_b)
    zapremina = (kateta_a ** 2 * kateta_b ** 2 * pi) / (3 * hipotenuza)
    return povrsina, zapremina

a = int(input('kateta_a = '))
b = int(input('kateta_b = '))
print("(povrsina, zapremina) = ", povrsina_zapremina_tijela(a,b))
