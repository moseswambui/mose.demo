from person import Person
from manager import Manager

bob=Person(name='Bob smith', age=43, pay=20000)
sue=Person(name='Sue janes', age=45, pay=50000)
tom=Manager(name='Tom Doe', age=59, pay=70000)

db=[bob, sue, tom]
for obj in db:
    obj.giveRaise(.11)

for obj in db:
    print(obj.lastName(), '=>', obj.pay)

for obj in db:
    print(obj.lastName())