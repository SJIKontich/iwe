import pytest

from lib.utils import *

try:
    from reeks4 import vraag01
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag01():
    check_exact_match(vraag01, "faculteit", (1,), 1)
    check_exact_match(vraag01, "faculteit", (2,), 2)
    check_exact_match(vraag01, "faculteit", (3,), 6)
    check_exact_match(vraag01, "faculteit", (4,), 24)
    check_exact_match(vraag01, "faculteit", (0,), 1)
