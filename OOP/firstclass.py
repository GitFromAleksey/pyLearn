
##------------------------------------------------------------------------------
class SimpleClass: # имя класса
    u'Simple Class __doc__'
    var = 87 # совместно используемая переменная
    'Simple Class constructor'
    def __init__(self):
        print('SimpleClass.Constructor ')
        print('self',self)
    
    def f():
        return 'Hello World'
##------------------------------------------------------------------------------
class FirstClass: # Определить объект класса
    def setdata(self, value): # Определить методы класса
        self.data = value # self – это экземпляр
    def display(self):
        print ('FirstClass.data:',self.data) # self.data: данные экземпляров
##------------------------------------------------------------------------------
class SecondClass(FirstClass): # Наследует setdata
    def display(self): # Изменяет display
        print ('SecondClass.data: "%s"' % self.data)
##------------------------------------------------------------------------------
class ThirdClass(SecondClass): # Наследует SecondClass
    def __init__(self, value): # Вызов "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # Для выражения "self + other"
        return ThirdClass(self.data + other)
    def __mul__(self, other):
        self.data = self.data * other # Для выражения "self * other"
##------------------------------------------------------------------------------

def main():
    smc = SimpleClass()

    print(smc.__doc__)
    print('SimpleClass.var = ', smc.var)
    print('SimpleClass.f() = ', SimpleClass.f())
    SimpleClass.var = 0
    print('smc.var = ', smc.var)
    smc.var = 1
    print('SimpleClass.var = ', SimpleClass.var)

    fc = FirstClass()
    fc.setdata(5)
    fc.display()

    sc = SecondClass()
    sc.setdata(6)
    sc.display()

    tc = ThirdClass('abc')
    tc.display()
    tc = tc + 'def'
    tc.display()
    tc * 3
    tc.display()

    print('Superclass:',ThirdClass.__base__)
    print('Superclass:',SecondClass.__base__)
    print('Superclass:',FirstClass.__base__)
    
if __name__ == '__main__':
    main()
