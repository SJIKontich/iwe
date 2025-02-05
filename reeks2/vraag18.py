
# Vectoren (d)

# (d) Schrijf een functie ''scalairproduct'' die het scalair product van twee vectoren berekent.

# Voorbeeld:

# >>> scalairproduct([1, 2, 3], [4, 5, 6])
# 1*4 + 2*5 + 3*6

# Formule:
# v1[0]*v2[0] + v1[1]*v2[1] + ... + v1[n]*v2[n]

# Zet hier je code
def scalairproduct(v1, v2):
    som = 0
    for i in range(len(v1)):
        som = som + v1[i] * v2[i]
    return som