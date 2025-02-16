# Recursie

Recursie betekent dat een functie zichzelf aanroept. Dit kan handig zijn als je een probleem hebt dat je kan opdelen in kleinere problemen die op dezelfde manier opgelost kunnen worden.

## Voorbeeld 1

Je kent recursie al van rijen. Veel rijen hebben een expliciet en een recursief voorschrift.

De rekenkundige rij met verschil 1 heeft als recursief voorschrift: $a_{n+1} = a_n + 1$. 
Je definieert een term van de rij op basis van de vorige term.

Een functie schrijven die de $n$-de term van deze rij berekent, kan op de volgende manier:

```python
def rekenkundige_rij(n):
    if n == 0:
        return 0
    else:
        return rekenkundige_rij(n-1) + 1
```

Je merkt dat de functie `rekenkundige_rij` zichzelf aanroept. Dit is een voorbeeld van recursie.

Elke recursieve functie heeft een basisgeval nodig. Dit is een geval waarvoor de functie niet zichzelf aanroept, maar een waarde teruggeeft. In dit geval is het basisgeval $n = 0$. Als $n = 0$, dan is de $n$-de term van de rekenkundige rij gelijk aan 0.

## Voorbeeld 2

De rij van Fibonacci is een bekende rij die je kan definiëren met recursie. De rij begint met de getallen 0 en 1. De volgende termen van de rij zijn de som van de twee voorgaande termen. Het recursief voorschrift is dan: $F_{n+2} = F_{n+1} + F_n$.

Er zijn nu 2 basisgevallen nodig: $F_0 = 0$ en $F_1 = 1$. 