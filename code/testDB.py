# import sqlite3
#
# try:
#     sqlite_connection = sqlite3.connect("test_db.db")
#     cursor = sqlite_connection.cursor()
#     print('база данных создана и успешно подключена')
#
#     sqlite_query = "select sqlite_version();"
#     cursor.execute(sqlite_query)
#     rez = cursor.fetchall()
#     print("версия базы данных:", rez)
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к базе", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("соединение с базой закрыто")
#
# try:
#     sqlite_connection = sqlite3.connect("test_db.db")
#     cursor = sqlite_connection.cursor()
#     print("база подключена")
#
#     sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
#                                 id INTEGER PRIMARY KEY,
#                                 name TEXT NOT NULL,
#                                 email text NOT NULL UNIQUE,
#                                 joining_date datetime,
#                                 salary REAL NOT NULL);'''
#     cursor.execute(sqlite_create_table_query)
#     sqlite_connection.commit()
#     print("таблица создана")
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("ошибка при подключении к базе", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("база данных закрыта")


import sqlite3

sqlite_connection = None  # подключение к базе данных


def new_db():  # создание новой базы данных и изменение файла конфигурации
    try:
        global sqlite_connection
        sqlite_connection = sqlite3.connect("../db/test_db_2.db")
        cursor = sqlite_connection.cursor()
        cursor.execute('''CREATE TABLE student(
                                                id integer,
                                                first_name text,
                                                second_name text,
                                                born_data datetime);''')
        #///////////////////////////////
        cursor.execute('''INSERT INTO student VALUES(1,"DIMA","SNETKOV","1995-03-12");''')
        cursor.execute(('''INSERT INTO student(id, first_name) VALUES (2,"Alex");'''))
        sqlite_connection.commit()
        #///////////////////////////////
        cursor.close()

        print("создание новой базы данных прошло успешно")
        file_config = open("../config", "r")
        list_config = file_config.readlines()
        file_config.close()
        print(list_config)  # //////////////////////////////
        list_config[0] = "1\n"
        file_config = open("../config", "w")
        file_config.writelines(list_config)
        file_config.close()
        print("изменена конфигурация запуска программы:")
        print(list_config)  # ///////////////////////////////////
    except sqlite3.Error as error:
        print("произошла ошибка при создании базы данных:", error)
        if(sqlite_connection):
            sqlite_connection.close()
            print("база данных отключена по причине ошибки в блоке создания новой базы")
        exit()


file_config = open("../config", "r")
check_db_config = file_config.readline();
file_config.close()
check_db_config = int(check_db_config)
if check_db_config == 0:
    new_db()
elif check_db_config == 1:  # подключение к базе данных
    try:
        sqlite_connection = sqlite3.connect("../db/test_db_2.db")
        #/////////////////////////////
        cursor = sqlite_connection.cursor()
        # cursor.execute(
        #     '''INSERT INTO student (first_name,second_name,born_data)VALUES("Sasha","Shiroglazov","1995-03-12 12:34");''')
        cursor.execute('''DELETE FROM student where born_data="1995-03-13 12:34"; ''')
        # print(cursor.fetchall())#/////////////////////////////
        print("внесено изменений:", sqlite_connection.total_changes)#////////////////////////////
        sqlite_connection.commit()
        cursor.close()
        #/////////////////////////////
        print("подключение к базе данных прошло успешно")
    except sqlite3.Error as error:
        print("произошла ошибка при подключении базы:", error)
        exit()

if (sqlite_connection):
    sqlite_connection.close()
    print("база данных закрыта по завершению программы")
