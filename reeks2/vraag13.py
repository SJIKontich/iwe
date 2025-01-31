
# Product

# Schrijf een functie product die een lijst van getallen als parameter heeft
# en het product van de getallen in de lijst teruggeeft.

# Zet hier je code
def product(getallen: list) -> int:
    result = 1
    for getal in getallen:
        result *= getal
    return result