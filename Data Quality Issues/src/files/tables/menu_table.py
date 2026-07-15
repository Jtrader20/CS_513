from src.files.data_file_utils.data_file import DataFile, DataColumn
from src.files.violations.missing_values import MissingValuesViolation
from src.files.violations.number_lower_bound import NumberLowerBoundViolation
from src.files.violations.regex_format import RegexFormatViolation
from src.files.violations.type_mismatch import TypeMismatchViolation, TypeMismatch

from pathlib import Path

CURRENT_DIR = Path.cwd()
ROOT_DIR = CURRENT_DIR.parent
DATA_DIR = ROOT_DIR / "Data" / "NYPL-menus"
MENU = DATA_DIR / "Menu.csv"

def get_menu_table() -> DataFile:
    id = DataColumn("id").add_potential_violation(MissingValuesViolation())

    name = DataColumn("name").add_potential_violation(MissingValuesViolation())

    sponsor = DataColumn("sponsor")

    event = DataColumn("event")

    venue = DataColumn("venue")

    place = DataColumn("place")

    physical_description = DataColumn("physical_description")

    occasion = DataColumn("occasion")

    notes = DataColumn("notes")

    call_number = (
        DataColumn("call_number")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
            .add_potential_violation(RegexFormatViolation(r"(1|2)[0-9]{3}-(1|2)[0-9]{3}"))
    )

    keywords = DataColumn("keywords").add_potential_violation(RegexFormatViolation(r"(?:[A-Z0-9.]+; ?)*"))

    language = DataColumn("language")

    date = (
        DataColumn("date")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
            .add_potential_violation(RegexFormatViolation(r"(?:1|2)[0-9]{3}-(?:0|1)[0-9]-(?:0|1|2|3)[0-9]"))
    )

    location_type = DataColumn("location_type")

    currency = DataColumn("currency").add_potential_violation(MissingValuesViolation())

    currency_symbol = DataColumn("currency_symbol")

    status = DataColumn("status").add_potential_violation(MissingValuesViolation())

    page_count = (
        DataColumn("page_count")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    ) 

    dish_count = (
        DataColumn("dish_count")
            .add_potential_violation(MissingValuesViolation())
            .add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
            .add_potential_violation(NumberLowerBoundViolation(0))
    )

    file = (
        DataFile("Menu", MENU)
            .add_column(id)
            .add_column(name)
            .add_column(sponsor)
            .add_column(event)
            .add_column(venue)
            .add_column(place)
            .add_column(physical_description)
            .add_column(occasion)
            .add_column(notes)
            .add_column(call_number)
            .add_column(keywords)
            .add_column(language)
            .add_column(date)
            .add_column(location_type)
            .add_column(currency)
            .add_column(currency_symbol)
            .add_column(status)
            .add_column(page_count)
            .add_column(dish_count)
    )

    return file