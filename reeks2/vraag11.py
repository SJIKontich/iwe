from itertools import product

# Loops en lists (d)

# (d) Toon het product van alle getallen van ``values`` op het scherm mbv de index van elk getal.

values = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Zet hier je code
product = 1
for i in range(len(values)):
    product = product * values[i]
print(product)