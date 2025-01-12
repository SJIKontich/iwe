from reeks2 import vraag09
from lib.utils import check_exact_match

def test_vraag09():
    check_exact_match(vraag09, "product", ([1, 2, 6],), 12)