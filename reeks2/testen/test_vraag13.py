from reeks2 import vraag13
from lib.utils import check_exact_match

def test_vraag13():
    check_exact_match(vraag13, "afstand", ([1, 2, 3], [4, 5, 6]), 5.196152422706632)