
# 2048 in 1D

# b. Schrijf een functie voeg_2_toe die een lijst als parameter heeft en een nieuwe lijst teruggeeft
# waarbij er een 2 wordt toegevoegd op een willekeurige plek in de lijst waar een nul staat.
# Gebruik random.randint om een willekeurige index te kiezen.
# Je mag ervan uitgaan dat er minstens één nul in de lijst staat.

# Voorbeeld van randint:

# getal = random.randint(0, 10) # geeft een willekeurig getal tussen 0 en 10 (incl.)

import random

def voeg_2_toe(lijst):
    # Zet hier je code, je mag de pass hieronder verwijderen, die staat er zodat de testen kunnen werken
    index = random.randint(0, len(lijst) - 1)
    while lijst[index] != 0:
        index = random.randint(0, len(lijst) - 1)
    lijst[index] = 2
    return lijst