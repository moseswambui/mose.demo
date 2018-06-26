class Person:
    def __init__(self, name, age, job=None, pay=0):
        self.name=name
        self.age=age
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0+percent)

    def __str__(self):
        return ('%s > %s: %s %s>') %(self.__class__.__name__,self.name,self.job, self.pay)

class Manager(Person):
    def __int__(self, name,age, pay):
        Person.__init__(self, name, age, 'manager', pay)

    def giveRaise(self, percent+bonus):
        Person.giveRaise(1.0+percent+bonus)

if __name__ == '__main__':
    bob=Person('Bob collymore', 54, 'developer', 59000)
    sue=Person('sue janes', 44, 'hardware', 49503)
    tom=Manager('Tom Doe', 60, 505000)

    print(sue, sue.pay, sue.lastName())

    for obj in (bob, sue, tom):
        obj.giveRaise(0.5+34)
        print(obj)
