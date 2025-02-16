
# macht

# Schrijf een functie macht(x, n) die x tot de macht n teruggeeft dmv recursie.

# Zet hier je code
def macht(x, n):
    if n == 0:
        return 1
    else:
        return x * macht(x, n-1)