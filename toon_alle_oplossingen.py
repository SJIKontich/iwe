import os
import subprocess

# Haal de huidige branch op
current_branch = os.popen("git branch --show-current").read().strip()

# Wijzigingen tijdelijk opslaan als er niet-gecommitete wijzigingen zijn
if os.popen("git status --porcelain").read().strip():
    subprocess.run(["git", "stash", "push", "-m", "Tijdelijke wijzigingen"])

# Wissel naar de 'oplossing' branch
subprocess.run(["git", "checkout", "oplossing"])
