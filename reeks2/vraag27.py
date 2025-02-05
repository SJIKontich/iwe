
# Schaar, steen, papier.

# bekijk het filmpje en noteer de strategie die je best speelt in twee regels

# https://youtu.be/rudzYPHuewc?si=ZKHZhRD4dS2UwaMp

# Regels:
# Als je wint, ... (vul aan)
# Als je verliest, ... (vul aan)

# De functie geeft de keuze terug die de speler moet spelen om te winnen.


# regels:
# als je wint, speel dan wat de andere speelde
# als je verliest, speel dan wat er niet gespeeld werd


def schaar_steen_papier_helper(jij, tegenspeler):
    # de variabele jij en tegenspeler is een van "schaar", "steen" of "papier"

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


