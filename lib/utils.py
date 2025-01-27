# python
import os
import pytest
import inspect
from io import StringIO
import sys
import json
import requests
from pathlib import Path

# Constants for Google Forms submission
# GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfVwBwDdUL8oKIvBp7tw9cVz86qC8dfxpXm-nWtmrbqGPqxDQ/viewform?usp=pp_url&entry.842475428=Tom&entry.2108741726=1&entry.816748641=2"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfVwBwDdUL8oKIvBp7tw9cVz86qC8dfxpXm-nWtmrbqGPqxDQ/formResponse"
LOG_FILE = "submitted_tests.json"

# Load submitted tests log
submitted_tests = {}
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as log_file:
        submitted_tests = json.load(log_file)


def save_submission_log():
    """Save the updated submission log to the log file."""
    with open(LOG_FILE, "w") as log_file:
        json.dump(submitted_tests, log_file)


def submit_google_form(reeks, vraag_nummer, student_id):
    """Submit the form if not already submitted for this test."""
    key = f"{reeks}_vraag{vraag_nummer:02}"

    if key in submitted_tests and submitted_tests[key] == student_id:
        # print(f"[INFO] Formulier voor {key} is al eerder ingediend voor student {student_id}.")
        return

    # Data for Google Forms submission
    form_data = {
        "entry.2108741726": reeks,  # Pas deze aan voor reeks
        "entry.816748641": vraag_nummer,  # Pas deze aan voor vraag nummer
        "entry.842475428": student_id,  # Pas deze aan voor student ID
    }

    response = requests.post(GOOGLE_FORM_URL, data=form_data)

    if response.status_code == 200:
        # print(f"[INFO] Formulier succesvol ingediend voor {key}.")
        submitted_tests[key] = student_id
        save_submission_log()
    else:
        print(f"[ERROR] Formulier indiening mislukt voor {key}. Status: {response.status_code}")

def extract_reeks_and_vraag(test_file_path):
    """Extract reeks and vraag number from the test file path."""
    path_parts = Path(test_file_path).parts
    try:
        reeks = path_parts[-3]  # Assuming the structure is: .../reeksX/testen/test_vraagYY.py
        test_file_name = path_parts[-1]
        if not test_file_name.startswith("test_vraag") or not test_file_name.endswith(".py"):
            pytest.fail(f"Ongeldig testbestand: '{test_file_name}'. Naam moet 'test_vraagYY.py' zijn.")
        vraag_nummer = int(test_file_name.replace("test_vraag", "").replace(".py", ""))
        return reeks, vraag_nummer
    except (IndexError, ValueError):
        pytest.fail(f"Kan reeks en vraagnummer niet bepalen uit pad: {test_file_path}")

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

    # Als de test slaagt, log de voortgang
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename
    reeks, vraag_nummer = extract_reeks_and_vraag(test_file_path)
    student_id = os.getlogin()  # Huidige aangemelde gebruiker als ID
    submit_google_form(reeks, vraag_nummer, student_id)

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

    # Als de test slaagt, log de voortgang
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename
    reeks, vraag_nummer = extract_reeks_and_vraag(test_file_path)
    student_id = os.getlogin()  # Huidige aangemelde gebruiker als ID
    submit_google_form(reeks, vraag_nummer, student_id)

def run_student_code_and_compare():
    # Get the file path of the calling test file
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename

    # Determine reeks and vraag_nummer from the file path
    reeks, vraag_nummer = extract_reeks_and_vraag(test_file_path)

    test_dir = os.path.dirname(test_file_path)
    base_dir = os.path.dirname(test_dir)
    vraag_file = os.path.join(base_dir, f"vraag{vraag_nummer:02}.py")
    if not os.path.exists(vraag_file):
        pytest.fail(f"Het bestand '{vraag_file}' bestaat niet.")

    # Capture the student's output
    output_capture = StringIO()
    sys.stdout = output_capture

    # Execute the entire student's code
    student_file_path = vraag_file
    with open(student_file_path, "r") as student_code:
        code = student_code.read()
        exec(code, globals())

    sys.stdout = sys.__stdout__

    # Verwachte output uit het .out-bestand lezen
    output_file_path = os.path.join(test_dir, f"vraag{vraag_nummer:02}.out")
    if not os.path.exists(output_file_path):
        pytest.fail(f"Het bestand '{output_file_path}' met verwachte output bestaat niet.")

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

    # Als de test slaagt, log de voortgang
    student_id = os.getlogin()  # Huidige aangemelde gebruiker als ID
    submit_google_form(reeks, vraag_nummer, student_id)

