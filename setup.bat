@echo off

REM Controleer of Python is geïnstalleerd
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is niet geïnstalleerd of niet toegevoegd aan PATH.
    pause
    exit /b
)

REM Maak de virtuele omgeving aan als deze niet bestaat
IF NOT EXIST ".venv" (
    echo Virtuele omgeving wordt aangemaakt...
    python -m venv .venv
) ELSE (
    echo Virtuele omgeving bestaat al.
)

REM Activeer de virtuele omgeving
echo Virtuele omgeving activeren...
call .venv\Scripts\activate.bat

REM Installeer requirements als requirements.txt bestaat
IF EXIST "requirements.txt" (
    echo Pakketten installeren uit requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo requirements.txt niet gevonden. Geen pakketten om te installeren.
)

echo Setup voltooid. Virtuele omgeving is actief.
cmd /k
