
# Som

# Schrijf een functie som die een lijst van getallen als parameter heeft
# en de som van de getallen in de lijst teruggeeft.
#
# Bij het schrijven van een functie is het een goed idee om te werken volgens een vaste methode:
# 1. Schrijf de naam van de functie.
# 2. Schrijf de parameters van de functie en gebruik betekenisvolle namen.
# 3. Maak een variabele waar het resultaat in wordt opgeslagen. Kies opnieuw een betekenisvolle naam.
# 4. Geeft deze variabele een logische beginwaarde (0, een lege lijst, 1, ...).
# 5. Voeg een return toe van die variabele.
# 6. Begin nu pas met de code van de functie.

# Zet hier je code
def som(getallen):
    som = 0
    for getal in getallen:
        som += getal
    return som