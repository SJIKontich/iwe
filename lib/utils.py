# python
import os
import pytest
import inspect
from io import StringIO
import sys


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
    if not os.path.exists(vraag_file):
        pytest.fail(f"Het bestand '{vraag_file}' bestaat niet.")
    # Voeg hier de logica toe om de studentcode uit te voeren en te vergelijken

    # Capture the student's output
    output_capture = StringIO()
    sys.stdout = output_capture

    # Execute the entire student's code
    task_number = vraag_nummer
    if task_number < 10:
        task_number = f"0{task_number}"
    student_file_path = vraag_file
    with open(student_file_path, "r") as student_code:
        code = student_code.read()
        exec(code, globals())

    sys.stdout = sys.__stdout__

    # Verwachte output uit het .out-bestand lezen
    output_file_path = os.path.join(base_dir, f"testen/vraag{task_number}.out")
    with open(output_file_path, "r") as output_file:
        expected_output = output_file.read().strip()

    # Prepare outputs for comparison
    generated_output = output_capture.getvalue().strip()

    # Assert with detailed output on failure
    if generated_output != expected_output:
        print("\n\n------- Verwacht -------\n\n" + expected_output)
        print("\n------- Gekregen -------\n\n" + generated_output)
        print("\n------- Verschil -------:\n")
        for expected, actual in zip(expected_output.splitlines(), generated_output.splitlines()):
            print(f"Verwacht: {expected}")
            print(f"Gekregen:   {actual}")
            print()
        assert False, "De output komt niet overeen, zie hierboven voor details."
