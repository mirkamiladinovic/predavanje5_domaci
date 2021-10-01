"""
Napisati metod int gcd(int n, int m) koji vraća najveći zajednički djelilac brojeva m
i n.
"""

def gcd(m, n):
    if m < n: 
        (m, n) = (n, m)
    while m % n != 0:
        (m, n) = (n, m % n)
    return n

m = int(input('m = '))
n = int(input('n = '))

print(gcd(m, n))