
# Nulmatrix maken

# Schrijf een functie nulmatrix(aantalrijen,aantalkolommen) om een nulmatrix te maken.
#
# Doe dit in stappen (elke stap heeft een extra test). Probeer met een matrix met
# - 1 rij en 1 kolom en roep de functie nulvector op van de vorige vraag
# - 1 rij en 3 kolommen
# - 2 rijen en 3 kolommen

from reeks3.vraag01 import nulvector

# Zet hier je code
def nulmatrix(aantalrijen, aantalkolommen):
    matrix = []
    for i in range(aantalrijen):
        matrix.append(nulvector(aantalkolommen))
    return matrix