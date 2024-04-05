import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "llm_project"

list_of_files = [
    f"{project_name}/data/raw/data.txt",
    f"{project_name}/data/processed/__init__.py",
    f"{project_name}/model/__init__.py",
    f"{project_name}/model/architecture.py",
    f"{project_name}/model/training.py",
    f"{project_name}/model/inference.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/preprocessing.py",
    f"{project_name}/utils/evaluation.py",
    "README.md",
    "requirements.txt",
    ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
