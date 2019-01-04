import os

sourseFileName = '1.txt'

def findFile(dir):
    print('in: ',dir)

    if os.path.isdir(dir):
        for ls in os.listdir(dir):
            if os.path.isdir(ls):
                print('dir: ', ls)
                findFile(os.path.abspath(ls))
            elif os.path.isfile(ls):
                print('abspath: ', os.path.abspath(ls))
                print('file: ',ls)


def main():
    cwd = os.getcwd()
    print(cwd)

    findFile(cwd)

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
