"""
10. Napisati kod koji za kvadratnu jednacinu ax2 + bx + c =0 
ispituje da li ima realna rješenja.
"""

def ima_li_realna_rjesenja(a,b,c):
    if 2 * a != 0 and b ** 2 - 4 * a * c >= 0:
        return True
    return False

aa = int(input('a = '))
bb = int(input('b = '))
cc = int(input('c = '))
print(ima_li_realna_rjesenja(aa, bb, cc))