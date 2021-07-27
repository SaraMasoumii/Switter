import copy
import uuid
from typing import Any, Dict, List, Set

from field import Field


class Table:

    def __init__(self, fields: Dict[str, Field]) -> None:

        self._rows: Dict[str, Dict[str, str]] = {}
        self._columns: Dict[str, List[str]] = {}
        self._fields = copy.deepcopy(fields)
        for key in self._fields:
            self._columns[key] = []

    def generateID(self) -> str:
        return str(uuid.uuid4())

    def addRow(self, data: Dict[str, str]) -> None:

        for key, val in data.items():
            if key not in self._fields:
                raise ValueError(f'{key} key is not in fields!')

            if not self._fields[key].isValueble(val):
                raise ValueError(f'Value is not type of {self._fields[key].type}!')

            if self._fields[key].unique and (val in self._columns[key]):
                raise ValueError('Duplicate value!')

        if len(self._fields) != len(data):
            raise ValueError('Not enough fields!')

        row = copy.deepcopy(data)
        self._rows[self.generateID()] = row

        for key, val in row.items():
            self._columns[key].append(val)


    def getRow(self, id: str) -> Dict[str, str]:
        return copy.deepcopy(self._rows[id])

    def getRows(self, ids: Set[str]) -> List[Dict[str, str]]:
        rows = []
        for id in ids:
            rows.append(self.getRow(id))

        return rows

    def deleteRow(self, id: str) -> None:
        del self._rows[id]

    def deleteRows(self, ids: Set[str]) -> None:
        for id in ids:
            self.deleteRow(id)

    def updateRow(self, id: str, newData: Dict[str, str]) -> Dict[str, str]:
        for key in self._rows[id]:
            if key in newData:
                self._rows[id][key] = newData[key]
                
        return self._rows[id]


    def selectRows(self, equal: bool, field: str, value: str) -> Set[str]:
        if field not in self._fields:
            raise ValueError('Invalid field!')

        rowsID = set()
        for id, row in self._rows.items():
            if (equal and row[field] == value) or ((not equal) and row[field] != value):
                rowsID.add(id)

        return rowsID

