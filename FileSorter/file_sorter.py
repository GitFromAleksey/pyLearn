import os

sourseFileName = '1.txt'

def findFile(fileName, dir):
    if os.path.isdir(dir):
        print(' ', dir,' is dir')
        for ls in os.listdir(dir):
            print(ls)
            if os.path.isfile(ls):
                print(ls + ' is file')

def main():
    cwd = os.getcwd()
    print(cwd)

    findFile('file', cwd)

    # cwd = 'C:\Users\AMD\Desktop\Аня свадьба'.encode()
    # cwd = 'C:\Users\AMD\Desktop\Аня свадьба'
    # dir = 'C:\Users\AMD\Desktop\Аня свадьба'

    # for root, dirs, files in os.walk(cwd):
        # print('root: ', root)
        # print('dirs: ', dirs)
        # print('files: ', files)

    # str = 'Русский шрифт'
    # print('str = ', str)

if __name__ == '__main__':
    main()
