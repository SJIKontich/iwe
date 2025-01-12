from reeks2 import vraag08
from lib.utils import check_exact_match

def test_vraag08():
    check_exact_match(vraag08, "som", ([1, 2, 6],), 9)