import pytest

from lib.utils import *

try:
    from reeks2 import vraag11
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")


def test_vraag11():
    run_student_code_and_compare()
