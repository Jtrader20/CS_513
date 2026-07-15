from src.files.data_file_utils.data_file import DataFile, DataColumn
from src.files.violations.missing_values import MissingValuesViolation
from src.files.violations.number_lower_bound import NumberLowerBoundViolation
from src.files.violations.number_upper_bound import NumberUpperBoundViolation
from src.files.violations.type_mismatch import TypeMismatchViolation, TypeMismatch

from pathlib import Path

CURRENT_DIR = Path.cwd()
ROOT_DIR = CURRENT_DIR.parent
DATA_DIR = ROOT_DIR / "Data" / "NYPL-menus"
DISH = DATA_DIR / "Dish.csv"

def get_dish_table() -> DataFile:
    file = DataFile("Dish", DISH)

    id = DataColumn("id")
    id.add_potential_violation(MissingValuesViolation())

    name = DataColumn("name")
    name.add_potential_violation(MissingValuesViolation())
    name.add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))

    description = DataColumn("description")
    description.add_potential_violation(MissingValuesViolation())

    menus_appeared = DataColumn("menus_appeared")
    menus_appeared.add_potential_violation(MissingValuesViolation())
    menus_appeared.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER, TypeMismatch.FLOAT]))
    menus_appeared.add_potential_violation(NumberLowerBoundViolation(0))

    times_appeared = DataColumn("times_appeared")
    times_appeared.add_potential_violation(MissingValuesViolation())
    times_appeared.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER, TypeMismatch.FLOAT]))
    times_appeared.add_potential_violation(NumberLowerBoundViolation(0))

    first_appeared = DataColumn("first_appeared")
    first_appeared.add_potential_violation(MissingValuesViolation())
    first_appeared.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
    first_appeared.add_potential_violation(NumberLowerBoundViolation(1700))
    first_appeared.add_potential_violation(NumberUpperBoundViolation(2026))

    last_appeared = DataColumn("last_appeared")
    last_appeared.add_potential_violation(MissingValuesViolation())
    last_appeared.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
    last_appeared.add_potential_violation(NumberLowerBoundViolation(1700))
    last_appeared.add_potential_violation(NumberUpperBoundViolation(2026))

    lowest_price = DataColumn("lowest_price")
    lowest_price.add_potential_violation(MissingValuesViolation())
    lowest_price.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    lowest_price.add_potential_violation(NumberLowerBoundViolation(0.0))
    lowest_price.add_potential_violation(NumberUpperBoundViolation(100.0))

    highest_price = DataColumn("highest_price")
    highest_price.add_potential_violation(MissingValuesViolation())
    highest_price.add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
    highest_price.add_potential_violation(NumberLowerBoundViolation(0.0))
    highest_price.add_potential_violation(NumberUpperBoundViolation(200.0))

    file.add_column(id)
    file.add_column(name)
    file.add_column(description)
    file.add_column(menus_appeared)
    file.add_column(times_appeared)
    file.add_column(first_appeared)
    file.add_column(last_appeared)
    file.add_column(lowest_price)
    file.add_column(highest_price)

    return file