from reeks2 import vraag15
from lib.utils import check_exact_match, check_approx_match


def f(x):
    return x ** 2


def test_vraag15():
    check_exact_match(vraag15, "integraal", (f, 0, 1, 1), 0)
    check_exact_match(vraag15, "integraal", (f, 0, 1, 2), 1 / 8)
    check_approx_match(vraag15, "integraal", (f, 0, 1, 1000), 0.3328335)
