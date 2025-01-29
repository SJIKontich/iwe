
# 2048 in 1D

# DEZE VRAAG WERD AL VOOR JOU GEMAAKT, JE MOET HIER NIETS DOEN als je de vorige vragen hebt opgelost

# d. Schrijf een functie naar_links die een lijst als parameter heeft en die de functie naar_links1
# herhaalt voor alle elementen van de lijst (eerst het meest linkse element en zo verder naar rechts).
# De functie geeft een nieuwe lijst terug die het resultaat is van het verschuiven van alle elementen naar links.

from reeks2.vraag22 import naar_links1

# Zet hier je code: evt gewoon geven
def naar_links(lijst):
    n = len(lijst)
    gewijzigd = True
    while gewijzigd:
        gewijzigd = False
        for i in range(n):
            oudelijst = lijst.copy()
            lijst = naar_links1(lijst, i)
            if lijst != oudelijst:
                gewijzigd = True
    return lijst