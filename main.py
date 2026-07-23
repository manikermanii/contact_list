from contact import Contact

from tkinter import *
from tkinter import messagebox
from tkinter import ttk



contact_list = []


def save_click():
    contact = Contact(name.get(), family.get(), title.get(), number.get())
    

    contact_list.append(contact)

    table.insert(
        parent="",
        index=END,
        values=tuple(contact.to_tuple())
    )

    messagebox.showinfo(
        title="INFO",
        message="CONTACT SAVED"
    )

    name.set("")
    phone.set("")
    email.set("")
    address.set("")


window = Tk()
window.title("دفترچه مخاطبین")
window.geometry("750x350")



menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")



Label(window, text="نام مخاطب").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=90, y=20)



Label(window, text="شماره تلفن").place(x=20, y=60)
phone = StringVar()
Entry(window, textvariable=phone).place(x=90, y=60)



Label(window, text="ایمیل").place(x=20, y=100)
email = StringVar()
Entry(window, textvariable=email).place(x=90, y=100)



Label(window, text="آدرس").place(x=20, y=140)
address = StringVar()
Entry(window, textvariable=address).place(x=90, y=140)




table = ttk.Treeview(
    window,
    height=12,
    columns=[1, 2, 3, 4],
    show="headings"
)



table.column(1, width=120)
table.column(2, width=120)
table.column(3, width=150)
table.column(4, width=120)



table.heading(1, text="نام مخاطب")
table.heading(2, text="شماره تلفن")
table.heading(3, text="ایمیل")
table.heading(4, text="آدرس")



table.place(
    x=230,
    y=20,
    width=500,
    height=250
)




Button(
    window,
    width=10,
    text="ذخیره",
    command=save_click
).place(x=80, y=190)


window.mainloop()