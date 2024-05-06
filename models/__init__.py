#Importation des dépendances
import sqlite3

conn = sqlite3.connect('GestionTaches.db') 
cursor  = conn.cursor()

def create_userTable():
     cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            nom VARCHAR(250),
            prenom VARCHAR(250),
            nomUser VARCHAR(250) UNIQUE,
            email VARCHAR(250) UNIQUE,
            passe VARCHAR(250),
            role INTEGER
        )""" )
     
create_userTable()

def create_task_table():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS taches (
        task text,
        category text,
        date_added text,
        date_completed text,
        status integer,
        position integer,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        )""" )

create_task_table()