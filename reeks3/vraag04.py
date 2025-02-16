# Zoek de fout in de volgende code:

def som(n):
    totaal = 0
    i = 0
    while i < n:
        i = i + 1
        totaal = totaal + i
    return totaal

# De functie zou de som van alle getallen van 1 tot en met n moeten teruggeven.

# 1. Schrijf een test met 3 assertions die deze verwachting verifieert. Je zal merken dat de test faalt.
#       Gebruik de stop knop (rood vierkantje rechtsboven of links bij de testen) om de test te stoppen.

def test_som():
    assert som(2) == 3
    assert som(3) == 6
    assert som(4) == 10

# 2. Gebruik de debugger om ALLE fouten te vinden en de test te laten slagen.
