
# Rijst

# Een koning wil een beloning geven aan een onderdaan.
# Hij wil de onderdaan belonen met rijst.
# De koning wil de onderdaan belonen met 1 rijstkorrel op het eerste vakje van een schaakbord,
# 2 rijstkorrels op het tweede vakje,
# 4 rijstkorrels op het derde vakje,
# 8 rijstkorrels op het vierde vakje, enzovoort.
# De koning wil de onderdaan belonen met rijst op alle 64 vakjes van het schaakbord.

# a) Schrijf een recursieve functie aantal_rijstkorrels(n) dat berekent hoeveel rijstkorrels er op het n-de vakje van het schaakbord liggen.
# b) Schrijf een iteratieve functie totaal_aantal_rijstkorrels() dat berekent hoeveel rijstkorrels de koning moet geven aan de onderdaan.

# Zet hier je code
def aantal_rijstkorrels(n):
    if n == 1:
        return 1
    else:
        return 2 * aantal_rijstkorrels(n-1)

def totaal_aantal_rijstkorrels():
    resultaat = 0
    for i in range(1, 65):
        resultaat = resultaat + aantal_rijstkorrels(i)
    return resultaat