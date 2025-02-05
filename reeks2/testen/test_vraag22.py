import pytest

from lib.utils import *

try:
    from reeks2 import vraag22
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag22():
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 0), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 1), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 3), [8, 2, 2, 0])
    check_exact_match(vraag22, "naar_links1", ([8, 2, 2, 0], 2), [8, 4, 0, 0])
