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


if __name__ == "__main__":
    app()