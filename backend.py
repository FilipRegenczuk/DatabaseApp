import sqlite3

def connect():
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS testDB (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, date_of_birth TEXT, country_of_birth TEXT, sex TEXT, pesel INTEGER)")
    connection.commit()
    connection.close()