from reeks2 import vraag12
from lib.utils import check_exact_match

def test_vraag12():
    check_exact_match(vraag12, "som", ([1, 2, 6],), 9)