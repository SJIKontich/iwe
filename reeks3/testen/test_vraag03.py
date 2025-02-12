import pytest

from lib.utils import *

try:
    from reeks8 import vraag03
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag03():
    check_exact_match(vraag03, "eenheidsmatrix", (3,), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
