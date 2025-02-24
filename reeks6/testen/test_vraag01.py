import pytest

from lib.utils import *

try:
    from reeks6 import vraag01
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag01():
    check_exact_match(vraag01, "lees_regel", ("tekst.txt",), "dit is een versleutelde boodschap met een ceasar cipher van 3:\n")
