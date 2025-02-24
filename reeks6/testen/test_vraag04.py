import pytest

from lib.utils import *

try:
    from reeks6 import vraag04
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag04():
    check_exact_match(vraag04, "lees_regels", ("tekst.txt",), ["dit is een versleutelde boodschap met een ceasar cipher van 3:","nl krx ydq sxbqkr"])
