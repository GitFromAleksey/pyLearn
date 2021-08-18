##------------------------------------------------------------------------------
class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
    def action(self):
        assert 0, 'action must be defined'
##------------------------------------------------------------------------------
class Inheritor(Super):
    pass
##------------------------------------------------------------------------------
class Replacer(Super):
    def method(self):
        print('in Replaser.method')
##------------------------------------------------------------------------------
class Extender(Super):
    def method(self):
        print('starting Extender.method')
        super().method()
        print('ending Extender.method')
##------------------------------------------------------------------------------
class Provider(Super):
    def action(self):
        print('in Provider.action')
##------------------------------------------------------------------------------
def main():
##    s = Super()
##    s.action()
    for klass in (Inheritor,Replacer,Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
##------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
##------------------------------------------------------------------------------

##------------------------------------------------------------------------------
