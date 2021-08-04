import typer

app = typer.Typer(name="demo", add_completion=False, help="This is a demo app.")


@app.command()
def hello_world(name):
    """Say hello

    Args:
        name (str): Your name
    """
    print(f"hello {name}!")


@app.command()
def goodbye_world(name):
    """Say goodbye

    Args:
        name (str): Your name
    """
    print(f"goodbye {name}!")


@app.command()
def add(n1: int = typer.Argument(..., help="An integer"), 
        n2: int = typer.Argument(..., help="An integer")):
    """Add two numbers

    Args:
        n1 (Int): First number
        n2 (Int): Second number
    """
    print(n1 + n2)


if __name__ == "__main__":
    app()