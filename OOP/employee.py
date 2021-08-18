
class Employee:
    def __init__(self, name):
        self.name  = name
        print('Employee Constructor')
    def computeSalary(self):
        print(self.name + ' Employee Salary')
    def giveRaise(self):
        print(self.name + ' Employee giveRaise')
    def promote(self):
        print(self.name + ' Employee promote')
    def retire(self):
        print(self.name + ' Employee retire')
