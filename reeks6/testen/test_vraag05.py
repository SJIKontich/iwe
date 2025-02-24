import pytest

from lib.utils import *

try:
    from reeks6 import vraag05
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag05():
    check_exact_match(vraag05, "lees_getal", ("getallen1.txt",), 1)
