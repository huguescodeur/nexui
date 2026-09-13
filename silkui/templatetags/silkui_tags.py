from django.template import Library, Node
from django.template.base import token_kwargs
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.text import slugify

register = Library()


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _resolve(raw_kwargs, context):
    resolved = {}
    for key, val in raw_kwargs.items():
        try:
            resolved[key] = val.resolve(context)
        except Exception:
            resolved[key] = ""
    return resolved


def _build_attrs(kwargs):
    parts = []
    if kwargs.get("attrs"):
        parts.append(str(kwargs["attrs"]))
    for key, value in kwargs.items():
        if key.startswith("hx_"):
            parts.append(f'hx-{key[3:].replace("_", "-")}="{value}"')
        elif key.startswith("data_"):
            parts.append(f'data-{key[5:].replace("_", "-")}="{value}"')
    return " ".join(parts)


def _clean(kwargs):
    return {k: v for k, v in kwargs.items() if not k.startswith(("hx_", "data_")) and k != "attrs"}


def _render(template_name, ctx):
    return mark_safe(render_to_string(template_name, ctx))


# ---------------------------------------------------------------------------
# SlotNode — generic block tag that renders a template with {{ slot }}
# ---------------------------------------------------------------------------

class SlotNode(Node):
    def __init__(self, template_name, nodelist, raw_kwargs):
        self.template_name = template_name
        self.nodelist = nodelist
        self.raw_kwargs = raw_kwargs

    def render(self, context):
        slot = mark_safe(self.nodelist.render(context))
        kwargs = _resolve(self.raw_kwargs, context)
        return _render(self.template_name, {
            "slot": slot,
            "attrs": mark_safe(_build_attrs(kwargs)),
            **_clean(kwargs),
        })


def _block(template_name, end_tag):
    """Factory — creates a block tag that wraps its content in a component template."""
    def tag_func(parser, token):
        bits = token.split_contents()
        raw_kwargs = token_kwargs(bits[1:], parser)
        nodelist = parser.parse((end_tag,))
        parser.delete_first_token()
        return SlotNode(template_name, nodelist, raw_kwargs)
    return tag_func


# ---------------------------------------------------------------------------
# Button
#
#   {% button %}Save{% endbutton %}
#   {% button variant="destructive" %}Delete{% endbutton %}
#   {% button variant="outline" size="sm" hx_post="/save/" %}Send{% endbutton %}
# ---------------------------------------------------------------------------
register.tag("button", _block("components/button.html", "endbutton"))


# ---------------------------------------------------------------------------
# Badge
#
#   {% badge %}New{% endbadge %}
#   {% badge variant="destructive" %}Error{% endbadge %}
# ---------------------------------------------------------------------------
register.tag("badge", _block("components/badge.html", "endbadge"))


# ---------------------------------------------------------------------------
# Alert
#
#   {% alert %}
#     {% alert_title %}Heads up!{% endalert_title %}
#     {% alert_description %}Something happened.{% endalert_description %}
#   {% endalert %}
#
#   {% alert variant="destructive" %}
#     {% alert_title %}Error{% endalert_title %}
#     {% alert_description %}Your session expired.{% endalert_description %}
#   {% endalert %}
# ---------------------------------------------------------------------------
register.tag("alert", _block("components/alert.html", "endalert"))
register.tag("alert_title", _block("components/alert-title.html", "endalert_title"))
register.tag("alert_description", _block("components/alert-description.html", "endalert_description"))


# ---------------------------------------------------------------------------
# Card
#
#   {% card %}
#     {% card_header %}
#       {% card_title %}Revenue{% endcard_title %}
#       {% card_description %}Monthly earnings{% endcard_description %}
#     {% endcard_header %}
#     {% card_content %}
#       <p class="text-3xl font-bold">$45,231</p>
#       {% button variant="outline" size="sm" %}View all{% endbutton %}
#     {% endcard_content %}
#     {% card_footer %}
#       {% button %}Save{% endbutton %}
#     {% endcard_footer %}
#   {% endcard %}
# ---------------------------------------------------------------------------
register.tag("card", _block("components/card.html", "endcard"))
register.tag("card_header", _block("components/card-header.html", "endcard_header"))
register.tag("card_title", _block("components/card-title.html", "endcard_title"))
register.tag("card_description", _block("components/card-description.html", "endcard_description"))
register.tag("card_content", _block("components/card-content.html", "endcard_content"))
register.tag("card_footer", _block("components/card-footer.html", "endcard_footer"))


