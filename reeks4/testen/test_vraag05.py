import pytest

from lib.utils import *

try:
    from reeks4 import vraag05
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag05():
    check_exact_match(vraag05, "som", (3,), 6)
    check_exact_match(vraag05, "som", (4,), 10)
    check_exact_match(vraag05, "som", (5,), 15)
