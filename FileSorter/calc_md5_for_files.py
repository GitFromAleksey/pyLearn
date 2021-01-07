# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime
import hashlib
import json

# скрипт считает md5 для всех файлов во всех поддиректориях

root_path = 'E:\базафото'

print("root_path:", root_path)

## -----------------------------------------------------------------------------
def md5_calc(file):
    hash_md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

## -----------------------------------------------------------------------------
def directory_traversal(path):
    file_count = 0
    all_files = []
    
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            all_files.append(file_path)
            file_count = file_count + 1
    return file_count, all_files
    
## -----------------------------------------------------------------------------
def main():
    
    file_count, all_files = directory_traversal(root_path)

    fname = root_path.replace('\\','_')
    fname = 'md5_' + fname.replace(':','_') + '_' + str(time.time()) +'.json'
    
    f_json = open(fname,'w')
    time_begin = time.time()
    for file in all_files:
        file_size_bytes = os.path.getsize(file)

        file_info = file + ': ' + str(int(file_size_bytes/1024)) + 'kbyte; '
        file_open_time = str( datetime.datetime.fromtimestamp( os.path.getatime(file)) )
        file_create_time = str( datetime.datetime.fromtimestamp(os.path.getctime(file)) )
        file_modified_time = str( datetime.datetime.fromtimestamp(os.path.getmtime(file)) )

        time_calc_begin = time.time()
        md5 = md5_calc(file)
        time_end = time.time()
        time_calc_md5 = '; time:' + str(time_end - time_calc_begin)
        line = str(file_count) + '. ' + file_info + md5_calc(file) + time_calc_md5

        dict_data_line = {
                'file_path' : file,
                'md5' : md5,
                'file_size_bytes' : file_size_bytes,
                'create_time' : file_create_time,
                'modified_time' : file_modified_time
            }
        json_string = json.dumps(dict_data_line, ensure_ascii=False)
        print(line)
        f_json.write(json_string + '\n')
        if file_count > 0:
            file_count -= 1

    f_json.close()
    
    time_end = time.time()
    print('time:', (time_end - time_begin))
    print('time.ctime:', time.ctime(time_end - time_begin))
    print(len(all_files))
    print("file_count:", file_count)

    pass
    
## -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
 
