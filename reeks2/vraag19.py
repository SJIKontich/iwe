
# Integralen

# Schrijf een functie ''integraal'' die een benadering berekent van de integraal van `f` tussen `a` en `b` met 'n' deelintervallen.

# Denk eraan: integraal(f, a, b, n) = (b-a)/n * (f(x1) + f(x2) + ... + f(xn)) waarbij x1, x2, ..., xn de grenzen van de deelintervallen zijn.

def f(x):
    return x**2

# Zet hier je code
def integraal(f, a, b, n):
    # maak variabelen aan voor de som en de breedte van de deelintervallen
    ...
    # x neemt de eerste waarde aan van het eerste deelinterval
    x = ...
    for i in ...:
        som = ...
        # x neemt de waarde aan van het volgende deelinterval
        x = ...
    return ...