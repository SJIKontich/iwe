
# Vectoren (c)

# (c) Schrijf een functie ''afstand'' die de afstand tussen twee vectoren berekent.

# Voorbeeld:

# >>> afstand([1, 2], [3, 4])
# sqrt((1-3)**2 + (2-4)**2)

# formule:

# sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + ... + (v1[n] - v2[n])**2)

from math import sqrt

# Zet hier je code
def afstand(v1, v2):
    som = 0
    for i in range(len(v1)):
        som = som + (v1[i] - v2[i])**2
    return sqrt(som)
