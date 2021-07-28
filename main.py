from database import *
from application import *

d = Database('schema.txt')

t = d._tables['User']

print(t._rows)