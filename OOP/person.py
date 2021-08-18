
class GenericDisplay:
    def gatherAttrs(self):
        attrs = '\n'
        for key in self.__dict__:
            attrs += '\t%s = %s\n' % (key, self.__dict__[key])
        return attrs

    def __str__(self):
        return ('<%s: %s>' % (self.__class__.__name__, self.gatherAttrs()))

class Person(GenericDisplay):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lastName(self):
        return self.name.split()[-1]

    def birthDay(self):
        self.age += 1

class Employee(Person):
    def __init__(self, name, age, job = None, pay = 0):
        Person.__init__(self, name, age)
        self.job = job
        self.pay = pay

    def birthDay(self):
        self.age += 2

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 40)
    print(bob)
    print(bob.lastName())
    bob.birthDay()
    print(bob)

    sue = Employee('Sue Jones', 44, job = 'dev', pay = 100000)
    print(sue)
    print(sue.lastName())
    sue.birthDay()
    sue.giveRaise(.10)
    print(sue)
