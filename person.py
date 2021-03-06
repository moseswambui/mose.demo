class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

if __name__ =='__main__':
    bob= Person('Bob Smith', 54, 54000, 'software developer')
    sue=Person('Sue Jones', 43, 63000, 'hardware woman')
    print(bob.name, sue.pay)
    print(bob.lastName())
    sue.giveRaise(0.22)
    print(sue.pay)