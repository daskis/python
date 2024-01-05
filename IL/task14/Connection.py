import sqlite3
from sqlite3 import Error


class Connection:
    def __init__(self):
        try:
            self.con = sqlite3.connect("db14.db")
            self.cursor = self.con.cursor()
            print("Connected")
        except Error:
            print("Error connecting to the database")