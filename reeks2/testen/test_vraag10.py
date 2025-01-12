from reeks2 import vraag10
from lib.utils import check_exact_match

def test_vraag10():
    check_exact_match(vraag10, "gemiddelde", ([1, 2, 6],), 3)