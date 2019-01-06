import os

sourseFileName = '1.txt'

def findFile(dir):

    print('findFile(dir): ',dir)

    if os.path.isdir(dir):
        for ls in os.listdir(dir):
            if os.path.isdir(ls):
                print('is dir: ', ls)
                findFile(os.path.abspath(ls))
            if os.path.isfile(ls):
#                 print('abspath: ', os.path.abspath(ls))
                print('is file: ',ls)


def main():
    cwd = os.getcwd()
#     print('current dir: ', cwd)

    findFile(cwd)


if __name__ == '__main__':
    main()
