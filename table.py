import copy
from file import File
import uuid
from typing import Any, Dict, List, Set

from field import Field


class Table:

    def __init__(self, filePath: str, fields: Dict[str, Field]) -> None:

        self._file = File(filePath)
        self._rows: Dict[str, Dict[str, str]] = {}
        self._columns: Dict[str, List[str]] = {}
        self._fields = copy.deepcopy(fields)
        for key in self._fields:
            self._columns[key] = []
        

    def save(self) -> None:
        lines = []
        lines.append('#' + ' ' + ' '.join(self._fields.keys()))
        for id, row in self._rows.items():
            lines.append(id + ' ' + ' '.join(row.values()))
        self._file.write(lines)

    def load(self) -> None:
        
        self._rows: Dict[str, Dict[str, str]] = {}
        self._columns: Dict[str, List[str]] = {}
        for key in self._fields:
            self._columns[key] = []
        
        lines = list(self._file.read())
        fields = list(self._fields.keys())
        for line in lines[1:]:
            values = map(str, line.split())
            id = values.pop(0)
            row = {}
            for i in range(len(values)):
                row[fields[i]] = values[i]
            self._rows[id] = row

    def generateID(self) -> str:
        return str(uuid.uuid4())

    def checkRow(self, data: Dict[str, str]) -> None:
        for key, val in data.items():
            if key not in self._fields:
                raise ValueError(f'{key} key is not in fields!')

            if not self._fields[key].isValueble(val):
                raise ValueError(f'Value is not type of {self._fields[key].type}!')

            if self._fields[key].unique and (val in self._columns[key]):
                raise ValueError('Duplicate value!')

        if len(self._fields) != len(data):
            raise ValueError('Not enough fields!')

    def addRow(self, data: Dict[str, str]) -> None:

        self.checkRow(data)
        row = copy.deepcopy(data)
        id = self.generateID()
        self._rows[id] = row

        for key, val in row.items():
            self._columns[key].append(val)
        
        self._file.write([id + ' ' + ' '.join(row.values())], True)

    def getRow(self, id: str) -> Dict[str, str]:
        if id not in self._rows:
            raise ValueError("ID doesn't exist!")
        return copy.deepcopy(self._rows[id])

    def getRows(self, ids: Set[str]) -> List[Dict[str, str]]:
        return [self.getRows(id) for id in ids]

    def deleteRow(self, id: str) -> None:
        if id not in self._rows:
            raise ValueError("ID doesn't exist!")
        self._rows.pop(id)

    def deleteRows(self, ids: Set[str]) -> None:
        for id in ids:
            self.deleteRow(id)

    def updateRow(self, id: str, newData: Dict[str, str]) -> None:
        self.checkRow(newData)
        for key in self._rows[id]:
            self._rows[id][key] = newData[key]

    def selectRows(self, equal: bool, field: str, value: str) -> Set[str]:
        if field not in self._fields:
            raise ValueError('Invalid field!')

        rowsID = set()
        for id, row in self._rows.items():
            if (equal and row[field] == value) or ((not equal) and row[field] != value):
                rowsID.add(id)

        return rowsID

