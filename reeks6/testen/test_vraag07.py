import pytest

from lib.utils import *

try:
    from reeks6 import vraag07
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag07():
    check_exact_match(vraag07, "product", ([[1,2],[3,4]], [[5,6],[7,8]]), [[19,22],[43,50]])
