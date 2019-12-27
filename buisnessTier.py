from databaseTier import Database

database = Database()

class Buisness:

    def view_command(self):
        return database.view()

    def search_command(self, pesel, name, surname):
        return database.search(pesel, name, surname)

    def add_command(self, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        database.insert(name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate)

    def update_command(self, id, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate):
        database.update(id, name, surname, father, mother, birthDate, birthCity, birthCountry, sex, pesel, state, nationality, address, country, countryPriev, deathDate)

    def get_countries(self):
        return database.combobox_countries_input()

    def get_states(self):
        return database.combobox_states_input()

    def get_sex(self):
        return ('K', 'M')

    def show_history_command(self, id):
        return database.view_history(id)