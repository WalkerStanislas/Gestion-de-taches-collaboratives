#Importation des dépendances
import sqlite3
from typing import List
import datetime
from models.taskModel import Todo
import hashlib

conn = sqlite3.connect('GestionTaches.db') # Création de la base de données nommée  GestionTaches
cursor  = conn.cursor()

def create_userTable(): #Création d'une table pour les utilisateurs
     cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS User (
            id_User INTEGER PRIMARY KEY,
            nom VARCHAR(250),
            prenom VARCHAR(250),
            nomUser VARCHAR(250),
            email VARCHAR(250),
            passe VARCHAR(250),
            role VARCHAR(50)
        )""" )
     
create_userTable()



def create_task_table(): # Création d'une table pour les taches avec  06 colonnes
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Taches (
        task text,
        category text,
        date_added text,
        date_completed text,
        status integer,
        position integer,
        id_User INTEGER,
        FOREIGN KEY (id_User) REFERENCES User(id_User)
        )""" )

create_task_table()

def insert_Tache(tache: Todo): # Opération d'insertion de tâche
    cursor.execute('SELECT COUNT(*) FROM Taches')
    count = cursor.fetchone()[0]
    tache.position = count if count else 0
    with conn:
        cursor.execute('INSERT INTO Taches VALUES (:task, :category, :date_added, :date_completed, :status, :position, :id_User)',
                       {'task':tache.task, 'category':tache.category, 'date_added': tache.date_added, 'date_completed':tache.date_completed, 'status':tache.status,'position':tache.position, 'id_User':tache.id_User})


def get_all_tasks() -> List[Todo]: # Récupérer toutes les tâches (pour l'administrateur)
    cursor.execute('SELECT * FROM Taches')
    results = cursor.fetchall()
    taches = []
    for resultat in results:
        taches.append(Todo(*resultat))
    return taches

def delete_tasks(position): # Supprimer une tâche (réservé à l'administrateur)
    cursor.execute('SELECT COUNT(*) FROM Taches')
    count = cursor.fetchone()[0]

    with conn:
        cursor.execute("DELETE FROM Taches WHERE position=:position", {"position": position})
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)


def change_position(old_position: int, new_position: int, commit = True):
    cursor.execute('UPDATE Taches SET position = :position_new WHERE position = :position_old',
                   {'position_old': old_position, 'position_new':new_position})
    if commit:
        conn.commit


def update_tasks(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            cursor.execute('UPDATE Taches SET task = : task, category = :category WHERE position = :position',
                           {'position':position, 'task':task, 'category':category})
        elif task is not None:
            cursor.execute('UPDATE Taches SET task = : task WHERE position = :position',
                           {'position':position, 'task':task})
        elif category is not None:
            cursor.execute('UPDATE Taches SET category = :category WHERE position = :position',
                           {'position':position, 'category':category})
            
def complete_task(position: int):
    with conn:
        cursor.execute('UPDATE Taches SET status = 3, date_completed = :date_completed WHERE position = :position',
                       {'position':position, 'date_completed':datetime.datetime.now().isoformat()})
        
def assign_tasks(position: int):
    with conn:
        cursor.execute('UPDATE Taches SET status = 2, date_completed = :date_completed WHERE position = :position',
                       {'position':position, 'date_completed':datetime.datetime.now().isoformat()})
        
# Connexion utilisateur
def login_user():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM User WHERE nomUser=? AND passe=?", (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Connexion réussie.")
        return user
    else:
        print("Identifiants incorrects.")
        return None


def inscription():
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO User (nomUser, passe) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    #print("Inscription réussie.")

# Récupérer les tâches de l'utilisateur
def get_user_tasks(user_id):
    cursor.execute("SELECT * FROM Taches WHERE id_User=?", (user_id,))
    tasks = cursor.fetchall()
    return tasks
