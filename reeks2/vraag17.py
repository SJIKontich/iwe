
# 2048 in 1D

# b. Schrijf een functie voeg_2_toe die een lijst als parameter heeft en een nieuwe lijst teruggeeft
# waarbij er een 2 wordt toegevoegd op een willekeurige plek in de lijst waar geen nul staat.

# c. Schrijf een functie naar_links1 die een lijst als parameter heeft en een index i,
# en die een nieuwe lijst teruggeeft waarbij het element op index i één plaats naar links is opgeschoven.
# Je doet dat volgens de regels van het spel 2048: als het element op index i gelijk is aan 0,
# gebeurt er niets. Als het element op index i gelijk is aan het element op index i+1, dan worden
# deze twee elementen samengevoegd tot één element dat gelijk is aan de som van de twee elementen.
# Het element op index i+1 wordt dan 0. Als het element op index i niet gelijk is aan 0 en niet gelijk
# is aan het element op index i+1, gebeurt er niets.
# Als het element helemaal links in de lijst staat, gebeurt er niets.

# d. Schrijf een functie naar_links die een lijst als parameter heeft en die de functie naar_links1
# herhaalt voor alle elementen van de lijst (eerst het meest linkse element en zo verder naar rechts).
# De functie geeft een nieuwe lijst terug die het resultaat is van het verschuiven van alle elementen naar links.

# e. Schrijf een functie naar_rechts1 die een lijst als parameter heeft en een index i,
# en die een nieuwe lijst teruggeeft waarbij het element op index i één plaats naar rechts is opgeschoven.

# f. Schrijf een functie naar_rechts die een lijst als parameter heeft en die de functie naar_rechts1
# herhaalt voor alle elementen van de lijst (eerst het meest rechtse element en zo verder naar links).
# De functie geeft een nieuwe lijst terug die het resultaat is van het verschuiven van alle elementen naar rechts.

# g. Schrijf een functie speel die een lijst initialiseert en dan telkens aan de gebruiker vraagt wat er moet gebeuren.
# De gebruiker kan een van de volgende acties kiezen: 'l' (naar links), 'r' (naar rechts), 'q' (stoppen).
# - Als de gebruiker 'l' kiest, wordt de functie naar_links uitgevoerd.
# - Als de gebruiker 'r' kiest, wordt de functie naar_rechts uitgevoerd.
# - Na elke actie wordt er ook een nieuwe 2 toegevoegd aan de lijst op een willekeurige plaats
#   (via de functie voeg_2_toe) en wordt de lijst op het scherm getoond.
# - Als de lijst vol staat met getallen die niet nul zijn, stopt het spel.
# - Als de gebruiker 'q' kiest, stopt het spel.

# Zet hier je code