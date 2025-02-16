import pytest

from lib.utils import *

try:
    from reeks4 import vraag11
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag06():
    check_exact_match(vraag11, "fib", (1,), 1)
    check_exact_match(vraag11, "fib", (2,), 1)
    check_exact_match(vraag11, "fib", (3,), 2)
    check_exact_match(vraag11, "fib", (4,), 3)
    check_exact_match(vraag11, "fib", (5,), 5)
    check_exact_match(vraag11, "fib", (6,), 8)
    check_exact_match(vraag11, "fib", (7,), 13)