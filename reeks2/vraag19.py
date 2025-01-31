
# Integralen

# Schrijf een functie `integraal` die een functie `f`, een startpunt `a`, een eindpunt `b` en een
# parameter `n` als argumenten heeft en de benadering van de integraal van `f` tussen `a` en `b`
# berekent. De parameter `n` geeft aan hoeveel deelintervallen van gelijke breedte gebruikt
# worden. De functie geeft de benadering van de integraal terug.

# De breedte van de deelintervallen is `(b - a) / n`. De benadering van de integraal wordt
# berekend door de som van de oppervlaktes van rechthoeken die de functie `f` benaderen op
# elk deelinterval.

# Riemann toonde aan dat het niet uitmaakt welke rechthoeken je gebruikt om de (georienteerde) oppervlakte te
# benaderen (ondersom, bovensom, linkersom, rechtersom, ...), de benadering van de
# integraal zal altijd naar dezelfde waarde convergeren als `n` naar oneindig gaat.

# De functie kan je testen met de gegeven functie `f`. We zullen voor de eenvoud de linkergrens
# van de rechthoek gebruiken om de functie te benaderen. De functie moet de benadering
# van de integraal teruggeven.

# Voorbeeld:
#
# def f(x):
#     return x**2
#
# integraal(f, 0, 1, 100) -> 0.3283500000000001

def f(x):
    return x**2

# Zet hier je code
def integraal(f, a, b, n):
    dx = (b - a) / n
    som = 0
    # of met start variabele
    start = a
    for i in range(n):
        som += f(a + i * dx)
        # som += f(start)
        # start += dx
    return som * dx

