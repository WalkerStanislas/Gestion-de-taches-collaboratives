import hashlib
from models.user import User
"""Importation des dependances necessaires"""


class Auth:
    """Une class Auth sans constructeur"""
    def login_user(self):
        """Permet a un utilisateur de se connecter"""
        username = input("Nom d'utilisateur ou adresse email : ")
        password = input("Mot de passe : ")
        user = self.login(username, password)
        if user is None:
            print("Identifiants incorrects")
        return user

    def login(self, username, password):
        """Permet a un utilisateur de se connecter"""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User().get(username)
        if user is not None and user.password == hashed_password:
            return user
        else:
            return None

    def inscription(self):
        username = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")
        user = User(username=username, password=password)
        user.save()

    def update(self, username):
        nom = input("Nom de famille : ")
        prenom = input("Prenom : ")
        email = input("Email : ")
        user = User().get(username)
        user.nom = nom
        user.prenom = prenom
        user.email = email
        user.update()
        return user
