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
    file = DataFile("MenuItem", MENU_ITEM)

    id = DataColumn("id")
    id.add_potential_violation(MissingValuesViolation())

    menu_page_id = DataColumn("menu_page_id")
    menu_page_id.add_potential_violation(MissingValuesViolation())

    price = DataColumn("price")
    price.add_potential_violation(MissingValuesViolation())
    price.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    price.add_potential_violation(NumberLowerBoundViolation(0.0))
    price.add_potential_violation(NumberUpperBoundViolation(100.0))

    high_price = DataColumn("high_price")
    high_price.add_potential_violation(MissingValuesViolation())
    high_price.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    high_price.add_potential_violation(NumberLowerBoundViolation(0.0))
    high_price.add_potential_violation(NumberUpperBoundViolation(100.0))

    dish_id = DataColumn("dish_id")
    dish_id.add_potential_violation(MissingValuesViolation())

    created_at = DataColumn("created_at")
    created_at.add_potential_violation(MissingValuesViolation())
    created_at.add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
    created_at.add_potential_violation(RegexFormatViolation(r"(?:2|1)[0-9]{3}-(?:(?:0[1-9])|1[0-2])-(?:0|1|2|3)[0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} UTC"))

    updated_at = DataColumn("updated_at")
    created_at.add_potential_violation(MissingValuesViolation())
    updated_at.add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
    created_at.add_potential_violation(RegexFormatViolation(r"(?:2|1)[0-9]{3}-(?:(?:0[1-9])|1[0-2])-(?:0|1|2|3)[0-9] [0-9]{2}:[0-9]{2}:[0-9]{2} UTC"))

    xpos = DataColumn("xpos")
    xpos.add_potential_violation(MissingValuesViolation())
    xpos.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    xpos.add_potential_violation(NumberLowerBoundViolation(0.0))

    ypos = DataColumn("ypos")
    ypos.add_potential_violation(MissingValuesViolation())
    ypos.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    ypos.add_potential_violation(NumberLowerBoundViolation(0.0))

    file.add_column(id)
    file.add_column(menu_page_id)
    file.add_column(price)
    file.add_column(high_price)
    file.add_column(dish_id)
    file.add_column(created_at)
    file.add_column(updated_at)
    file.add_column(xpos)
    file.add_column(ypos)

    return file