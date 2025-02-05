
# 2048 in 1D

# b. Schrijf een functie voeg_2_toe die een lijst als parameter heeft en een nieuwe lijst teruggeeft
# waarbij er een 2 wordt toegevoegd op een willekeurige plek in de lijst waar een nul staat.
# Gebruik random.randint om een willekeurige index te kiezen.
# Je mag ervan uitgaan dat er minstens één nul in de lijst staat.

# Voorbeeld van randint:

# getal = randint(0, 10) # geeft een willekeurig getal tussen 0 en 10 (incl.)

from random import randint

def voeg_2_toe(lijst):
    # kies een willekeurige index
    random_index = randint(0, len(lijst) - 1)

    # zolang de waarde op die index niet 0 is, kies een nieuwe index
    while lijst[random_index] != 0:
        random_index = ...

    # zet een 2 op die index
    lijst[random_index] = ...

    return lijst
