
# Zoek de fout in de volgende code:

def som(getallen):
    totaal = 0
    for getal in getallen:
        if getal > 0:
            totaal = totaal + getal
        else:
            totaal = 0
    return totaal

# 1. Wat verwacht je dat deze code doet?



# 2. Schrijf een test die deze verwachting verifieert.

# 3. Voeg nu een extra assert toe die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.