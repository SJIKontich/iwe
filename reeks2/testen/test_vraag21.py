import pytest

from lib.utils import *

try:
    from reeks2 import vraag21
    from reeks2.vraag21 import voeg_2_toe
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag21():
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([0, 0, 0, 0]).count(2) == 1, "Er is geen 2 toegevoegd aan de lijst [0, 0, 0, 0]")
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([0, 2, 0, 0]).count(2) == 2, "Er is geen 2 toegevoegd aan de lijst [0, 2, 0, 0]")
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([2, 2, 2, 0]).count(2) == 4, "Er is geen 2 toegevoegd aan de lijst [2, 2, 2, 0]")
