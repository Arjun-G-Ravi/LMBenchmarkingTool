'''
This cleans up the library
'''
import os
import shutil
from pathlib import Path

def clean_project():
    # Get the directory where this script is located
    root_dir = Path(__file__).parent.parent
    input(f'Going to clean the directory: {root_dir}')
    
    # Patterns of directories to remove
    dirs_to_remove = [
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "build",
        "dist",
        ".eggs",
    ]
    
    # Patterns of files to remove
    files_to_remove = [
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".coverage",
    ]
    
    print(f"🧹 Cleaning project at: {root_dir}\n")

    # 1. Walk through all directories to find files and subdirectories
    for path in root_dir.rglob("*"):
        
        # Skip if path belongs to a hidden git folder or venv
        if ".git" in path.parts or ".venv" in path.parts or "venv" in path.parts:
            continue

        # Remove specific files (like .pyc)
        if path.is_file():
            for pattern in files_to_remove:
                if path.match(pattern):
                    try:
                        path.unlink()
                        print(f"Deleted file: {path.relative_to(root_dir)}")
                    except Exception as e:
                        print(f"Error deleting {path.name}: {e}")

        # Remove specific directories (like __pycache__)
        elif path.is_dir():
            if path.name in dirs_to_remove or path.name.endswith(".egg-info"):
                try:
                    shutil.rmtree(path)
                    print(f"Deleted folder: {path.relative_to(root_dir)}")
                except Exception as e:
                    print(f"Error deleting {path.name}: {e}")

    print("\n✨ Project cleaned successfully!")

if __name__ == "__main__":
    clean_project()