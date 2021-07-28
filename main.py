from database import Database

d = Database('schema.txt')

t = d._tables['User']

print(t._rows)