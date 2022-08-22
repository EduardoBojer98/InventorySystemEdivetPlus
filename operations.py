import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='', db='data_db'
    )

def signin(user,password):
    username=user.get()
    password=password.get()
    #metoda za rad sa bazom za login

def signup():