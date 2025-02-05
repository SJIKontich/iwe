import pytest

from lib.utils import *

try:
    from reeks2 import vraag14
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag14():
    check_exact_match(vraag14, "gemiddelde", ([1, 2, 6],), 3)