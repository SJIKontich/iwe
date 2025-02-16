
# Zoek de fout in de volgende code:

def f(getallen):
    m = 0
    for getal in getallen:
        if getal > m:
            m = getal
    return m

# 1. Wat verwacht je dat deze code doet? Bekijk de code en voer dit bestand uit.
print(f([1, 2, 3]))
print(f([3, 2, 1]))
print(f([3, 2, 10, 1]))

# Antwoord: de code geeft het grootste getal in de lijst terug

# 2. Schrijf een test die deze verwachting verifieert.

"""
    Je schrijft een test door een nieuwe functie toe te voegen die start met "test_" en je eindigt met assert ...
     (op de plaats van ... vul je de test in)
"""

## Voorbeeld: (verwijder de # zodat deze code kan uitgevoerd worden)

def test_f():
    assert f([1, 2, 3]) == 3

## voer de test uit door op het play icoontje naast de functie te klikken

# 3. Voeg nu een extra assert toe aan de functie en zorg dat die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.