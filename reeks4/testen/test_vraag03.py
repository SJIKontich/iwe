import pytest

from lib.utils import *

try:
    from reeks4 import vraag03
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag03():
    check_exact_match(vraag03, "fib", (1,), 1)
    check_exact_match(vraag03, "fib", (2,), 1)
    check_exact_match(vraag03, "fib", (3,), 2)
    check_exact_match(vraag03, "fib", (4,), 3)
    check_exact_match(vraag03, "fib", (5,), 5)
    check_exact_match(vraag03, "fib", (6,), 8)
    check_exact_match(vraag03, "fib", (7,), 13)
