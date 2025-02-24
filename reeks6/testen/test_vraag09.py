import pytest

from lib.utils import *

try:
    from reeks6 import vraag09
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag09():
    filename = "getallen_newline.txt"
    vraag09.schrijf_getallen(filename,[1, 2, 3])
    file = open(filename)
    assert file.readline() == "1\n"
    assert file.readline() == "2\n"
    assert file.readline() == "3\n"
    file.close()
    os.remove(filename)

