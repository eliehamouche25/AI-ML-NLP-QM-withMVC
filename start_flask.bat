@echo off
REM =============================================
REM      Script de démarrage Flask amélioré
REM =============================================

REM Obtenir le chemin absolu du dossier courant
set "PROJECT_DIR=%cd%"
echo Projet : %PROJECT_DIR%

REM Vérifier et créer l'environnement virtuel si nécessaire
if not exist ".venv" (
    echo [INFO] Création de l'environnement virtuel...
    python -m venv .venv
)

REM Activer l'environnement virtuel
echo [INFO] Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

REM Installer les dépendances si requirements.txt existe
if exist requirements.txt (
    echo [INFO] Installation des dépendances...
    pip install -r requirements.txt
) else (
    echo [AVERTISSEMENT] Aucun fichier requirements.txt trouvé.
)

REM Vérifier si run.py existe
if not exist run.py (
    echo [ERREUR] Le fichier run.py est introuvable. Veuillez vérifier le nom ou l’emplacement.
    pause
    exit /b
)

REM Définir les variables d’environnement
set FLASK_APP=run.py
set FLASK_ENV=development

REM Démarrer le serveur Flask
echo [INFO] Lancement du serveur Flask sur http://127.0.0.1:5000 ...
python -m flask run --port=5000

REM Garder la fenêtre ouverte après l’arrêt du serveur
pause