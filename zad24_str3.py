"""
Napisati kod koji za datu godinu odredjuje da li je prestupna 
i štampa odgovarajucu poruku.
"""

def prestupna(godina):
    if godina % 4 == 0:
        if godina % 100 == 0:
            if godina % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

g = int(input('godina = '))
print(prestupna(g))