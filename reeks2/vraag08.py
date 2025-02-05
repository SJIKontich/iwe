
# Loops en lists (a)

# Je kan al loopen over een lijst met een for-lus op basis van de waarden,
# maar in veel gevallen heb je ook de index (de positie, beginnend bij 0) nodig.

# Voorbeeld:
# for i in range(len(lijst)):
#     print("Op index",i, "staat het getal", lijst[i])

# dit toont telkens de index (de positie in de lijst, beginnend bij 0) en de waarde van de lijst op die index.

# Stel dat je een variabele ``values`` hebt met de volgende waarden:
# values = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (a) Schrijf een loop om elk getal op een
# nieuwe lijn af te drukken op het scherm,
# maar gebruik deze keer de index van elk getal.

values = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Zet hier je code
for i in range(len(values)):
    print(values[i])