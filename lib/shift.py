import os
import re

def shift_vragen(root_dir, start_index, shift_amount, dry_run=False):
    # Verzamel en sorteer de bestanden
    student_files = sorted([f for f in os.listdir(root_dir) if re.match(r"vraag\d{2}\.py", f)])
    test_files = sorted([f for f in os.listdir(root_dir + "/testen") if re.match(r"test_vraag\d{2}\.py", f)])

    # Reverse loop om overschrijven te vermijden
    for index in range(len(student_files) - 1, start_index - 2, -1):
        old_student_file = student_files[index]
        old_test_file = test_files[index]

        # Bepaal het nieuwe nummer
        new_index = index + shift_amount + 1
        new_student_file = f"vraag{new_index:02}.py"
        new_test_file = f"test_vraag{new_index:02}.py"

        # Toon wat er gaat gebeuren
        print(f"\nHernoemen: {old_student_file} → {new_student_file}")
        print(f"Hernoemen: {old_test_file} → {new_test_file}")

        # Pas testbestand aan als dry-run uit staat
        if not dry_run:
            os.rename(os.path.join(root_dir, old_student_file), os.path.join(root_dir, new_student_file))
            os.rename(os.path.join(root_dir, "testen/" + old_test_file), os.path.join(root_dir, "testen/" + new_test_file))

            # Testbestand intern aanpassen
            test_file_path = os.path.join(root_dir, "testen/" + new_test_file)
            with open(test_file_path, 'r') as file:
                content = file.read()

            # Update import statements en testfuncties
            # content = re.sub(r"from reeks\d+\.vraag\d{2}", f"from {root_dir}.vraag{new_index:02}", content)
            # content = re.sub(r"def test_vraag\d{2}", f"def test_vraag{new_index:02}", content)
            # content = re.sub(r"from reeks\d+ import vraag\d{2}", f"from {root_dir} import vraag{new_index:02}", content)
            # content = re.sub(r"if not hasattr\(vraag\d{2}", f"if not hasattr(vraag{new_index:02}", content)
            # content = re.sub(r"resultaat = vraag\d{2}\.", f"resultaat = vraag{new_index:02}.", content)
            content = re.sub(r"vraag\d{2}", f"vraag{new_index:02}", content)

            with open(test_file_path, 'w') as file:
                file.write(content)

    print(f"\nShift van {shift_amount} uitgevoerd vanaf vraag{start_index:02}!")
    if dry_run:
        print("\n[DRY RUN]: Geen bestanden gewijzigd, alleen simulatie uitgevoerd.")

# ✅ Gebruik: Shift met dry-run
shift_vragen("reeks2", start_index=14, shift_amount=1, dry_run=True)

# ✅ Gebruik: Echte shift
# shift_vragen("reeks2", start_index=14, shift_amount=1, dry_run=False)
