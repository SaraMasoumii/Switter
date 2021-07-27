from file import File
from typing import Dict, List, Set

from field import Field
from table import Table


class Database:

	def __init__(self, schemaPath: str) -> None:

		self._tables: Dict[str, Table] = {}
		self.__handleSchema(schemaPath)

	def __handleSchema(self, schemaPath: str) -> None:
		
		fields: Dict[str, Field] = {}
		tableName = ''
		schemaFile = File(schemaPath)
		
		for line in schemaFile.read():

			if line == '' or line == '\n':
				self._tables[tableName] = Table(tableName, fields)
				fields.clear()

			parts = line.split()

			if len(parts) == 1:
				tableName = parts[0]

			elif len(parts) > 1:
				fields[parts[0]] = Field(parts[-1], len(parts) == 3)

	def __where(self, table: Table, query: str) -> Set[str]:
		pass

	def __select(self, query: str) -> List[Dict[str, str]]:
		pass

	def __delete(self, query: str) -> None:
		pass

	def __update(self, query: str) -> None:
		pass

	def __insert(self, query: str) -> None:

		qlist = query.split()
		if qlist[2] not in self._tables:
			raise ValueError('Table not exist!')

		table = self._tables[qlist[2]]

		valueList = []
		tmp = ''
		value = qlist[-1]
		for i in range(1, len(value) - 1):
			if value[i] != ',' and i != len(value) - 2:
				tmp += value[i]

			else:
				valueList.append(tmp)
				tmp = ''

		data = {}
		tableFields = list(table._fields.keys())
		for i in range(len(valueList)):
			data[tableFields[i]] = valueList[i]

		table.addRow(data)

	def query(self, query: str):
		if query[-1] != ';':
			raise ValueError('Need a ; in the end of query')

		if 'INSERT INTO' in query:
			self.__insert(query)

		elif 'SELECT FROM' in query:
			self.__select(query)




