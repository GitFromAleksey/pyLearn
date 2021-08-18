
class Callback:
    def __init__(self, color):
        self.color = color
    def __del__(self):
        print('__del__.' + self.color)

    def __call__(self):
        print('turn', self.color)

    def changeColor(self):
        print('turn', self.color)

class Button:
    def __init__(self, command):
        self.command = command

    def PushButton(self):
        self.command()

def main():
    cb1 = Callback('blue')
    cb2 = Callback('green')
    cb3 = (lambda color = 'red': 'turn ' + color)
    

    B1 = Button(command = cb1)
    B2 = Button(command = cb2)
    B3 = Button(command = cb1.changeColor)

    B1.PushButton()
    B2.PushButton()
    print(cb3())
    B3.PushButton()
##    cb1()
##    cb2()
    
    pass

if __name__ == '__main__':
    main()
