from reeks2 import vraag21
from lib.utils import check_assertion
from reeks2.vraag21 import voeg_2_toe


def test_vraag21():
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([0, 0, 0, 0]).count(2) == 1, "Er is geen 2 toegevoegd aan de lijst [0, 0, 0, 0]")
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([0, 2, 0, 0]).count(2) == 2, "Er is geen 2 toegevoegd aan de lijst [0, 2, 0, 0]")
    check_assertion(vraag21, "voeg_2_toe", voeg_2_toe([2, 2, 2, 0]).count(2) == 4, "Er is geen 2 toegevoegd aan de lijst [2, 2, 2, 0]")
