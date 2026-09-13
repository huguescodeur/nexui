# SilkUI

UI components for Django. Copy, own, customize. Inspired by [shadcn/ui](https://ui.shadcn.com/).

[![PyPI version](https://img.shields.io/pypi/v/silkui)](https://pypi.org/project/silkui/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/silkui)](https://pypi.org/project/silkui/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Philosophy

SilkUI is not a traditional dependency. When you run `silkui add button`, it copies `button.html` directly into your project's `templates/components/` directory. **You own the code.** Edit the Tailwind classes, change the structure, add your own logic — no upstream updates will ever overwrite your work.

Components are Django template tags built on:
- **Tailwind CSS** — utility classes for styling
- **Alpine.js** — lightweight client-side interactivity (modal, dropdown, tabs, toast)
- **HTMX** — optional, via `hx_*` kwargs on any component

---

## Installation

```bash
pip install silkui
```

Add to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "silkui",
]
```

Run the initializer in your project root:

```bash
silkui init
```

This creates:
- `silkui.json` — project config
- `static/css/silkui.css` — CSS variables for theming
- `templates/components/` — where your component files will live
- `.vscode/settings.json` — configures djlint as the HTML formatter (see [Formatter](#formatter))

### With Tailwind installed via npm (recommended for real projects)

Add the SilkUI colors to your `tailwind.config.js`:

```js
// tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" },
        secondary: { DEFAULT: "hsl(var(--secondary))", foreground: "hsl(var(--secondary-foreground))" },
        destructive: { DEFAULT: "hsl(var(--destructive))", foreground: "hsl(var(--destructive-foreground))" },
        muted: { DEFAULT: "hsl(var(--muted))", foreground: "hsl(var(--muted-foreground))" },
        accent: { DEFAULT: "hsl(var(--accent))", foreground: "hsl(var(--accent-foreground))" },
        card: { DEFAULT: "hsl(var(--card))", foreground: "hsl(var(--card-foreground))" },
        popover: { DEFAULT: "hsl(var(--popover))", foreground: "hsl(var(--popover-foreground))" },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
}
```

Then in `base.html`, just link the compiled CSS:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/tailwind.css' %}">
<link rel="stylesheet" href="{% static 'css/silkui.css' %}">

<!-- x-data on body so all components share the same Alpine scope -->
<body x-data>
  {% block content %}{% endblock %}

  <!-- Alpine.js — required for modal, dropdown, tabs, toast -->
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js"></script>
</body>
```

### With Tailwind CDN (quick start / prototyping only)

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/silkui.css' %}">
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          border: "hsl(var(--border))", input: "hsl(var(--input))", ring: "hsl(var(--ring))",
          background: "hsl(var(--background))", foreground: "hsl(var(--foreground))",
          primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" },
          secondary: { DEFAULT: "hsl(var(--secondary))", foreground: "hsl(var(--secondary-foreground))" },
          destructive: { DEFAULT: "hsl(var(--destructive))", foreground: "hsl(var(--destructive-foreground))" },
          muted: { DEFAULT: "hsl(var(--muted))", foreground: "hsl(var(--muted-foreground))" },
          accent: { DEFAULT: "hsl(var(--accent))", foreground: "hsl(var(--accent-foreground))" },
          card: { DEFAULT: "hsl(var(--card))", foreground: "hsl(var(--card-foreground))" },
          popover: { DEFAULT: "hsl(var(--popover))", foreground: "hsl(var(--popover-foreground))" },
        },
        borderRadius: { lg: "var(--radius)", md: "calc(var(--radius) - 2px)", sm: "calc(var(--radius) - 4px)" },
      },
    },
  }
</script>

