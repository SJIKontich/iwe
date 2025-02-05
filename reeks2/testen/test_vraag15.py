import pytest

from lib.utils import *

try:
    from reeks2 import vraag15
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag15():
    check_exact_match(vraag15, "vectorsom", ([1, 2, 3], [4, 5, 6]), [5, 7, 9])