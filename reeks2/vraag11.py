
# Loops en lists (d)

# Stel dat je een variabele ``values`` hebt met de volgende waarden:
# values = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (d) Schrijf een loop die alle getallen
# van ``values`` vermenigvuldigt en het product op het scherm toont,
# maar gebruik deze keer de index van elk getal.

values = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Zet hier je code
product = 1
for i in range(len(values)):
    product *= values[i]
print(product)