<body x-data>
  {% block content %}{% endblock %}
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js"></script>
</body>
```

> The CDN inline config is required because Tailwind CDN doesn't read `tailwind.config.js`. With npm this goes in the config file and `base.html` stays clean.

---

## CLI

```bash
silkui add button           # add a single component
silkui add button card tabs # add multiple at once
silkui add --all            # add every available component
silkui list                 # list available and installed components
```

---

## Usage

Load the tags at the top of any template:

```django
{% load silkui_tags %}
```

---

## Components

---

### Button

```bash
silkui add button
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `variant` | `default` `secondary` `outline` `ghost` `destructive` `link` | `default` | Visual style |
| `size` | `sm` `md` `lg` `icon` | `md` | Size |
| `type` | `button` `submit` `reset` | `button` | HTML type |
| `disabled` | bool | `False` | Disables the button |
| `class` | string | — | Extra Tailwind classes |
| `hx_*` | string | — | HTMX attributes (`hx_post`, `hx_target`, `hx_swap`…) |
| `data_*` | string | — | Data attributes (`data_controller`…) |

**Usage**

```django
{% button %}Save{% endbutton %}
{% button variant="secondary" %}Cancel{% endbutton %}
{% button variant="outline" %}Outline{% endbutton %}
{% button variant="ghost" %}Ghost{% endbutton %}
{% button variant="destructive" %}Delete{% endbutton %}
{% button variant="link" %}Link{% endbutton %}

{% button size="sm" %}Small{% endbutton %}
{% button size="lg" %}Large{% endbutton %}
{% button size="icon" %}★{% endbutton %}

{% button disabled=True %}Disabled{% endbutton %}
{% button type="submit" class="w-full" %}Submit{% endbutton %}

{% button hx_post="/save/" hx_target="#result" hx_swap="outerHTML" %}Save{% endbutton %}
{% button variant="destructive" hx_delete="/items/42/" hx_confirm="Are you sure?" %}Delete{% endbutton %}
```

---

### Badge

```bash
silkui add badge
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `variant` | `default` `secondary` `destructive` `outline` | `default` | Visual style |
| `class` | string | — | Extra Tailwind classes |

**Usage**

```django
{% badge %}Default{% endbadge %}
{% badge variant="secondary" %}Beta{% endbadge %}
{% badge variant="destructive" %}Error{% endbadge %}
{% badge variant="outline" %}New{% endbadge %}
```

---

### Alert

```bash
silkui add alert
```

**Parameters — `alert`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `variant` | `default` `destructive` | `default` | Visual style |
| `class` | string | — | Extra Tailwind classes |

**Parameters — `alert_title` / `alert_description`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `class` | string | — | Extra Tailwind classes |

**Usage**

```django
{% alert %}
  {% alert_title %}Heads up!{% endalert_title %}
  {% alert_description %}You can add components to your project.{% endalert_description %}
{% endalert %}

{% alert variant="destructive" %}
  {% alert_title %}Error{% endalert_title %}
  {% alert_description %}Your session has expired. Please log in again.{% endalert_description %}
{% endalert %}
```

---

### Card

```bash
silkui add card
```

**Parameters**

| Component | Parameters | Description |
|---|---|---|
| `card` | `class` | Outer wrapper |
| `card_header` | `class` | Header section (padding + flex column) |
| `card_title` | `class` | `<h3>` title |
| `card_description` | `class` | Muted subtitle |
| `card_content` | `class` | Main content area |
| `card_footer` | `class` | Footer row |

**Usage**

```django
{% card %}
  {% card_header %}
    {% card_title %}Total Revenue{% endcard_title %}
    {% card_description %}Monthly earnings{% endcard_description %}
  {% endcard_header %}
  {% card_content %}
    <p class="text-3xl font-bold">$45,231</p>
    <p class="text-xs text-muted-foreground mt-1">+20.1% from last month</p>
  {% endcard_content %}
  {% card_footer %}
    {% button variant="outline" size="sm" %}View details{% endbutton %}
  {% endcard_footer %}
{% endcard %}
```

Sub-components can be used independently:

```django
{% card_title %}Standalone title{% endcard_title %}
{% card_description %}Without the full card wrapper{% endcard_description %}
```

---

### Input

```bash
silkui add input
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `name` | string | — | Field name (required) |
| `type` | `text` `email` `password` `number` `tel` `url` … | `text` | HTML input type |
| `id` | string | same as `name` | HTML id |
| `label` | string | — | Label text above the field |
| `value` | string | — | Pre-filled value |
| `placeholder` | string | — | Placeholder text |
| `required` | bool | `False` | Marks field as required |
| `disabled` | bool | `False` | Disables the field |
| `readonly` | bool | `False` | Makes the field read-only |
| `hint` | string | — | Helper text below the field |
| `error` | string | — | Error message (red) |
| `icon` | string | — | Icon shown inside the field (emoji or SVG string) |
| `icon_position` | `left` `right` | `left` | Icon position |
| `container_class` | string | — | Classes on the outer wrapper |
| `input_class` | string | — | Classes on the `<input>` |
| `label_class` | string | — | Classes on the `<label>` |
| `hx_*` | string | — | HTMX attributes |
| `data_*` | string | — | Data attributes |

