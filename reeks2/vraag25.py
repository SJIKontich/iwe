
# 2048 in 1D

# DEZE VRAAG WERD AL VOOR JOU GEMAAKT, JE MOET HIER NIETS DOEN als je de vorige vragen hebt opgelost

# f. Schrijf een functie naar_rechts die een lijst als parameter heeft en die de functie naar_rechts1
# herhaalt voor alle elementen van de lijst (eerst het meest rechtse element en zo verder naar links).
# De functie geeft een nieuwe lijst terug die het resultaat is van het verschuiven van alle elementen naar rechts.

from reeks2.vraag24 import naar_rechts1

# Zet hier je code
def naar_rechts(lijst):
    n = len(lijst)
    gewijzigd = True
    while gewijzigd:
        gewijzigd = False
        for i in range(n - 1, -1, -1):
            oudelijst = lijst.copy()
            lijst = naar_rechts1(lijst, i)
            if lijst != oudelijst:
                gewijzigd = True
    return lijst