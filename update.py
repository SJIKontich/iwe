# python
import os

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch != "mijn-oplossingen":
    os.system("git checkout -b mijn-oplossingen")

# Commands to update the student's branch with the latest changes from the main branch
os.system("git config pull.rebase false")
os.system("git pull origin main") # doet ineens merge