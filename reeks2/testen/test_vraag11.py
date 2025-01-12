from reeks2 import vraag11
from lib.utils import check_exact_match

def test_vraag11():
    check_exact_match(vraag11, "vectorsom", ([1, 2, 3], [4, 5, 6]), [5, 7, 9])