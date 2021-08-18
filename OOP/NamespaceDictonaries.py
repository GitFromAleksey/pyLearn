
class Super:
    def hello(self):
        self.data1 = 'spam'

class sub(Super):
    def hola(self):
        self.data2 = 'eggs'

def classtree(cls, indent):
    print('.'*indent, cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls,indent+3)

def instancetree(inst):
    print('Tree of ', inst)
    classtree(inst.__class__, 3)

def main():
    X = sub()
    Y = sub()
    print('X.__dict__: ' + str(X.__dict__))
    print('X.__class__: ' + str(X.__class__))
    print('sub.__bases__: ' + str(sub.__bases__))
    print('Super.__bases__: ' + str(Super.__bases__))
    print()
    X.hello()
    print('X.__dict__: ' + str(X.__dict__))
    print('sub.__dict__: ' + str(sub.__dict__))
    print('Super.__dict__: ' + str(Super.__dict__))
    X.hola()
    print('X.__dict__: ' + str(X.__dict__))
    print('sub.__dict__: ' + str(sub.__dict__))
    print('Super.__dict__: ' + str(Super.__dict__))
    print('Y.__dict__: ' + str(Y.__dict__))

    print()
    instancetree(sub())

if __name__ == '__main__':
    main()
