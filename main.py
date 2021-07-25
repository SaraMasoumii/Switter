from database import Database

d = Database('schema.txt')

t = d._tables['User']
row = { 'username': 'Sarah Genius', 'password' : 'Amir ham bahooshe', 'joined_at': '2021-12-11' }
row1 = { 'username': 'Sarah Genius', 'password' : 'asdas', 'joined_at': '2021-12-11' }
t.addRow(row)
t.addRow(row1)
print(t.selectRow())