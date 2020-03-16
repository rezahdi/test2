import sqlite3


class Database:
    def __init__(self):
        self.create_items_table()
        self.create_users_table()

    @classmethod
    def create_users_table(cls):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        create_users_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text,password text)'
        cursor.execute(create_users_table)

        connection.commit()
        connection.close()
        print("Users table created")

    @classmethod
    def create_items_table(cls):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        create_items_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price float )'
        cursor.execute(create_items_table)

        connection.commit()
        connection.close()
        print("Items table created")
