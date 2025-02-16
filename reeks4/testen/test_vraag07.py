import pytest

from lib.utils import *

try:
    from reeks4 import vraag07
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag07():
    check_exact_match(vraag07, "macht", (2, 3), 8)
    check_exact_match(vraag07, "macht", (3, 2), 9)
