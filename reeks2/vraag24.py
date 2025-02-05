
# 2048 in 1D

# e. Schrijf een functie naar_rechts1 die een lijst als parameter heeft en een index i,
# en die een nieuwe lijst teruggeeft waarbij het element op index i één plaats naar rechts is opgeschoven.

# Je doet dat volgens de regels van het spel 2048:
# - als het element helemaal rechts in de lijst staat,
#       gebeurt er niets.
# - als het element op index i gelijk is aan 0,
#       gebeurt er niets.
# - als het element op index i gelijk is aan het element op index i+1,
#       dan worden deze twee elementen samengevoegd tot de som van de twee elementen.
#       Het element op index i wordt dan 0.
# - als het element op index i+1 gelijk is aan 0,
#       dan wordt het element op index i één plaats naar rechts opgeschoven.
# - als het element op index i niet gelijk is aan het element op index i+1,
#       gebeurt er niets.

def naar_rechts1(l, i):
    # laat dit staan en werk in je code enkel met lijst
    lijst = l.copy()

    # Zet hier je code
    if i == len(lijst) - 1:
        return lijst
    if lijst[i] == 0:
        return lijst
    if lijst[i] == lijst[i + 1]:
        lijst[i + 1] *= 2
        lijst[i] = 0
        return lijst
    elif lijst[i + 1] == 0:
        lijst[i + 1] = lijst[i]
        lijst[i] = 0
        return lijst
    return lijst
