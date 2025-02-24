#!/usr/bin/env python3
import subprocess
import os
import sys
from datetime import datetime


def haal_hint_op(reeks, vraag, niveau):
    """
    Haalt de versie van het bestand op uit de branch `niveau`.
    """
    bestand_pad = f"reeks{reeks}/vraag{vraag:02d}.py"
    try:
        # Gebruik git show om de inhoud van het bestand op te halen uit de gewenste branch.
        resultaat = subprocess.run(
            ["git", "show", f"{niveau}:{bestand_pad}"],
            capture_output=True,
            text=True,
            check=True
        )
        return resultaat.stdout
    except subprocess.CalledProcessError as e:
        print("Fout bij het ophalen van de hint:")
        print(e.stderr)
        sys.exit(1)


def maak_backup(bestand_pad, reeks, vraag, niveau):
    """Maakt een unieke backup van het bestand in een aparte map binnen de reeks."""
    backup_map = f"reeks{reeks}/backups"
    os.makedirs(backup_map, exist_ok=True)

    # Voeg een timestamp toe aan de backup bestandsnaam
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_pad = os.path.join(backup_map, f"vraag{vraag:02d}_{niveau}_{timestamp}.py")

    if os.path.exists(bestand_pad):
        os.rename(bestand_pad, backup_pad)
        print(f"Een backup van het originele bestand is gemaakt: {backup_pad}")


def pas_hint_toe(reeks, vraag, niveau):
    bestand_pad = f"reeks{reeks}/vraag{vraag:02d}.py"
    hint_inhoud = haal_hint_op(reeks, vraag, niveau)
    maak_backup(bestand_pad, reeks, vraag, niveau)
    with open(bestand_pad, "w") as f:
        f.write(hint_inhoud)
    print(f"De hint van niveau '{niveau}' is toegepast op {bestand_pad}.")


def main():
    print("=== Hint toepassen script ===")
    try:
        reeks = int(input("Voor welke reeks? (nummer, bv. 1): ").strip())
        vraag = int(input("Voor welke vraag? (nummer, bv. 2): ").strip())
        niveau_keuze = int(input("Welk hintniveau? (1 = niveau1, 2 = niveau2, 3 = niveau3, 4 = oplossing): ").strip())
    except ValueError:
        print("Ongeldige invoer. Gebruik alleen nummers.")
        sys.exit(1)

    # Map de invoer naar de juiste branchnaam
    niveau_mapping = {1: "niveau1", 2: "niveau2", 3: "niveau3", 4: "oplossing"}
    niveau = niveau_mapping.get(niveau_keuze)

    if niveau is None:
        print("Ongeldige keuze voor hintniveau. Kies 1, 2, 3 of 4.")
        sys.exit(1)

    # Controleer of de map voor de reeks bestaat
    if not os.path.isdir(f"reeks{reeks}"):
        print(f"Map 'reeks{reeks}' bestaat niet in de huidige directory.")
        sys.exit(1)

    pas_hint_toe(reeks, vraag, niveau)


if __name__ == "__main__":
    main()
