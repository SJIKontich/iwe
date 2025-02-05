import pytest

from lib.utils import *

try:
    from reeks2 import vraag12
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag12():
    check_exact_match(vraag12, "som", ([1, 2, 6],), 9)