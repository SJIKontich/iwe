from reeks2 import vraag16
from lib.utils import check_exact_match

def test_vraag16():
    check_exact_match(vraag16, "vectorpuntproduct", ([1, 2, 3], [4, 5, 6]), [4, 10, 18])