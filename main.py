import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


# from operations import CRUDOP


class MainFrame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+10+10")
        self.root.title("Inventory System EdivetPlus | SI6/17")
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
        title = Label(self.root, text="IMS EdivetPlus", font=('Arial Bold', 25), bg="#67B7D1", fg='white', anchor="w",
                      padx=20)
        title.place(x=0, y=0, relwidth=1, height=60)

        btn_logout = Button(self.root,command=self.logout, text="Logout", font=("Arial", 15), bg='red', fg='white', cursor='hand2')
        btn_logout.place(x=1200, y=15, height=35, width=120)

        # ===================Search fildovi
        SearchFrame = LabelFrame(self.root, text="search Item", font=('Arial', 15), bg='#67B7D1', bd=2, relief=RIDGE)
        SearchFrame.place(x=400, y=0, width=600, height=60)

        sel_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchType,
                                  values=("Select", "Name", "Manufacturer"), state='readonly',
                                  justify=CENTER, font=('Arial', 15))
        sel_search.place(x=5, y=0, width=180)
        sel_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=('Arial', 15), bg='white')
        txt_search.place(x=200, y=0)

        btn_search = Button(SearchFrame, command=self.search, text="Search", font=('Arial', 15), bg="#EEEEEE",
                            fg='black', cursor='hand2')
        btn_search.place(x=450, y=0, width=120, height=30)

        # ============================imena fildova za imput
        idlabel = Label(self.root, text="ItemID", font=('Arial', 15))
        namelabel = Label(self.root, text="Name", font=('Arial', 15))
        pricelabel = Label(self.root, text="Price", font=('Arial', 15))
        quantitylabel = Label(self.root, text="Quantity", font=('Arial', 15))
        manufacturerlabel = Label(self.root, text="Manufacturer", font=('Arial', 15))
        idlabel.place(x=50, y=100, height=50, width=150)
        namelabel.place(x=50, y=150, height=50, width=150)
        pricelabel.place(x=50, y=200, height=50, width=150)
        quantitylabel.place(x=50, y=250, height=50, width=150)
        manufacturerlabel.place(x=50, y=300, height=50, width=150)

        # =====================fildovi za imput podataka
        itemEntry = Entry(self.root, textvariable=self.var_itemID, width=55, bd=5, font=('Arial', 15))
        nameEntry = Entry(self.root, textvariable=self.var_name, width=55, bd=5, font=('Arial', 15))
        priceEntry = Entry(self.root, textvariable=self.var_price, width=55, bd=5, font=('Arial', 15))
        quantityEntry = Entry(self.root, textvariable=self.var_quantity, width=55, bd=5, font=('Arial', 15))
        manufacturerEntry = Entry(self.root, textvariable=self.var_manufacturer, width=55, bd=5, font=('Arial', 15))
        itemEntry.place(x=200, y=100, height=50, width=400)
        nameEntry.place(x=200, y=150, height=50, width=400)
        priceEntry.place(x=200, y=200, height=50, width=400)
        quantityEntry.place(x=200, y=250, height=50, width=400)
        manufacturerEntry.place(x=200, y=300, height=50, width=400)
        # =================buttons za dodavalje obrisanje itd
        addBtn = Button(self.root, command=self.add, text="Add", padx=65, pady=25, width=10, bd=5, font=('Arial', 15),
                        bg="#84F894")
        addBtn.place(x=750, y=100)
        deleteBtn = Button(self.root, command=self.delete, text="Delete", padx=65, pady=25, width=10, bd=5,
                           font=('Arial', 15), bg="#FF9999")
        deleteBtn.place(x=750, y=200)
        updateBtn = Button(self.root, command=self.update, text="Update", padx=65, pady=25, width=10, bd=5,
                           font=('Arial', 15), bg="#84E8F8")
        updateBtn.place(x=1050, y=100)
        resetBtn = Button(self.root, command=self.clear, text="Clear", padx=65, pady=25, width=10, bd=5,
                          font=('Arial', 15), bg="#F398FF")
        resetBtn.place(x=1050, y=200)

        # =============show data table=======================================
        item_frame = Frame(self.root, bd=3, relief=RIDGE)
        item_frame.place(x=0, y=380, relwidth=1, height=315)

        scrolly = Scrollbar(item_frame, orient=VERTICAL)

        self.ItemTable = ttk.Treeview(item_frame, columns=("ItemID", "Name", "Price", "Quantity", "Manufacturer"),
                                      yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.ItemTable.yview)

        self.ItemTable["show"] = 'headings'

        self.ItemTable.heading("ItemID", text='ID')
        self.ItemTable.heading("Name", text='Name')
        self.ItemTable.heading("Price", text='Price')
        self.ItemTable.heading("Quantity", text='Quantity')
        self.ItemTable.heading("Manufacturer", text='Manufacturer')

        self.ItemTable.column("ItemID", width=90)
        self.ItemTable.column("Name", width=100)
        self.ItemTable.column("Price", width=100)
        self.ItemTable.column("Quantity", width=100)
        self.ItemTable.column("Manufacturer", width=100)
        self.ItemTable.pack(fill=BOTH, expand=1)
        self.ItemTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # =============================add method
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_itemID.get() == "":
                messagebox.showerror("Error", "Item ID must be required", parent=self.root)
            else:
                cur.execute("Select * from items where itemID=?", (self.var_itemID.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This item ID already assigned, try diffrent", parent=self.root)
                else:
                    cur.execute("Insert into items (ItemID,Name,Price,Quantity,Manufacturer) values(?,?,?,?,?)", (
                        self.var_itemID.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_manufacturer.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', "Item added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # =========================show data method
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from items")
            rows = cur.fetchall()
            self.ItemTable.delete(*self.ItemTable.get_children())
            for row in rows:
                self.ItemTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

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
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_itemID.get() == "":
                messagebox.showerror("Error", "Item ID must be required", parent=self.root)
            else:
                cur.execute("Select * from items where itemID=?", (self.var_itemID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "This item ID is invalid", parent=self.root)
                else:
                    cur.execute("Update items set Name=?,Price=?,Quantity=?,Manufacturer=? where ItemID=?", (
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_manufacturer.get(),
                        self.var_itemID.get(),
                    ))
                    con.commit()
                    messagebox.showinfo('Success', "Item updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # =====================delete data method

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_itemID.get() == "":
                messagebox.showerror("Error", "Item ID must be required", parent=self.root)
            else:
                cur.execute("Select * from items where itemID=?", (self.var_itemID.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "This item ID is invalid", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute('delete from items where itemID=?', (self.var_itemID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Item deleted successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_itemID.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_quantity.set("")
        self.var_manufacturer.set("")
        self.var_searchType.set("Select")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchType.get() == "Select":
                messagebox.showerror("Error", "Selector search my option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute(
                    "select * from items where " + self.var_searchType.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.ItemTable.delete(*self.ItemTable.get_children())
                    for row in rows:
                        self.ItemTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def logout(self):
        self.root.destroy()
        os.system("python login.py")


root = Tk()
obj = MainFrame(root)
root.mainloop()
