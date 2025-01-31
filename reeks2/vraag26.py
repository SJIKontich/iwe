
# 2048 in 1D

# DEZE VRAAG WERD AL VOOR JOU GEMAAKT, JE MOET HIER NIETS DOEN als je de vorige vragen hebt opgelost.
# Voer dit bestand uit om te spelen ;-)

# g. Schrijf een functie speel die een lijst initialiseert en dan telkens aan de gebruiker vraagt wat er moet gebeuren.
# De gebruiker kan een van de volgende acties kiezen: 'l' (naar links), 'r' (naar rechts), 'q' (stoppen).
# - Als de gebruiker 'l' kiest, wordt de functie naar_links uitgevoerd.
# - Als de gebruiker 'r' kiest, wordt de functie naar_rechts uitgevoerd.
# - Na elke actie wordt er ook een nieuwe 2 toegevoegd aan de lijst op een willekeurige plaats
#   (via de functie voeg_2_toe) en wordt de lijst op het scherm getoond.
# - Als de lijst vol staat met getallen die niet nul zijn, stopt het spel.
# - Als de gebruiker 'q' kiest, stopt het spel.

from vraag20 import initialiseer
from vraag21 import voeg_2_toe
from vraag23 import naar_links
from vraag25 import naar_rechts

# Zet hier je code
def speel(n):
    lijst = initialiseer(n)
    lijst = voeg_2_toe(lijst)
    while True:
        print(lijst)
        actie = input("Wat wil je doen? ")
        if actie == "l":
            lijst = naar_links(lijst)
        elif actie == "r":
            lijst = naar_rechts(lijst)
        elif actie == "q":
            break
        else:
            print("Ongeldige actie")
        lijst = voeg_2_toe(lijst)

# voer dit bestand uit om te spelen
speel(10)

# OPDRACHT:
# 1. maak een bestand 2028.py aan en kopieer de code van alle vorige vragen in dit bestand
# 2. voer dit bestand uit om te spelen om te controleren dat het nog steeds werkt
# 3. meld je aan op chatgpt.com en probeer een gui te schrijven met tkinter om het spel te spelen met jouw eigen code
# 4. voer de code uit en speel het spel even om te controleren dat het werkt
# 5. zorg dat het spel er zoveel mogelijk uitziet als het originele spel 2048 (incl de gekleurde vakjes) en zorg dat het werkt met de pijltjestoetsen