from pandas import Series, isna


from .violation import Violation

class NumberUpperBoundViolation(Violation):
    def __init__(self, upper_bound: int | float):
        super().__init__()
        self._upper_bound = upper_bound

    def _set_name(self) -> str:
        return "Upper Bound"
    
    def test_for_violation(self, data_frame: Series) -> dict:
        row_indexes = []
        for index, value in data_frame.items():
            if isna(value):
                continue
            if not isinstance(value, int | float):
                continue
            if value > self._upper_bound:
                row_indexes.append(index)

        return {
            "violation": self._get_name(),
            "count": len(row_indexes),
            "row_indexes": row_indexes
        }