import pytest

from lib.utils import *

try:
    from reeks2 import vraag25
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag25():
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 2, 0],), [0, 0, 8, 4])
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 2, 2],), [0, 8, 2, 4])
    check_exact_match(vraag25, "naar_rechts", ([8, 2, 0, 2],), [0, 0, 8, 4])