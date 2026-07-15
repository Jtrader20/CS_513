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
    file = DataFile("Menu", MENU)

    id = DataColumn("id")
    id.add_potential_violation(MissingValuesViolation())

    name = DataColumn("name")
    name.add_potential_violation(MissingValuesViolation())

    sponsor = DataColumn("sponsor")

    event = DataColumn("event")

    venue = DataColumn("venue")

    place = DataColumn("place")

    physical_description = DataColumn("physical_description")

    occasion = DataColumn("occasion")

    notes = DataColumn("notes")

    call_number = DataColumn("call_number")
    call_number.add_potential_violation(MissingValuesViolation())
    call_number.add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
    call_number.add_potential_violation(RegexFormatViolation(r"(1|2)[0-9]{3}-(1|2)[0-9]{3}"))

    keywords = DataColumn("keywords")
    keywords.add_potential_violation(RegexFormatViolation(r"(?:[A-Z0-9.]+; ?)*"))

    language = DataColumn("language")

    date = DataColumn("date")
    date.add_potential_violation(MissingValuesViolation())
    date.add_potential_violation(TypeMismatchViolation([TypeMismatch.STRING]))
    date.add_potential_violation(RegexFormatViolation(r"(?:1|2)[0-9]{3}-(?:0|1)[0-9]-(?:0|1|2|3)[0-9]"))

    location_type = DataColumn("location_type")

    currency = DataColumn("currency")
    currency.add_potential_violation(MissingValuesViolation())

    currency_symbol = DataColumn("currency_symbol")

    status = DataColumn("status")
    status.add_potential_violation(MissingValuesViolation())

    page_count = DataColumn("page_count")
    page_count.add_potential_violation(MissingValuesViolation())
    page_count.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
    page_count.add_potential_violation(NumberLowerBoundViolation(0))

    dish_count = DataColumn("dish_count")
    dish_count.add_potential_violation(MissingValuesViolation())
    dish_count.add_potential_violation(TypeMismatchViolation([TypeMismatch.INTEGER]))
    dish_count.add_potential_violation(NumberLowerBoundViolation(0))

    file.add_column(id)
    file.add_column(name)
    file.add_column(sponsor)
    file.add_column(event)
    file.add_column(venue)
    file.add_column(place)
    file.add_column(physical_description)
    file.add_column(occasion)
    file.add_column(notes)
    file.add_column(call_number)
    file.add_column(keywords)
    file.add_column(language)
    file.add_column(date)
    file.add_column(location_type)
    file.add_column(currency)
    file.add_column(currency_symbol)
    file.add_column(status)
    file.add_column(page_count)
    file.add_column(dish_count)

    return file