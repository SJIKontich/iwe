
# Vectoren (a)

# (a) Schrijf een functie vectorsom die twee vectoren optelt. De vectoren worden
# voorgesteld als lijsten van getallen. De functie geeft de som van de twee
# vectoren terug. De lengte van de twee vectoren is gelijk en de functie moet
# hier niet op controleren.
#
# Voorbeeld:
#
# vectorsom([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]

# Zet hier je code
def vectorsom(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result