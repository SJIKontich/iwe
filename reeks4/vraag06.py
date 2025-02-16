
# Vergelijk som met een for loop en recursie

# Kopieer de code van vraag03.py en pas deze aan zodat je de berekening van de som vergelijkt met een for loop en recursie.

# Zet hier je code

import time
import reeks4.vraag04
import reeks4.vraag05

n = 10

start = time.time()
print("De som van 1 tot en met", n, "is", reeks4.vraag04.som(n))
print("dit duurde met een for loop" , time.time() - start, "seconden")

start = time.time()
print("De som van 1 tot en met", n, "is", reeks4.vraag05.som(n))
print("dit duurde met recursie" , time.time() - start, "seconden")

# welke methode is sneller?

# recursie

# pas n aan naar 100, welke methode is nu sneller?

# recursie

# pas n aan naar 1000, welke methode is nu sneller?

# recursie werkt niet meer

# wat is de conclusie?
