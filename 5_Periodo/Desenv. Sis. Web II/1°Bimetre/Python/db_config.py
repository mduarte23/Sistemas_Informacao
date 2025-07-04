import pymysql

DB_HOST = '54.91.193.137'
BD_USER = 'libertas'
BD_PASSWORD = '123456'
BD_NAME = 'libertas5per'

def connect_db():
    return pymysql.connect(host=DB_HOST, user=BD_USER, password=BD_PASSWORD, db=BD_NAME)
