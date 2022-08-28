import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

class functions:
    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All filds are requaierd", parent=self.root)
            else:
                cur.execute("select * from users where Name=? AND password=?",
                            (self.username.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid username or password", parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python main.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)