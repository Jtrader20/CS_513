from src.files.data_file_utils.data_file import DataFile, DataColumn
from src.files.violations.missing_values import MissingValuesViolation
from src.files.violations.number_lower_bound import NumberLowerBoundViolation
from src.files.violations.type_mismatch import TypeMismatchViolation, TypeMismatch

from pathlib import Path

CURRENT_DIR = Path.cwd()
ROOT_DIR = CURRENT_DIR.parent
DATA_DIR = ROOT_DIR / "Data" / "NYPL-menus"
MENU_PAGE = DATA_DIR / "MenuPage.csv"

def get_menu_page_table() -> DataFile:
    id = DataColumn("id").add_potential_violation(MissingValuesViolation())

    menu_id = DataColumn("menu_id").add_potential_violation(MissingValuesViolation())

    page_number = DataColumn("page_number").add_potential_violation(MissingValuesViolation())

    image_id = DataColumn("image_id").add_potential_violation(MissingValuesViolation())

    full_height = (
        DataColumn("full_height")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT, TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    )

    full_width = (
        DataColumn("full_width")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT, TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    )

    uuid = DataColumn("uuid").add_potential_violation(MissingValuesViolation())

    file = (
        DataFile("MenuPage", MENU_PAGE)
            .add_column(id)
            .add_column(menu_id)
            .add_column(page_number)
            .add_column(image_id)
            .add_column(full_height)
            .add_column(full_width)
            .add_column(uuid)
    )

    return file