import copy
from typing import Any, Dict, List

from field import Field


class Table:

    def __init__(self, fields: Dict[str, Field]) -> None:

        self._rows: List[Dict[str, Any]] = []
        self._columns: Dict[str, List[Any]] = {}
        self._fields = copy.deepcopy(fields)
        for key in self._fields:
            self._columns[key] = []

    def addRow(self, data: Dict[str, Any]) -> None:

        for key, val in data.items():
            if key not in self._fields:
                raise ValueError(f'{key} key is not in columns!')

            if not self._fields[key].isValueble(val):
                raise ValueError(f'Value is not type of {self._fields[key].type}!')
            
            if self._fields[key].unique and (val in self._columns[key]):
                raise ValueError('Duplicate value!')
        
        if len(self._fields) != len(data):
            raise ValueError('Not enough fields!')

        for key, val in data.items():
            self._columns[key].append(val)

        self._rows.append(data)

    def selectRow(self) -> List[Dict[str, Any]]:
        # rows: List[Dict[str, Any]] = []
        # for row in self._rows:
        #     rows.append(row)
        # return rows
        return self._rows
