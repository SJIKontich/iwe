
# Matrices optellen

# Schrijf een functie som(m1,m2) die de som van de twee matrices teruggeeft.
# Maak gebruik van de functie nulmatrix, aantalrijen en aantalkolommen.

# Voorbeeld:

# >>> som([[1, 2], [3, 4]], [[5, 6], [7, 8]])
# [[6, 8], [10, 12]]

from reeks3.vraag02 import nulmatrix
from reeks3.vraag04 import aantalrijen
from reeks3.vraag05 import aantalkolommen

# Zet hier je code
def som(m1, m2):
    m = nulmatrix(aantalrijen(m1), aantalkolommen(m1))
    for i in range(aantalrijen(m1)):
        for j in range(aantalkolommen(m1)):
            m[i][j] = m1[i][j] + m2[i][j]

    return m