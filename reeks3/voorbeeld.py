# Bij de aankoop van zakken calletjes krijg je 20% korting vanaf 6 stuks.
# Een zak kost 24 euro. De functie prijs(n) rekent uit
# welke prijs je moet betalen indien je n zakken koopt.

# Zoek de fout in de volgende code:
def prijs(n):
    if n > 6:
        return 24 * n * 0.80
    else:
        return 24 * n

# 1. Wat verwacht je dat deze code doet? Bekijk de code en voer dit bestand uit.
print(prijs(1))
print(prijs(3))
print(prijs(6))


# 2. Schrijf een test die deze verwachting verifieert.

"""
    Je schrijft een test door een nieuwe functie toe te voegen die start met "test_" en je eindigt met assert ...
     (op de plaats van ... vul je de test in)
"""

## Voorbeeld: (verwijder de # om deze code te activeren)

# def test_f():
#     assert f([1, 2, 3]) == 3

## voer de test uit door op het play icoontje naast de functie te klikken

# 3. Voeg nu een extra assert toe aan de functie en zorg dat die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.