**Usage**

```django
{% input name="email" label="Email" type="email" placeholder="you@example.com" required=True %}
{% input name="password" label="Password" type="password" %}
{% input name="search" label="Search" icon="🔍" icon_position="left" %}
{% input name="bio" label="Bio" hint="Max 160 characters." %}
{% input name="username" label="Username" error="This username is already taken." %}
{% input name="ref" label="Code" readonly=True value="NX-2024" %}

{# With Django form field #}
{% input name="email" label="Email" type="email" value=form.email.value error=form.email.errors.0 %}

{# Live search with HTMX #}
{% input name="q" placeholder="Search..." icon="🔍" hx_get="/search/" hx_trigger="keyup changed delay:300ms" hx_target="#results" %}
```

---

### Textarea

```bash
silkui add textarea
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `name` | string | — | Field name (required) |
| `id` | string | same as `name` | HTML id |
| `label` | string | — | Label text |
| `value` | string | — | Pre-filled value |
| `placeholder` | string | — | Placeholder text |
| `rows` | number | — | Number of visible rows |
| `required` | bool | `False` | Marks field as required |
| `disabled` | bool | `False` | Disables the field |
| `readonly` | bool | `False` | Read-only |
| `hint` | string | — | Helper text |
| `error` | string | — | Error message (red) |
| `container_class` | string | — | Classes on the outer wrapper |
| `input_class` | string | — | Classes on the `<textarea>` |
| `label_class` | string | — | Classes on the `<label>` |
| `hx_*` | string | — | HTMX attributes |

**Usage**

```django
{% textarea name="message" label="Message" placeholder="Write your message..." rows=4 %}
{% textarea name="bio" label="Bio" hint="Max 160 characters." %}
{% textarea name="notes" label="Notes" value=form.notes.value error=form.notes.errors.0 %}
```

---

### Select

```bash
silkui add select
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `name` | string | — | Field name (required) |
| `id` | string | same as `name` | HTML id |
| `label` | string | — | Label text |
| `choices` | list of 2-tuples | `[]` | Options: `[("value", "Label"), …]` |
| `value` | string | — | Pre-selected value |
| `placeholder` | string | — | Empty first option text |
| `required` | bool | `False` | Marks field as required |
| `disabled` | bool | `False` | Disables the field |
| `hint` | string | — | Helper text |
| `error` | string | — | Error message (red) |
| `container_class` | string | — | Classes on the outer wrapper |
| `input_class` | string | — | Classes on the `<select>` |
| `label_class` | string | — | Classes on the `<label>` |
| `hx_*` | string | — | HTMX attributes |

**Usage**

```python
# views.py
ROLE_CHOICES = [
    ("admin", "Administrator"),
    ("editor", "Editor"),
    ("viewer", "Viewer"),
]
```

```django
{% select name="role" label="Role" choices=role_choices placeholder="Select a role..." %}

{# Pre-selected value #}
{% select name="role" label="Role" choices=role_choices value="editor" %}

{# With Django form field #}
{% select name="role" label="Role" choices=form.role.field.choices value=form.role.value %}
```

---

### Checkbox

