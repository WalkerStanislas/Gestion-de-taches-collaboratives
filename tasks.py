import cmd
import typer
from rich.console import Console
from rich.table import Table
from models.database import complete_task, delete_tasks, get_user_tasks,get_all_tasks, insert_Tache, update_tasks, login_user, inscription, assign_tasks
from models.taskModel import Todo

console = Console()
app = typer.Typer()

class TacheCMD(cmd.Cmd):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.prompt = f"({self.user[3]}) "

    def do_EOF(self, arg):
        """Quitter la console avec Ctrl-z"""
        return True

    def emptyline(self):
        """Ne rien faire si aucune commande n'est rentre """
        return False

    def do_quit(self, arg):
        """Quit la console avec la commande quit"""
        return True
    
    @app.command(short_help='Ajouter une tâche')
    def do_add(self, arg):
        task = input("Entrez le titre de la tâche:\n")
        category = input("Entrez la description de la tâche:\n")

        typer.echo(f"ajout de la tâche {task}, {category}") 
        todo = Todo(task=task, category=category, id_User=self.user[0])
        insert_Tache(todo)
        self.do_show(None)

    @app.command(short_help='Supprimer une tâche')
    def do_delete(self, arg, position: int):
        """Suppression"""
        typer.echo(f"supression {position}")

        delete_tasks(position-1) # Position commence à 1 mais la base de données, elle commence à 0
        self.show()

    @app.command(short_help='Modifier une tâche')
    def do_update(self, arg, position: int, task: str = None , category: str = None):
        typer.echo(f"Mise à jour {position}")

        update_tasks(position-1, task, category)
        self.show()

    @app.command(short_help='Completer une tâche')
    def do_complete(self, arg, position: int):
        typer.echo(f"Validation {position}")

        complete_task(position-1)
        self.show()

    @app.command(short_help='Assigner une tâche')
    def do_assign_task(self, arg, position: int):
        typer.echo(f"Assignation {position}")

        assign_tasks(position-1)
        self.show()

    @app.command(short_help='Affichage')
    def do_show(self, arg):
        """Affichage"""
        user =self.user
        tasks = get_user_tasks(user[0])
        console.print("[bold magenta]Todos[/bold magenta]!","🌍")

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Tache", min_width=20)
        table.add_column("Categorie", min_width=12, justify="right")
        table.add_column("Etat", min_width=12, justify="right")

        def get_category_color(category):
            COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Installation réseau': 'cyan' ,'Sports': 'green'}
            if  category in COLORS:
                return COLORS[category]
            return 'white'

        for idx, task in enumerate(tasks,start=1):
            c= get_category_color(task.category)
            if task.status == 2:
                is_done_str = '⏳'
            elif task.status == 3:
                is_done_str ='✔️'
            else:
                is_done_str ='❌' 
            table.add_row(str(idx),task.task, f"[{c}]{task.category}[/{c}]",is_done_str)
        console.print(table)
