
# som tem n

# Schrijf een functie som(n) die de som van de getallen van 1 tot en met n teruggeeft dmv recursie.

# Zet hier je code
def som(n):
    if n == 0:
        return 0
    else:
        return n + som(n-1)