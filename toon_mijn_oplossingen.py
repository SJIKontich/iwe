# python
import os

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch == "oplossing":
    os.system("git checkout mijn-oplossingen") # als ze iets hebben aangepast, krijgen ze een error