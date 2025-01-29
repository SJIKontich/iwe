from reeks2 import vraag23
from lib.utils import check_exact_match


def test_vraag23():
    check_exact_match(vraag23, "naar_links", ([8, 2, 2, 0],), [8, 4, 0, 0])
    check_exact_match(vraag23, "naar_links", ([8, 2, 2, 2],), [8, 4, 2, 0])
    check_exact_match(vraag23, "naar_links", ([8, 2, 0, 2],), [8, 4, 0, 0])
