
from pathlib import Path

# Project root directory
root = Path(".")

# Folders to create
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests",
]

# Files to create
files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]

# Create the project root
root.mkdir(parents=True, exist_ok=True)

# Create all folders
for folder in folders:
    folder_path = root / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Folder created/exists: {folder_path}")

# Create empty files without overwriting existing files
for file in files:
    file_path = root / file

    if not file_path.exists():
        file_path.touch()
        print(f"File created: {file_path}")
    else:
        print(f"File already exists; preserved: {file_path}")

print("\nProject directory structure is ready!")
print(f"Project location: {root.resolve()}")
