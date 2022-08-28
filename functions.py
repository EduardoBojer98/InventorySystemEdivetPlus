import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from main import MainFrame


class op:

    ###################### loginuj se
    def login(self,username,password):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if username == "" or password == "":
                messagebox.showerror("Greska", "Sva polja su potrebna", parent=self.root)
            else:
                cur.execute("select * from users where Name=? AND password=?",(username, password))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Greska", "Pogresno", parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python main.py")
        except Exception as ex:
            messagebox.showerror("Greska", f"greska od : {str(ex)}", parent=self.root)

    ########################## Dodaj korisnika
    def adduser(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.userID.get() == "":
                messagebox.showerror("Greska", "ID je potreban", parent=self.root)
            else:
                cur.execute("Select * from users where userID=?", (self.userID.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Greska", "Ovaj ID je vec koriscen stavi drugi", parent=self.root)
                else:
                    cur.execute("Insert into users (userID,Name,password) values(?,?,?)", (
                        self.userID.get(),
                        self.username.get(),
                        self.password.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Uspesno', "korisnik dodat uspesno", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Greska", f"Greska od : {str(ex)}", parent=self.root)

####################
