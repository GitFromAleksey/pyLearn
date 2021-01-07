# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import json
import pathlib
import shutil

MAIN_DIRECTORY_JSON = 'md5_E__базафото_1609533674.311391.json'
COMPARED_DIRECTORY_JSON = 'md5_E__COPY_foto_Новая папка.json'

DIR_FOR_NEW_FILES = 'C:\git\COPY_foto_Новая папка'

## -----------------------------------------------------------------------------
def GetJsonFileContent(json_file_name):
    f = open(json_file_name, 'r')
    lines_list = []
    for line in f:
        lines_list.append(json.loads(line))
    print('total read lines:', len(lines_list), ', form file:', json_file_name)
    return lines_list

## -----------------------------------------------------------------------------
def main(argv):
    print(argv)

    content_main_dir = GetJsonFileContent(MAIN_DIRECTORY_JSON)
    content_compare_dir = GetJsonFileContent(COMPARED_DIRECTORY_JSON)

    result_list = []
    for compare_item in content_compare_dir:
        compare_md5 = compare_item['md5']
        is_find = False
        for main_item in content_main_dir:
            if compare_md5 == main_item['md5']:
               is_find = True
               break
        if not is_find:
            result_list.append(compare_item)
            print(compare_item['file_path'])

    print(len(result_list))

    for res_item in result_list:
        shutil.copy(res_item['file_path'], DIR_FOR_NEW_FILES)
    
    pass
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv)
 
 
