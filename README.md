# Gestion des Taches collaboratives
- [Collaborateurs](#Collaborateurs)
- [Dependances](#Dependances)
- [Structure](#Structure)
- [Excecution](#Execution)
- [Résultats](#Résultats)
## Collaborateurs
[Compaore Walker](https://github.com/WalkerStanislas) &&
[SAWADOGO Souleymane](https://github.com/Soulsaw)
## Dependances
Pour executer ce projet il est necessaires d'avoir ``python3.10`` ou une version superieure et de s'assurer d'avoir les dependances ``sqlit3`` ``rich`` et ``typer`` dans votre machine. Ces dependances sont necessaires à l'execution du projet. Au cas où ces dependances ne sont pas installées, ils peuvent être installé par les commandes suivantes:
---
> ``pip install sqlite3``
---
> ``pip install typer``
---
> ``pip install  rich``
---
Une fois que ces dependances sont installées, voyont ensemble comment executer le projet dans la prochaine section.
## Structure
La structure du projet est comme suite:
---
D'abord il y'a un package ``models`` contenant trois fichiers:
1. [__init__.py](models/__init__.py) Qui permet de rendre le dossier ``model`` en package et aussi contient le code permet la connection a la base de donnée ``Sqlite``.
2. [user.py](models/user.py) Ce fichier contient des fonctions permettant d'`inserer` de `supprimer`, la `mise a jour`, l'obtention de la `liste des utilisateur`, obtenir le `nombre total d'utilisateur` et enfin permet de `retrouver un utilisateur a travers son nom d'utilisateur ou son adresse email`
3. [task.py](models/task.py) Ce fichier a la même `structure que le precédent, seulemant qu'il gère les taches`.
---
Ensuite on à un package `tests` contenant les fichiers suivants:
1. [__init__.py](tests/__init__.py) Pour rendre le `dossier` en package
2. [test_user.py](tests/test_models/test_task.py) Contenant l'implementation des tests unitaires pour les [taches](models/task.py)
3. [test_task.py](tests/test_models/test_user.py) Contenant l'implementation des tests unitaires pour l'[utilisateur](models/user.py)
---
- [auth.py](auth.py) Contenant les fonctions d'authentification et d'inscription d'un utilisateur
- [test_auth.py](test_auth.py) Contenant les tests pour l'[authentification](auth.py)
- [sub_console.py](sub_console.py) Contenant l'implementation d'un module `cmd` pour l'interaction. Dédié à un utilisateur connecté.
- [console.py](console.py) Contenant l'implementation d'un module `cmd`, et constitue le premier contact avec l'utilisateur. Cette ``console`` donne l'option a un utilisateur de soit `se connecter` ou de `s'incrire` s'il n'a pas encore de compte.
## Execution
Pour executer le présent projet, il suffit de ce placé dans la racine du projet et executer la commande ``python console.py`` pour lancer la console principale.
Dans le cas où vous ne savez pas quelles commandes taper, taper `help` dans n'importe quel console
---
Les testes unitaires peuvent aussi être exécuter avec la commande `python -m unittest -v`.
## Resultats
Ceci constitue quelques resultats d'exécution.
1. Inscription et Connexion
![Inscription et connexion](res/signin_login.png "Inscription")
2. Ajout et mise à jour d'une tâche
![Ajout et mise a jour](res/add_update.png "Ajout et mise a jour")
3. Suppression et affichage de la liste des taches
![delete and show](res/show_delete.png "Delete and show")
4. Affichage profile utilisateur et mise a jour de son profile
![show profile](res/profils_update.png "Voir profile")
5. Assigner une tache
![assign task](res/complete_statistique.png "assigner une tache")
8. Completer une tache
![complete task](res/complete_statistique.png "Completer une tache")
9. Test unitaire
![Unittest](res/unittests.png "Test Unitaire")
10. Demo
[![Demo](res/signin_login.png "Inscription")](https://youtu.be/YknXutXMa40 "Video demo d'execution")
