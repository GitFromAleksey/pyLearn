# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import json

# скрипт ищет дубли файлов в тойже директории

JSON_MD5_FILE_NAME = 'md5_E__БазаФото_1633181621.968188.json'
RESULT_TXT_FILE_NAME = 'find_copy_result_' + str(time.time()) + '.txt'
RESULT_JSON_FILE_NAME = 'find_copy_result_' + str(time.time()) + '.json'

ROOT_PATH = 'C:\git\CompareFiles'
JSON_MD5_FILE_PATH = ROOT_PATH + '\\'  + JSON_MD5_FILE_NAME
RESULT_TXT_FILE_PATH = ROOT_PATH + '\\' + RESULT_TXT_FILE_NAME
RESULT_JSON_FILE_PATH = ROOT_PATH + '\\' + RESULT_JSON_FILE_NAME


print('JSON_MD5_FILE_PATH:', JSON_MD5_FILE_PATH)

## -----------------------------------------------------------------------------
def Md5Compare(data_1, data_2):
    res = False
    if data_1['file_path'] != data_2['file_path']:
        res = (data_1['md5'] == data_2['md5'])
    return res
## -----------------------------------------------------------------------------
def ReadFromJson(file_path):
    f = open(file_path, 'rb')
    lines_list = []
    for line in f:
        lines_list.append(line)
    print('total read lines:', len(lines_list), ', form file:', file_path)
    return lines_list
## -----------------------------------------------------------------------------
def main():
    result_dict = {} # словарь результатов поиска({opriginal_file_path:'', copy_files_list]})

    json_content = ReadFromJson(JSON_MD5_FILE_PATH)

    f_result = open(RESULT_TXT_FILE_PATH, 'w')

    count_of_matches = 0
    common_size_bytes = 0
    for line in json_content:
        info = str()
        json_data = json.loads(line)
        begin_compare_flag = False
        is_matches = False
        info = '\r\noriginal: ' + json_data['file_path']
        copy_string_list = []
        for subline in json_content:
            sub_data = json.loads(subline)
            if (begin_compare_flag == True) and (Md5Compare(json_data, sub_data) == True):
                is_matches = True
                count_of_matches += 1
                info += '\r\ncopy: ' + sub_data['file_path']
                copy_string_list.append(sub_data['file_path'])
                common_size_bytes += json_data['file_size_bytes']
                json_content.remove(subline)
            if json_data['file_path'] == sub_data['file_path']:
                begin_compare_flag = True
## были найдены совпадения
        if is_matches == True:
            result_dict.update({json_data['file_path']: copy_string_list})
            f_result.write('< ' + info + ' >\n')
            print(info)

    f_json_result = open(RESULT_JSON_FILE_PATH, 'w')
    f_json_result.write( json.dumps(result_dict, ensure_ascii=False) )
    f_json_result.close()
    
    print('Count of matches: ', count_of_matches)
    print('\nОбъём копий файлов:')
    print(f'общее кол-во: {common_size_bytes} байт')
    print(f'общее кол-во: {common_size_bytes/1024} Кбайт')
    print(f'общее кол-во: {common_size_bytes/1024/1024} Мбайт')

    f_result.write('общее кол-во Мбайт:' + str(common_size_bytes/1024/1024) + '\n')
    f_result.close()
    pass
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
 
 
