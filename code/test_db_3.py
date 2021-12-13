import sqlite3
import tkinter as tk

# region окно программы
# root = tk.Tk()-
# regionend

db = None


def create_db():
    global db
    try:
        db = sqlite3.connect("../db/test_db_3.db", timeout=5)
        print("Успешное подключение к базе данных")
    except sqlite3.Error as error:
        print("Ошибка:", error)
        exit()
    try:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE employees (employees_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                  first_name TEXT,
                                                  last_name TEXT,
                                                  hire_date DATE);''')
        cursor.execute('''CREATE TABLE jobs (job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             job_title TEXT NOT NULL,
                                             min_salary REAL NOT NULL,
                                             max_salary REAL NOT NULL);''')
        cursor.execute('''CREATE TABLE department(department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                  department_name TEXT NOT NULL,
                                                  manager_id INTEGER NOT NULL,
                                                  date DATE NOT NULL);''')
        cursor.execute('''CREATE TABLE job_history (employees_id INTEGER,
                                                   start_date DATE ,
                                                   end_date DEFAULT NULL,
                                                   salary REAL,
                                                   commission_pct REAL,
                                                   job_id INTEGER,
                                                   department_id INTEGER,
                                                   PRIMARY KEY(employees_id,start_date),
                                                   FOREIGN KEY (employees_id) REFERENCES employees(employees_id) ON DELETE CASCADE, 
                                                   FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
                                                   FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE);''')
        insert_list = [("Бухгалтер", 30000, 70000),
                       ("Программист", 50000, 150000),
                       ("Аналитик", 40000, 70000)]
        cursor.executemany('''INSERT INTO jobs (job_title,min_salary,max_salary) values(?,?,?);''', insert_list)
        insert_list = [("Бухгалтерия", 12, "1995-03-12"),
                       ("IT", 14, "1999-09-12"),
                       ("Отдел аналитики", 10, "1999-09-12")]
        cursor.executemany('''INSERT INTO department (department_name,manager_id,date) values(?,?,?);''', insert_list)

        cursor.execute('''CREATE TRIGGER qqq AFTER INSERT ON employees BEGIN 
                        INSERT INTO job_history (employees_id, start_date) VALUES (NEW.employees_id,new.hire_date); 
                                                                    END;''')
        # cursor.execute('''CREATE TRIGGER qqq2 BEFORE UPDATE job_history.salary''')


        # insert_list = [("Дима", "Снеков", "1995-03-12"), ("Алексей", "Пасевич"), ("Катерина", "Коцур", "1999-09-12"),
        #                ("Наталья","Снеткова"), ("Екатерина","Галушкина")]
        # cursor.executemany(
        #     '''INSERT INTO student (first_name,last_name,born_date) values (?,?,?);''', insert_list)

        db.commit()
        cursor.close()
        print("База успешно создана")
    except sqlite3.Error as error:
        print("Ошибка:", error)
        if db:
            db.close()
            print("База данных закрыта по причине ошибки в create_db")
        exit()


def db_connect():
    global db
    try:
        db = sqlite3.connect("../db/test_db_3.db", timeout=5)
        cursor = db.cursor()
        cursor.execute('''PRAGMA FOREIGN_KEYS=ON;''')
        print("Успешное подключение к базе данных")
    except sqlite3.Error as error:
        print("Ошибка подключения к базе данных:", error)


# db_connect()
create_db()
# region интерфейс
# l_ = tk.Label(root, text="fddfdf")
# l_.pack()

# regionend
# root.mainloop()
