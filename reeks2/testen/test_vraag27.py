from reeks2 import vraag27
from lib.utils import check_exact_match, check_approx_match


def test_vraag27():
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("schaar", "papier"), "papier")
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("steen", "schaar"), "schaar")
    check_exact_match(vraag27, "schaar_steen_papier_helper", ("papier", "steen"), "steen")