from person import Person

class Manager(Person):
    def giveRaise(self, percent,bonus=0.1):
        self.pay *= (1.0 + percent + bonus)
if __name__ =='__main__':
    tom=Manager(name='Tom doe',age=60, pay=60000 )
    print(tom.lastName())
    tom.giveRaise(0.2)
    print(tom.pay)