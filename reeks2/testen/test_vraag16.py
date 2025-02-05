import pytest

from lib.utils import *

try:
    from reeks2 import vraag16
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag16():
    check_exact_match(vraag16, "vectorpuntproduct", ([1, 2, 3], [4, 5, 6]), [4, 10, 18])