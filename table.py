import copy
import uuid
from typing import Any, Dict, List, Set

from field import Field


class Table:

	def __init__(self, fields: Dict[str, Field]) -> None:

		self._rows: List[Dict[str, str]] = []
		self._columns: Dict[str, List[str]] = {}
		self._fields = copy.deepcopy(fields)
		for key in self._fields:
			self._columns[key] = []
		self._columns['#'] = []

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
		row['#'] = self.generateID()
		
		for key, val in row.items():
			self._columns[key].append(val)

		self._rows.append(row)

	def getRows(self, ids: Set[str]) -> List[Dict[str, str]]:
		rows = []
		for row in self._rows:

			if row['#'] in ids:
				rowCopy = copy.deepcopy(row)
				rowCopy.pop('#')
				rows.append(rowCopy)

		return rows

	def selectRows(self, equal: bool, field: str, value: str) -> Set[str]:
		if field not in self._fields:
			raise ValueError('Invalid field!')

		rowsID = set()
		for row in self._rows:
			if (equal and row[field] == value) or ((not equal) and row[field] != value):
				rowsID.add(row['#'])
				
		return rowsID
