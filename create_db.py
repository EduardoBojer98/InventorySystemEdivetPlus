import sqlite3


def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items(itemID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Price text,Quantity text,Manufacturer text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS users(userID INTEGER PRIMARY KEY AUTOINCREMENT,Name text,password text)")
    con.commit()



create_db()
