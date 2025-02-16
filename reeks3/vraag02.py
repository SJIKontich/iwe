
# Zoek de fout in de volgende code:

def som(getallen):
    totaal = 0
    for getal in getallen:
        if getal > 0:
            totaal = totaal + getal
        else:
            totaal = totaal + 0 # of doe de else weg
    return totaal

# 1. Wat verwacht je dat deze code doet?

# Antwoord: de code geeft de som van alle positieve getallen in de lijst terug


# 2. Schrijf een test die deze verwachting verifieert.

def test_som():
    assert som([1, 2, 3]) == 6
    assert som([1, 2, -3]) == 3

# 3. Voeg nu een extra assert toe die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.
