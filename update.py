# python
import os
import sys

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch != "mijn-oplossingen":
    os.system("git checkout -b mijn-oplossingen")
    # print("Error: Je hebt de setup niet uitgevoerd.")
    # sys.exit(1)

# Commands to update the student's branch with the latest changes from the main branch
# os.system("git add .")
# os.system('git commit -m "Mijn oplossingen"')
# os.system("git checkout main")
os.system("git config pull.rebase false")
os.system("git pull origin main") # doet ineens merge
# os.system("git checkout mijn-oplossingen")
# os.system("git merge main")