import pytest

from lib.utils import *

try:
    from reeks6 import vraag11
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag11():
    filename = "matrix_write.txt"
    vraag11.schrijf_matrix(filename, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    file = open(filename)
    assert file.readline().strip() == "1 2 3"
    assert file.readline().strip() == "4 5 6"
    assert file.readline().strip() == "7 8 9"
    file.close()
    os.remove(filename)

