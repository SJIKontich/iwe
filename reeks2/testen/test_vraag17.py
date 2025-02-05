import pytest

from lib.utils import *

try:
    from reeks2 import vraag17
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag17():
    check_exact_match(vraag17, "afstand", ([1, 2, 3], [4, 5, 6]), 5.196152422706632)