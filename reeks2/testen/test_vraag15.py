from reeks2 import vraag15
from lib.utils import check_exact_match

def test_vraag15():
    check_exact_match(vraag15, "vectorsom", ([1, 2, 3], [4, 5, 6]), [5, 7, 9])