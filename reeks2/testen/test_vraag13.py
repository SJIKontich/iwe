from reeks2 import vraag13
from lib.utils import check_exact_match

def test_vraag13():
    check_exact_match(vraag13, "product", ([1, 2, 6],), 12)