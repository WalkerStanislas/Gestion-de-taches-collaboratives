import unittest
from models.task import Task
from models.user import User
import os
from models import drop_all_tables
from models import create_userTable
from models import drop_all_tables

class TestTask(unittest.TestCase):
    """"""
    def setUp(self):
        """"""
        self.user1 = User(username="admin", password="admin123", role=3)
        self.user1.save()
        self.user1 = User().get(self.user1.username)
        self.user2 = User(username="epo123", password="1234")
        self.user2.save()
        self.user2 = User().get(self.user2.username)

    def tearDown(self):
        """Action a effectuer apres le test unittaire"""
        try:
            os.remove("GestionTaches.db")
            os.rename("Gestion.db", "GestionTaches.db")
        except Exception:
            pass

    def test_task_instance(self):
        """Verifier qu'une instance d'utilisateur
        creer a les bons attributs
        """
        task = Task(task="Home-Work", category="Faire les devoir de maison")
        self.assertEqual(task.task, "Home-Work")
        self.assertEqual(task.category, "Faire les devoir de maison")

    def test_user2_role(self):
        """Tester si l'utilisateur 2 est administrateur"""
        usr = self.user1
        user2 = User().get(usr.username)
        self.assertEqual(user2.role, 3)

    def test_update_task(self):
        """Tester la modification d'un task"""
        user1 = User().get(self.user1.username)
        user2 = User().get(self.user2.username)
        tasks_user1 = Task().get(user1.user_id)
        tasks_user2 = Task().get(user2.user_id)
        if len(tasks_user1) > 0:
            task1 = tasks_user1[0]
            task1.task = "Taches modifier"
            task1.category = "Categorie modifier"
            task1.id_User = self.user1.user_id
            task1.update()
            task1_up = Task().get(user1.user_id)[0]
            self.assertEqual(task1.task, task1_up.task)
            self.assertEqual(task1.category, task1_up.category)
        if len(tasks_user2) > 0:
            task2 = tasks_user2[0]
            task2.task = "Task 2 update"
            task2.category = "Task 2 description"
            task2.id_User = self.user2.user_id
            task2.update()
            task2_up = Task().get(user2.user_id)[0]
            self.assertEqual(task2.task, task2_up.task)
            self.assertEqual(task2.category, task2_up.category)

    def test_assign_task(self):
        """Tester qu'un administrateur a assigner une tache"""
        user1 = User().get(self.user1.username)
        tasks_user1 = Task().get(user1.user_id)
        if len(tasks_user1) > 0:
            task1 = tasks_user1[0]
            task2 = tasks_user1[1]
            t1 = task1.assign_tasks()
            t2 = task2.assign_tasks()
            self.assertEqual(t1.status, 2)
            self.assertEqual(t2.status, 2)


    def test_add_task(self):
        """Permettre l'ajout d'une nouvelle task"""
        user1 = self.user1
        user2 = self.user2
        task1 = Task(task="Maintenance", category="Mise a jour des logiciel",
                     id_User=user1.user_id)
        task2 = Task(task="Reparation", category="Reparation des portes",
                     id_User=user1.user_id)
        task11 = Task(task="Conception", category="Conception du model",
                      id_User=user2.user_id)
        task21 = Task(task="Deploiement", category="Mise en production \
                      de l'application", id_User=user2.user_id)
        t1 = task1.save()
        t2 = task2.save()
        t11 = task11.save()
        t21 = task21.save()
        self.assertEqual(t1.status, 1)
        self.assertEqual(t2.status, 1)
        self.assertLessEqual(t21.status, 2)
        self.assertEqual(t11.status, 1)
        self.assertEqual(Task().count(user1.user_id), 2)
        self.assertEqual(Task().count(user2.user_id), 2)
