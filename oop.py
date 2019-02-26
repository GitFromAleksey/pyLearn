

class FirstClass: # имя класса
    u'Simple Class'
    var = 87 # публичная переменная
    __var = 90 # приватная переменная
    
    def __init__(self):
        print('FirstClass.Constructor ')
        print('self',self)
    
    def f():
        return 'Hello World'


    
fc = FirstClass()

print('FirstClass.var = ', FirstClass.var)
print('FirstClass.f() = ', FirstClass.f())

