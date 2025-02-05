
# Vectoren (b)

# (b) Schrijf een functie vectorpuntproduct die het puntproduct van twee vectoren
# berekent. De vectoren worden voorgesteld als lijsten van getallen. De functie
# geeft het puntproduct van de twee vectoren terug. De lengte van de twee
# vectoren is gelijk en de functie moet hier niet op controleren.
# Het puntproduct van twee vectoren is een vector waarvan elk element het product
# is van de overeenkomstige elementen van de twee vectoren.
#
# Voorbeeld:
#
# vectorpuntproduct([1, 2, 3], [4, 5, 6]) -> [4, 10, 18]
#
# merk op dat je dus een nieuwe lijst teruggeeft

# Zet hier je code
def vectorpuntproduct(v1, v2):
    product = []
    for i in range(len(v1)):
        product.append(v1[i] * v2[i])
    return product