# ---------------------------------------------------------------------------
# Input  (form element — not a container, stays as simple tag)
#
#   {% input name="email" label="Email" type="email" %}
#   {% input name="search" icon="🔍" icon_position="left" hx_get="/search/" hx_trigger="keyup changed delay:300ms" hx_target="#results" %}
# ---------------------------------------------------------------------------
@register.simple_tag
def input(**kwargs):
    return _render("components/input.html", {
        "type":            kwargs.get("type", "text"),
        "name":            kwargs.get("name", ""),
        "id":              kwargs.get("id", kwargs.get("name", "")),
        "value":           kwargs.get("value", ""),
        "placeholder":     kwargs.get("placeholder", ""),
        "label":           kwargs.get("label", ""),
        "required":        kwargs.get("required", False),
        "disabled":        kwargs.get("disabled", False),
        "readonly":        kwargs.get("readonly", False),
        "hint":            kwargs.get("hint", ""),
        "error":           kwargs.get("error", ""),
        "icon":            kwargs.get("icon", ""),
        "icon_position":   kwargs.get("icon_position", "left"),
        "container_class": kwargs.get("container_class", ""),
        "input_class":     kwargs.get("input_class", ""),
        "label_class":     kwargs.get("label_class", ""),
        "wrapper_class":   kwargs.get("wrapper_class", "relative"),
        "attrs":           mark_safe(_build_attrs(kwargs)),
    })


# ---------------------------------------------------------------------------
# Modal
#
#   {% modal id="confirm" title="Are you sure?" description="This cannot be undone." %}
#     <p class="text-sm text-muted-foreground">All data will be removed.</p>
#     <div class="mt-4 flex justify-end gap-2">
#       {% button variant="outline" %}Cancel{% endbutton %}
#       {% button variant="destructive" %}Delete{% endbutton %}
#     </div>
#   {% endmodal %}
#
#   Open with trigger_label param or from anywhere:
#     <button @click="$dispatch('open-modal', { id: 'confirm' })">Open</button>
# ---------------------------------------------------------------------------
register.tag("modal", _block("components/modal.html", "endmodal"))


# ---------------------------------------------------------------------------
# Tabs
#
#   {% tabs active="account" %}
#     {% tab id="account" label="Account" %}
#       {% input name="username" label="Username" %}
#       {% button %}Save{% endbutton %}
#     {% endtab %}
#     {% tab id="settings" label="Settings" %}
#       Settings content here.
#     {% endtab %}
#   {% endtabs %}
# ---------------------------------------------------------------------------

class TabNode(Node):
    def __init__(self, tab_id, label, nodelist):
        self.tab_id = tab_id
        self.label = label
        self.nodelist = nodelist

    def render(self, context):
        return ""


class TabsNode(Node):
    def __init__(self, nodelist, raw_kwargs):
        self.nodelist = nodelist
        self.raw_kwargs = raw_kwargs

    def render(self, context):
        tabs = []
        for node in self.nodelist:
            if isinstance(node, TabNode):
                tabs.append({
                    "id":      node.tab_id.resolve(context) if node.tab_id else "",
                    "label":   node.label.resolve(context) if node.label else "",
                    "content": mark_safe(node.nodelist.render(context)),
                })
        kwargs = _resolve(self.raw_kwargs, context)
        active = kwargs.get("active", tabs[0]["id"] if tabs else "")
        return _render("components/tabs.html", {
            "tabs":        tabs,
            "active_tab":  active,
            "class":       kwargs.get("class", ""),
            "tabs_class":  kwargs.get("tabs_class", ""),
            "panel_class": kwargs.get("panel_class", ""),
        })


@register.tag("tabs")
def tabs_tag(parser, token):
    bits = token.split_contents()
    raw_kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(("endtabs",))
    parser.delete_first_token()
    return TabsNode(nodelist, raw_kwargs)


@register.tag("tab")
def tab_tag(parser, token):
    bits = token.split_contents()
    raw_kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(("endtab",))
    parser.delete_first_token()
    return TabNode(
        tab_id=raw_kwargs.get("id"),
        label=raw_kwargs.get("label"),
        nodelist=nodelist,
    )


