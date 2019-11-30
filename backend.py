import sqlite3

def connect():
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, date_of_birth TEXT, country_of_birth TEXT, sex TEXT, pesel INTEGER)")
    connection.commit()
    connection.close()

def insert(name, surname, birthDate, birthCountry, sex, pesel):
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test VALUES (NULL, ?, ?, ?, ?, ?, ?)", (name, surname, birthDate, birthCountry, sex, pesel))
    connection.commit()
    connection.close()

def view():
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")
    rows = cursor.fetchall()
    connection.close()
    return rows

connect()   # connecting to database anytime you switch on app
insert("Filip", "Regeńczuk", "1997-02-10", "Poland", "M", "97021012345")
print(view())