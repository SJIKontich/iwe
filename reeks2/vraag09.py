
# Loops en lists (b)

# Stel dat je een variabele ``values`` hebt met de volgende waarden:
# values = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (b) Schrijf een loop om het kwadraat van
# elk getal op een nieuwe lijn af te drukken op het scherm,
# maar gebruik deze keer de index van elk getal.

values = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Zet hier je code
for i in range(len(values)):
    print(values[i] ** 2)