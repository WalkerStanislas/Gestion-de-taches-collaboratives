import cmd
import typer
from rich.console import Console
from auth import Auth

TacheCMD = __import__('sub_console').TacheCMD
console = Console()
app = typer.Typer()


class GTCCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(base) '

    def do_EOF(self, arg):
        """Quitter la console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quitter le programme"""
        return True

    @app.command(short_help='Inscrivez-vous')
    def do_signin(self, arg):
        """Inscrivez-vous"""
        Auth().inscription()
        typer.echo("Inscription réussie")

    @app.command(short_help='Connectez-vous')
    def do_login(self, arg):
        """Connectez-vous"""
        user = None
        while user is None:
            user = Auth().login_user()
        typer.echo(f"Vous êtes maintenant connecté en tant que: \
                   {user.username}")
        TacheCMD(user).cmdloop()


if __name__ == "__main__":
    GTCCommand().cmdloop()
