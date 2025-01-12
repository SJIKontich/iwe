
# Vectoren (d)

# (d) Schrijf een functie scalairproduct die het scalair product van twee vectoren
# berekent. De vectoren worden voorgesteld als lijsten van getallen. De functie
# geeft het scalair product van de twee vectoren terug. De lengte van de twee
# vectoren is gelijk en de functie moet hier niet op controleren.

# Zet hier je code
def scalairproduct(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))