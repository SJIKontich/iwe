import os
import subprocess

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch == "mijn-oplossingen":
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "commit mijn oplossingen en switch naar alle oplossingen"])
    subprocess.run(["git", "checkout", "oplossing"])