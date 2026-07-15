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

    id = DataColumn("id").add_potential_violation(MissingValuesViolation())

    name = (
        DataColumn("name")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
    )

    description = (
        DataColumn("description")
            .add_potential_violation(MissingValuesViolation())
    ) 

    menus_appeared = (
        DataColumn("menus_appeared")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER, TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    )

    times_appeared = (
        DataColumn("times_appeared")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER, TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    )

    first_appeared = (
        DataColumn("first_appeared")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(1700))
            .add_potential_violation(NumberUpperBoundViolation(2026))
    )

    last_appeared = (
        DataColumn("last_appeared")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(1700))
            .add_potential_violation(NumberUpperBoundViolation(2026))
    )

    lowest_price = (
        DataColumn("lowest_price")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
            .add_potential_violation(NumberUpperBoundViolation(100.0))
    )

    highest_price = (
        DataColumn("highest_price")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.FLOAT]))
            .add_potential_violation(NumberLowerBoundViolation(0.0))
            .add_potential_violation(NumberUpperBoundViolation(200.0))
    )

    file = (
        DataFile("Dish", DISH)
            .add_column(id)
            .add_column(name)
            .add_column(description)
            .add_column(menus_appeared)
            .add_column(times_appeared)
            .add_column(first_appeared)
            .add_column(last_appeared)
            .add_column(lowest_price)
            .add_column(highest_price)
    )

    return file