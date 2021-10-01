"""
Napisati metod int zbirIzIntervala(int a, int b) koji vraća zbir svih cijelih
brojeva iz intervala [a,b]
"""

def zbir_brojeva_intervala(a,b):
    zbir = 0
    i = a
    while i <= b:
        zbir = zbir + i
        i = i + 1
    return zbir

a = int(input('a = '))
b = int(input('b = '))
print(zbir_brojeva_intervala(a,b))