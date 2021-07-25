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

    def query(self, query: str):
        pass


        
