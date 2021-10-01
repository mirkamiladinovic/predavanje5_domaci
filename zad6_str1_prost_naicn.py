"""
dati su realni brojevi x, y, alfa, beta, a i b. izracunati izraze
"""
from math import *

x = eval(input('unesi x '));
y = eval(input('unesi y '));

alfa = eval(input('unesi alfa '));
beta = eval(input('uneis beta '));

a = eval(input('unesi a '));
b = eval(input('unesi b '));

prvi_izraz = (x ** 3) / 3 - 3 * (y ** 2) + (x + 1) / (2 * y + 3)
drugi_izraz = -5 * sqrt(x + sqrt(y))
treci_izraz = 1 + 1 / (2 + 1 / ( 3 + 1 / 4))
cetvrti_izraz = 3 * sin(2*alfa) * cos(2 * beta) - 5 * (tan(alfa + beta)) ** 2
peti_izraz = sqrt(a ** 2 + b ** 2 - 2 * a * b * sin(alfa))

print(prvi_izraz, drugi_izraz, treci_izraz, cetvrti_izraz, peti_izraz)