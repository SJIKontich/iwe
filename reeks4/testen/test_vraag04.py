import pytest

from lib.utils import *

try:
    from reeks4 import vraag04
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag04():
    check_exact_match(vraag04, "som", (3,), 6)
    check_exact_match(vraag04, "som", (4,), 10)
    check_exact_match(vraag04, "som", (5,), 15)
