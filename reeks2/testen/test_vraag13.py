import pytest

from lib.utils import *

try:
    from reeks2 import vraag13
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag13():
    check_exact_match(vraag13, "product", ([1, 2, 6],), 12)