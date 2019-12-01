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

def search(pesel):
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test WHERE pesel=?", (pesel,))
    rows = cursor.fetchall()
    connection.close()
    return rows
    
def update(id, name, surname, birthDate, birthCountry, sex, pesel):
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE test SET name=?, surname=?, date_of_birth=?, country_of_birth=?, sex=?, pesel=? WHERE id=?", (name, surname, birthDate, birthCountry, sex, pesel, id))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect("testDB.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM test WHERE id=?", (id,))
    connection.commit()
    connection.close()
 


connect()   # connecting to database anytime you switch on app


#insert("Jan", "Kowalski", "1990-12-13", "Poland", "M", "90121312345")
#print(view())
#print(search("97021012345"))
#delete("97021012345")
#update(2, "Bartosz", "Kowalski", "1990-12-13", "Poland", "M", 90121312345)

