from .data_column import DataColumn
from pathlib import Path
import pandas as pd

class DataFile:
    def __init__(self, name: str, file_path: Path):
        self._name = name
        self._file_path = file_path
        self._columns: list[DataColumn] = []
        self._data_frame = pd.read_csv(self._file_path)

    def _get_columns_report(self) -> list:
        columns: list = []
        for col in self._columns:
            columns.append(col.get_column_report(self._data_frame))
        return columns

    def add_column(self, column: DataColumn):
        self._columns.append(column)

    def get_file_report(self) -> dict:
        return {
            "name": self._name,
            "columns": self._get_columns_report()
        }