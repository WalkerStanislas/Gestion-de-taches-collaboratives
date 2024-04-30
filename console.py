import cmd
import typer
from rich.console import Console
from rich.table import Table
from models.database import complete_task, delete_tasks, get_all_tasks, insert_Tache, update_tasks, login_user, inscription, assign_tasks
from models.taskModel import Todo
TacheCMD = __import__('tasks').TacheCMD

console = Console()

app = typer.Typer()

class GTCCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(base) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    @app.command(short_help='Inscrivez-vous')
    def do_sigin(self, arg):
        """Inscrivez-vous"""
        inscription()
        typer.echo(f"Inscription réussie")

    @app.command(short_help='Connectez-vous')
    def do_login(self, arg):
        """Connectez-vous"""
        user = None
        while user is None:
            user = login_user()
        typer.echo(f"Vous êtes maintenant connecté en tant que: {user[3]}")  # user[3] correspond au champ nomUser dans la base de données
        TacheCMD(user).cmdloop()



if __name__ ==  "__main__":
    GTCCommand().cmdloop()