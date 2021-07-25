from typing import Dict

from field import Field
from table import Table

import copy


class Database:

    def __init__(self, schemaPath: str) -> None:
        
        self._tables: Dict[str, Table] = {}
        self.__handleSchema(schemaPath)

    def __handleSchema(self, schemaPath: str) -> None:

        schemaFile = open(schemaPath, 'r')

        fields: Dict[str, Field] = {}
        tableName = ''

        while True:
            line = schemaFile.readline()

            if line == '' or line == '\n':
                self._tables[tableName] = Table(fields)
                fields.clear()

                if line == '':
                    break

            parts = line.split()

            if len(parts) == 1:
                tableName = parts[0]

            elif len(parts) > 1:
                fields[parts[0]] = Field(parts[-1], len(parts) == 3)


    def __insert(self, query):
        qlist = query.split()

        if qlist[2] not in self._tables:
            raise ValueError('Table not exist!')

        table = self._tables[qlist[2]]

        valuelist = []
        s = ''
        value = qlist[-1]
        for i in range(1, len(value) - 1):
            if value[i] != ',' and i != len(value) - 2:
                s += value[i]

            else:
                valuelist.append(s)
                s = ''

        data = {}
        tablefields = list(table._fields.keys())
        for i in range(len(valuelist)):
            data[tablefields[i]] = valuelist[i]

        table.addRow(data)

    def query(self, query: str):
        if query[-1] != ';':
            raise ValueError('Need a ; in the end of query')

        else:
            if 'INSERT INTO' in query:
                self.__insert(query)






        
