from reeks3 import vraag01
from lib.utils import check_exact_match

def test_vraag01():
    check_exact_match(vraag01, "nulvector", (3,), [0, 0, 0])
