import sqlite3
from enum import Enum

DB_FILE       = 'db_file.db'
CREATE_TABLE  = 'CREATE TABLE '
IF_NOT_EXISTS = 'IF NOT EXISTS '
TEXT_NOT_NULL = 'TEXT NOT NULL,'
SELECT        = 'SELECT '

class ColumnType(Enum):
    null    = 'NULL'    # значение NULL
    integer = 'INTEGER' # Целые числа.
    text    = 'TEXT'    # Текстовые данные.
    real    = 'REAL'    # Числа с плавающей запятой.
    blob    = 'BLOB'    # Двоичные данные.


class DbHelper:

    def __init__(self, db_file: str = '') -> None:
        self.db = None
        self.cursor = None

        if db_file == '':
            return

        if self.DbConnect(db_file) == False:
            return

    def __del__(self) -> None:
        if self.db != None:
            self.db.close()

    def DbConnect(self, db_file: str = '') -> bool:
        try:
            self.db = sqlite3.connect(db_file)
            self.cursor = self.db.cursor()
        except:
            return False
        return True

    def GetTablesNames(self):
        ''' возвращает название всех таблиц в базе '''
        res = []
        if self.cursor == None:
            return None
        self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
        for name in self.cursor.fetchall():
            res.append(name[0])
        if len(res) == 0:
            return None
        return res

    def GetTableColumnsInfo(self, table_name:str=''):
        ''' возвращает параметры всех колонок таблицы '''
        res = []
        if self.cursor == None:
            return None
        self.cursor.execute('PRAGMA table_info('+table_name+')')
        for title_info in self.cursor.fetchall():
            title = {   'cid'       :title_info[0],
                        'name'      :title_info[1],
                        'type'      :title_info[2],
                        'notnull'   :title_info[3],
                        'dflt_value':title_info[4],
                        'pk'        :title_info[5]}
            res.append(title)
        return res

    def TableCreate(self, table_name: str = ''):
        ''' создаёт новую таблицу '''

        if table_name == '':
            return
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS '''+table_name+''' (
        id INTEGER PRIMARY KEY
        )
        ''')
        self.db.commit()

    def TableDrop(self, table_name:str='') -> bool:
        ''' удаляет таблицу '''
        if table_name == '':
            return False
        if table_name in self.GetTablesNames():
            self.cursor.execute('DROP TABLE '+table_name)
            return True
        else:
            return False

    def AddColumn(self, table_name: str='', column_name:str='', ctype: ColumnType=ColumnType.text):
        ''' добавляет новую колонку в таблицу '''
        if table_name == '':
            return
        if column_name == '':
            return
        self.cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {ctype}')

    def InsertData(self, table_name: str='', data: dict=None) -> bool:
        ''' запись/вставка данных '''
        if table_name == '' or data == None:
            return False
        columns = ''
        values = ''
        for key in data.keys():
            columns += key + ','
            if type(data[key]) == str:
                values += '"'+str(data[key])+'"' + ','
            else:
                values += str(data[key]) + ','
        columns = columns.strip(',')
        values = values.strip(',')
        request = f''' INSERT INTO {table_name} ({columns}) VALUES ({values}) '''
        self.cursor.execute(request)
        self.db.commit()
        return True

    def ReadAllDataFromTable(self, table_name: str=''):
        ''' отдаёт все данные из таблицы '''
        if table_name == '':
            return
        res = {}
        title = []
        for info in self.GetTableColumnsInfo(table_name=table_name):
            title.append(info['name'])
        request = f'''SELECT * FROM {table_name}'''
        self.cursor.execute(request)
        for data in self.cursor.fetchall():
            index = 0
            for d in data:
                column_name = title[index]
                if res.get(column_name) == None:
                    res[column_name] = []    
                res[column_name].append(d)
                index += 1
        return res

def main():

    table_name = 'TABLE_NAME'
    column_int  = 'column_int'
    column_text = 'column_text'
    column_real = 'column_real'
    column_blob = 'column_blob'

    db_helper = DbHelper()
    db_helper = DbHelper(DB_FILE)

    tables_names = db_helper.GetTablesNames()
    if tables_names == None:

        print(f'Создание таблицы с именем: {table_name}')

        db_helper.TableCreate(table_name)
        db_helper.AddColumn(table_name, column_int,  ColumnType.integer.value)
        db_helper.AddColumn(table_name, column_text, ColumnType.text.value)
        db_helper.AddColumn(table_name, column_real, ColumnType.real.value)
        db_helper.AddColumn(table_name, column_blob, ColumnType.blob.value)

        print(f'Добавление данных в таблицу: {table_name}')

        data = { column_int: 1, column_text: 'text', column_real: 3.14, column_blob: 1 }
        db_helper.InsertData(table_name=table_name, data=data)
        data = { column_int: 2, column_text: 'text1', column_real: 3.1415, column_blob: 2 }
        db_helper.InsertData(table_name=table_name, data=data)
        data = { column_int: 3, column_text: 'text2', column_real: 3.1415926, column_blob: 3 }
        db_helper.InsertData(table_name=table_name, data=data)

    tables_names = db_helper.GetTablesNames()
    print(f'Чтение списка таблиц из базы данных: {tables_names}')

    print(f'Чтение данных из таблицы: {table_name}')
    table_content = db_helper.ReadAllDataFromTable(table_name=table_name)
    print(table_content)
    print(f'Удаление таблицы: {table_name}')
    db_helper.TableDrop(table_name=table_name)


if __name__ == '__main__':
    main()
