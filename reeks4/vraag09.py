
# Vergelijk macht met een for loop en recursie

# Kopieer de code van vraag03.py en pas deze aan zodat je de berekening van de macht vergelijkt met een for loop en recursie.

# Zet hier je code
import time
import reeks4.vraag07
import reeks4.vraag08

x = 2
n = 10

start = time.time()
print(x, "tot de macht", n, "is", reeks4.vraag07.macht(x, n))
print("dit duurde met een for loop", time.time() - start, "seconden")

start = time.time()
print(x, "tot de macht", n, "is", reeks4.vraag08.macht(x, n))
print("dit duurde met recursie", time.time() - start, "seconden")

# welke methode is sneller?

# recursie

# pas n aan naar 100, welke methode is nu sneller?

# recursie

# pas n aan naar 1000, welke methode is nu sneller?

# recursie werkt niet meer

# wat is de conclusie?

# recursie is sneller voor kleine getallen, maar voor grote getallen werkt recursie niet meer