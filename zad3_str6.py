"""
Napisati metod double duzinaDuzi(double x1, double y1, double x2,
double y2) koji vraća dužinu duži čije su krajnje tačke A(x1, y1) i B(x2,y2).
"""
from math import *

def duzina_duzi(x1,y1,x2,y2):
    duzina = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return duzina

x = int(input('x1 = '))
y = int(input('y1 = '))
xx = int(input('x2 = '))
yy = int(input('y2 = '))
print('d(A,B) = ', duzina_duzi(x, y, xx, yy))