import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def create_products(conn):
    create_product(conn, ('Agusha', 50, 100))
    create_product(conn, ('Lays', 90, 100))
    create_product(conn, ('Mojito', 70, 100))
    create_product(conn, ('Nitro', 70, 100))
    create_product(conn, ('Flash', 60, 100))
    create_product(conn, ('Huggies', 20, 100))
    create_product(conn, ('Russkaya kartoshka', 50, 100))
    create_product(conn, ('Cookies', 80, 100))
    create_product(conn, ('Candies', 450, 100))
    create_product(conn, ('Marshmallow', 40, 100))
    create_product(conn, ('Tomatoes', 70, 100))
    create_product(conn, ('Cucumber', 80, 100))
    create_product(conn, ('Potato', 40, 100))
    create_product(conn, ('Carrot', 45, 100))
    create_product(conn, ('Watermelon', 20, 100))


def update_product_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_product_price(conn, product: tuple):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_product_by_id(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def print_products_by_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE quantity > 5 AND price < 100.0'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def print_all_product_by_title(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ("%"+word+"%",))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


connection = create_connection(db_name='hw.db')

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    create_table(connection, create_products_table)
    create_products(connection)
    update_product_price(connection, (500, 11))
    delete_product_by_id(connection, 7)
    print_all_products(connection)
    print_products_by_price_and_quantity(connection)
    print_all_product_by_title(connection, 'Nitro')
