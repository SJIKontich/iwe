import pytest

from lib.utils import *

try:
    from reeks6 import vraag08
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag08():
    check_exact_match(vraag08, "lees_matrix", ("matrix.txt",), [[1, 2, 3], [4, 5, 6]])
