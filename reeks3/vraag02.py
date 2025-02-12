
# Zoek de fout in de volgende code:

def som_positieve_getallen(getallen):
    totaal = 0
    for getal in getallen:
        if getal > 0:
            totaal += getal
        else:
            totaal = 0
    return totaal

# De functie zou de som van alle positieve getallen in de lijst moeten teruggeven.
# Test de functie met verschillende lijsten en zoek de fout.

# 1. Wat verwacht je dat deze code doet?



# 2. Schrijf een test die deze verwachting verifieert.

# 3. Voeg nu een extra assert toe aan de test_som_positieve_getallen functie en zorg dat die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.