import unittest
from models.user import User
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
