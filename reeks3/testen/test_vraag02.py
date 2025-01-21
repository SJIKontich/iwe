from reeks3 import vraag02
from lib.utils import check_exact_match

def test_vraag02_1_1():
    check_exact_match(vraag02, "nulmatrix", (1, 1), [[0]])

def test_vraag02_1_3():
    check_exact_match(vraag02, "nulmatrix", (1, 3), [[0, 0, 0]])

def test_vraag02_2_3():
    check_exact_match(vraag02, "nulmatrix", (2, 3), [[0, 0, 0], [0, 0, 0]])

def test_vraag02_3_2():
    check_exact_match(vraag02, "nulmatrix", (3, 2), [[0, 0], [0, 0], [0, 0]])