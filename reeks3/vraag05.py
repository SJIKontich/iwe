# Zoek de fout in de volgende code:

def som_van_reeks(n):
    totaal = 0
    for i in range(n):
        totaal = totaal + i
    return totaal

# De functie zou de som van alle getallen van 1 tot en met n moeten teruggeven.

# 1. Schrijf een test met drie assertions die deze verwachting verifieert. Je zal merken dat de test faalt.
def test_som_van_reeks():
    assert som_van_reeks(1) == 1
    assert som_van_reeks(2) == 3
    assert som_van_reeks(3) == 6

# 2. Gebruik de debugger om de fout te vinden en de test te laten slagen.