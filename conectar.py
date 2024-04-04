import mysql.connector

def connect():
    mydb = mysql.connector.connect (
        host="localhost",
        user="root",
        password="",
        database="biblioteca_aureliano"
    )
    return mydb