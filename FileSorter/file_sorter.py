# -*- coding: utf-8 -*-

import os
# from test.badsyntax_future3 import result
# from fileinput import filename

def CompareByFileContent(filePath1, filePath2):
    print('Compare file', os.path.split(filePath1)[1], 'with',os.path.split(filePath2)[1], 'by content')
    result = True
        
    if os.path.exists(filePath1) == False or os.path.exists(filePath1) == False:
        result = False
        return result
    
    file1 = open(filePath1, 'rb')
    file2 = open(filePath2, 'rb')
    
    try:
        byteFile1 = file1.read(1)
        byteFile2 = file2.read(1)
        while byteFile1 != b"" or byteFile2 != b"":
            if byteFile1 != byteFile2:
                result = False
                return result
            byteFile1 = file1.read(1)
            byteFile2 = file2.read(1)
    except IOError:
        result = False
        return result
    finally:
        file1.close()
        file2.close()
        
    return result
                        

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
                    if CompareByFileContent(filePath, searchFileFullPath):
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
    sourseFilePath = "C:\\Users\\HP-G7000\\Desktop\\test"
    searchDirectory = 'D:\\БазаФото'
    
#     filePath = os.path.join(sourseFilePath, sourseFileName)
    fileCounter = 0;
    allFiles = GetAllFilesFromDir(sourseFilePath)
    for sourseFileName in allFiles:
        print('File No:', fileCounter, 'of', len(allFiles))
        print('sourseFileName: ',sourseFileName)
        fileCounter += 1
        findFilesList = SearchFileBySize(sourseFileName, searchDirectory)
        print('findFilesList: ',findFilesList)
        if findFilesList:
            SaveResultToFile(sourseFileName, findFilesList)

#     findFilesList = SearchFileByName(filePath, searchDirectory)
#     print(findFilesList)

#     SaveResultToFile(filePath, findFilesList)

#     findFilesList = SearchSameFiles(filePath, searchDirectory)
#     print(findFilesList)

    print('\nEnd of program.')


if __name__ == '__main__':
    main()
