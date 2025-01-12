
# Product

# Schrijf een functie product die een lijst van getallen als parameter heeft
# en het product van de getallen in de lijst teruggeeft.

# Zet hier je code
def product(l):
    return 1 if len(l) == 0 else l[0] * product(l[1:])