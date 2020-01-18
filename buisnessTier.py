""" BusinessTier module is responsible for transactions, flow of data and services """

from databaseTier import Database

database = Database()

class Buisness:

    # The method is returning a view of all people in DB
    def view_command(self):
        return database.view()

    # The method is returning a view of the person, who is searched in DB
    def search_command(self, pesel, name, surname):
        return database.search(pesel, name, surname)

    # The method is adding a new person into DB
    def add_command(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        database.insert(name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate)

    # The method is updating selected person in DB 
    def update_command(self, id, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        database.update(id, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate)

    # The method is returning a list of countries in DB
    def get_countries(self):
        return database.combobox_countries_input()

    # The method is returning a list of states in DB
    def get_states(self):
        return database.combobox_states_input()

    # The method is returning sexes
    def get_sex(self):
        return ('K', 'M')

    # The method is returning a list of 
    def get_services(self):
        return database.combobox_services_input()

    # The method is returning a history of selected person
    def show_history_command(self, id):
        return database.view_history(id)

    # The method is saving a proposal from client to a txt file
    def save_proposal_command(self, pesel, name, surname, service, newData):
        fileName = pesel.get() + ".txt"
        file = open(fileName, 'w')
        file.write(name.get() + "\n" + surname.get() + "\n" + service.get() + "\n" + newData.get())
        file.close()

    def get_user(self):
        return ("Pracownik", "Klient")

    def check_password(self, user, password):
        if user.get() == "Pracownik" and password.get() == "Pracownik":
            return "pracownik"
        if user.get() == "Klient" and password.get() == "Klient":
            return "klient"
        else:
            return "wrong"

