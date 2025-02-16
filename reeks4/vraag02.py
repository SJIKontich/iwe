
# Faculteit

# Schrijf een functie faculteit(n) die de faculteit van n teruggeeft dmv recursie.

# Zet hier je code
def faculteit(n):
    if n == 0:
        return 1
    else:
        return n * faculteit(n-1)