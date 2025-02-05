
# Schaar, steen, papier.

# bekijk het filmpje en noteer de strategie die je best speelt in twee regels

# https://youtu.be/rudzYPHuewc?si=ZKHZhRD4dS2UwaMp

# implementeer de functie schaar_steen_papier_helper met twee parameters:
# - de variabele jij bevat de keuze van de speler: schaar, steen of papier
# - de variabele tegenspeler bevat de keuze van de tegenspeler: schaar, steen of papier
# De functie geeft de keuze terug die de speler moet spelen om te winnen. Als het gelijk spel is, moet je niets ingeven.
# De functie drukt ook af of de speler wint of verliest.
#
# 1. zorg dat de functie werkt door de testen te laten draaien
# 2. probeer het nu uit per 3: 2 spelen tegen mekaar en 1 gebruikt de computer om alles in te geven. De eerste speler
#   mag mee kijken op de computer. De computer geeft dan een hint wat je moet spelen. Je doet dat door helemaal onderaan
#   dit bestand de regel schaar_steen_papier_helper_ui() uit te commentarieren (hashtag verwijderen dus). Je voert dan
#   dit bestand uit.


# regels:
# als je wint, speel dan wat de andere speelde
# als je verliest, speel dan wat er niet gespeeld werd


def schaar_steen_papier_helper(jij, tegenspeler):
    # de variabele jij bevat nu de keuze van de speler: schaar, steen of papier
    # de variabele tegenspeler bevat nu de keuze van de tegenspeler: schaar, steen of papier

    # als het gelijk spel is, moet je niets ingeven

    # Zet hier je code
    if (jij == "schaar" and tegenspeler == "papier") or (jij == "steen" and tegenspeler == "schaar") or (jij == "papier" and tegenspeler == "steen"):
        print("Jij wint")
        return tegenspeler
    else:
        nietgespeeld = ""
        if jij != "schaar" and tegenspeler != "schaar":
            nietgespeeld = "schaar"
        elif jij != "steen" and tegenspeler != "steen":
            nietgespeeld = "steen"
        else:
            nietgespeeld = "papier"
        print("Jij verliest")
        return nietgespeeld

def schaar_steen_papier_helper_ui():
    while True:
        jij = input("Wat speel jij? ") # de variabele jij bevat nu de keuze van de speler: schaar, steen of papier
        tegenspeler = input("Wat speelt je tegenspeler? ") # de variabele tegenspeler bevat nu de keuze van de tegenspeler: schaar, steen of papier

        speel = schaar_steen_papier_helper(jij, tegenspeler)
        print("Speel nu", speel)

# schaar_steen_papier_helper_ui()