# python
import os

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch == "mijn-oplossingen":
    os.system("git add .")
    os.system("git commit -m 'commit mijn oplossingen en switch naar alle oplossingen'")
    os.system("git checkout oplossing")