
# Vectoren (b)

# (b) Schrijf een functie ''vectorpuntproduct'' die een vector berekent waarvan elk element het product
# is van de overeenkomstige elementen van de twee vectoren.

# Voorbeeld:

# >>> vectorpuntproduct([1, 2, 3], [4, 5, 6])
# [4, 10, 18]

# Zet hier je code
def vectorpuntproduct(v1, v2):
    product = []
    for i in range(len(v1)):
        product.append(v1[...] * v2[...])
    return product