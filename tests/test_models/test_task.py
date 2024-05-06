
import unittest
from models.task import Task
from models.user import User
import datetime
import os


class TestTask(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        try:
            os.rename("GestionTaches.db", "Gestion.db")
        except Exception:
            pass
        self.user1 = User(username="admin", password="admin123", role=3)
        self.user1.save()
        self.user1 = User().get(self.user1.username)
        self.user2 = User(username="epo123", password="1234")
        self.user2.save()
        self.user2 = User().get(self.user2.username)
    
    def tearDown(self):
        try:
            os.remove("GestionTaches.db")
            os.rename("Gestion.db", "GestionTaches.db")
        except :
            pass

    def test_task_instance(self):
        """"""
        """Verifier qu'une instance d'utilisateur creer a les bons attributs"""
        task = Task(task="Home-Work", category="Faire les devoir de maison")
        self.assertEqual(task.task, "Home-Work")
        self.assertEqual(task.category,"Faire les devoir de maison")

    def test_add_task(self):
        """Permettre l'ajout d'une nouvelle task"""
        user1 = self.user1
        user2 = self.user2
        task1 = Task(task="Maintenance", category="Mise a jour des logiciel",id_User=user1.user_id)
        task2 = Task(task="Reparation", category="Reparation des portes",id_User=user1.user_id)
        task11 = Task(task="Conception", category="Conception du model",id_User=user2.user_id)
        task21 = Task(task="Deploiement", category="Mise en production de l'application",id_User=user2.user_id)
        task1.save()
        task2.save()
        task11.save()
        task21.save()
        self.assertEqual(Task().count(user1.user_id), 2)
        self.assertEqual(Task().count(user2.user_id), 2)