```bash
silkui add checkbox
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `name` | string | — | Field name (required) |
| `id` | string | same as `name` | HTML id |
| `label` | string | — | Label text (inline, next to checkbox) |
| `value` | string | — | Value submitted with the form |
| `checked` | bool | `False` | Pre-checked state |
| `required` | bool | `False` | Marks field as required |
| `disabled` | bool | `False` | Disables the field |
| `hint` | string | — | Helper text below |
| `error` | string | — | Error message (red) |
| `container_class` | string | — | Classes on the outer wrapper |
| `input_class` | string | — | Classes on the `<input>` |
| `label_class` | string | — | Classes on the `<label>` |
| `hx_*` | string | — | HTMX attributes |

**Usage**

```django
{% checkbox name="terms" label="I accept the terms and conditions" required=True %}
{% checkbox name="newsletter" label="Receive marketing emails" hint="Unsubscribe at any time." %}
{% checkbox name="active" label="Active account" checked=True %}
{% checkbox name="locked" label="Locked option" disabled=True %}
```

---

### Radio

```bash
silkui add radio
```

Group radios by sharing the same `name`. The `id` is auto-generated as `name-value` (e.g. `name="plan"` + `value="pro"` → `id="plan-pro"`).

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `name` | string | — | Group name (required) |
| `value` | string | — | This option's value (required) |
| `id` | string | `name-value` | HTML id (auto-generated) |
| `label` | string | — | Label text (inline) |
| `checked` | bool | `False` | Pre-selected state |
| `required` | bool | `False` | Marks field as required |
| `disabled` | bool | `False` | Disables this option |
| `container_class` | string | — | Classes on the wrapper |
| `input_class` | string | — | Classes on the `<input>` |
| `label_class` | string | — | Classes on the `<label>` |
| `hx_*` | string | — | HTMX attributes |

**Usage**

```django
{% radio name="plan" value="free" label="Free" %}
{% radio name="plan" value="pro" label="Pro" checked=True %}
{% radio name="plan" value="enterprise" label="Enterprise" %}
{% radio name="plan" value="legacy" label="Legacy" disabled=True %}
```

---

### Separator

```bash
silkui add separator
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `orientation` | `horizontal` `vertical` | `horizontal` | Direction |
| `class` | string | — | Extra Tailwind classes |

**Usage**

```django
{% separator %}

{% separator class="my-8" %}

<div class="flex h-6 items-center gap-4">
  <span>Left</span>
  {% separator orientation="vertical" %}
  <span>Right</span>
</div>
```

---

### Tabs

```bash
silkui add tabs
```

**Parameters — `tabs`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `active` | string | first tab id | Active tab on load |
| `class` | string | — | Classes on the root wrapper |
| `tabs_class` | string | — | Classes on the tab buttons row |
| `panel_class` | string | — | Classes on each content panel |

**Parameters — `tab`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `id` | string | — | Unique tab identifier (required) |
| `label` | string | — | Tab button label (required) |

**Usage**

```django
{% tabs active="account" %}
  {% tab id="account" label="Account" %}
    {% input name="username" label="Username" %}
    {% button type="submit" %}Save{% endbutton %}
  {% endtab %}
  {% tab id="password" label="Password" %}
    {% input name="current" label="Current password" type="password" %}
    {% input name="new" label="New password" type="password" %}
    {% button type="submit" %}Update{% endbutton %}
  {% endtab %}
  {% tab id="billing" label="Billing" %}
    <p class="text-sm text-muted-foreground">No billing information on file.</p>
  {% endtab %}
{% endtabs %}
```

---

### Dropdown

```bash
silkui add dropdown
```

**Parameters — `dropdown`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `trigger_label` | string | — | Button label (required) |
| `trigger_class` | string | — | Extra classes on the trigger button |
| `class` | string | — | Classes on the root wrapper |
| `menu_class` | string | — | Classes on the dropdown panel |

**Parameters — `dropdown_item`**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `href` | string | `#` | Link URL |
| `disabled` | bool | `False` | Greys out the item |
| `hx_*` | string | — | HTMX attributes |

**Usage**

```django
{% dropdown trigger_label="My Account" %}
  {% dropdown_item href="/profile/" %}Profile{% enddropdown_item %}
  {% dropdown_item href="/settings/" %}Settings{% enddropdown_item %}
  {% dropdown_separator %}
  {% dropdown_item href="/logout/" %}Log out{% enddropdown_item %}
{% enddropdown %}

{# With HTMX #}
{% dropdown trigger_label="Actions" %}
  {% dropdown_item href="#" hx_post="/publish/" hx_target="#status" %}Publish{% enddropdown_item %}
  {% dropdown_separator %}
  {% dropdown_item href="#" hx_delete="/items/42/" hx_confirm="Delete?" %}Delete{% enddropdown_item %}
{% enddropdown %}
```

