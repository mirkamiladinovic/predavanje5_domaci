"""
Napisati metod double promjena(double x, double a) koji vraća broj a*x, ako je
x nenegativan i a/x, ako je x negativan.
"""

def promjena(a, x):
    if x >= 0:
        promjena1 = a * x
        return promjena1
    else:
        promjena2 = a / x
        return promjena2

A = int(input('a = '))
X = int(input('x = '))
     
print('promjena je', promjena(A,X))