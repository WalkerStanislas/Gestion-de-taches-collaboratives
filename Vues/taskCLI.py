import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help='Ajouter une tâche')
def add(task: str, category: str):
    typer.echo(f"ajout de la tâche {task}, {category}")

@app.command()
def delete(position: int):
    typer.echo(f"supression {position}")

@app.command()
def update(position: int, task: str = None , category: str = None):
    typer.echo(f"ajout de la tâche {task}, {category}")

if __name__ ==  "__main__":
    app()