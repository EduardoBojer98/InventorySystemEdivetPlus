import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Inventory system for EDIVET+")
root.geometry('1030x380')
my_tree = ttk.Treeview(root)
storeName = 'EdivetPlus'

titleLabel = Label(root,text=storeName, font=('Arial bold',30),bd=2)
titleLabel.grid(row=0,column=0,columnspan=8,padx=20,pady=20)

#imena fildova
idLabel =Label(root,text="ID",font=("Arial bold",15))
nameLabel =Label(root,text="Name",font=("Arial bold",15))
priceLabel =Label(root,text="Price",font=("Arial bold",15))
quantityLabel =Label(root,text="Quantity",font=("Arial bold",15))
idLabel.grid(row=1,column=0,padx=10,pady=10)
nameLabel.grid(row=2,column=0,padx=10,pady=10)
priceLabel.grid(row=3,column=0,padx=10,pady=10)
quantityLabel.grid(row=4,column=0,padx=10,pady=10)

#unos podataka
entryId=Entry(root,width=25,bd=5,font=("Arial bold",15))
entryName=Entry(root,width=25,bd=5,font=("Arial bold",15))
entryPrice=Entry(root,width=25,bd=5,font=("Arial bold",15))
entryQuantity = Entry(root,width=25,bd=5,font=("Arial bold",15))
entryId.grid(row=1,column=1,columnspan=3,padx=5,pady=5)
entryName.grid(row=2,column=1,columnspan=3,padx=5,pady=5)
entryPrice.grid(row=3,column=1,columnspan=3,padx=5,pady=5)
entryQuantity.grid(row=4,column=1,columnspan=3,padx=5,pady=5)

buttonEnter=Button(
    root,text="Enter",padx=5,pady=5,width=5,bd=3,font=("Arial bold",15),bg="#00FF00"
)
buttonEnter.grid(row=5,column=1,columnspan=1)

buttonUpdate=Button(
    root,text="Update",padx=5,pady=5,width=5,bd=3,font=("Arial bold",15),bg="#0000FF"
)
buttonUpdate.grid(row=5,column=2,columnspan=1)

buttonDelete=Button(
    root,text="Delete",padx=5,pady=5,width=5,bd=3,font=("Arial bold",15),bg="#ff0000"
)
buttonDelete.grid(row=5,column=3,columnspan=1)

style=ttk.Style()
style.configure("Treeview.Heading",font=("Arial bold",15))

my_tree['columns']=("ID","Name","Price","Quantity")
my_tree.column("#0",width=0, stretch=NO)
my_tree.column("ID",anchor=W,width=100)
my_tree.column("Name",anchor=W,width=200)
my_tree.column("Price",anchor=W,width=150)
my_tree.column("Quantity",anchor=W,width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

my_tree.tag_configure("grow",background="#EEEEEE",font=("Arial bold",15))
my_tree.grid(row=1,column=5,columnspan=4,rowspan=5,padx=10,pady=10)


root.mainloop()