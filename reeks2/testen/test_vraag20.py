from reeks2 import vraag20
from lib.utils import check_exact_match, check_approx_match


def test_vraag20():
    check_exact_match(vraag20, "initialiseer", (3,),[0,0,0])
    check_exact_match(vraag20, "initialiseer", (5,),[0,0,0,0,0])