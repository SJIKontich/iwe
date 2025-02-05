import pytest

from lib.utils import *

try:
    from reeks2 import vraag01
except (SyntaxError, IndentationError) as e:
    pytest.exit("Er staat een fout in de code")

def test_vraag01():
    check_if_code_contains("for ","for loop")
    run_student_code_and_compare()
