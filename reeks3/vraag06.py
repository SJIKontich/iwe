# Zoek de fout in de volgende code:

def som_even_indexen(lijst):
    som = 0
    # begin bij laatste element
    i = len(lijst) - 1
    while i != 0:
        som = som + lijst[i]
        i = i - 2
    return som

# De functie loopt over alle elementen van een lijst van achter naar voor, maar slaat er telkens een over.
# De functie geeft de som van die elementen terug.

# 1. Schrijf een test die deze verwachting verifieert. Je zal merken dat de test faalt.

# 2. Gebruik de debugger om de fout te vinden en de test te laten slagen.