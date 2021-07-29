from database import *
from application import *

a = Application()
d = a.database
t = d._tables['User']
#row = { 'username' : 'mamad', 'password' : 'amir', 'joined_at' : '2020/01/01' }
#t.addRow(row)

#print(d.query('DELETE FROM User WHERE username==nesa;'))

#print(t._rows)