from reeks2 import vraag12
from lib.utils import check_exact_match

def test_vraag12():
    check_exact_match(vraag12, "vectorpuntproduct", ([1, 2, 3], [4, 5, 6]), [4, 10, 18])