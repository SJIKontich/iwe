# python
import os

# Commands to update the student's branch with the latest changes from the main branch
os.system("git add .")
os.system('git commit -m "Mijn oplossingen"')
os.system("git checkout main")
os.system("git config pull.rebase false")
os.system("git pull origin main")
os.system("git checkout mijn-oplossingen")
os.system("git merge main")