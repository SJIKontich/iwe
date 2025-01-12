from reeks2 import vraag14
from lib.utils import check_exact_match

def test_vraag14():
    check_exact_match(vraag14, "scalairproduct", ([1, 2, 3], [4, 5, 6]), 32)