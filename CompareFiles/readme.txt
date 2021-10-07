1. calc_md5_for_files.py
- вычисляет md5 для всех файлов в указанной папке и иодпапках
- для переменной root_path = '' нужно указать путь к папке
- результат - json файл типа "md5_путь_к_папке_х.х.json"

2. find_files_copy_by_md5.py
- в json файле от предыдущего скрипта "md5_путь_к_папке_х.х.json" ищет копии
файлов и вычисляет занимаемую ими память
- результат: "find_copy_result_x.x.txt" и "find_copy_result_x.x.json"
- для переменной JSON_MD5_FILE_NAME = '' нужно указать путь к анализируемому 
файлу "md5_путь_к_папке_х.х.json"

3. compare_dirs.py
- сравнивает два json файла с md5 двух папок
MAIN_DIRECTORY_JSON = 'md5_1.json'
COMPARED_DIRECTORY_JSON = 'md5_2.json'
- если в MAIN_DIRECTORY_JSON отсутствуют файлы из COMPARED_DIRECTORY_JSON, то
они копируются в директорию DIR_FOR_NEW_FILES = 'путь'