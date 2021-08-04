from click.termui import style
from rich import console
import typer
from rich.console import Console


app = typer.Typer(name="demo", add_completion=False, help="This is a demo app.")
console = Console()

@app.command()
def create_db(table: str = typer.Option(..., prompt="What is the name of the table?",
                                        confirmation_prompt=True)):
    console.print(f"Creating table in database {table}", style="green")

@app.command()
def delete_db(table: str = typer.Option(..., prompt="What is the name of the table?",
                                        confirmation_prompt=True)):
    sure = typer.confirm(f"Are you really sure you want to delete {table}?")
    if sure:
        console.print(f"Deleting table in database {table}", style="red")
    else:
        console.print(f"Back to safety!", style="green")

if __name__ == "__main__":
    app()