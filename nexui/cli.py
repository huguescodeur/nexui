import click
from nexui.commands.init import init
from nexui.commands.add import add
from nexui.commands.list import list_components


@click.group()
@click.version_option(package_name="nexui")
def main():
    """NexUI — UI components for Django, inspired by shadcn/ui.

    Components are copied into your project. You own the code.
    """


main.add_command(init)
main.add_command(add)
main.add_command(list_components, name="list")
