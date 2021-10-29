import sqlite3

sqlite_connection = None


def new_db():
    global sqlite_connection
    try:
        sqlite_connection = sqlite3.connect("../db/test_db22.db", timeout=5)
        print("подкключение к базе прошло успешно")
    except sqlite3.Error as error:
        print("произошла ошибка при подключении к базе данных:", error)
        exit()
    try:
        cursor = sqlite_connection.cursor()
        cursor.execute('''PRAGMA FOREIGN_KEYS=ON;''')
        cursor.execute('''CREATE TABLE student (id integer PRIMARY KEY AUTOINCREMENT,
                                                first_name text not null,
                                                second_name text not null,
                                                born_date date);''')

        cursor.execute('''CREATE TABLE facultet_name_list (id integer PRIMARY KEY AUTOINCREMENT,
                                                          name text NOT NULL,
                                                          create_date date);''')

        cursor.execute('''CREATE TABLE facultet_student (id_student integer not null,
                                                         id_facultet integer not null,
                                                         in_date date,
                                                         out_date date DEFAULT NULL,
                                                         foreign key (id_student) references student(id) on delete cascade,
                                                         foreign key (id_facultet) references facultet_name_list(id) on delete cascade) ;''')

        insert_list = [("Дима", "Снетков", "1995-03-12"), ("Саша", "Широглазов", "1998-06-29"),
                       ("Лёша", "Пасевич", "1999-02-19"), ("Беслан", "Ибрагимов", "1998-04-13"),
                       ("Катя", "Коцур", "1999-09-12"), ("Наталья", "Снеткова", "1970-06-19"),
                       ("Екатерина", "Галушкина", "1997-01-16"), ("Андрей", "Снетков", "1967-09-01")]
        cursor.executemany('''INSERT INTO student (first_name,second_name,born_date) values (?,?,?);''', insert_list)
        insert_list = [("фпм", "1950-03-24"), ("матфак", "1970-03-03"), ("эконом", "1990-02-05")]
        cursor.executemany('''INSERT INTO facultet_name_list (name, create_date) values(?,?);''', insert_list)
        sqlite_connection.commit()
        cursor.close()
        check_config = open("../config2", "r")
        config_list = check_config.readlines()
        check_config.close()
        config_list[0] = "1\n"
        check_config = open("../config2", "w")
        check_config.writelines(config_list)
        check_config.close()
    except sqlite3.Error as error:
        print("произошла ошибка при созданнии в базе данных стартовых таблиц:", error)
        if (sqlite_connection):
            sqlite_connection.close()
            print("база данных закрыта из-за ошибки при создании стартовых таблиц")
        exit()


check_config_file = open("../config2", "r")  # /////////////////////////продумать создание файла конфигурации
check_config = check_config_file.read(1)
check_config_file.close()
try:
    check_config = int(check_config)
except:
    print("файл конфигурации нарушен, не числовое значение")
    exit()

# подключение к базе данных
if check_config == 0:
    new_db()
elif check_config == 1:
    try:
        sqlite_connection = sqlite3.connect("../db/test_db22.db", timeout=5)
        cursor = sqlite_connection.cursor()
        cursor.execute('''PRAGMA FOREIGN_KEYS=ON;''')
        cursor.close()
        print("успешное подключение к базе данных")
    except sqlite3.Error as error:
        print("ошибка при подключении к базе данных:", error)
        exit()
else:
    print("Ошибка: повреждение файла конфигурации")
    exit()
# конец подключения к базе данных

try:
    cursor = sqlite_connection.cursor()
    # cursor.execute('''INSERT INTO student VALUES (8, "Саша", "Широглазов", "1966-06-29 15:33");''')
    # cursor.execute('''SELECT * FROM student WHERE first_name="Саша";''')
    # cursor.execute('''SELECT * FROM student GROUP BY id;''')
    # rez = cursor.fetchall()
    # print(rez)
    # cursor.execute('''UPDATE student SET first_name="Кирил", second_name="Волошин" WHERE first_name="Беслан";''')
    # cursor.close()
    # sqlite_connection.commit()
    # cursor = sqlite_connection.cursor()

    name = [("Дима", "фпм", "2013-09-01"), ("Катя", "матфак", "2015-04-04"), ("Наталья", "эконом", "1987-03-23"),
            ("Беслан", "фпм", "2015-09-01"), ("Андрей", "матфак", "1980-09-01")]
    cursor.executemany(
        '''INSERT INTO facultet_student (id_student, id_facultet, in_date) values (
                                (select id from student where first_name=?),
                                (select id from facultet_name_list where name=?), ?);''', name)

    # cursor.execute('''CREATE TABLE student2 AS select * from student where 1=0;''')

    # cursor.execute('''SELECT student.first_name, student.second_name, student.born_date, facultet_student.in_date,
    #                 facultet_name_list.name as facultet
    #                 FROM student JOIN facultet_student
    #                 ON student.id=facultet_student.id_student
    #                 JOIN facultet_name_list
    #                 ON facultet_student.id_facultet=facultet_name_list.id
    #                 where facultet_name_list.id=1
    #                 ;''')

    # студенты одного конкретного факультета
    name = ("фпм",)
    cursor.execute('''SELECT student.first_name, student.second_name, facultet_student.in_date as data_postuplenia
                        FROM facultet_student  JOIN facultet_name_list
                        ON facultet_name_list.id=facultet_student.id_facultet
                        join student
                        on student.id =facultet_student.id_student
                        where facultet_name_list.name=?;
                        ''', name)

    ###
    # cursor.execute('''delete from student where id==6;''')
    result = cursor.fetchall()
    print(result)
    sqlite_connection.commit()
    cursor.close()
    print("данные в таблицу факультет_студень успешно добавленны")
except sqlite3.Error as error:
    print("Произошла ошибка в основном теле программы:", error)

if (sqlite_connection):
    sqlite_connection.close()
    print("база данных закрыта по завершения программы")
