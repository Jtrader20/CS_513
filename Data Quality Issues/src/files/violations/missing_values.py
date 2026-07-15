from pandas import Series, isna

from .violation import Violation

class MissingValuesViolation(Violation):
    def __init__(self):
        super().__init__()

    def _set_name(self) -> str:
        return "Missing Values"
    
    def test_for_violation(self, data_frame: Series) -> dict:
        row_indexes = []
        for index, value in data_frame.items():
            if isna(value):
                row_indexes.append(index)

        return {
            "violation": self._get_name(),
            "count": len(row_indexes),
            "row_indexes": row_indexes
        }