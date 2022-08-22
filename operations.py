import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='', db='data_db'
    )
    return conn

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def add()
