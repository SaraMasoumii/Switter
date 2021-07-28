from typing import Dict, List, Set

from field import Field
from file import File
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

			if line == '':
				self._tables[tableName] = Table(f'tables/{tableName.lower()}.txt', fields)
				fields.clear()

			parts = line.split()

			if len(parts) == 1:
				tableName = parts[0]

			elif len(parts) > 1:
				fields[parts[0]] = Field(parts[-1], len(parts) == 3)

	def __where(self, table: Table, query: str) -> Set[str]:
		pass

	def __select(self, query: str) -> List[Dict[str, str]]:
		que = query.split(' WHERE ')
		tableName = que[0].split()[-1]
		table = self._tables[tableName]
		ids: Set[str] = self.__where(table, que[1])
		table.getRows(ids)

	def __delete(self, query: str) -> None:
		que = query.split(' WHERE ')
		tableName = que[0].split()[-1]
		table = self._tables[tableName]
		ids: Set[str] = self.__where(table, que[1])
		table.deleteRows(ids)

	def __update(self, query: str) -> None:
		que1 = query.split(' WHERE ')
		que2 = que1[1].split(' VALUES ')
		que3 = que2[1][1 : -2]
		tableName = que1[0].split()[-1]
		table = self._tables[tableName]
		ids: Set[str] = self.__where(table, que2[0])

		if len(ids) > 1:
			raise ValueError('There are more than one row with this conditions!')

		id = list(ids)[0]

		valueList = que3.split(',')
		newData: Dict[str, str] = {}
		tableFields = list(table._fields.keys())

		newData = {tableFields[i]: valueList[i] for i in range(len(valueList))}

		table.updateRow(id, newData)

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

		tableFields = list(table._fields.keys())
		data = { tableFields[i]: valueList[i] for i in range(len(valueList)) }

		table.addRow(data)

	def query(self, query: str):
		if query[-1] != ';':
			raise ValueError('Need a ; in the end of query')

		if 'INSERT INTO' in query:
			self.__insert(query)

		elif 'SELECT FROM' in query:
			self.__select(query)

		elif 'DELETE FROM' in query:
			self.__delete(query)

		elif 'UPDATE' in query:
			self.__update(query)




