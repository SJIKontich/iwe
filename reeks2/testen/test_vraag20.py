import pytest

from lib.utils import *

try:
    from reeks2 import vraag20
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag20():
    check_exact_match(vraag20, "initialiseer", (3,),[0,0,0])
    check_exact_match(vraag20, "initialiseer", (5,),[0,0,0,0,0])