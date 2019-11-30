import tkinter
import backend


def view_command():
    listbox.delete(0, tkinter.END)
    for row in backend.view():
        listbox.insert(tkinter.END, row)

def search_command():
    listbox.delete(0, tkinter.END)
    for row in backend.search(pesel.get()):
        listbox.insert(tkinter.END, row)

def add_command():
    backend.insert(name.get(), surname.get(), birthDate.get(), birthCountry.get(), sex.get(), pesel.get())
    listbox.delete(0, tkinter.END)
    listbox.insert(tkinter.END, (name.get(), surname.get(), birthDate.get(), birthCountry.get(), sex.get(), pesel.get()))

window = tkinter.Tk()

window.title("Humans database")
window.resizable(0, 0)
window.geometry('700x180')

# labels:
labelName = tkinter.Label(window, text="Name:")
labelName.grid(row=0, column=0)
labelSurname = tkinter.Label(window, text="Surname:")
labelSurname.grid(row=0, column=2)
labelDate = tkinter.Label(window, text="Date of birth:")
labelDate.grid(row=0, column=4)
labelCountry = tkinter.Label(window, text="Country of birth:")
labelCountry.grid(row=1, column=0)
labelSex = tkinter.Label(window, text="Sex:")
labelSex.grid(row=1, column=2)
labelPesel = tkinter.Label(window, text="PESEL:")
labelPesel.grid(row=1, column=4)

# entries:
name = tkinter.StringVar()
entryName = tkinter.Entry(window, textvariable=name)
entryName.grid(row=0, column=1)
surname = tkinter.StringVar()
entrySurname = tkinter.Entry(window, textvariable=surname)
entrySurname.grid(row=0, column=3)
birthDate = tkinter.StringVar()
entryBirthDate = tkinter.Entry(window, textvariable=birthDate)
entryBirthDate.grid(row=0, column=5)
birthCountry = tkinter.StringVar()
entryBirthCountry = tkinter.Entry(window, textvariable=birthCountry)
entryBirthCountry.grid(row=1, column=1)
sex = tkinter.StringVar()
entrySex = tkinter.Entry(window, textvariable=sex)
entrySex.grid(row=1, column=3)
pesel = tkinter.StringVar()
entryPesel = tkinter.Entry(window, textvariable=pesel)
entryPesel.grid(row=1, column=5)

# listbox:
listbox = tkinter.Listbox(window, height=6, width=110)
listbox.grid(row=2, column=0, columnspan=6)

# scrollbar
scrollbar = tkinter.Scrollbar(window)
scrollbar.grid(row=2, column=6)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# buttons:
buttonViewAll = tkinter.Button(window, text="View all", width=12, command=view_command)
buttonViewAll.grid(row=3, column=0)
buttonSearch = tkinter.Button(window, text="Search PESEL", width=12, command=search_command)
buttonSearch.grid(row=3, column=1)
buttonAdd = tkinter.Button(window, text="Add entry", width=12, command=add_command)
buttonAdd.grid(row=3, column=2)
buttonUpdate = tkinter.Button(window, text="Update", width=12)
buttonUpdate.grid(row=3, column=3)
buttonDelete = tkinter.Button(window, text="Delete", width=12)
buttonDelete.grid(row=3, column=4)
buttonClose = tkinter.Button(window, text="Close", width=12)
buttonClose.grid(row=3, column=5)




window.mainloop()