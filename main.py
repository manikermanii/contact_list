from contact import Contact
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title("دفترچه مخاطبین")
window.geometry("750x350")



contact_list = []

def save_click():
    name = name.get()
    family = family.get()
    title = email.get()
    number = address.get()

    contact = Contact(name, family, title, number)
    contact_list.append(contact)

    table.insert(parent="", index=END, values=tuple(contact.to_tuple()))

    messagebox.showinfo(title="INFO", message="CONTACT SAVED")

    name.set("")
    family.set("")
    email.set("")
    address.set("")



