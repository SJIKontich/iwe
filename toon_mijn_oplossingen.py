import os
import subprocess

# Wissel naar de 'oplossing' branch
try:
    subprocess.run(["git", "checkout", "main"], check=True)
except subprocess.CalledProcessError as e:
    print("Er liep iets mis bij het wisselen naar jouw code.", e)
else:
    print("doe niets voorlopig")
    exit()
    # Zet de wijzigingen van de leerling terug als er iets was gestasht
    if os.popen("git stash list").read().strip():
        subprocess.run(["git", "stash", "apply"])
        if os.popen("git status --porcelain").read().strip():
            print("Er zijn conflicten opgetreden bij het toepassen van de stash. De gestashte versie wordt teruggezet.")
            subprocess.run(["git", "checkout", "stash@{0}", "--", "."])
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", "Conflicten opgelost door gestashte versie terug te zetten"])
        else:
            subprocess.run(["git", "stash", "drop"])