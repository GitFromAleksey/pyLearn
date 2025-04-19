import sqlite3
from enum import Enum

DB_FILE = 'db_file.db'
CREATE_TABLE = 'CREATE TABLE '
IF_NOT_EXISTS = 'IF NOT EXISTS '
TEXT_NOT_NULL = 'TEXT NOT NULL,'
SELECT = 'SELECT '

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

    def TableDrop(self, table_name:str=''):
        ''' удаляет таблицу '''
        if table_name == '':
            return
        if table_name in self.GetTablesNames():
            self.cursor.execute('DROP TABLE '+table_name)
            print('drop ok')
        else:
            print('drop error')

    def AddColumn(self, table_name: str='', column_name:str='', ctype: ColumnType=ColumnType.text):
        ''' добавляет новую колонку в таблицу '''
        if table_name == '':
            return
        if column_name == '':
            return
        self.cursor.execute(f'ALTER TABLE {table_name} ADD COLUMN {column_name} {ctype}')

    def InsertData(self, table_name:str=''):
        ''' запись/вставка данных '''
#        Table: Users3
#            Title: id
#            Title: new_column
#            Title: new_column2
        request = f'''
        INSERT INTO Users3
        (id, new_column, new_column2)
        VALUES (4, 'data0', 'data1') '''
        print(request)
        self.cursor.execute(request)
        self.db.commit()
#        self.cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
        pass

    def ReadAllDataFromTable(self, table_name:str=''):
        ''' отдаёт все данные из таблицы '''
        request = f'''SELECT * FROM Users3'''
        print(request)
        self.cursor.execute(request)
        res = self.cursor.fetchall()
        print(res)

def main():

    db_helper = DbHelper()
    db_helper = DbHelper(DB_FILE)

    for table_name in db_helper.GetTablesNames():
        print(f'Table: {table_name}')
        for title in db_helper.GetTableColumnsInfo(table_name):
            print(f'Title: {title["name"]}')

#    db_helper.InsertData()
    db_helper.ReadAllDataFromTable()
#    db_helper.AddColumn('Users3','new_column2',ColumnType.text.value)
#    db_helper.TableDrop('Users3')
#    db_helper.TableCreate('Users3')

    return

    db = sqlite3.connect(DB_FILE) # установка соединения с базой
    c = db.cursor() # получение курсора
    # Методы курсора
    # execute(), executemany() - методы выполнения SQL
    # fetchone(), fetchall() - методы получения результатов

    # создание таблицы "Users"
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
    )
    ''')
    # NULL: значение NULL
    # INTEGER: Целые числа.
    # TEXT: Текстовые данные.
    # REAL: Числа с плавающей запятой.
    # BLOB: Двоичные данные.

#    c.execute('PRAGMA table_info(Users)')
    c.execute('SELECT name FROM sqlite_master WHERE type="table";')
    res = c.fetchall()

    print(res)
    db.commit() # сохранение изменений в базе

    db.close() # закрытие соединения с базой
    pass

if __name__ == '__main__':
    main()
