import pytest

from lib.utils import *

try:
    from reeks2 import vraag27
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag27():
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("schaar", "papier"), "papier")
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("steen", "schaar"), "schaar")
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("papier", "steen"), "steen")