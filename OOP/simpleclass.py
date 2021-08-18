

##------------------------------------------------------------------------------
class SimpleClass: # имя класса
    u'Simple Class __doc__'
    var = 87 # совместно используемая переменная
    'Simple Class constructor'
    def __init__(self):
##        self.var = 99
        print('SimpleClass.Constructor ')
        print('self',self)

    def display(self):
        print ('display:', self.var, SimpleClass.var )
    
    def f():
        print ('Hello World')

def main():
    smc = SimpleClass()

    print(smc.__doc__)
    print('SimpleClass.var = ', smc.var)
    print('SimpleClass.f() = ', SimpleClass.f())
    SimpleClass.var = 0
    print('smc.var = ', smc.var)
    smc.var = 1
    print('SimpleClass.var = ', SimpleClass.var)
    print('smc.var = ', smc.var)
    SimpleClass.var = 2
    print('SimpleClass.var = ', SimpleClass.var)
    print('smc.var = ', smc.var)

##    SimpleClass.display()
    smc.display()


    
if __name__ == '__main__':
    main()
