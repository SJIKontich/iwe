import pytest

from lib.utils import *

try:
    from reeks8 import vraag05
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag05():
    check_exact_match(vraag05, "aantalkolommen", ([[1, 2, 3], [4, 5, 6]],), 3)
