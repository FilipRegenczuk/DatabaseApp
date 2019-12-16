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
        view = """
            SELECT id_danych, imie, nazwisko, imie_i_nazwisko_rodowe_ojca, imie_i_nazwisko_rodowe_matki, data_urodzenia, miejsce_urodzenia, kraj_pochodzenia, plec, pesel, stan_cywilny, obywatelstwo_lub_stan_bezpanstwowca, adres_zameldowania_na_pobyt_staly, kraj_miejsca_zamieszkania, kraj_poprzedniego_miejsca_zamieszkania, data_zgonu 
            FROM dane_osobowe
        """
        self.cursor.execute(view)
        rows = self.cursor.fetchall()
        return rows


    def search(self, pesel, name, surname):
        search = """
            SELECT id_danych, imie, nazwisko, imie_i_nazwisko_rodowe_ojca, imie_i_nazwisko_rodowe_matki, data_urodzenia, miejsce_urodzenia, kraj_pochodzenia, plec, pesel, stan_cywilny, obywatelstwo_lub_stan_bezpanstwowca, adres_zameldowania_na_pobyt_staly, kraj_miejsca_zamieszkania, kraj_poprzedniego_miejsca_zamieszkania, data_zgonu 
            FROM dane_osobowe 
            WHERE pesel=%s OR (imie=%s AND nazwisko=%s)
        """
        self.cursor.execute(search, (pesel, name, surname))
        rows = self.cursor.fetchall()
        return rows
        

    def insert(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        insert = """
            INSERT INTO dane_osobowe 
            VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert, (name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate))
        self.connection.commit()


    def update(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        update = """
        UPDATE dane_osobowe 
        SET imie=%s, nazwisko=%s, imie_i_nazwisko_rodowe_ojca=%s, imie_i_nazwisko_rodowe_matki=%s, data_urodzenia=%s, miejsce_urodzenia=%s, kraj_pochodzenia=%s, plec=%s, pesel=%s, stan_cywilny=%s, obywatelstwo_lub_stan_bezpanstwowca=%s, adres_zameldowania_na_pobyt_staly=%s, kraj_miejsca_zamieszkania=%s, kraj_poprzedniego_miejsca_zamieszkania=%s, data_zgonu=%s 
        WHERE id_danych=%s
        """
        self.cursor.execute(update, (name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate, id))
        self.connection.commit()


    """
    def delete(self, id):
        self.cursor.execute("DELETE FROM dane_osobowe WHERE id_danych=%s", (id,))
        self.connection.commit()
    """

    