# ---------------------------------------------------------------------------
# Dropdown
#
#   {% dropdown trigger_label="My Account" %}
#     {% dropdown_item href="/profile/" %}Profile{% enddropdown_item %}
#     {% dropdown_item href="/settings/" %}Settings{% enddropdown_item %}
#     {% dropdown_separator %}
#     {% dropdown_item href="/logout/" %}Logout{% enddropdown_item %}
#   {% enddropdown %}
# ---------------------------------------------------------------------------

class DropdownItemNode(Node):
    def __init__(self, nodelist, raw_kwargs):
        self.nodelist = nodelist
        self.raw_kwargs = raw_kwargs

    def render(self, context):
        kwargs = _resolve(self.raw_kwargs, context)
        attrs = _build_attrs(kwargs)
        content = self.nodelist.render(context)
        href = kwargs.get("href", "#")
        disabled_cls = "pointer-events-none opacity-50" if kwargs.get("disabled") else ""
        return mark_safe(
            f'<a href="{href}" role="menuitem" '
            f'class="relative flex cursor-pointer select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none transition-colors hover:bg-accent hover:text-accent-foreground focus:bg-accent focus:text-accent-foreground {disabled_cls}" '
            f'x-on:click="open = false" {attrs}>{content}</a>'
        )


class DropdownSeparatorNode(Node):
    def render(self, context):
        return '<div class="-mx-1 my-1 h-px bg-muted"></div>'


register.tag("dropdown", _block("components/dropdown.html", "enddropdown"))


@register.tag("dropdown_item")
def dropdown_item_tag(parser, token):
    bits = token.split_contents()
    raw_kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(("enddropdown_item",))
    parser.delete_first_token()
    return DropdownItemNode(nodelist, raw_kwargs)


@register.tag("dropdown_separator")
def dropdown_separator_tag(parser, token):
    token.split_contents()
    return DropdownSeparatorNode()


# ---------------------------------------------------------------------------
# Checkbox
#
#   {% checkbox name="terms" label="J'accepte les CGU" %}
#   {% checkbox name="newsletter" label="Recevoir les emails" checked=True hint="Désactivable à tout moment." %}
# ---------------------------------------------------------------------------
@register.simple_tag
def checkbox(**kwargs):
    name = kwargs.get("name", "")
    return _render("components/checkbox.html", {
        "name":            name,
        "id":              kwargs.get("id", name),
        "value":           kwargs.get("value", ""),
        "checked":         kwargs.get("checked", False),
        "label":           kwargs.get("label", ""),
        "required":        kwargs.get("required", False),
        "disabled":        kwargs.get("disabled", False),
        "hint":            kwargs.get("hint", ""),
        "error":           kwargs.get("error", ""),
        "container_class": kwargs.get("container_class", ""),
        "input_class":     kwargs.get("input_class", ""),
        "label_class":     kwargs.get("label_class", ""),
        "attrs":           mark_safe(_build_attrs(kwargs)),
    })


# ---------------------------------------------------------------------------
# Radio
#
#   {% radio name="plan" value="free" label="Free" %}
#   {% radio name="plan" value="pro" label="Pro" checked=True %}
#
#   L'id par défaut est "name-value" pour éviter les collisions dans un groupe.
# ---------------------------------------------------------------------------
@register.simple_tag
def radio(**kwargs):
    name = kwargs.get("name", "")
    value = kwargs.get("value", "")
    default_id = f"{slugify(name)}-{slugify(value)}" if name and value else slugify(name)
    return _render("components/radio.html", {
        "name":            name,
        "id":              kwargs.get("id", default_id),
        "value":           value,
        "checked":         kwargs.get("checked", False),
        "label":           kwargs.get("label", ""),
        "required":        kwargs.get("required", False),
        "disabled":        kwargs.get("disabled", False),
        "container_class": kwargs.get("container_class", ""),
        "input_class":     kwargs.get("input_class", ""),
        "label_class":     kwargs.get("label_class", ""),
        "attrs":           mark_safe(_build_attrs(kwargs)),
    })


