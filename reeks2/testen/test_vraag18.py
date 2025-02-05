import pytest

from lib.utils import *

try:
    from reeks2 import vraag18
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag18():
    check_exact_match(vraag18, "scalairproduct", ([1, 2, 3], [4, 5, 6]), 32)