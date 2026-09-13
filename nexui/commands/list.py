import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

console = Console()


@click.command()
def list_components():
    """List all available NexUI components."""
    from nexui.registry import get_registry

    registry = get_registry()

    installed = set()
    config_path = Path("nexui.json")
    if config_path.exists():
        config = json.loads(config_path.read_text())
        components_dir = Path(config.get("components_dir", "templates/components"))
        if components_dir.exists():
            installed = {f.stem for f in components_dir.glob("*.html")}

    table = Table(title="NexUI Components", show_header=True, header_style="bold")
    table.add_column("", width=2)
    table.add_column("Component", style="bold")
    table.add_column("Description")
    table.add_column("Alpine.js", justify="center")

    for name, meta in registry.items():
        status = "[green]✓[/green]" if name in installed else " "
        needs_alpine = "[cyan]yes[/cyan]" if meta.get("alpine") else "[dim]no[/dim]"
        table.add_row(status, name, meta.get("description", ""), needs_alpine)

    console.print()
    console.print(table)
    console.print(f"\n[dim]{len(registry)} components available, {len(installed)} installed[/dim]")
    console.print("[dim]Run [bold]nexui add <name>[/bold] to install a component.[/dim]\n")
