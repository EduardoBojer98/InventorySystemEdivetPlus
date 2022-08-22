import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from operations import CRUDOP


class MainFrame:
    crud=
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+10+10")
        self.root.title("Inventory System EdivetPlus | SI6/17")
        self.my_tree = ttk.Treeview(root)

        title = Label(self.root, text="IMS EdivetPlus", font=('Arial Bold', 25), bg="#67B7D1", fg='white', anchor="w",padx=20).place(x=0, y=0, relwidth=1, height=60)

        btn_logout = Button(self.root, text="Logout", font=("Arial", 15), bg='red', fg='white', cursor='hand2').place(x=1200, y=15, height=35, width=120)

        self.idlabel = Label(self.root, text="ItemID", font=('Arial', 15))
        self.namelabel = Label(self.root, text="Name", font=('Arial', 15))
        self.pricelabel = Label(self.root, text="Price", font=('Arial', 15))
        self.quantitylabel = Label(self.root, text="Quantity", font=('Arial', 15))
        self.manufacturerlabel = Label(self.root, text="Manufacturer", font=('Arial', 15))
        self.idlabel.place(x=50, y=100, height=50, width=150)
        self.namelabel.place(x=50, y=150, height=50, width=150)
        self.pricelabel.place(x=50, y=200, height=50, width=150)
        self.quantitylabel.place(x=50, y=250, height=50, width=150)
        self.manufacturerlabel.place(x=50, y=300, height=50, width=150)

        self.itemEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
        self.nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
        self.priceEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
        self.quantityEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
        self.manufacturerEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
        self.itemEntry.place(x=200, y=100, height=50, width=400)
        self.nameEntry.place(x=200, y=150, height=50, width=400)
        self.priceEntry.place(x=200, y=200, height=50, width=400)
        self.quantityEntry.place(x=200, y=250, height=50, width=400)
        self.manufacturerEntry.place(x=200, y=300, height=50, width=400)

        self.addBtn = Button(root, text="Add", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84F894")
        self.addBtn.place(x=750, y=70)
        self.deleteBtn = Button(root, text="Delete", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#FF9999")
        self.deleteBtn.place(x=750, y=170)
        self.searchBtn = Button(root, text="Search", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#F4FE82")
        self.searchBtn.place(x=750, y=270)
        self.updateBtn = Button(root, text="Update", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84E8F8")
        self.updateBtn.place(x=1050, y=70)
        self.resetBtn = Button(root, text="Reset", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#F398FF")
        self.resetBtn.place(x=1050, y=170)
        self.selectBtn = Button(root, text="Select", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#EEEEEE")
        self.selectBtn.place(x=1050, y=270)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Arial Bold', 15))
        self.my_tree['columns'] = ("ID", "Name", "Price", "Quantity", "Manufacturer")
        self.my_tree.column('#0', width=0, stretch=NO)
        self.my_tree.column("ID", anchor=W, width=170)
        self.my_tree.column("Name", anchor=W, width=150)
        self.my_tree.column("Price", anchor=W, width=150)
        self.my_tree.column("Quantity", anchor=W, width=165)
        self.my_tree.column("Manufacturer", anchor=W, width=150)
        self.my_tree.heading("ID", text="Item ID", anchor=W)
        self.my_tree.heading("Name", text="Item Name", anchor=W)
        self.my_tree.heading("Price", text="Item Price", anchor=W)
        self.my_tree.heading("Quantity", text="Item Quantity", anchor=W)
        self.my_tree.heading("Manufacturer", text="Item Manufacturer", anchor=W)

        refreshTable(self.my_tree)


root = Tk()
obj = MainFrame(root)
root.mainloop()
