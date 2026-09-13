import click
from silkui.commands.init import init
from silkui.commands.add import add
from silkui.commands.list import list_components


@click.group()
@click.version_option(package_name="silkui")
def main():
    """SilkUI — UI components for Django, inspired by shadcn/ui.

    Components are copied into your project. You own the code.
    """


main.add_command(init)
main.add_command(add)
main.add_command(list_components, name="list")
