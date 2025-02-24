import pytest

from lib.utils import *

try:
    from reeks5 import vraag04
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag05():
    check_exact_match(vraag04, "aantalrijen", ([[1, 2, 3], [4, 5, 6]],), 2)
