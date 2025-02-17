# Bekijk https://drive.google.com/file/d/1x986WswUK8LfAp2CfVRjMcbbXv8ZdI-q/view

# Bij de aankoop van zakken calletjes krijg je 20% korting vanaf 6 stuks.
# Een zak kost 24 euro. De functie prijs(n) rekent uit
# welke prijs je moet betalen indien je n zakken koopt.

# Zoek de fout in de volgende code:
def prijs(n):
    if n >= 6:
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

## Voorbeeld:

def test_prijs():
    assert prijs(1) == 24           # zal slagen
    assert prijs(3) == 72           # zal slagen
    assert prijs(6) == 144 * 0.8    # zal falen

## voer de test uit door op het play icoontje naast de functie te klikken

# 3. Voeg nu een extra assert toe aan de functie en zorg dat die faalt.

# 4. Gebruik de debugger om de fout te vinden en de test te laten slagen.

## Zet een breakpoint op regel 30 (dit is de assertion die faalt).
## Klik op de debug knop (naast de run knop).
## Klik op het icoontje met de pijl naar onder (step into). Je stapt nu de functie binnen.
## Klik op het icoontje met de pijl naar boven en beneden (step over). Je stapt nu naar de volgende regel.
## Terwijl je over de regel gaat, zie je de waarde van de variabelen veranderen.
## Zoek de fout en pas de code aan. Voer de test opnieuw uit.
