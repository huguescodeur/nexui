import json
from pathlib import Path

import click
from rich.console import Console

console = Console()


def _load_config() -> dict:
    config_path = Path("nexui.json")
    if not config_path.exists():
        console.print("[red]nexui.json not found. Run [bold]nexui init[/bold] first.[/red]")
        raise SystemExit(1)
    return json.loads(config_path.read_text())


@click.command()
@click.argument("components", nargs=-1)
@click.option("--all", "all_components", is_flag=True, help="Install all available components")
@click.option("--overwrite", is_flag=True, help="Overwrite existing files")
def add(components, all_components, overwrite):
    """Add one or more components to your project.

    Examples:

      nexui add button

      nexui add button card input

      nexui add --all
    """
    from nexui.registry import get_registry, get_component_files

    registry = get_registry()

    if all_components:
        components = tuple(registry.keys())

    if not components:
        console.print("[yellow]No component specified. Use --all to install everything.[/yellow]")
        console.print("Run [bold]nexui list[/bold] to see available components.")
        return

    config = _load_config()
    components_dir = Path(config["components_dir"])
    js_dir = Path(config["js_dir"])

    for name in components:
        name = name.lower()
        if name not in registry:
            console.print(f"[red]✗[/red] Component [bold]{name}[/bold] not found.")
            console.print("  Run [bold]nexui list[/bold] to see available components.")
            continue

        meta = registry[name]
        files = get_component_files(name)
        installed_count = 0

        for filename, content in files.items():
            dest = js_dir / filename if filename.endswith(".js") else components_dir / filename

            if dest.exists() and not overwrite:
                console.print(f"  [yellow]~[/yellow] {dest} already exists (use --overwrite to replace)")
                continue

            dest.write_text(content)
            console.print(f"  [green]✓[/green] {dest}")
            installed_count += 1

        if installed_count > 0:
            console.print(f"[green]Added[/green] [bold]{name}[/bold]")

            if meta.get("alpine"):
                console.print(
                    f"  [dim]Requires Alpine.js — "
                    "add [cyan]<script defer src=\"https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js\"></script>[/cyan] "
                    "to your base template[/dim]"
                )

            if meta.get("dependencies"):
                console.print(f"  [dim]Also needed: {', '.join(meta['dependencies'])}[/dim]")

            _print_usage(name, meta)


def _print_usage(name: str, meta: dict) -> None:
    usage = meta.get("usage")
    if usage:
        console.print(f"\n  [dim]Usage:[/dim]")
        console.print(f"  [cyan]{usage}[/cyan]\n")
