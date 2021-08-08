from database import *
from application import *

a = Application()
d = a.database
t = d._tables['Users']
#row = { 'username' : 'mamad', 'password' : 'amir', 'joined_at' : '2020/01/01' }
#t.addRow(row)

print(d.query('SELECT FROM Users WHERE username==sarah OR password==amir;'))

#print(t._rows)