from random import randint as rnd

def QuickSort(array:list):
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    result = QuickSort(less) + [pivot] + QuickSort(greater)
    return result

def main():
    notsortedarr = [rnd(0, 100) for i in range(100)]
    print(f'Not sorted: {notsortedarr}')
    sorted = QuickSort(notsortedarr)
    print(f'Sorted arr: {sorted}')

if __name__ == '__main__':
    main()