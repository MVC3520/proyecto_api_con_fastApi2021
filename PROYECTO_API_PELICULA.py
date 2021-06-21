import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()

con = sql_connection()

sql_table(con)
"""
conn = pyodbc.connect ('DRIVER={ODBC Driver 17 for SQL server};'
                      'Server=LAPTOP-1A34F55U\SQLMIGUEL;'
                      'Database=PROYECTO_API_PELICULA;'
                      'Trusted_connect=Yes')    # seguridad integrada
                      #'UID=sa')
                      #'PWD=12345678')
                      
engine = create_engine(conn)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
cursor = conn.cursor()
cursor.execute('select * from persona')

for row in cursor:
    print(row)"""