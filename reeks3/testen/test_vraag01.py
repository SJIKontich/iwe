from reeks3 import vraag01
from lib.utils import check_exact_match

def test_vraag01():
    check_exact_match(vraag01, "som", ([[1,2,3],[0,1,0]],[[4,2,0],[1,4,-1]]), [[5,4,3],[1,5,-1]])
