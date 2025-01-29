from reeks2 import vraag17
from lib.utils import check_exact_match

def test_vraag17():
    check_exact_match(vraag17, "afstand", ([1, 2, 3], [4, 5, 6]), 5.196152422706632)