# ---------------------------------------------------------------------------
# Textarea
#
#   {% textarea name="message" label="Message" placeholder="Write..." rows=4 %}
#   {% textarea name="bio" label="Bio" value=form.bio.value hint="Max 160 chars." error=form.bio.errors.0 %}
# ---------------------------------------------------------------------------
@register.simple_tag
def textarea(**kwargs):
    return _render("components/textarea.html", {
        "name":            kwargs.get("name", ""),
        "id":              kwargs.get("id", kwargs.get("name", "")),
        "value":           kwargs.get("value", ""),
        "placeholder":     kwargs.get("placeholder", ""),
        "label":           kwargs.get("label", ""),
        "required":        kwargs.get("required", False),
        "disabled":        kwargs.get("disabled", False),
        "readonly":        kwargs.get("readonly", False),
        "rows":            kwargs.get("rows", ""),
        "hint":            kwargs.get("hint", ""),
        "error":           kwargs.get("error", ""),
        "container_class": kwargs.get("container_class", ""),
        "input_class":     kwargs.get("input_class", ""),
        "label_class":     kwargs.get("label_class", ""),
        "attrs":           mark_safe(_build_attrs(kwargs)),
    })


# ---------------------------------------------------------------------------
# Select
#
#   {% select name="role" label="Role" choices=role_choices placeholder="Pick one" %}
#   {% select name="country" label="Country" choices=form.country.field.choices value=form.country.value %}
#
#   choices = liste de 2-tuples: [("us", "United States"), ("uk", "United Kingdom")]
# ---------------------------------------------------------------------------
@register.simple_tag
def select(**kwargs):
    return _render("components/select.html", {
        "name":            kwargs.get("name", ""),
        "id":              kwargs.get("id", kwargs.get("name", "")),
        "value":           kwargs.get("value", ""),
        "placeholder":     kwargs.get("placeholder", ""),
        "label":           kwargs.get("label", ""),
        "required":        kwargs.get("required", False),
        "disabled":        kwargs.get("disabled", False),
        "choices":         kwargs.get("choices", []),
        "hint":            kwargs.get("hint", ""),
        "error":           kwargs.get("error", ""),
        "container_class": kwargs.get("container_class", ""),
        "input_class":     kwargs.get("input_class", ""),
        "label_class":     kwargs.get("label_class", ""),
        "attrs":           mark_safe(_build_attrs(kwargs)),
    })


# ---------------------------------------------------------------------------
# Table
#
#   {% table %}
#     {% table_header %}
#       {% table_row %}
#         {% table_head %}Name{% endtable_head %}
#         {% table_head %}Status{% endtable_head %}
#       {% endtable_row %}
#     {% endtable_header %}
#     {% table_body %}
#       {% for user in users %}
#       {% table_row %}
#         {% table_cell %}{{ user.name }}{% endtable_cell %}
#         {% table_cell %}{{ user.status }}{% endtable_cell %}
#       {% endtable_row %}
#       {% endfor %}
#     {% endtable_body %}
#   {% endtable %}
# ---------------------------------------------------------------------------
register.tag("table",         _block("components/table.html",         "endtable"))
register.tag("table_header",  _block("components/table-header.html",  "endtable_header"))
register.tag("table_body",    _block("components/table-body.html",    "endtable_body"))
register.tag("table_footer",  _block("components/table-footer.html",  "endtable_footer"))
register.tag("table_row",     _block("components/table-row.html",     "endtable_row"))
register.tag("table_head",    _block("components/table-head.html",    "endtable_head"))
register.tag("table_cell",    _block("components/table-cell.html",    "endtable_cell"))
register.tag("table_caption", _block("components/table-caption.html", "endtable_caption"))


# ---------------------------------------------------------------------------
# Separator
#
#   {% separator %}
#   {% separator orientation="vertical" class="mx-4" %}
# ---------------------------------------------------------------------------
@register.simple_tag
def separator(**kwargs):
    return _render("components/separator.html", {
        "orientation": kwargs.get("orientation", "horizontal"),
        "class":       kwargs.get("class", ""),
    })


# ---------------------------------------------------------------------------
# Toast  — place once in base.html
#
#   {% toast %}
#
#   Trigger from any element:
#     @click="$dispatch('toast', { title: 'Done!', variant: 'success' })"
# ---------------------------------------------------------------------------
@register.simple_tag
def toast(**kwargs):
    return _render("components/toast.html", {"class": kwargs.get("class", "")})
