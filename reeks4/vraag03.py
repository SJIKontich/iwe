
# Vergelijk faculteit met een for loop en recursie

# Lees de code hieronder.

import time
import reeks4.vraag01
import reeks4.vraag02

n = 10

start = time.time()
print(n,"! = ", reeks4.vraag01.faculteit(n))
print("dit duurde met een for loop" , time.time() - start, "seconden")

start = time.time()
print(n,"! = ", reeks4.vraag02.faculteit(n))
print("dit duurde met recursie" , time.time() - start, "seconden")

# wat doet deze code?

# welke methode is sneller?

# pas n aan naar 100, welke methode is nu sneller?

# pas n aan naar 1000, welke methode is nu sneller?

# wat is de conclusie?
