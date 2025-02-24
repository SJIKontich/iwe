import pytest

from lib.utils import *

try:
    from reeks6 import vraag06
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag06():
    check_exact_match(vraag06, "lees_getallen", ("getallen1.txt",), [1, 2, 3])
