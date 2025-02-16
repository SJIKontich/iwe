import pytest

from lib.utils import *

try:
    from reeks4 import vraag10
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag10a():
    check_exact_match(vraag10, "aantal_rijstkorrels", (1,), 1)
    check_exact_match(vraag10, "aantal_rijstkorrels", (2,), 2)
    check_exact_match(vraag10, "aantal_rijstkorrels", (3,), 4)

def test_vraag10b():
    check_exact_match(vraag10, "totaal_aantal_rijstkorrels", (), 18446744073709551615)
