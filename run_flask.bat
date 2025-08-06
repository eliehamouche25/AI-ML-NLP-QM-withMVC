@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Set Flask app environment variable
set FLASK_APP=run.py

REM Run Flask server
python -m flask run

REM Pause so you can see output (optional)
pause