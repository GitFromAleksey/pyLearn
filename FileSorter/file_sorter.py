import os


def main():
    cwd = os.getcwd()
    print(cwd)

    # cwd = 'C:\Users\AMD\Desktop\Аня свадьба'.encode()
    # cwd = 'C:\Users\AMD\Desktop\Аня свадьба'
    # dir = 'C:\Users\AMD\Desktop\Аня свадьба'

    for root, dirs, files in os.walk(cwd):
        print('root: ', root)
        print('dirs: ', dirs)
        print('files: ', files)

    str = 'Русский шрифт'
    print('str = ', str)

if __name__ == '__main__':
    main()
