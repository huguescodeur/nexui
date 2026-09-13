# Contributing to NexUI

## Ways to contribute

- **Report a bug** — open an issue with steps to reproduce
- **Suggest a component** — open an issue describing the use case
- **Submit a fix or new component** — open a pull request

## Running the demo locally

```bash
git clone https://github.com/huguescodeur/nexui.git
cd nexui
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"
python demo/manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000).

## Adding a new component

1. Create `nexui/registry/components/<name>/` with:
   - `<name>.html` — the template
   - `meta.json` — metadata (name, description, files, usage example)
2. Register the tag in `nexui/templatetags/nexui_tags.py`
3. Add a demo section in `demo/templates/index.html`
4. Sync the template to `demo/templates/components/`

## Code style

- Templates use Tailwind utility classes only — no custom CSS
- Tags with children → block tag via `SlotNode` / `_block()` factory
- Tags without children (void elements) → `@register.simple_tag`
- All `hx_*` kwargs auto-convert to `hx-*` attributes via `_build_attrs()`

## Commit style

```
feat: add switch component
fix: radio id collision in groups
docs: update select usage examples
```
