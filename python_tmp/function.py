

def fib(n):
    print()
    print('fib:')
    a,b = 0,1
    while b< n:
        print(b, end=', ')
        a,b=b,a+b

fib(2000)

def fib2(n):
    print()
    print('fib2:')
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result

fib100 = fib2(100)
print(fib100)


def ask_ok(prompt, retries=4, complaint='Yes or no< pleas!'):
    while True:
        ok = input(prompt)
        if ok in ('y','yeah','yes','yep'):
            print ('return True')
            return True
        if ok in ('n','no','nop','nope'):
            print('return False')
            return False
        retries = retries - 1
        if retries < 0:
            print('IOError(refusenik user)')
            raise IOError('refusenik user')
        print('complaint')

ask_ok('Do you really want to quit?')

def make_inkrementator(n):
    return lambda x: x + n

f = make_inkrementator(42)
print(f)
