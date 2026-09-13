import json
from pathlib import Path

COMPONENTS_DIR = Path(__file__).parent / "components"
BASE_CSS_FILE = Path(__file__).parent / "base.css"


def get_registry() -> dict:
    registry = {}
    for component_dir in sorted(COMPONENTS_DIR.iterdir()):
        if not component_dir.is_dir():
            continue
        meta_file = component_dir / "meta.json"
        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            registry[meta["name"]] = meta
    return registry


def get_component_files(name: str) -> dict[str, str]:
    component_dir = COMPONENTS_DIR / name
    return {
        f.name: f.read_text()
        for f in component_dir.iterdir()
        if f.suffix in (".html", ".js")
    }


def get_base_css() -> str:
    return BASE_CSS_FILE.read_text()
