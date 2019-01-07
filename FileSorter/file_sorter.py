# -*- coding: utf-8 -*-

import os
# from fileinput import filename

def SaveResultToFile(fileFullPath, savingData):

    saveFileName = fileFullPath + '.res.txt'
    writeStr = ''
    
    file = open(saveFileName, 'w')

    try:
        if file:
            for data in savingData:
                writeStr += data +'\n'
            file.write(writeStr)
    except IOError:
        print('IOerror')
    finally:
        file.close()
    

def SearchSameFiles(searchFileFullPath, dirForFinding):
    print('Search same files')
    result = [] # list

    searchFilePath = os.path.split(searchFileFullPath)[0]
    searchFileName = os.path.split(searchFileFullPath)[1]
    
    os.chdir(searchFilePath)
    searchFileSize = os.path.getsize(searchFileName)

    if os.path.isdir(dirForFinding):
        for curDir, dirs, files in os.walk(dirForFinding):
            for file in files:
                filePath = os.path.join(curDir,file)
                if os.path.samefile(filePath, searchFileFullPath):
                    result.append(filePath)
                    print('same files')
    return result    
        

def SearchFileBySize(searchFileFullPath, dirForFinding):
    print('Search by size')
    result = [] # list

    searchFilePath = os.path.split(searchFileFullPath)[0]
    searchFileName = os.path.split(searchFileFullPath)[1]
    
    os.chdir(searchFilePath)
    searchFileSize = os.path.getsize(searchFileName)

    if os.path.isdir(dirForFinding):
        for curDir, dirs, files in os.walk(dirForFinding):
            for file in files:
                os.chdir(curDir)
                filePath = os.path.join(curDir,file)
                fileSize = os.path.getsize(filePath)
                if fileSize == searchFileSize:
                    result.append(filePath)
    return result

def SearchFileByName(searchFileFullPath, dirForFinding):
    print('Search by name')
    result = [] # list

    searchFilePath = os.path.split(searchFileFullPath)[0]
    searchFileName = os.path.split(searchFileFullPath)[1]
    
    os.chdir(searchFilePath)
    searchFileSize = os.path.getsize(searchFileName)

    if os.path.isdir(dirForFinding):
        for curDir, dirs, files in os.walk(dirForFinding):
            for file in files:
                if searchFileName == file:
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

def GetAllFilesFromDir(sourseDir):
    result = []
    
    if os.path.isdir(sourseDir):
        for curDir, dirs, files in os.walk(sourseDir):
            for file in files:
                filePath = os.path.join(curDir,file)
                result.append(filePath)
    return result

def main():
    print('os.name: ', os.name)
    print('os.altsep: ', os.altsep)
    cwd = os.getcwd()
    print('current dir: ', cwd)

#     sourseFileName = '1.txt'
#     sourseFileName = ''
#     sourseFilePath = "C:\\Users\\AMD\\eclipse-workspace\\pyLearn\\FileSorter"
    sourseFilePath = "C:\\Users\\HP-G7000\\Desktop\\Фото с телефона нужно переместить в базу"
    searchDirectory = 'D:\\БазаФото'
    
#     filePath = os.path.join(sourseFilePath, sourseFileName)

    for sourseFileName in GetAllFilesFromDir(sourseFilePath):
        print('sourseFileName: ',sourseFileName)
        findFilesList = SearchFileBySize(sourseFileName, searchDirectory)
        print('findFilesList: ',findFilesList)
        if findFilesList:
            SaveResultToFile(sourseFileName, findFilesList)

#     findFilesList = SearchFileByName(filePath, searchDirectory)
#     print(findFilesList)

#     SaveResultToFile(filePath, findFilesList)

#     findFilesList = SearchSameFiles(filePath, searchDirectory)
#     print(findFilesList)


if __name__ == '__main__':
    main()
