from database import Database

d = Database('schema.txt')

t = d._tables['User']

d.query('INSERT INTO User VALUES (sarah,ee,2021/02/01);')
print(t._rows)
d.query('DELETE FROM User WHERE username==”sarah” OR phone==”09171656786”;')
print(t._rows)