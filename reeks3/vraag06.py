# Zoek de fout in de volgende code:

def som(lijst):
    som = 0
    # begin bij laatste element
    i = len(lijst) - 1
    while i != 0:
        som = som + lijst[i]
        # ga in stapjes van 2 naar het begin van de lijst
        i = i - 2
    return som

# 1. Wat verwacht je dat deze code doet?

# Antwoord: de code geeft de som van alle elementen vanaf het laatste element in de lijst en slaagt telkens 1 element over

# 2. Schrijf een test die deze verwachting verifieert.

# 3. Gebruik de debugger om de fout te vinden en de test te laten slagen.