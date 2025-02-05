
# Vectoren (d)

# (d) Schrijf een functie scalairproduct die het scalair product van twee vectoren
# berekent. De vectoren worden voorgesteld als lijsten van getallen. De functie
# geeft het scalair product van de twee vectoren terug. De lengte van de twee
# vectoren is gelijk en de functie moet hier niet op controleren.

# Formule:
# v1[0]*v2[0] + v1[1]*v2[1] + ... + v1[n]*v2[n]

# Zet hier je code
def scalairproduct(v1, v2):
    product = 0
    for i in range(len(v1)):
        product += v1[i] * v2[i]
    return product