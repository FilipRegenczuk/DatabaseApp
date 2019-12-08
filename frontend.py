import tkinter
from backend import Database


database = Database("testDB.db")

class Window(object):

    def __init__(self, window):
        self.window = window

        # window features:
        window.title("Dział Ewidencji Ludności")
        window.resizable(0, 0)
        window.geometry('1100x280')

        # LABELS:
        # 0. row
        labelName = tkinter.Label(window, text="Imię:")
        labelName.grid(row=0, column=0)
        labelSurname = tkinter.Label(window, text="Nazwisko:")
        labelSurname.grid(row=0, column=2)
        labelFather = tkinter.Label(window, text="Imię i nazwisko rodowe ojca:")
        labelFather.grid(row=0, column=4)
        labelMother = tkinter.Label(window, text="Imię i nazwisko rodowe matki:")
        labelMother.grid(row=0, column=6)
        # 1. row
        labelBirthDate = tkinter.Label(window, text="Data urodzenia:")
        labelBirthDate.grid(row=1, column=0)
        labelBirthCity = tkinter.Label(window, text="Miejsce urodzenia:")
        labelBirthCity.grid(row=1, column=2)
        labelBirthCountry = tkinter.Label(window, text="Kraj pochodzenia:")
        labelBirthCountry.grid(row=1, column=4)
        labelSex = tkinter.Label(window, text="Płeć:")
        labelSex.grid(row=1, column=6)
        # 2. row
        labelPesel = tkinter.Label(window, text="Numer PESEL:")
        labelPesel.grid(row=2, column=0)
        labelStatus = tkinter.Label(window, text="Stan cywilny:")
        labelStatus.grid(row=2, column=2)
        labelNationality = tkinter.Label(window, text="Obywatelstwo:")
        labelNationality.grid(row=2, column=4)
        labelAddress = tkinter.Label(window, text="Adres zameldowania:")
        labelAddress.grid(row=2, column=6)
        # 3. row
        labelCountry = tkinter.Label(window, text="Kraj zamieszkania:")
        labelCountry.grid(row=3, column=0)
        labelCountryPriev = tkinter.Label(window, text="Kraj poprzedniego zamieszkania:")
        labelCountryPriev.grid(row=3, column=2)
        labelDeathDate = tkinter.Label(window, text="Data zgonu:")
        labelDeathDate.grid(row=3, column=4)
        # 4. row
        labelChangeDate = tkinter.Label(window, text="Data zmiany:")
        labelChangeDate.grid(row=4, column=0)
        labelChangeTime = tkinter.Label(window, text="Godzina zmiany:")
        labelChangeTime.grid(row=4, column=2)


        # ENTRIES:
        # 0. row
        self.name = tkinter.StringVar()
        self.entryName = tkinter.Entry(window, textvariable=self.name)
        self.entryName.grid(row=0, column=1)
        self.surname = tkinter.StringVar()
        self.entrySurname = tkinter.Entry(window, textvariable=self.surname)
        self.entrySurname.grid(row=0, column=3)
        self.father = tkinter.StringVar()
        self.entryFather = tkinter.Entry(window, textvariable=self.father)
        self.entryFather.grid(row=0, column=5)
        self.mother = tkinter.StringVar()
        self.entryMother = tkinter.Entry(window, textvariable=self.mother)
        self.entryMother.grid(row=0, column=7)
        # 1. row
        self.birthDate = tkinter.StringVar()
        self.entryBirthDate = tkinter.Entry(window, textvariable=self.birthDate)
        self.entryBirthDate.grid(row=1, column=1)
        self.birthCity = tkinter.StringVar()
        self.entryBirthCity = tkinter.Entry(window, textvariable=self.birthCity)
        self.entryBirthCity.grid(row=1, column=3)
        self.birthCountry = tkinter.StringVar()
        self.entryBirthCountry = tkinter.Entry(window, textvariable=self.birthCountry)
        self.entryBirthCountry.grid(row=1, column=5)
        self.sex = tkinter.StringVar()
        self.entrySex = tkinter.Entry(window, textvariable=self.sex)
        self.entrySex.grid(row=1, column=7)
        # 2. row
        self.pesel = tkinter.StringVar()
        self.entryPesel = tkinter.Entry(window, textvariable=self.pesel)
        self.entryPesel.grid(row=2, column=1)
        self.state = tkinter.StringVar()
        self.entryState = tkinter.Entry(window, textvariable=self.state)
        self.entryState.grid(row=2, column=3)
        self.nationality = tkinter.StringVar()
        self.entryNationality = tkinter.Entry(window, textvariable=self.nationality)
        self.entryNationality.grid(row=2, column=5)
        self.address = tkinter.StringVar()
        self.entryAddress = tkinter.Entry(window, textvariable=self.address)
        self.entryAddress.grid(row=2, column=7)
        # 3. row
        self.country = tkinter.StringVar()
        self.entryCountry = tkinter.Entry(window, textvariable=self.country)
        self.entryCountry.grid(row=3, column=1)
        self.countryPriev = tkinter.StringVar()
        self.entryCountryPriev = tkinter.Entry(window, textvariable=self.countryPriev)
        self.entryCountryPriev.grid(row=3, column=3)
        self.deathDate = tkinter.StringVar()
        self.entryDeathDate = tkinter.Entry(window, textvariable=self.deathDate)
        self.entryDeathDate.grid(row=3, column=5)
        # 4. row
        self.changeDate = tkinter.StringVar()
        self.entryChangeDate = tkinter.Entry(window, textvariable=self.changeDate)
        self.entryChangeDate.grid(row=4, column=1)
        self.changeTime = tkinter.StringVar()
        self.entryChangeTime = tkinter.Entry(window, textvariable=self.changeTime)
        self.entryChangeTime.grid(row=4, column=3)

        # listbox:
        self.listbox = tkinter.Listbox(window, height=8, width=180)
        self.listbox.grid(row=5, column=0, columnspan=8)

        # scrollbar
        self.scrollbar = tkinter.Scrollbar(window)
        self.scrollbar.grid(row=5, column=8)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)


        # bind
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        # buttons:
        buttonViewAll = tkinter.Button(window, text="View all", width=12, command=self.view_command)
        buttonViewAll.grid(row=6, column=0)
        buttonSearch = tkinter.Button(window, text="Search PESEL", width=12, command=self.search_command)
        buttonSearch.grid(row=6, column=1)
        buttonAdd = tkinter.Button(window, text="Add entry", width=12, command=self.add_command)
        buttonAdd.grid(row=6, column=2)
        buttonUpdate = tkinter.Button(window, text="Update", width=12, command=self.update_command)
        buttonUpdate.grid(row=6, column=3)
        buttonDelete = tkinter.Button(window, text="Delete", width=12, command=self.delete_command)
        buttonDelete.grid(row=6, column=4)
        buttonClose = tkinter.Button(window, text="Close", width=12, command=window.destroy)
        buttonClose.grid(row=6, column=5)



    # This function is used to return id of selected row. 
    # Futhermore it prints selected row in labels.
    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.listbox.curselection()[0]
            selected_tuple = self.listbox.get(index)
            self.entryName.delete(0, tkinter.END)
            self.entryName.insert(tkinter.END, selected_tuple[1])
            self.entrySurname.delete(0, tkinter.END)
            self.entrySurname.insert(tkinter.END, selected_tuple[2])
            self.entryBirthDate.delete(0, tkinter.END)
            self.entryBirthDate.insert(tkinter.END, selected_tuple[3])
            self.entryBirthCountry.delete(0, tkinter.END)
            self.entryBirthCountry.insert(tkinter.END, selected_tuple[4])
            self.entrySex.delete(0, tkinter.END)
            self.entrySex.insert(tkinter.END, selected_tuple[5])
            self.entryPesel.delete(0, tkinter.END)
            self.entryPesel.insert(tkinter.END, selected_tuple[6])
        except IndexError:
            pass

    def view_command(self):
        self.listbox.delete(0, tkinter.END)
        for row in database.view():
            self.listbox.insert(tkinter.END, row)

    def search_command(self):
        self.listbox.delete(0, tkinter.END)
        for row in database.search(self.pesel.get()):
            self.listbox.insert(tkinter.END, row)

    def add_command(self):
        database.insert(self.name.get(), self.surname.get(), self.birthDate.get(), self.birthCountry.get(), self.sex.get(), self.pesel.get())
        self.listbox.delete(0, tkinter.END)
        self.listbox.insert(tkinter.END, (self.name.get(), self.surname.get(), self.birthDate.get(), self.birthCountry.get(), self.sex.get(), self.pesel.get()))

    def update_command(self):
        database.update(selected_tuple[0], self.name.get(), self.surname.get(), self.birthDate.get(), self.birthCountry.get(), self.sex.get(), self.pesel.get())

    def delete_command(self):
        database.delete(selected_tuple[0])
    


window = tkinter.Tk()
Window(window)
window.mainloop()