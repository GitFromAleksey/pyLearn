import employee as e


class Egineer(e.Employee):
    def __init__(self,name):
        print('Egineer Constructor')
        super().__init__(name)
        
    def computeSalary(self):
        print(self.name + ' Egineer Salary')

class Manager(e.Employee):
    def __init__(self,name):
        print('Manager Constructor')
        super().__init__(name)
        
    def computeSalary(self):
        print(self.name + ' Manager Salary\ncall super.computeSalary:')
        super().computeSalary()
    

def main():


    bob = e.Employee('Bob')
    mel = Egineer('Mel')
    ken = Manager('Ken')

    empls = [bob, mel, ken]
    for emp in empls:
        print()
        emp.computeSalary()
        emp.giveRaise()
        emp.promote()
        emp.retire()

    e.Employee.giveRaise(bob)

    pass


if __name__ == '__main__':
    main()
