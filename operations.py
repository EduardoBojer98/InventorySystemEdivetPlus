import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


class databaseconn:
    def connection(self):
        conn = pymysql.connect(
            host='localhost', user='root', password='', db='data_db'
        )
        return conn


class CRUDOP:
    def read(self):
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data")
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    def refreshTable(my_tree):
        for data in my_tree.get_children():
            my_tree.delete(data)

        for array in read():
            my_tree.insert(parent='', index='end', iid=array, text="", values=array)

        my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial', 12))
        my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

    def add(self, itemEntry, nameEntry, priceEntry, quantityEntry, manufacturerEntry, my_tree):
        itemid = str(itemEntry.get())
        itemname = str(nameEntry.get())
        itemprice = str(priceEntry.get())
        itemquantity = str(quantityEntry.get())
        itemmanufacturer = str(manufacturerEntry.get())

        if (itemid == "" or itemid == " ") or (itemname == "" or itemname == " ") or (
                itemprice == "" or itemprice == " ") or (itemquantity == "" or itemquantity == " ") or (
                itemmanufacturer == "" or itemmanufacturer == " "):
            messagebox.showinfo("Error", "Please fill up the blank entry")
            return
        else:
            try:
                conn = connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO data VALUES ('" + itemid + "','" + itemname + "','" + itemprice + "','" + itemquantity + "','" + itemmanufacturer + "')")
                conn.commit()
                conn.close()
            except:
                messagebox.showinfo("Error", "Item ID already exist")
                return
        refreshTable(my_tree)
