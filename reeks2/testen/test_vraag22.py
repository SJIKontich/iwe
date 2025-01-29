from reeks2 import vraag22
from lib.utils import check_exact_match


def test_vraag22():
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 0), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 1), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 3), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 2), [8, 4, 0, 0])
