# Zoek de fout in de volgende code:

def tel_klinkers(lijst):
    klinkers = ["a", "e", "i", "o", "u"]
    aantal = 0
    for letter in lijst:
        if letter in klinkers:
            aantal = aantal + 1
    return aantal

# 1. Wat verwacht je dat deze code doet?



# 2. Schrijf een test die deze verwachting verifieert.

# 3. Voeg nu een extra assert toe die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.