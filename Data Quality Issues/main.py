from src.files.data_file_utils.data_file import DataFile
from src.files.tables.dish_table import get_dish_table
from src.files.tables.menu_table import get_menu_table
from src.files.tables.menu_item_table import get_menu_item_table
from src.files.tables.menu_page_table import get_menu_page_table

from pathlib import Path
import json

CURRENT_DIR = Path.cwd()
OUTPUT_FILE = CURRENT_DIR / "violations.json"

def main():
    files: list[DataFile] = []
    files.append(get_dish_table())
    files.append(get_menu_table())
    files.append(get_menu_item_table())
    files.append(get_menu_page_table())

    print("files loaded")


    reports = []
    for file in files:
        print(f"Working on file: {file._name}")
        reports.append(file.get_file_report())

    report = {
        "files": reports
    }
        
    with open (OUTPUT_FILE, 'w', encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("file report generated ")


if __name__ == "__main__":
    main()
