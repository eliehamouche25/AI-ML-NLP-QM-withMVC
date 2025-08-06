import os

# Define folders to create
folders = [
    "AI_ML_NLP_QM_MVC03/app/controllers",
    "AI_ML_NLP_QM_MVC03/app/models",
    "AI_ML_NLP_QM_MVC03/app/views",
    "AI_ML_NLP_QM_MVC03/app/templates",
    "AI_ML_NLP_QM_MVC03/app/static/css",
    "AI_ML_NLP_QM_MVC03/app/static/js",
    "AI_ML_NLP_QM_MVC03/app/static/img",
    "AI_ML_NLP_QM_MVC03/docs",
    "AI_ML_NLP_QM_MVC03/tests"
]

# Define empty placeholder files
files = [
    "AI_ML_NLP_QM_MVC03/app/__init__.py",
    "AI_ML_NLP_QM_MVC03/app/controllers/main_controller.py",
    "AI_ML_NLP_QM_MVC03/app/controllers/ml_controller.py",
    "AI_ML_NLP_QM_MVC03/app/controllers/quantum_controller.py",
    "AI_ML_NLP_QM_MVC03/app/models/user_model.py",
    "AI_ML_NLP_QM_MVC03/app/models/ml_model.py",
    "AI_ML_NLP_QM_MVC03/app/models/quantum_model.py",
    "AI_ML_NLP_QM_MVC03/app/views/render_helpers.py",
    "AI_ML_NLP_QM_MVC03/app/templates/layout.html",
    "AI_ML_NLP_QM_MVC03/app/templates/index.html",
    "AI_ML_NLP_QM_MVC03/app/templates/dashboard.htm",
    "AI_ML_NLP_QM_MVC03/app/templates/error.htm",
    "AI_ML_NLP_QM_MVC03/app/templates/register.htm",
    "AI_ML_NLP_QM_MVC03/config.py",
    "AI_ML_NLP_QM_MVC03/run.py",
    "AI_ML_NLP_QM_MVC03/requirements.txt",
    "AI_ML_NLP_QM_MVC03/.env",
    "AI_ML_NLP_QM_MVC03/docs/README.md"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create empty files
for file in files:
    with open(file, 'w') as f:
        f.write("")  # Placeholder content
    print(f"Created file: {file}")
