import webbrowser
from importlib.metadata import PackageNotFoundError

import typer
from pkg_resources import DistributionNotFound

from browsedocs.html import get_html, write_html
from browsedocs.packages import (
    installed_packages,
    package_dependencies,
    package_description,
    package_homepage,
)

app = typer.Typer()


@app.command()
def help(package: str, pypi: bool = typer.Option(False, "--pypi")):
    try:
        page = (
            f"https://pypi.org/project/{package}" if pypi else package_homepage(package)
        )
    except PackageNotFoundError:
        typer.echo(f"Package {package} not found")
        raise typer.Exit(1)

    if page is None:
        typer.echo(f"Package {package} has no homepage")
        raise typer.Exit(1)

    typer.echo(f"Opening {page}...")
    webbrowser.open_new_tab(page)


@app.command(name="list")
def list_packages(deps_of: str = typer.Option(None, "--deps-of")):
    if deps_of is None:
        typer.echo("Listing installed packages\n")
        packages = installed_packages()
    else:
        typer.echo(f"Listing depencies of {deps_of}\n")
        try:
            packages = package_dependencies(deps_of)
        except DistributionNotFound:
            typer.echo(f"Package {deps_of} not found")
            raise typer.Exit(1)
    for package in packages:
        typer.echo(package)


@app.command()
def readme(package: str):
    description, content_type = package_description(package)
    html = get_html(description, content_type=content_type)
    index = write_html(html).as_uri()
    typer.echo(f"Opening {index}...")
    webbrowser.open_new_tab(index)


if __name__ == "__main__":
    app()
