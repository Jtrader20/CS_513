from abc import ABC, abstractmethod
from pandas import Series

class Violation(ABC):
    def __init__(self):
        self._name = self._set_name()

    @abstractmethod
    def _set_name(self) -> str:
        pass

    def _get_name(self) -> str:
        return self._name

    def get_violation_report(self, col: Series) -> dict:
        violation_indexes = self.test_for_violation(col)
        return {
            "violation": self._get_name(),
            "count": len(violation_indexes)
            # "row_indexes": violation_indexes
        }
    
    @abstractmethod
    def test_for_violation(self, data_frame: Series) -> dict:
        pass