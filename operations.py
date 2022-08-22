import pymysql

def connection():
    conn = pymysql.connect(
        host='localhost', user='root', password='', db='data_db'
    )
    return conn
