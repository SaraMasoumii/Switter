from database import *
from application import *

a = Application()
d = a.database
t = d._tables['User']
#row = { 'username' : 'mamad', 'password' : 'amir', 'joined_at' : '2020/01/01' }
#t.addRow(row)

print(d.query('SELECT FROM User WHERE username==sarah OR password==amir;'))

#print(t._rows)