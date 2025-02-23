import os
from pathlib import Path

def update_file_in_all_branches(file_to_update):
    # Get the absolute path of the repository root
    repo_root = Path(__file__).resolve().parent.parent

    # Change the working directory to the repository root
    os.chdir(repo_root)

    # Get the current branch
    current_branch = os.popen("git branch --show-current").read().strip()

    # List of branches to update (excluding main)
    branches = ["oplossing", "niveau1", "niveau2", "niveau3"]

    # Iterate over all branches and update them
    for branch in branches:
        # Switch to the branch
        os.system(f"git checkout {branch}")

        # Copy the specified file from the main branch
        os.system(f"git checkout main -- {file_to_update}")

        # Commit the change
        os.system(f"git add {file_to_update}")
        os.system(f'git commit -m "Update {file_to_update} vanuit main" || echo "Geen wijzigingen in {file_to_update} om te committen."')

    # Switch back to the original branch
    os.system(f"git checkout {current_branch}")

# Example usage
update_file_in_all_branches("update.py")