from pandas import Series, isna

from enum import Enum

class TypeMismatch(Enum):
    STRING = str
    INTEGER = int
    FLOAT = float
    BOOLEAN = bool

from .violation import Violation

class TypeMismatchViolation(Violation):
    def __init__(self, correct_types: list[TypeMismatch]):
        super().__init__()
        self._correct_types = correct_types
        self._expected_types = tuple(t.value for t in self._correct_types)

    def _set_name(self) -> str:
        return "Type Mismatch"
    
    def test_for_violation(self, data_frame: Series) -> dict:
        row_indexes = []
        for index, value in data_frame.items():
            if isna(value):
                continue
            if not isinstance(value, self._expected_types):
                row_indexes.append(index)

        return {
            "violation": self._get_name(),
            "count": len(row_indexes),
            "row_indexes": row_indexes
        }