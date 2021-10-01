"""
Odrediti gustinu naseljenosti
te države.
"""

def gustina_naseljenosti(povrsina_drzave, br_stanovnika):
    return br_stanovnika / povrsina_drzave

p = int(input('Povrsina drzave je: '))
n = int(input('Broj stanovnika je: '))
print('Gustina naseljenosti je: ', round(gustina_naseljenosti(p,n),0),'st/km^2')