import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# gui
root = Tk()
root.title("Inventory System EdivetPlus")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)

label = Label(root, text="Inventory System EdivetPlus", font=('Arial Bold', 25))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

idlabel = Label(root, text="ItemID", font=('Arial', 15))
namelabel = Label(root, text="Name", font=('Arial', 15))
pricelabel = Label(root, text="Price", font=('Arial', 15))
quantitylabel = Label(root, text="Quantity", font=('Arial', 15))
manufacturerlabel = Label(root, text="Manufacturer", font=('Arial', 15))

idlabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
namelabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
pricelabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
quantitylabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
manufacturerlabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

itemEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
priceEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
quantityEntry = Entry(root, width=55, bd=5, font=('Arial', 15))
manufacturerEntry = Entry(root, width=55, bd=5, font=('Arial', 15))

itemEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
manufacturerEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(root, text="Add", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84F894")
updateBtn = Button(root, text="Update", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84E8F8")
deleteBtn = Button(root, text="Delete", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#FF9999")
searchBtn = Button(root, text="Search", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#F4FE82")
resetBtn = Button(root, text="Reset", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#F398FF")
selectBtn = Button(root, text="Select", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#EEEEEE")

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))
my_tree['columns'] = ("ID", "Name", "Price", "Quantity", "Manufacturer")
my_tree.column('#0', width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=170)
my_tree.column("Name", anchor=W, width=150)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=165)
my_tree.column("Manufacturer", anchor=W, width=150)

my_tree.heading("ID", text="Item ID", anchor=W)
my_tree.heading("Name", text="Item Name", anchor=W)
my_tree.heading("Price", text="Item Price", anchor=W)
my_tree.heading("Quantity", text="Item Quantity", anchor=W)
my_tree.heading("Manufacturer", text="Item Manufacturer", anchor=W)

root.mainloop()
