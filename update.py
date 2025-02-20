import os

# Haal de huidige branch op
current_branch = os.popen("git branch --show-current").read().strip()

# **Wijzigingen tijdelijk opslaan als er niet-gecommitete wijzigingen zijn**
if os.popen("git status --porcelain").read().strip():
    os.system("git stash push -m 'Tijdelijke wijzigingen'")

# Fetch alle remote branches
os.system("git fetch --all")

# Lijst met branches die exact moeten overeenkomen met de remote versie
branches = ["oplossing", "niveau1", "niveau2", "niveau3"]

for branch in branches:
    # Check of de branch al lokaal bestaat
    local_branches = os.popen("git branch").read()

    if branch not in local_branches:
        # Maak de branch lokaal en link deze aan de remote versie
        os.system(f"git branch --track {branch} origin/{branch}")

    # Forceer update zonder merge-conflicten
    os.system(f"git checkout {branch}")
    os.system(f"git reset --hard origin/{branch}")

# Terug naar de originele branch (mijn-oplossingen)
if current_branch != "mijn-oplossingen":
    os.system("git checkout mijn-oplossingen")

# **Haal de nieuwste versie van update.py uit main en vervang de huidige**
os.system("git checkout origin/main -- update.py")

# **Commit de update.py wijziging zonder andere bestanden aan te raken**
os.system("git add update.py")
os.system('git commit -m "Update update.py vanuit main" || echo "Geen wijzigingen in update.py om te committen."')

# **(Optioneel) Push de update naar de remote repo als leerlingen dat mogen**
# os.system("git push origin mijn-oplossingen")

# **Zet de wijzigingen van de leerling terug als er iets was gestasht**
if os.popen("git stash list").read().strip():
    os.system("git stash pop")
