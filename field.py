import datetime
import re

class Field:
    
    def __init__(self, type: str, unique: bool) -> None:

        self.type = type
        self.unique = unique


    def isValueble(self, value) -> bool:

        t = self.type
        if t == 'INTEGER':
            return type(value) == int

        elif t == 'BOOLEAN':
            return type(value) == bool

        elif t == 'TIMESTAMP':

            if type(value) != str:
                return False

            try:
                datetime.datetime.strptime(value, '%Y-%m-%d')
                return True

            except ValueError:
                return False

        elif re.match('^CHAR\((\d+)\)$', t):

            l = int(re.findall("CHAR\((\d+)\)", t)[0])
            return type(value) == str and len(value) <= l

        return False



#print(re.findall("INSERT INTO (\w+) VALUES", "INSERT INTO users VALUES (eminem,1234,2020/02/01)"))