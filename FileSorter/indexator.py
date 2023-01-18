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
        index_file_data = self.FindIndexFile(directory)
        self.FindFileCopy(index_file_data)
        
        self.files_info_list = self.GetAllFilesInfo(self.directory)
        if index_file_data != None:
            self.CompareFilesInfo(index_file_data, self.files_info_list)
        self.ext_dict = self.FindAllFilesExtentions(self.files_info_list)
        self.CalcAllFilesHash()

    def FindFileCopy(self, files_list):
        ''' Ищет копии файлов в списке по HASH '''
        f_list = files_list.copy()
        result = []
        copy_size = 0
        copy_count = 0
        for cmp_fl in f_list:
            f_list.remove(cmp_fl)
            copy_list = []
            copy_list.append(cmp_fl)
            for fl in f_list:
                if cmp_fl[INFO_HASH] == fl[INFO_HASH]:
                    copy_list.append(fl)
                    f_list.remove(fl)
                    copy_size += fl[INFO_SIZE]
                    copy_count += 1
            if len(copy_list) > 1:
                result.append(copy_list)

        print(f'Количество копий файлов: {copy_count}')
        print(f'Размер копий файлов: {copy_size} bytes')
##        for cp_fls in result:
##            _str = 20*'-' + '\n'
##            for fl in cp_fls:
##                _str += f'{fl[INFO_NAME]}; '
##            print(_str)

        return (result, copy_count, copy_size)
        

    def CompareFilesInfo(self, index_list, files_list):
        ''' Сравнивает два списка файлов. Ищет новые, удаленные, перименованные. '''
        if len(index_list) != len(files_list):
            print(f'Изменилось количество файлов. Было {len(index_list)}, стало {len(files_list)}')

        delete_files = []
        for idx in index_list:
            file = idx
            for fl in files_list:
                if idx[INFO_NAME] == fl[INFO_NAME]:
                    file = None
                    break
            if file != None:
                delete_files.append(file)

        add_files = []
        rename_files = []
        for idx in files_list:
            file = idx
            for fl in index_list:
                if idx[INFO_NAME] == fl[INFO_NAME]:
                    file = None
                    break
            if file != None:
                file[INFO_HASH] = self.CalcFileHash(file)
                add_files.append(file)
                for idxf in index_list:
                    if file[INFO_HASH] == idxf[INFO_HASH]:
                        rename_files.append(file)
                        add_files.remove(file)

        print(f'Удаленных файлов: {len(delete_files)}')
        for delf in delete_files:
            print(f'{delf[INFO_PATH]}')
        print(f'Добавленных файлов: {len(add_files)}')
        for addf in add_files:
            print(f'{addf[INFO_PATH]}')
        print(f'Переименованых файлов: {len(rename_files)}')
        for renf in rename_files:
            print(f'{renf[INFO_PATH]}')

        return (delete_files, add_files, rename_files)
        

    def FindIndexFile(self, directory):
        ''' Ищет файл с информацией индексации файлов. '''
        index_file = self.directory + '\\' + 'index.json'
        try:
            f_json = open(index_file,'r', encoding='utf-8')
            data = json.load(f_json)
            f_json.close()
            print(f'Найден файл индексации каталога: "index.json"')
            return data
        except:
            return None

    def SaveIndexingData(self):
        fname = self.directory + '\\' + 'index.json'
        print(f'Сохранение результатов в файл "{fname}"')
        f_json = open(fname,'w', encoding='utf-8')
        json_string = json.dump(self.files_info_list, f_json, ensure_ascii = False, indent=2)
        f_json.close()

    def CalcAllFilesHash(self):
        print(f'Рассчёт хэшей для всех файлов:')
        count = len(self.files_info_list)
        for finf in self.files_info_list:
            print(f'{115*" "}\r', end="")
            print(f'Осталось {count} файлов. Рассчёт для "{finf[INFO_NAME]}"\r', end="")
            count -= 1
            finf[INFO_HASH] = self.CalcFileHash(finf)
        print(f'{115*" "}\r', end="")
        print(f'Закончен рассчёт хэш для всех файлов.')
        self.SaveIndexingData()

    def CalcFileHash(self, file_info):
        hash_md5 = hashlib.md5()
        with open(file_info[INFO_PATH], 'rb') as f:
            for chunk in iter(lambda: f.read(), b''):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def GetAllFilesInfo(self, directory):
        ''' возвращает список путей ко всем файлам во всех поддиректориях '''
        print(f'Поиск всех файлов...')
        files_info_list = []
        
        for root, dirs, files in os.walk(directory):
            for name in files:
                if '.git' in root:
                    continue
                file_path = os.path.join(root, name)
                files_info_list.append(self.GetFileInfo(file_path)) # TODO нужно возвращать этот парамерт
        print(f'\rНайдено файлов: {len(files_info_list)}')

        return files_info_list

    def FindAllFilesExtentions(self, files_paths_list):
        ''' подсчитывает сколько есть разных расширений '''
        print(f'Поиск типов файлов...')
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
        print(f'Найдено {len(extensions_dict)} типов файлов.')
        print(f'Список найденных типов файлов:')
        for key in extensions_dict:
            print(f'    "{key}": {extensions_dict[key]}')
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
    
    input('Нажмите Enter для выхода...')

if __name__ == '__main__':
    main()
