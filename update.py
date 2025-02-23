import os

# Haal de huidige branch op
current_branch = os.popen("git branch --show-current").read().strip()

# Wijzigingen tijdelijk opslaan als er niet-gecommitete wijzigingen zijn
if os.popen("git status --porcelain").read().strip():
    os.system('git stash push -m "Tijdelijke wijzigingen"')

# Fetch alle remote branches
os.system("git fetch --all")

# Lijst van branches die we willen updaten (geen main)
branches = ["oplossing", "niveau1", "niveau2", "niveau3"]

# Doorloop alle branches en werk ze bij
for branch in branches:
    # Check of de branch al lokaal bestaat
    local_branches = os.popen("git branch").read()

    if branch not in local_branches:
        # Maak de branch lokaal en link deze aan de remote versie
        os.system(f"git checkout -b {branch} origin/{branch}")
    else:
        # Als de branch al bestaat, wissel naar de juiste branch
        os.system(f"git checkout {branch}")

    # Forceer update zonder merge-conflicten
    os.system(f"git reset --hard origin/{branch}")

# Terug naar de originele branch
os.system(f"git checkout {current_branch}")

# Haal de nieuwste versie van main op
os.system("git pull origin main")

# Zet de wijzigingen van de leerling terug als er iets was gestasht
if os.popen("git stash list").read().strip():
    os.system("git stash apply")
    if os.popen("git status --porcelain").read().strip():
        print("Er zijn conflicten opgetreden bij het toepassen van de stash. Los deze handmatig op.")
    else:
        os.system("git stash drop")