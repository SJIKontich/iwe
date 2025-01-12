
# Vectoren (c)

# (c) Schrijf een functie afstand die de afstand tussen twee vectoren berekent. De
# vectoren worden voorgesteld als lijsten van getallen. De functie geeft de
# afstand tussen de twee vectoren terug. De lengte van de twee vectoren is gelijk
# en de functie moet hier niet op controleren.
# Denk eraan dat de afstand tussen twee vectoren gelijk is aan de wortel van de som
# van de kwadraten van de verschillen van de overeenkomstige elementen van de
# vectoren (de Euclidische afstand).
#
# Voorbeeld:
#
# afstand([1, 0, 0], [0,0,0]) -> 1.0
# afstand([1, 0, 1], [0,0,0]) -> 1.4142135623730951 (wortel 2)
#
# formule:
# sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + ... + (v1[n] - v2[n])**2)

# Zet hier je code
from math import sqrt

def afstand(v1, v2):
    return sqrt(sum((v1[i] - v2[i])**2 for i in range(len(v1))))