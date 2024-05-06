from . import conn, cursor
import hashlib
"""Importation des dependances python"""

class User:
    """Definition de la classe User"""
    def __init__(self, user_id=None,nom=None,prenom=None, username=None,email=None, password=None, role=1):
        """Constructeur de la classe user"""
        self.user_id = user_id
        self.nom = nom
        self.prenom = prenom
        self.username = username
        self.email = email
        self.password =  password
        self.role = role
        
    def save(self):
        """Cette method permet d'inserer un utilisateur"""
        password = hashlib.sha256(self.password.encode()).hexdigest()
        cursor.execute("INSERT INTO users (nomUser, passe, role) VALUES (?, ?, ?)", (self.username, password, self.role))
        conn.commit()

    def to_dict(self):
        """Cette function return dictionnaire d'un instance"""
        new_dict = self.__dict__.copy()
        return new_dict

    def update(self):
        """Mise a jour du nom et prenom de l'utilisateur"""
        cursor.execute("UPDATE users SET nom = :nom, prenom = :prenom, email = :email WHERE nomUser = :username",
                       {'nom':self.nom,'prenom':self.prenom, 'email':self.email, 'username':self.username})
        conn.commit()

    def delete(self, user_id):
        """Delete the current user"""
        cursor.execute("DELETE FROM users WHERE user_id = :user_id",{'user_id':user_id})
        conn.commit()

    def close(self):
        """Fermer la connection a la base de donnee"""
        conn.close()

    def all(self):
        """Retourn la liste de tout les utilisateurs"""
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
        results = [User(*result) for result in results]
        return results

    def get(self, username=None):
        """
        Retourne toute la liste des utilisateurs ou un utilisateur par son nom utilisateur
        """
        results = self.all()
        if username is not None:
            for result in results:
                if result.username.__eq__(username):
                    return result
            return None
        return results

    def count(self):
        """Permet de compter le nombre d'utilisateur"""
        users = self.all()
        return len(users)