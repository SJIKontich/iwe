import pytest

from lib.utils import *

try:
    from reeks6 import vraag10
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag10():
    filename = "getallen_spatie.txt"
    vraag10.schrijf_getallen(filename,[1, 2, 3])
    file = open(filename)
    assert file.readline().strip() == "1 2 3"
    file.close()
    os.remove(filename)

