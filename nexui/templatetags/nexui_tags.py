from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('components/button.html')
def button(**kwargs):
    context = {
        'label': kwargs.get('label', 'Button'),
        'type': kwargs.get('type', 'button'),
        'class': kwargs.get('class'),
        'icon': kwargs.get('icon'),
        'icon_type': kwargs.get('icon_type', 'emoji'),
        'icon_position': kwargs.get('icon_position', 'left'),
        'icon_size': kwargs.get('icon_size', 'base'),
        'icon_color': kwargs.get('icon_color'),
        'disabled': str(kwargs.get('disabled', False)).lower() in ('true', '1'),
    }

    htmx_attrs = []

    # Construction de l'URL dynamique via reverse
    if 'url_name' in kwargs:
        method = kwargs.get('method', 'post').lower()

        url_params = kwargs.get('url_params', [])

        if isinstance(url_params, str):
            url_params = [p.strip() for p in url_params.split(",")]

        try:
            url = reverse(kwargs['url_name'], args=url_params)
            htmx_attrs.append(f'hx-{method}="{url}"')
        except Exception as e:
            htmx_attrs.append(f'data-error="URL not found: {e}"')

    for key, value in kwargs.items():
        if key.startswith('hx-') or key.startswith('data-hx-'):
            htmx_attrs.append(f'{key}="{value}"')

    context['attributes'] = mark_safe(' '.join(htmx_attrs))

    # Add any extra attributes if specified
    if 'attrs' in kwargs:
        context['attributes'] = mark_safe(f"{context['attributes']} {kwargs['attrs']}")

    return context

