from database import Database

d = Database('schema.txt')

t = d._tables['User']

d.query('INSERT INTO User VALUES (eminem,ee,2021/02/01);')

print(t._rows)
print(t.selectRows(True, 'username', 'eminem'))
print(t.getRows(t.selectRows(True, 'username', 'eminem')))