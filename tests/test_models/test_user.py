#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""
import unittest
from models.user import User
import hashlib
import os

class TestUser(unittest.TestCase):
    """Test de la classe User"""

    def setUp(self):
        """Renomer le fichier de base de donne avant le test"""
        pass

    def tearDown(self):
        """Supprimer la base de donner de test et ramener la base de donne initial"""

    def test_user_instance(self):
        """Verifier qu'une instance d'utilisateur creer a les bons attributs"""
        user = User(username="walker", password="walker1234")
        self.assertEqual(user.username, "walker")
        self.assertEqual(user.password,"walker1234")
        self.assertEqual(user.role, 1)

    def test_insert_user(self):
        """Tester si un utilisateur est sauvegerder dans la base de donnee"""
        user_inst = User(username="test", password="test123")
        user_inst.save()
        user = User().get(username=user_inst.username)
        self.assertIsInstance(user_inst, User)
        self.assertIsInstance(user, User)
        self.assertEqual(user_inst.username, user.username)
        password = user_inst.password
        self.assertEqual(hashlib.sha256(password.encode()).hexdigest(), user.password)
    
    def test_login_user(self):
        """Test la connexion avec un utilisateur existant dans la base de donnee"""
        ex_user = User(username="test", password="test123")
        user = User().get(username=ex_user.username)
        self.assertIsNotNone(user)
        self.assertEqual(hashlib.sha256(ex_user.password.encode()).hexdigest(), user.password)


if __name__ == '__main__':
    unittest.main()