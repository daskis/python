import sqlite3
from Connection import Connection


class CreatingTables(Connection):
    def __init__(self):
        super().__init__()
    def creating_tables(self):
        cursor = self.con.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dishes (
                id INTEGER PRIMARY KEY,
                dish_name TEXT,
                price REAL,
                description TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Menu (
                id INTEGER PRIMARY KEY,
                dish_id INTEGER,
                FOREIGN KEY (dish_id) REFERENCES Dishes(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Orders (
                id INTEGER PRIMARY KEY,
                dish_id INTEGER,
                order_date TEXT,
                FOREIGN KEY (dish_id) REFERENCES Dishes(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                id INTEGER PRIMARY KEY,
                employee_name TEXT,
                position TEXT,
                salary REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tables (
                id INTEGER PRIMARY KEY,
                table_number INTEGER,
                capacity INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Reservations (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                table_id INTEGER,
                reservation_date TEXT,
                FOREIGN KEY (customer_id) REFERENCES Customers(id),
                FOREIGN KEY (table_id) REFERENCES Tables(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ingredients (
                id INTEGER PRIMARY KEY,
                ingredient_name TEXT,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Suppliers (
                id INTEGER PRIMARY KEY,
                supplier_name TEXT,
                contact_number TEXT,
                email TEXT
            )
        ''')

