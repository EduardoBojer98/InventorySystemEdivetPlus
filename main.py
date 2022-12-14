import dataclasses
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

from businesslogic import ItemService


# from operations import CRUDOP


class MainFrame:
    def __init__(self, root):
        self.item_service = ItemService()

        self.root = root
        self.root.geometry("1350x700+10+10")
        self.root.title("Sistem za proizvode EdivetPlus | SI 6/17")
        self.my_tree = ttk.Treeview(root)

        # ============Variables
        self.var_searchType = StringVar()
        self.var_searchtxt = StringVar()

        self.var_itemID = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_quantity = StringVar()
        self.var_manufacturer = StringVar()
        # =========================naslov programa
        title = Label(self.root, text="EdivetPlus", font=('Arial Bold', 25), bg="#67B7D1", fg='white', anchor="w",
                      padx=20)
        title.place(x=0, y=0, relwidth=1, height=60)

        btn_logout = Button(self.root,command=self.logout, text="Odjava", font=("Arial", 15), bg='red', fg='white', cursor='hand2')
        btn_logout.place(x=1200, y=15, height=35, width=120)

        # ===================Search fildovi
        SearchFrame = LabelFrame(self.root, text="search Item", font=('Arial', 15), bg='#67B7D1', bd=2, relief=RIDGE)
        SearchFrame.place(x=400, y=0, width=600, height=60)

        sel_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchType,
                                  values=("Izaberi", "Ime", "Proizvodjac"), state='readonly',
                                  justify=CENTER, font=('Arial', 15))
        sel_search.place(x=5, y=0, width=180)
        sel_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=('Arial', 15), bg='white')
        txt_search.place(x=200, y=0)

        btn_search = Button(SearchFrame, command=self.search, text="Pretraga", font=('Arial', 15), bg="#EEEEEE",
                            fg='black', cursor='hand2')
        btn_search.place(x=450, y=0, width=120, height=30)

        # ============================imena fildova za imput
        namelabel = Label(self.root, text="Ime", font=('Arial', 15))
        pricelabel = Label(self.root, text="Cena", font=('Arial', 15))
        quantitylabel = Label(self.root, text="Kolicina", font=('Arial', 15))
        manufacturerlabel = Label(self.root, text="Proizvodjac", font=('Arial', 15))
        namelabel.place(x=50, y=150, height=50, width=150)
        pricelabel.place(x=50, y=200, height=50, width=150)
        quantitylabel.place(x=50, y=250, height=50, width=150)
        manufacturerlabel.place(x=50, y=300, height=50, width=150)

        # =====================fildovi za imput podataka
        nameEntry = Entry(self.root, textvariable=self.var_name, width=55, bd=5, font=('Arial', 15))
        priceEntry = Entry(self.root, textvariable=self.var_price, width=55, bd=5, font=('Arial', 15))
        quantityEntry = Entry(self.root, textvariable=self.var_quantity, width=55, bd=5, font=('Arial', 15))
        manufacturerEntry = Entry(self.root, textvariable=self.var_manufacturer, width=55, bd=5, font=('Arial', 15))
        nameEntry.place(x=200, y=150, height=50, width=400)
        priceEntry.place(x=200, y=200, height=50, width=400)
        quantityEntry.place(x=200, y=250, height=50, width=400)
        manufacturerEntry.place(x=200, y=300, height=50, width=400)
        # =================buttons za dodavalje obrisanje itd
        addBtn = Button(self.root, command=self.add, text="Dodaj", padx=65, pady=25, width=10, bd=5, font=('Arial', 15),
                        bg="#84F894")
        addBtn.place(x=750, y=100)
        deleteBtn = Button(self.root, command=self.delete, text="Obrisi", padx=65, pady=25, width=10, bd=5,
                           font=('Arial', 15), bg="#FF9999")
        deleteBtn.place(x=750, y=200)
        updateBtn = Button(self.root, command=self.update, text="Azuriraj", padx=65, pady=25, width=10, bd=5,
                           font=('Arial', 15), bg="#84E8F8")
        updateBtn.place(x=1050, y=100)
        resetBtn = Button(self.root, command=self.clear, text="Cisti", padx=65, pady=25, width=10, bd=5,
                          font=('Arial', 15), bg="#F398FF")
        resetBtn.place(x=1050, y=200)

        # =============show data table=======================================
        item_frame = Frame(self.root, bd=3, relief=RIDGE)
        item_frame.place(x=0, y=380, relwidth=1, height=315)

        scrolly = Scrollbar(item_frame, orient=VERTICAL)

        self.ItemTable = ttk.Treeview(item_frame, columns=("ID", "Name", "Price", "Quantity", "Manufacturer"),
                                      yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.ItemTable.yview)

        self.ItemTable["show"] = 'headings'

        self.ItemTable.heading("ID", text='Sifra')
        self.ItemTable.heading("Name", text='Ime')
        self.ItemTable.heading("Price", text='Cena')
        self.ItemTable.heading("Quantity", text='Kolicina')
        self.ItemTable.heading("Manufacturer", text='Proizvodjac')

        self.ItemTable.column("ID", width=90)
        self.ItemTable.column("Name", width=100)
        self.ItemTable.column("Price", width=100)
        self.ItemTable.column("Quantity", width=100)
        self.ItemTable.column("Manufacturer", width=100)
        self.ItemTable.pack(fill=BOTH, expand=1)
        self.ItemTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # =============================add method
    def add(self):
        try:
            self.item_service.add_item(
                self.var_name.get(), self.var_price.get(), self.var_quantity.get(), self.var_manufacturer.get())
            messagebox.showinfo('Uspesno', "Proizvod dodat uspesno", parent=self.root)
            self.show()
        except Exception as e:
            messagebox.showerror("Greska", str(e), parent=self.root)

    # =========================show data method
    def show(self):
        self.ItemTable.delete(*self.ItemTable.get_children())
        items = self.item_service.get_all()
        for item in items:
            self.ItemTable.insert('', END, values=dataclasses.astuple(item))

    # ====================get data method
    def get_data(self, ev):
        f = self.ItemTable.focus()
        content = (self.ItemTable.item(f))
        row = content['values']
        self.var_itemID.set(row[0])
        self.var_name.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.var_manufacturer.set(row[4])

    # =========================update data method
    def update(self):
        try:
            self.item_service.update(int(self.var_itemID.get()), self.var_name.get(), self.var_price.get(), self.var_quantity.get(), self.var_manufacturer.get())
            messagebox.showinfo('Uspesno', "Proizvod azuriran uspesno", parent=self.root)
            self.show()
        except Exception as e:
            messagebox.showerror("Greska", str(e), parent=self.root)

    # =====================delete data method

    def delete(self):
        try:
            self.item_service.delete(int(self.var_itemID.get()))
            messagebox.showinfo("Obrisi", "Proizvod je uspesno obrisan", parent=self.root)
            self.show()
            self.clear()
        except Exception as e:
            messagebox.showerror("Greska", str(e), parent=self.root)

    def clear(self):
        self.var_itemID.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_manufacturer.set("")
        self.var_searchType.set("Izaberi")
        self.show()

    def search(self):
        self.ItemTable.delete(*self.ItemTable.get_children())
        items = self.item_service.get_all()
        for item in items:
            print(item)
            self.ItemTable.insert('', END, values=dataclasses.astuple(item))

        if self.var_searchType.get() == "Izaberi":
            messagebox.showerror("Greska", "Izaberite opciju za pretragu", parent=self.root)
            return

        self.ItemTable.delete(*self.ItemTable.get_children())
        items = self.item_service.search(self.var_searchType.get(), self.var_searchtxt.get())
        for item in items:
            self.ItemTable.insert('', END, values=dataclasses.astuple(item))

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


root = Tk()
obj = MainFrame(root)
root.mainloop()
