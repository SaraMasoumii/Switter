import copy
import uuid
from typing import Dict, List, Set

from database.field import Field
from database.file import File


class Table:

	def __init__(self, filePath: str, fields: Dict[str, Field]) -> None:

		self._file = File(filePath)
		self._fields = copy.deepcopy(fields)
		self._rows: Dict[str, Dict[str, str]] = {}
		try:
			self.load()
		except:
			self.save()

	def save(self) -> None:
		lines = []
		lines.append('#' + ' ' + ' '.join(self._fields.keys()))
		for id in self._rows:
			lines.append(self.textRow(id))
		self._file.write(lines)

	def load(self) -> None:
		rows = {}
		lines = list(self._file.read())
		fields = list(self._fields.keys())
		if '#' + ' ' + ' '.join(fields) != lines[0]:
			raise ValueError('Incorrect Fields!')
		for line in lines[1:]:
			if line == '':
				continue
			values = list(map(str, line.split()))
			id = values.pop(0)
			row = { fields[i] : values[i] for i in range(len(values)) }
			self.checkRow(row)
			if id in rows:
				raise ValueError('Duplicate value!')
			# Very Slow !!!!
			for key, val in row.items():
				if self._fields[key].unique:
					for _id, _row in rows.items():
						if _row[key] == val:
							raise ValueError('Duplicate value!')
			rows[id] = row
		self._rows = rows

	def generateID(self) -> str:
		return str(uuid.uuid4())

	def textRow(self, id = str) -> str:
		if id not in self._rows:
			raise ValueError("ID doesn't exist!")
		return id + ' ' + ' '.join(self._rows[id].values())

	def checkRow(self, data: Dict[str, str]) -> None:
		for key, val in data.items():
			if key not in self._fields:
				raise ValueError(f'{key} key is not in fields!')

			if not self._fields[key].isValueble(val):
				raise ValueError(f'Value is not type of {self._fields[key].type}!')

		if len(self._fields) != len(data):
			raise ValueError('Not enough fields!')

	def addRow(self, data: Dict[str, str]) -> None:
		self.checkRow(data)
		for key, val in data.items():
			if self._fields[key].unique:
				for id, row in self._rows.items():
					if row[key] == val:
						raise ValueError('Duplicate value!')

		row = copy.deepcopy(data)
		id = self.generateID()
		self._rows[id] = row
		self._file.write([self.textRow(id)], True)

	def getRow(self, id: str) -> Dict[str, str]:
		if id not in self._rows:
			raise ValueError("ID doesn't exist!")
		return copy.deepcopy(self._rows[id])

	def getRows(self, ids: Set[str]) -> List[Dict[str, str]]:
		return [self.getRow(id) for id in ids]

	def deleteRow(self, id: str) -> None:
		if id not in self._rows:
			raise ValueError("ID doesn't exist!")
		self._file.replace(self.textRow(id), '')
		self._rows.pop(id)

	def deleteRows(self, ids: Set[str]) -> None:
		for id in ids:
			self.deleteRow(id)

	def updateRow(self, id: str, newData: Dict[str, str]) -> None:
		self.checkRow(newData)
		for key, val in newData.items():
			if self._fields[key].unique:
				for _id, row in self._rows.items():
					if _id != id and row[key] == val:
						raise ValueError('Duplicate value!')
		oldRow = self.textRow(id)
		for key in self._rows[id]:
			self._rows[id][key] = newData[key]
		newRow = self.textRow(id)
		self._file.replace(oldRow, newRow)

	def selectRows(self, equal: bool, field: str, value: str) -> Set[str]:
		if field not in self._fields:
			raise ValueError('Invalid field!')

		rowsID = set()
		for id, row in self._rows.items():
			if (equal and row[field] == value) or ((not equal) and row[field] != value):
				rowsID.add(id)

		return rowsID

