from pandas import Series, isna
import re

from .violation import Violation

class RegexFormatViolation(Violation):
    def __init__(self, regex: str):
        super().__init__()
        self._regex = regex

    def _set_name(self) -> str:
        return "Regex Format"
    
    def test_for_violation(self, data_frame: Series) -> list:
        row_indexes = []
        for index, value in data_frame.items():
            if isna(value):
                continue
            if not isinstance(value, str):
                continue
            x = re.fullmatch(self._regex, value)
            if x is None:
                row_indexes.append(index)

        return row_indexes