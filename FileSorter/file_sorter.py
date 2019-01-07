import os
# from fileinput import filename


def SearchSameFiles(searchFile, sourseDir):
    print('Search same files')
    result = [] # list

    searchFilePath = os.path.split(searchFile)[0]
    searchFileName = os.path.split(searchFile)[1]
    
    os.chdir(searchFilePath)
    searchFileSize = os.path.getsize(searchFileName)

    if os.path.isdir(sourseDir):
        for curDir, dirs, files in os.walk(sourseDir):
            for file in files:
                filePath = os.path.join(curDir,file)
                if os.path.samefile(filePath, searchFile):
                    result.append(filePath)
                    print('same files')
    return result    
        

def SearchFileBySize(searchFile, sourseDir):
    print('Search by size')
    result = [] # list

    searchFilePath = os.path.split(searchFile)[0]
    searchFileName = os.path.split(searchFile)[1]
    
    os.chdir(searchFilePath)
    searchFileSize = os.path.getsize(searchFileName)

    if os.path.isdir(sourseDir):
        for curDir, dirs, files in os.walk(sourseDir):
            for file in files:
                os.chdir(curDir)
                filePath = os.path.join(curDir,file)
                fileSize = os.path.getsize(filePath)
                if fileSize == searchFileSize:
                    result.append(filePath)
    return result


def SearchFileByName(fileName,sourseDir):
    print('Search by name')
    result = [] # list

    if os.path.isdir(sourseDir):
        for curDir, dirs, files in os.walk(sourseDir):
            for file in files:
                if fileName == file:
                    filePath = os.path.join(curDir,file)
                    result.append(filePath)
    return result


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
            if os.path.isfile(ls):
                print('is file: ',ls)
            if os.path.isdir(ls):
                print('is dir: ', ls)


def main():
    path_ = "C:\\Users\\AMD\\eclipse-workspace\\pyLearn\\FileSorter"
    sourseFileName = '1.txt'
    
    print('os.name: ', os.name)
    print('os.altsep: ', os.altsep)

    cwd = os.getcwd()
    print('current dir: ', cwd)
    
    filePath = os.path.join(path_, sourseFileName)

    findFilesList = SearchFileByName(sourseFileName, cwd)
    print(findFilesList)

    findFilesList = SearchFileBySize(filePath, path_)
    print(findFilesList)

    findFilesList = SearchSameFiles(filePath, path_)
    print(findFilesList)

if __name__ == '__main__':
    main()
