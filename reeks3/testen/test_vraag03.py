from reeks3 import vraag03
from lib.utils import check_exact_match

def test_vraag03():
    check_exact_match(vraag03, "eenheidsmatrix", (3,), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
