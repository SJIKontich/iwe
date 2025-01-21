from reeks3 import vraag04
from lib.utils import check_exact_match

def test_vraag04():
    check_exact_match(vraag04, "som", ([[1,2,3],[0,1,0]],[[4,2,0],[1,4,-1]]), [[5,4,3],[1,5,-1]])
