import pytest

from lib.utils import *

try:
    from reeks6 import vraag06
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag06():
    check_exact_match(vraag06, "som", ([[1,2,3],[0,1,0]],[[4,2,0],[1,4,-1]]), [[5,4,3],[1,5,-1]])
