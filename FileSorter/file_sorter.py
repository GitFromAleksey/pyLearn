import os
from fileinput import filename

sourseFileName = 'dir_1.txt'

def FindFile(fileName,sourseDir):
    if os.path.isdir(sourseDir):
        for curDir, dirs, files in os.walk(sourseDir):
            for file in files:
                print(fileName, ' - ', file)
                if filename == file:
                    print(os.path.join(curDir,file))

def PrintAllDirsContent(dirPath):
    
    if os.path.isdir(dirPath):
        for curDir, dirs, files in os.walk(dirPath):
            for file in files:
                print('file: ', os.path.join(curDir,file))
                
            for dir in dirs:
                print('directory: ', os.path.join(curDir,dir))


def PrintDir(dirPath):

    print('findFile(dir): ',dirPath)

    if os.path.isdir(dirPath):
        for ls in os.listdir(dirPath):
#                 PrintDir(os.path.abspath(ls))
            if os.path.isfile(ls):
#                 print('abspath: ', os.path.abspath(ls))
                print('is file: ',ls)
            if os.path.isdir(ls):
                print('is dir: ', ls)

def main():
    print('os.name: ', os.name)
    print('os.altsep: ', os.altsep)

    cwd = os.getcwd()
    print('current dir: ', cwd)

#     PrintDir(cwd)
    path_ = "C:\\Users\\HP-G7000\\eclipse-workspace\\pyLearn"

#     PrintAllDirsContent("C:\\Users\\HP-G7000\\eclipse-workspace\\pyLearn\\FileSorter")
    FindFile(sourseFileName, cwd)


if __name__ == '__main__':
    main()
