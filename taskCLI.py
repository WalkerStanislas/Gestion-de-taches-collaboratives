import cmd
import typer
from rich.console import Console
from rich.table import Table
from models.database import complete_task, delete_tasks, get_all_tasks, insert_Tache, update_tasks, login_user, inscription, assign_tasks
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
