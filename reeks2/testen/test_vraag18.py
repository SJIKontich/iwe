from reeks2 import vraag18
from lib.utils import check_exact_match

def test_vraag18():
    check_exact_match(vraag18, "scalairproduct", ([1, 2, 3], [4, 5, 6]), 32)