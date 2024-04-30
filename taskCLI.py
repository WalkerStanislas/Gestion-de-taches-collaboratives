import typer
from rich.console import Console
from rich.table import Table
from models.database import complete_task, delete_tasks, get_all_tasks, insert_Tache, update_tasks, login_user, inscription, assign_tasks
from models.taskModel import Todo

console = Console()

app = typer.Typer()

@app.command(short_help='Inscrivez-vous')
def SignIn():
    inscription()
    typer.echo(f"Inscription réussie")  


@app.command(short_help='Connectez-vous')
def login():
    user = None
    while user is None:
        user = login_user()
    typer.echo(f"Vous êtes maintenant connecté en tant que: {user[3]}")  # user[3] correspond au champ nomUser dans la base de données


@app.command(short_help='Ajouter une tâche')
def add(task: str, category: str):
    typer.echo(f"ajout de la tâche {task}, {category}") 
    todo = Todo(task,category)
    
    insert_Tache(todo)
    show()


@app.command(short_help='Supprimer une tâche')
def delete(position: int):
    typer.echo(f"supression {position}")

    delete_tasks(position-1) # Position commence à 1 mais la base de données, elle commence à 0
    show()

@app.command(short_help='Modifier une tâche')
def update(position: int, task: str = None , category: str = None):
    typer.echo(f"Mise à jour {position}")

    update_tasks(position-1, task, category)
    show()

@app.command(short_help='Completer une tâche')
def complete(position: int):
    typer.echo(f"Validation {position}")

    complete_task(position-1)
    show()

@app.command(short_help='Assigner une tâche')
def assign_task(position: int):
    typer.echo(f"Assignation {position}")

    assign_tasks(position-1)
    show()

@app.command(short_help='Affichage')
def show():
    tasks = get_all_tasks()
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


if __name__ ==  "__main__":
    app()