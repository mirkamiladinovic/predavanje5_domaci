from math import *

def prvi_izraz(x, y):
    izraz1 = (x ** 3) / 3 - 3 * (y ** 2) + (x + 1) / (2 * y + 3)
    return izraz1

def drugi_izraz(x, y):
    izraz2 = (-5) * sqrt(x + sqrt(y))
    return izraz2 

def treci_izraz():
    izraz3 = 1 + 1 / (2 + 1 / ( 3 + 1 / 4))
    return izraz3

def cetvrti_izraz(alfa, beta):
    izraz4 = 3 * sin(2 * alfa) * cos(2 * beta) - 5 * (tan(alfa + beta)) ** 2
    return izraz4

def peti_izraz(a, b, alfa, beta):
    izraz5 = sqrt(a ** 2 + b ** 2 - 2 * a * b * sin(alfa))
    return izraz5

x1 = eval(input('unesi x '))
y1 = eval(input('unesi y '))  

alfa1 = eval(input('unesi alfa '))
beta1 = eval(input('unesi beta '))

a1 = eval(input('unesi a '))
b1 = eval(input('unesi b '))
    
print('Prvi izraz je jednak', prvi_izraz(x1,y1))
print('Drugi izraz je jednak', drugi_izraz(x1,y1))
print('Treci izraz je jednak', treci_izraz())
print('Cetvrti izraz je jednak', cetvrti_izraz(alfa1, beta1))
print('Peti izraz je jednak', peti_izraz(a1, b1, alfa1, beta1))