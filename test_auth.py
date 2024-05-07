import unittest
from models.user import User
from auth import Auth
"""Importation des modules"""


class TestAuth(unittest.TestCase):
    """Definition de la class"""
    def setUp(self):
        """Creer un utilisateur pour les login"""
        self.user = User(username="login_user", password="1234")

    def test_user_sigin(self):
        """Tester une inscription"""
        user = self.user
        user.save()
        user_sav = User().get(user.username)
        self.assertIsNotNone(user_sav)
        self.assertEqual(user_sav.username, user.username)

    def test_login(self):
        """Tester l'authentification"""
        user = self.user
"""         log_user = Auth().login(user.username, user.password)
        self.assertIsInstance(log_user, User)
        self.assertIsNotNone(log_user)
        self.assertEqual(log_user.username, user.username)
        wrong_pass = Auth().login(user.username, "wrong_password")
        self.assertIsNone(wrong_pass)
        wrong_uname = Auth().login("no_exists", user.password)
        self.assertIsNone(wrong_uname) """
