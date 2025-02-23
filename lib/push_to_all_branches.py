import os
from pathlib import Path

def push_to_all_branches():
    # Get the absolute path of the repository root
    repo_root = Path(__file__).resolve().parent.parent

    # Change the working directory to the repository root
    os.chdir(repo_root)

    branches = ["oplossing", "niveau1", "niveau2", "niveau3"]

    for branch in branches:
        os.system(f"git push origin {branch}")

push_to_all_branches()