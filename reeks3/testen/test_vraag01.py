import pytest

from lib.utils import *

try:
    from reeks3 import vraag01
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag01():
    check_exact_match(vraag01, "nulvector", (3,), [0, 0, 0])
