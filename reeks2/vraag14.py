
# Gemiddelde

# Schrijf een functie ''gemiddelde'' die een lijst van getallen als parameter heeft
# en het gemiddelde van de getallen in de lijst teruggeeft.

# Zet hier je code
def gemiddelde(getallen):
    som = 0
    for getal in getallen:
        som += getal
    return som / len(getallen)