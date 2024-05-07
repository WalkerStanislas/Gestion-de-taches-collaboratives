import sqlite3
"""Importation des dependances"""
conn = sqlite3.connect('GestionTaches.sqlite3')
cursor = conn.cursor()


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
        )""")


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
        )""")

def drop_all_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]};")
    conn.commit()

drop_all_tables()
create_userTable()
create_task_table()
