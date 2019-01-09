import sys

def fib(n):
    a,b = 0,1
    while b < n:
        print(b, end=' ')
        a,b = b, a+b
    print()

def fib2(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result


def main():
    fib(10)
    res = fib2(100)

    print(type(res))
    for r in res:
        print(r, end=' ')

    for path in sys.path:
        print(path)

if __name__ == '__main__':
    main()
