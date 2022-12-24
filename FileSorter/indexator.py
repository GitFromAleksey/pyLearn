import os
import time


PATH = 'E:\базафото' # 'E:\НовыеФото\WhatsApp Video'

## -----------------------------------------------------------------------------
class cIndexator:
    EXCLUDE_DIRS = ['.git']

    def __init__(self, directory):
        self.directory = directory

        self.files_paths_list = self.GetAllFiles(self.directory)
        

        print(f'Find: {len(self.files_paths_list)} files.')

        print(f'Find extensions:')
        ext_dict = self.FindAllFilesExtentions(self.files_paths_list)
        for key in ext_dict:
            print(f'"{key}": {ext_dict[key]}')
        
    def GetAllFiles(self, directory):
        ''' возвращает список путей ко всем файлам во всех поддиректориях '''
        files_paths_list = []
        
        for root, dirs, files in os.walk(directory):
            for name in files:
                if '.git' in root:
                    continue
                file_path = os.path.join(root, name)
                files_paths_list.append(file_path)

        return files_paths_list

    def FindAllFilesExtentions(self, files_paths_list):
        extensions_dict = {}
        for file_path in files_paths_list:
            ext = self.GetFileInfo(file_path)['file_ext']
            if (ext in extensions_dict):
                extensions_dict[ext] += 1
            else:
                extensions_dict[ext] = 1

        return extensions_dict

    def GetFileInfo(self, file_path):
        ''' возвращает информацию о файле '''
        stat_info = os.stat(file_path)
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_path)[1]

        info = {
            'Path' : file_path,
            'Size': stat_info.st_size,
            'Name': file_name,
            'file_ext' : file_ext,
            'Permissions' : stat_info.st_mode,
            'Owner' : stat_info.st_uid,
            'Device' : stat_info.st_dev,
            'Created' : stat_info.st_ctime,
            'Last modified' : stat_info.st_mtime,
            'Last accessed' : stat_info.st_atime
        }

        return info
## -----------------------------------------------------------------------------

def main():
    global PATH

    indexator = cIndexator(PATH)
    


if __name__ == '__main__':
    main()
