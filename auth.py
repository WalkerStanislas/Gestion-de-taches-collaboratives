import hashlib
from models.user import User
"""Importation des dependances necessaires"""

class Auth:
    """Une class Auth sans constructeur"""
    def login_user(self):
        """Permet a un utilisateur de se connecter"""
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User().get(username)
        if user and user.password.__eq__(hashed_password):
            return user
        else:
            print("Identifiants incorrects.")
            return None


    def inscription(self):
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        user = User(username=username, password=password)
        user.save()