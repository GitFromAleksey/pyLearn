import sys
from random import randint as rnd


def binary_search(lst,item):
    find_steps = 0
    lo = 0
    hi = len(lst)-1
    while lo <= hi:
        find_steps += 1
        mid = int((lo + hi)/2)
        guess = lst[mid]
        print(f'lo: {lo}, hi: {hi}, mid: {mid}, guess: {guess}')
        if guess == item:
            break
        if guess > item:
            hi = mid - 1
        else:
            lo = mid + 1
    print(f'Array size: {len(lst)}, Find steps: {find_steps}, find item: {guess}')
    if guess == item:
        return mid
    else:
        return None


def main():
#    sys.argv[1]
    x = [rnd(0, 100) for i in range(10)]
    print(f'Generating sequence: {x}')
    x.sort()
    print(f'Sorted sequence: {x}')
    num = int(input(f'Set int number to find:'))
    res = binary_search(x, num)
    print(f'Number find in position: {res}')

if __name__ == '__main__':
    main()