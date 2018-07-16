import shelve
from person import Person
from manager import Manager

mose = Person('Moses Ndungu', 43,600000, 'pentester')
dave=Person('David Mwangi', 44,89999, 'designer')
denno=Manager('dennis ngera', 45, 60000)
db = shelve.open('class-shelve')
db['mose']=mose
db['dave']=dave
db['denno']=denno

db.close()
db =open('class-shelve.bak')
for key in db:
    print(key)