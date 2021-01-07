# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import json
import pathlib

COMPARE_RESULT_FILE_PATH = 'compare_result_1609527373.8434548.json'

## -----------------------------------------------------------------------------
def main(argv):
    print(argv)

    json_file = open(COMPARE_RESULT_FILE_PATH)
    json_content = json.load(json_file)
    print(len(json_content))
    
    all_files_extension_list = []
    
    for key,val in json_content.items():
        file_extension = pathlib.Path(key).suffix
        all_files_extension_list.append(file_extension)
        if file_extension == '.jpg':#key.find('.jpeg') > 2:
            print('key:',key,',val',val)

    sort_extension_list = []
    for extension in all_files_extension_list:
        find_new_extension = False
        for sort_extension in sort_extension_list:
            if extension == sort_extension:
                find_new_extension = True
        if not find_new_extension:
            sort_extension_list.append(extension)

    print(sort_extension_list)
    
    pass
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv)
 
 
