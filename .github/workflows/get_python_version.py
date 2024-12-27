import sys
import json
import re
import os

def get_python_version(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            versions = [v.strip() for v in re.split(r'[,\s\n]+', content) if v.strip()]
            return versions
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_python_version.py <path_to_.python-version>")
        sys.exit(1)

    file_path = sys.argv[1]
    version = get_python_version(file_path)
    matrix_strategy = {"python-version": version}
    print(json.dumps(matrix_strategy))