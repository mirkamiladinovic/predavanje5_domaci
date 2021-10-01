"""
jedan galeon vrijedi sedamnaest srpova, a jedan srp dvadeset
devet knutova“. Napiši program koji za zadatu kolicinu galeona, srpova i knutova koju
Harry ima na svom racunu štampa kolika je ukupna kolicina tog novca izražena u
knutovima.
"""
def konvertovanje_galeona_i_srpova_u_knutove(g,s,k):
    zbir_knutova = g*17*29+s*29+k
    return zbir_knutova

galeon = int(input('g = '))
srp = int(input('s = '))
knut = int(input('k = '))
print('Harry ima', konvertovanje_galeona_i_srpova_u_knutove(galeon, srp, knut), 'knutova.')

"""
g = 1                       g = 1                     g = 1  
s = 0                       s = 1                     s = 1
k = 0                       k = 0                     k = 1
Harry ima 493 knutova.      Harry ima 522 knutova.    Harry ima 523 knutova. 
"""