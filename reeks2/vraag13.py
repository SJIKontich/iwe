
# Product

# Schrijf een functie product die een lijst van getallen als parameter heeft
# en het product van de getallen in de lijst teruggeeft.

# Zet hier je code
def product(getallen):
    product = 1
    for getal in getallen:
        product *= getal
    return product