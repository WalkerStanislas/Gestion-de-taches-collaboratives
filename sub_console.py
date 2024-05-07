import cmd
import typer
from rich.console import Console
from rich.table import Table
from models.task import Task
from auth import Auth
"""Importation des modules"""
console = Console()
app = typer.Typer()


class TacheCMD(cmd.Cmd):
    """Documentation de la classe"""
    def __init__(self, user):
        """Definition du constructeur"""
        super().__init__()
        self.user = user
        self.prompt = f"({self.user.username}) "

    def do_EOF(self, arg):
        """Quitter la console avec Ctrl-z"""
        return True

    def emptyline(self):
        """Ne rien faire si aucune commande n'est rentre """
        return False

    def do_logout(self, arg):
        """Quit la console avec la commande quit"""
        return True

    @app.command(short_help='Ajouter une tâche')
    def do_add(self, arg):
        """Ajout tache"""
        task = input("Entrez le titre de la tâche:")
        category = input("Entrez la description de la tâche:")
        typer.echo(f"ajout de la tâche {task}, {category}")
        task = Task(task=task, category=category, id_User=self.user.user_id)
        task.save()
        self.do_show(None)

    @app.command(short_help='Supprimer une tâche')
    def do_delete(self, arg):
        """Suppression"""
        try:
            self.do_show(None)
            position = int(input("Entrer la position de la " +
                                 "tâche sur la table:"))
            user = self.user
            if user.role == 3:
                taches = Task().get()
            else:
                taches = Task().get(user.user_id)
            if position <= len(taches):
                tache_cur = taches[position - 1]
                if tache_cur.status == 1:
                    typer.echo(f"supression {position}")
                    """Position commence à 1 mais la base de
                    données, elle commence à 0
                    """
                    tache_cur.delete()
                    self.do_show(None)
                else:
                    console.print("🚨", "[bold red]Tache deja" +
                                  "debuter impossible de supprimer")
            else:
                console.print("🚨", "[bold red]Aucune tache ne " +
                              "correspond a cette position")
        except Exception:
            console.print("🚨", "[bold red]Entrez un entier")

    @app.command(short_help='Modifier une tâche')
    def do_update(self, arg):
        """Mise à jour d'une tâche"""
        if arg.__eq__('profil'):
            users = Auth().update(self.user.username)
            self.user = users
            return
        try:
            self.do_show(None)
            position = int(input("Entrer la position " +
                                 "de la tâche sur la table:"))
            user = self.user
            if user.role == 3:
                taches = Task().get()
            else:
                taches = Task().get(user.user_id)
            if type(position) is int and position <= len(taches):
                tache_cur = taches[position - 1]
                if tache_cur.status == 3:
                    console.print("Tache deja complete rien a modifier")
                else:
                    task = str(input("Entrer le libelle " +
                                     "de la nouvelle tâche:"))
                    category = str(input("Entrer la description " +
                                         "de la nouvelle tâche:"))
                    tache_cur.task = task if task != "" else tache_cur.task
                    tache_cur.category = category if category != "" else\
                        tache_cur.category
                    tache_cur.update()
                    typer.echo(f"Mise à jour {position}")
                    self.do_show(None)

            else:
                console.print("🚨", "[bold red]Aucune tache " +
                              "ne correspond a cette position")
        except Exception:
            console.print("🚨", "[bold red]Entrez un entier")

    @app.command(short_help='Completer une tache')
    def do_complete(self, arg):
        """Completer une tâche"""
        user = self.user
        if user.role == 3:
            position = int(input("Entrer la position " +
                                 "de la tâche sur la table:"))
            typer.echo(f"Validation {position}")
            task = Task().get(position-1)
            task.complete_task()
            self.do_show(None)
        else:
            console.print("🚨", "[bold red]Vous n'êtes pas " +
                          "autoriser à éffectuer cette opération")

    @app.command(short_help='Assigner une tâche')
    def do_assign_task(self, arg):
        """Assignation d'une tache"""
        try:
            user = self.user
            if user.role == 3:
                taches = Task().get()
            else:
                console.print("🚨", "[bold red]Vous n'etes pas " +
                              "autorise a faire cette operation")
                return
            position = int(input("Entrer la position de la " +
                                 "tâche sur la table:"))
            if position < len(taches):
                tache_cur = taches[position - 1]
                if tache_cur.status == 1:
                    typer.echo(f"Assignation {position}")
                    tache_cur.assign_tasks()
                    self.do_show(None)
                else:
                    console.print("🚨", "[bold red]Tache " +
                                  "deja debuter impossible")
            else:
                console.print("🚨", "[bold red]Aucune tache ne " +
                              "correspond a cette position")
        except Exception:
            console.print("🚨", "[bold red]Entrez un entier")

    @app.command(short_help='Affichage')
    def do_show(self, arg):
        """Affichage"""
        user = self.user
        if user.role == 3:
            tasks = Task().get()
        else:
            tasks = Task().get(user.user_id)
        console.print("[bold magenta]Todos[/bold magenta]!", "🌍")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Tache", min_width=20)
        table.add_column("Categorie", min_width=12, justify="right")
        table.add_column("Etat", min_width=12, justify="right")

        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red',
                      'Installation réseau': 'cyan', 'Sports': 'green'}
            if category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, task in enumerate(tasks, start=1):
            c = get_category_color(task.category)
            if task.status == 2:
                is_done_str = '⏳'
            elif task.status == 3:
                is_done_str = '✔️'
            else:
                is_done_str = '❌'
            table.add_row(str(idx), task.task,
                          f"[{c}]{task.category}[/{c}]", is_done_str)
        console.print(table)

    def do_stats(self, arg):
        """Statistique sur les taches"""
        user = self.user
        if user.role == 3:
            tasks = Task().get()
        else:
            tasks = Task().get(user.user_id)
        console.print("[bold magenta]Statistique[/bold magenta]!", "🌍")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Taches Terminees", min_width=20)
        table.add_column("Taches En Cours", min_width=12, justify="right")
        table.add_column("Taches non debutees", min_width=12, justify="right")
        table.add_column("Total taches", min_width=12, justify="right")

        finish = [x for x in tasks if x.status == 3]
        start = [x for x in tasks if x.status == 1]
        ongoing = [x for x in tasks if x.status == 2]
        table.add_row(str(len(finish)), str(len(ongoing)),
                      str(len(start)), str(len(tasks)))
        console.print(table)

    def do_profils(self, arg):
        """Permet a l'utilisateur de voir sont profiles"""
        console.print("[bold magenta]Profile[/bold magenta]!", "🌍")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Nom", min_width=20)
        table.add_column("Prenom", min_width=12, justify="right")
        table.add_column("Username", min_width=12, justify="right")
        table.add_column("Email", min_width=12, justify="right")
        table.add_column("Role", min_width=12, justify="right")
        user = self.user
        roles = {1: "Standard", 2: "Technicien", 3: "Admin"}
        table.add_row(str(user.nom), str(user.prenom),
                      str(user.username), str(user.email),
                      str(roles.get(user.role)))
        console.print(table)
