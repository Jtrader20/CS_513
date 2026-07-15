from src.files.data_file_utils.data_file import DataFile, DataColumn
from src.files.violations.missing_values import MissingValuesViolation
from src.files.violations.number_lower_bound import NumberLowerBoundViolation
from src.files.violations.number_upper_bound import NumberUpperBoundViolation
from src.files.violations.regex_format import RegexFormatViolation
from src.files.violations.type_mismatch import TypeMismatchViolation, TypeMismatch

from pathlib import Path

CURRENT_DIR = Path.cwd()
ROOT_DIR = CURRENT_DIR.parent
DATA_DIR = ROOT_DIR / "Data" / "NYPL-menus"
MENU_ITEM = DATA_DIR / "MenuItem.csv"

def get_menu_item_table() -> DataFile:

    id = DataColumn("id").add_potential_violation(MissingValuesViolation())

    menu_page_id = DataColumn("menu_page_id").add_potential_violation(MissingValuesViolation())

    price = (
        DataColumn("price")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
            .add_potential_violation(NumberUpperBoundViolation(100.0))
    )

    high_price = (
        DataColumn("high_price")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
            .add_potential_violation(NumberUpperBoundViolation(100.0))
    ) 

    dish_id = DataColumn("dish_id").add_potential_violation(MissingValuesViolation())

    created_at = (
        DataColumn("created_at")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
            .add_potential_violation(RegexFormatViolation(r"(?:2|1)[0-9]{3}-(?:(?:0[1-9])|1[0-2])-(?:0|1|2|3)[0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} UTC"))
    )

    updated_at = (
        DataColumn("updated_at")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
            .add_potential_violation(RegexFormatViolation(r"(?:2|1)[0-9]{3}-(?:(?:0[1-9])|1[0-2])-(?:0|1|2|3)[0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} UTC"))
    )

    xpos = (
        DataColumn("xpos")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
    )

    ypos = (
        DataColumn("ypos")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
    )

    file = (
        DataFile("MenuItem", MENU_ITEM)
            .add_column(id)
            .add_column(menu_page_id)
            .add_column(price)
            .add_column(high_price)
            .add_column(dish_id)
            .add_column(created_at)
            .add_column(updated_at)
            .add_column(xpos)
            .add_column(ypos)
    )

    return file