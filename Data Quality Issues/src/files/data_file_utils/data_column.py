from src.files.violations.violation import Violation
from pandas import DataFrame

class DataColumn:
    def __init__(self, column_name: str):
        self._name = column_name
        self._potential_violations: list[Violation] = []

    def add_potential_violation(self, violation: Violation):
        self._potential_violations.append(violation)

    def get_column_report(self, data_frame: DataFrame) -> dict:
        return {
            "name": self._name,
            "violations": self._get_violations_report(data_frame)
        }

    def _get_violations_report(self, data_frame: DataFrame) -> list:
        violations: list = []
        for p_violation in self._potential_violations:
            violations.append(p_violation.get_violation_report(data_frame, self._name))
        return violations

    pass