import pytest

from lib.utils import *

try:
    from reeks2 import vraag24
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag24():
    check_exact_match(vraag24, "naar_rechts1", ([8, 2, 2, 0], 0), [8, 2, 2, 0])
    check_exact_match(vraag24, "naar_rechts1", ([8, 2, 2, 0], 1), [8, 0, 4, 0])
    check_exact_match(vraag24, "naar_rechts1", ([8, 2, 2, 0], 3), [8, 2, 2, 0])
    check_exact_match(vraag24, "naar_rechts1", ([8, 2, 2, 0], 2), [8, 2, 0, 2])
