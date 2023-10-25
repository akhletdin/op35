# СУБД - Система управления базами данных
# SQL - язык структурированных запросов
# CRUD - Create Read Update Delete
# DML - Data Manipulation Language

import sqlite3


def create_connection(db_file):
    """Создает соединение с БД"""
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


def create_table(connection, sql):
    """Создает таблицу"""
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_employee(connection, employee: tuple):
    # employee = ('Иванов Иван Иванович', 100000, 'плавание', '1990-01-01', True)
    sql = '''
    INSERT INTO employees 
    (fullname, salary, hobby, birth_date, is_married) 
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_employee_salary(connection, employee_id, new_salary):
    sql = '''UPDATE employees SET salary = ? WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (new_salary, employee_id))
    connection.commit()


def delete_employee(connection, employee_id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (employee_id,))
    connection.commit()


def select_all_employees(connection):
    sql = '''SELECT * FROM employees'''
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def select_employer_by_salary(connection, salary):
    sql = '''SELECT * FROM employees WHERE salary > ?'''
    cursor = connection.cursor()
    cursor.execute(sql, (salary,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

connection = create_connection("35-1.db")

sql_create_employees_table = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    salary FLOAT NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
);
'''

if connection:
    print("Соединение с БД установлено")
    create_table(connection, sql_create_employees_table)

    select_employer_by_salary(connection, 1500)
    # select_all_employees(connection)

    # delete_employee(connection, 2)
    # update_employee_salary(connection, 2, 777)

    # create_employee(connection, ('Иванов Иван Иванович', 100000, 'плавание', '1990-01-01', True))
    # create_employee(connection, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
    # create_employee(connection, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
    # create_employee(connection, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
    # create_employee(connection, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
    # create_employee(connection, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
    # create_employee(connection, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
    # create_employee(connection, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
    # create_employee(connection, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
    # create_employee(connection, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
    # create_employee(connection, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
    # create_employee(connection, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
    # create_employee(connection, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
    # create_employee(connection, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
    # create_employee(connection, ('William Tokenson', 1500, None, '1999-12-12', False))
    # create_employee(connection, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
    # create_employee(connection, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
    connection.close()


# '''
# ДЗ*:
# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
# 8. Добавить функцию, которая меняет количество товара по id
# 9. Добавить функцию, которая меняет цену товара по id
# 10. Добавить функцию, которая удаляет товар по id
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
# 12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле 100 сомов и количество которых больше чем 5 и распечатывала бы их в консоли
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
# 14. Протестировать каждую написанную функцию
# '''
