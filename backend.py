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
        
    def __del__(self):
        self.connection.close()

    def view(self):
        self.cursor.execute("SELECT * FROM dane_osobowe")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        self.cursor.execute("INSERT INTO dane_osobowe VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate))
        self.connection.commit()

    def search(self, pesel, name, surname):
        self.cursor.execute("SELECT * FROM dane_osobowe WHERE pesel=? OR (imie=? AND nazwisko=?)", (pesel, name, surname))
        rows = self.cursor.fetchall()
        return rows
        
    def update(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        self.cursor.execute("UPDATE dane_osobowe SET imie=?, nazwisko=?, imie_i_nazwisko_rodowe_ojca=?, imie_i_nazwisko_rodowe_matki=?, data_urodzenia=?, miejsce_urodzenia=?, kraj_pochodzenia=?, plec=?, pesel=?, stan_cywilny=?, obywatelstwo_lub_stan_bezpanstwowca=?, adres_zameldowania_na_pobyt_staly=?, kraj_miejsca_zamieszkania=?, kraj_poprzedniego_miejsca_zamieszkania=?, data_zgonu=? WHERE id=?", (name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate, id))
        self.connection.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM dane_osobowe WHERE id=?", (id,))
        self.connection.commit()


    
