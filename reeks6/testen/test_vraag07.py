import pytest

from lib.utils import *

try:
    from reeks6 import vraag07
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag07():
    check_exact_match(vraag07, "lees_getallen", ["getallen2.txt"], [1, 2, 3])
