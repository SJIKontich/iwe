from lib.utils import run_student_code_and_compare,check_if_code_contains

def test_vraag02():
    check_if_code_contains("for ","for loop")
    run_student_code_and_compare()