---

### Modal

```bash
silkui add modal
```

**Parameters**

| Parameter | Values | Default | Description |
|---|---|---|---|
| `id` | string | `modal` | Unique modal identifier |
| `title` | string | — | Modal heading |
| `description` | string | — | Subtitle below the heading |
| `trigger_label` | string | — | Built-in trigger button label |
| `trigger_class` | string | — | Classes on the trigger button |
| `modal_class` | string | — | Classes on the modal panel |

**Usage**

```django
{# With built-in trigger button #}
{% modal id="confirm" trigger_label="Delete account" title="Are you sure?" description="This cannot be undone." %}
  <p class="text-sm text-muted-foreground">All your data will be permanently removed.</p>
  <div class="mt-6 flex justify-end gap-2">
    {% button variant="outline" %}Cancel{% endbutton %}
    {% button variant="destructive" %}Yes, delete{% endbutton %}
  </div>
{% endmodal %}

{# Open from any element on the page #}
{% modal id="info" title="Information" %}
  <p class="text-sm text-muted-foreground">Modal content goes here.</p>
{% endmodal %}

<button @click="$dispatch('open-modal', { id: 'info' })">Open</button>

{# Load content dynamically with HTMX #}
{% modal id="edit" title="Edit item" %}
  <div id="edit-body"></div>
{% endmodal %}

<button hx-get="/items/42/edit/" hx-target="#edit-body"
        @click="$dispatch('open-modal', { id: 'edit' })">Edit</button>
```

---

### Toast

```bash
silkui add toast
```

Place **once** in `base.html`, inside `<body x-data>`:

```django
<body x-data>
  ...
  {% toast %}
</body>
```

**Trigger from any element:**

```html
<button @click="$dispatch('toast', { title: 'Saved!' })">Save</button>

<button @click="$dispatch('toast', { title: 'Done', description: 'Changes saved.', variant: 'success' })">
  Success
</button>

<button @click="$dispatch('toast', { title: 'Error', description: 'Try again.', variant: 'destructive' })">
  Error
</button>
```

**Toast event payload**

| Key | Values | Description |
|---|---|---|
| `title` | string | Toast heading (required) |
| `description` | string | Optional subtitle |
| `variant` | `default` `success` `destructive` | Visual style |

**Trigger from a Django view (HTMX):**

```python
def save(request):
    response = HttpResponse()
    response["HX-Trigger"] = '{"toast": {"title": "Saved!", "variant": "success"}}'
    return response
```

---

## HTMX integration

Every component accepts `hx_*` kwargs. Underscores convert to hyphens automatically:

```django
{% button hx_post="/save/" hx_target="#result" hx_swap="outerHTML" %}Save{% endbutton %}
{% input name="q" hx_get="/search/" hx_trigger="keyup changed delay:300ms" hx_target="#results" %}
```

`data_*` kwargs work the same way:

```django
{% button data_controller="confirm" data_message="Are you sure?" %}Delete{% endbutton %}
```

---

## Theming

Edit `static/css/silkui.css` to change colors and radius. All components use these CSS variables:

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --destructive: 0 84.2% 60.2%;
  --radius: 0.5rem;
  /* ... */
}
```

One change propagates to every component that uses that variable.

---

## Formatter

Django template tags **must stay on a single line**. Prettier and most HTML formatters break them when reformatting across lines.

`silkui init` automatically configures [djlint](https://djlint.com/) as the HTML formatter in `.vscode/settings.json`. djlint understands Django syntax and formats without breaking tags. VS Code will prompt you to install it on first open.

This only affects the current workspace — your other projects (React, Flask, etc.) are unaffected.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Issues and feedback: [github.com/huguescodeur/silkui/issues](https://github.com/huguescodeur/silkui/issues)

---

## License

MIT — see [LICENSE](LICENSE).
