import os
import time
import hashlib
import json

PATH = 'E:\НовыеФото\МаминаФлэшка' #'E:\базафото' #'E:\НовыеФото\WhatsApp Video'

INFO_PATH          = 'Path'
INFO_SIZE          = 'Size'
INFO_NAME          = 'Name'
INFO_FILE_EXT      = 'File_ext'
INFO_PERMISSIONS   = 'Permissions'
INFO_OWNER         = 'Owner'
INFO_DEVICE        = 'Device'
INFO_CREATED       = 'Created'
INFO_LAST_MODIFIED = 'Last modified'
INFO_LAST_ACCESSED = 'Last accessed'
INFO_HASH          = 'Hash'

## -----------------------------------------------------------------------------
class cIndexator:
    EXCLUDE_DIRS = ['.git']

    def __init__(self, directory):
        self.directory = directory
        print(f'path: {self.directory}')
        self.files_info_list = self.GetAllFilesInfo(self.directory)
        self.CalcAllFilesHash()
        print(f'file: {self.files_info_list}')
        print(f'Find: {len(self.files_info_list)} files')
        print(f'Size of files: {self.CalcSizeAllFiles(self.files_info_list)} bytes')
        self.ext_dict = self.FindAllFilesExtentions(self.files_info_list)
        print(f'Find extensions:')
        for key in self.ext_dict:
            print(f'"{key}": {self.ext_dict[key]}')

    def SaveIndexingData(self):
        fname = PATH + '\\' + 'index.json'
        f_json = open(fname,'w', encoding='utf-8')
        json_string = json.dump(self.files_info_list, f_json, ensure_ascii = False, indent=2)
##        f_json.write(json_string + '\n')

        f_json.close()

    def CalcAllFilesHash(self):
        for finf in self.files_info_list:
            finf[INFO_HASH] = self.CalcFileHash(finf)
        self.SaveIndexingData()

    def CalcFileHash(self, file_info):
        hash_md5 = hashlib.md5()
        with open(file_info[INFO_PATH], 'rb') as f:
            for chunk in iter(lambda: f.read(), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def GetAllFilesInfo(self, directory):
        ''' возвращает список путей ко всем файлам во всех поддиректориях '''
        files_info_list = []
        
        for root, dirs, files in os.walk(directory):
            for name in files:
                if '.git' in root:
                    continue
                file_path = os.path.join(root, name)
                files_info_list.append(self.GetFileInfo(file_path)) # TODO нужно возвращать этот парамерт

        return files_info_list

    def FindAllFilesExtentions(self, files_paths_list):
        ''' подсчитывает сколько есть разных расширений '''
        extensions_dict = {}
        for file_path in files_paths_list:
            ext = file_path[INFO_FILE_EXT]
            if (ext in extensions_dict):
                params = extensions_dict[ext]
                params['count'] += 1
                params['size'] += file_path[INFO_SIZE]
                extensions_dict[ext] = params
            else:
                extensions_dict[ext] = {'count': 1, 'size': 0}

        return extensions_dict

    def CalcSizeAllFiles(self, files_paths_list, extention = ''):
        size = 0
        for fileinfo in files_paths_list:
            size += fileinfo[INFO_SIZE]

        return size

    def GetFileInfo(self, file_path):
        ''' возвращает информацию о файле '''
        stat_info = os.stat(file_path)
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_path)[1]

        info = {
            INFO_PATH          : file_path,
            INFO_SIZE          : stat_info.st_size,
            INFO_NAME          : file_name,
            INFO_FILE_EXT      : file_ext,
            INFO_PERMISSIONS   : stat_info.st_mode,
            INFO_OWNER         : stat_info.st_uid,
            INFO_DEVICE        : stat_info.st_dev,
            INFO_CREATED       : stat_info.st_ctime,
            INFO_LAST_MODIFIED : stat_info.st_mtime,
            INFO_LAST_ACCESSED : stat_info.st_atime,
            INFO_HASH          : None
        }

        return info
## -----------------------------------------------------------------------------

def main():
    global PATH

    indexator = cIndexator(PATH)
    


if __name__ == '__main__':
    main()
