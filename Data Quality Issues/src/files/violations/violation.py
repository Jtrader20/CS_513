from abc import ABC, abstractmethod
from pandas import DataFrame, Series

class Violation(ABC):
    def __init__(self):
        self._name = self._set_name()

    @abstractmethod
    def _set_name(self) -> str:
        pass

    def _get_name(self) -> str:
        return self._name

    def get_violation_report(self, data_frame: DataFrame, column_name: str) -> dict:
        col = data_frame[column_name].copy()

        return self.test_for_violation(col)
    
    @abstractmethod
    def test_for_violation(self, data_frame: Series) -> dict:
        pass