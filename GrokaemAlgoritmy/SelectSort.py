from random import randint as rnd

def FindSmallest(arr:list):
    print(f'Find smallest array size: {len(arr)}')
    smallest_index = 0
    smallest = arr[smallest_index]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def SelectionSort(arr:list):
    print(f'Array size: {len(arr)}')
    sort_iterations = 0
    newArr = []
    for i in range(len(arr)):
        smallest = FindSmallest(arr)
        newArr.append(arr.pop(smallest))
        sort_iterations += 1
    print(f'Sort Iterations: {sort_iterations}')
    return newArr

def main():
    notsortedarr = [rnd(0, 100) for i in range(100)]
    print(f'Not sorted: {notsortedarr}')
    sorted = SelectionSort(notsortedarr)
    print(f'Sorted arr: {sorted}')

if __name__ == '__main__':
    main()