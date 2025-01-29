from reeks2 import vraag25
from lib.utils import check_exact_match, check_approx_match


def test_vraag25():
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 2, 0],), [0, 0, 8, 4])
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 2, 2],), [0, 8, 2, 4])
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 0, 2],), [0, 0, 8, 4])