# python
import os
import pytest
import inspect

def check_function_exists(module, function_name):
    if not hasattr(module, function_name):
        pytest.fail(f"De functie '{function_name}' is niet gedefinieerd.")

def check_exact_match(module, function_name, args, expected_result):
    check_function_exists(module, function_name)
    function = getattr(module, function_name)
    result = function(*args)
    if result != expected_result:
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        De functie '{function_name}' geeft niet het verwachte resultaat.{reset}")
        print(f"{red}E        Verwacht: {expected_result}{reset}")
        print(f"{red}E        Gekregen: {result}{reset}")
        assert False

def check_approx_match(module, function_name, args, expected_result, tolerance=1e-6):
    check_function_exists(module, function_name)
    function = getattr(module, function_name)
    result = function(*args)
    if not (expected_result - tolerance <= result <= expected_result + tolerance):
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        De functie '{function_name}' geeft niet het verwachte resultaat binnen de tolerantie.{reset}")
        print(f"{red}E        Verwacht: {expected_result} ± {tolerance}{reset}")
        print(f"{red}E        Gekregen: {result}{reset}")
        assert False

def run_student_code_and_compare(vraag_nummer):
    # Get the file path of the calling test file
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename
    test_dir = os.path.dirname(test_file_path)
    base_dir = os.path.dirname(test_dir)
    vraag_file = os.path.join(base_dir, f"vraag{vraag_nummer:02}.py")
    print(f"Debug: Constructed path to vraag file: {vraag_file}")  # Debug print statement
    if not os.path.exists(vraag_file):
        pytest.fail(f"Het bestand '{vraag_file}' bestaat niet.")
    # Voeg hier de logica toe om de studentcode uit te voeren en te vergelijken