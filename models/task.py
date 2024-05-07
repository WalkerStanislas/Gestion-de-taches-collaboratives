import datetime
from . import cursor, conn
"""Importation de tout les modules"""


class Task:
    def __init__(self, task=None, category=None,
                 date_added=datetime.datetime.now().isoformat(),
                 date_completed=None, status=1, position=None, id_User=None):
        self.task = task
        self.category = category
        self.date_added = date_added
        self.date_completed = date_completed
        self.status = status
        self.position = position
        self.id_User = id_User

    def __repr__(self) -> str:
        """Pour l'affichage d'une tache"""
        return f"({self.task},{self.category},{self.date_added}, \
            {self.date_completed},{self.status}, \
                {self.position},{self.id_User})"

    def to_dict(self):
        """Cette function return dictionnaire d'un instance"""
        new_dict = self.__dict__.copy()
        return new_dict

    def save(self):
        """Cette method permet d'inserer une tache"""
        count = self.count()
        self.position = count if count else 0
        with conn:
            cursor.execute("INSERT INTO taches VALUES \
                           (:task, :category, :date_added, \
                           :date_completed, :status, :position, :user_id)",
                           {'task': self.task, 'category': self.category,
                            'date_added': self.date_added,
                            'date_completed': self.date_completed,
                            'status': self.status, 'position': self.position,
                            'user_id': self.id_User})

    def change_position(old_position: int, new_position: int, commit=True):
        """Changement de la position d'une tache apres insertion"""
        cursor.execute("UPDATE taches SET position = :position_new WHERE \
                       position = :position_old",
                       {'position_old': old_position,
                        'position_new': new_position})
        if commit:
            conn.commit

    def update(self):
        """Mise a jour du nom et prenom de l'utilisateur"""
        with conn:
            cursor.execute("UPDATE taches SET task = :task, \
                           category = :category WHERE position = :position",
                           {'position': self.position, 'task': self.task,
                            'category': self.category})

    def delete(self):
        """Supprimer une taches en fonction de sa position"""
        count = self.count()
        with conn:
            cursor.execute("DELETE FROM taches WHERE position=:position",
                           {"position": self.position})
            for pos in range(self.position+1, count):
                self.change_position(pos, pos-1, False)

    def close(self):
        """Fermer la connection a la base de donnee"""
        conn.close()

    def all(self):
        """Retourn la liste de tout les taches"""
        cursor.execute('SELECT * FROM taches')
        results = cursor.fetchall()
        results = [Task(*result) for result in results]
        return results

    def get(self, user_id=None):
        """
        Retourne toute la liste des utilisateurs
        ou un utilisateur par son nom utilisateur
        """
        results = self.all()
        if user_id is not None:
            results = [result for result in results if
                       result.id_User == user_id]
        return results

    def count(self, user_id=None):
        """Permet de compter le nombre d'utilisateur"""
        tasks = self.all()
        if user_id is not None:
            tasks = [task for task in tasks if task.id_User == user_id]
        return len(tasks)

    def complete_task(self):
        with conn:
            cursor.execute("UPDATE taches SET status = 3, \
                           date_completed = :date_completed WHERE \
                           position = :position",
                           {'position': self.position,
                            'date_completed':
                            datetime.datetime.now().isoformat()
                            })

    def assign_tasks(self):
        """Permet d'assigner une tache un utilisateur
        et de marquer la tache comme debuter
        """
        with conn:
            cursor.execute("UPDATE taches SET status = 2, \
                           date_completed = :date_completed WHERE \
                           position = :position",
                           {'position': self.position,
                            'date_completed':
                            datetime.datetime.now().isoformat()
                            })
