# 1. zorg dat de functie werkt door de testen te laten draaien
# 2. probeer het nu uit per 3: 2 spelen tegen mekaar en 1 gebruikt de computer om alles in te geven. De eerste speler
#   mag mee kijken op de computer. De computer geeft dan een hint wat je moet spelen. Je doet dat door helemaal onderaan
#   dit bestand de regel schaar_steen_papier_helper_ui() uit te commentarieren (hashtag verwijderen dus). Je voert dan
#   dit bestand uit.

from reeks2.vraag27 import schaar_steen_papier_helper

def schaar_steen_papier_helper_ui():
    while True:
        jij = input("Wat speel jij? ") # de variabele jij bevat nu de keuze van de speler: schaar, steen of papier
        tegenspeler = input("Wat speelt je tegenspeler? ") # de variabele tegenspeler bevat nu de keuze van de tegenspeler: schaar, steen of papier

        speel = schaar_steen_papier_helper(jij, tegenspeler)
        print("Speel nu", speel)

schaar_steen_papier_helper_ui()