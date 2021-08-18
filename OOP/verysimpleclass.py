
class rec: pass


def main():
    rec.name = 'abc'
    rec.val = 10

    print('rec.name:',rec.name)
    print('rec.val:',rec.val)

    x = rec()
    y = rec()

    print('x.name:',x.name)
    print('y.name:',y.name)

    x.name = 'cba'

    print('rec.name:',rec.name)
    print('x.name:',x.name)
    print('y.name:',y.name)

    print('rec.__dict__.keys():',rec.__dict__.keys())
    print('x.__dict__.keys():',x.__dict__.keys())
    print('y.__dict__.keys():',y.__dict__.keys())

    print(x.__class__)
    print(x.__base__)
    
    pass


if __name__ == '__main__':
    main()
