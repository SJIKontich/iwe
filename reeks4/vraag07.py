
# macht

# Schrijf een functie macht(x, n) die x tot de macht n teruggeeft dmv een for loop.

# Zet hier je code
def macht(x, n):
    resultaat = 1
    for i in range(n):
        resultaat = resultaat * x
    return resultaat