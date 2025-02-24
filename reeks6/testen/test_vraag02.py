import pytest

from lib.utils import *

try:
    from reeks6 import vraag02
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag02():
    check_exact_match(vraag02, "lees_regel", ("tekst.txt",), "dit is een versleutelde boodschap met een ceasar cipher van 3:")
