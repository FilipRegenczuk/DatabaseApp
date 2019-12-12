import mysql.connector

class Database:

    def __init__(self):

        self.connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '6015',
        database = 'del'
        )

        self.cursor = self.connection.cursor()
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, date_of_birth TEXT, country_of_birth TEXT, sex TEXT, pesel INTEGER)")
        #self.connection.commit()

    def __del__(self):
        self.connection.close()

    def view(self):
        self.cursor.execute("SELECT * FROM dane_osobowe")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, name, surname, birthDate, birthCountry, sex, pesel):
        self.cursor.execute("INSERT INTO test VALUES (NULL, ?, ?, ?, ?, ?, ?)", (name, surname, birthDate, birthCountry, sex, pesel))
        self.connection.commit()

    def search(self, pesel):
        self.cursor.execute("SELECT * FROM test WHERE pesel=?", (pesel,))
        rows = self.cursor.fetchall()
        return rows
        
    def update(self, id, name, surname, birthDate, birthCountry, sex, pesel):
        self.cursor.execute("UPDATE test SET name=?, surname=?, date_of_birth=?, country_of_birth=?, sex=?, pesel=? WHERE id=?", (name, surname, birthDate, birthCountry, sex, pesel, id))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM test WHERE id=?", (id,))
        self.connection.commit()


    
