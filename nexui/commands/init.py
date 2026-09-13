import json
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel

console = Console()

DEFAULT_CONFIG = {
    "version": "1.0.0",
    "templates_dir": "templates",
    "components_dir": "templates/components",
    "static_dir": "static",
    "js_dir": "static/js/nexui",
    "css_dir": "static/css",
}

# Lines we ensure exist in .prettierignore
PRETTIER_IGNORE_ENTRIES = [
    "# Django templates — formatters like Prettier break template tags on multiline",
    "{templates_dir}/",
]


def _setup_prettier_ignore(templates_dir: str) -> None:
    """
    Add the templates directory to .prettierignore so HTML formatters
    don't break Django template tags when indenting across multiple lines.
    """
    ignore_path = Path(".prettierignore")
    entry = f"{templates_dir}/"

    existing = ignore_path.read_text() if ignore_path.exists() else ""

    if entry in existing:
        return

    lines_to_add = []
    comment = "# Django templates — formatters break {% %} tags across multiple lines"
    if comment not in existing:
        lines_to_add.append(comment)
    lines_to_add.append(entry)

    separator = "\n" if existing and not existing.endswith("\n") else ""
    new_content = existing + separator + "\n".join(lines_to_add) + "\n"

    ignore_path.write_text(new_content)
    console.print(f"[green]✓[/green] Added [bold]{entry}[/bold] to .prettierignore")


def _setup_djlint() -> None:
    djlint_path = Path(".djlintrc")
    if djlint_path.exists():
        return
    config = {"profile": "django", "indent": 2, "max_line_length": 120}
    djlint_path.write_text(json.dumps(config, indent=2))
    console.print("[green]✓[/green] Created [bold].djlintrc[/bold]")


def _setup_vscode() -> None:
    vscode_dir = Path(".vscode")
    vscode_dir.mkdir(exist_ok=True)

    settings_path = vscode_dir / "settings.json"
    if not settings_path.exists():
        settings = {
            "[html]": {
                "editor.defaultFormatter": "monosans.djlint",
                "editor.formatOnSave": True,
            },
            "files.associations": {"*.html": "django-html"},
            "prettier.ignorePath": ".prettierignore",
        }
        settings_path.write_text(json.dumps(settings, indent=2))
        console.print("[green]✓[/green] Created [bold].vscode/settings.json[/bold]")

    extensions_path = vscode_dir / "extensions.json"
    if not extensions_path.exists():
        extensions = {"recommendations": ["monosans.djlint"]}
        extensions_path.write_text(json.dumps(extensions, indent=2))
        console.print("[green]✓[/green] Created [bold].vscode/extensions.json[/bold] (VS Code will prompt to install djlint)")


@click.command()
@click.option("--templates-dir", default="templates", show_default=True, help="Templates directory")
@click.option("--static-dir", default="static", show_default=True, help="Static files directory")
def init(templates_dir, static_dir):
    """Initialize NexUI in your Django project."""
    config = {
        **DEFAULT_CONFIG,
        "templates_dir": templates_dir,
        "components_dir": f"{templates_dir}/components",
        "static_dir": static_dir,
        "js_dir": f"{static_dir}/js/nexui",
        "css_dir": f"{static_dir}/css",
    }

    # nexui.json
    config_path = Path("nexui.json")
    if config_path.exists():
        console.print("[yellow]nexui.json already exists, skipping.[/yellow]")
    else:
        config_path.write_text(json.dumps(config, indent=2))
        console.print("[green]✓[/green] Created [bold]nexui.json[/bold]")

    # Directories
    for key in ("components_dir", "js_dir", "css_dir"):
        Path(config[key]).mkdir(parents=True, exist_ok=True)

    # nexui.css
    from nexui.registry import get_base_css
    css_file = Path(config["css_dir"]) / "nexui.css"
    if not css_file.exists():
        css_file.write_text(get_base_css())
        console.print(f"[green]✓[/green] Created [bold]{css_file}[/bold]")

    # .prettierignore — Prettier must never reformat Django templates
    _setup_prettier_ignore(templates_dir)

    # .djlintrc — djlint understands Django syntax and formats HTML without
    # breaking {% %} tags. Use it instead of Prettier for HTML files.
    _setup_djlint()

    # .vscode/settings.json — configure djlint as the HTML formatter
    _setup_vscode()

    console.print(
        Panel(
            "\n".join([
                "[bold]NexUI initialized![/bold]",
                "",
                "Next steps:",
                "  1. Add [cyan]nexui[/cyan] to INSTALLED_APPS in settings.py",
                "  2. In your base template, add:",
                "     [cyan]<link rel=\"stylesheet\" href=\"{% static 'css/nexui.css' %}\">",
                "     [cyan]<script defer src=\"https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js\"></script>",
                "  3. Add a component:",
                "     [cyan]nexui add button[/cyan]",
                "  4. Use it in any template:",
                "     [cyan]{% load nexui_tags %}",
                "     [cyan]{% button label=\"Save\" variant=\"default\" %}[/cyan]",
            ]),
            title="[bold green]Done[/bold green]",
        )
    )
