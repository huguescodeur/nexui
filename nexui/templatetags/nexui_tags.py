from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template.base import Node, Token, TokenType
from django.template.loader import render_to_string

register = template.Library()

# ? Button Tag
@register.inclusion_tag('components/button.html')
def button(**kwargs):
    context = {
        'label': kwargs.get('label', 'Button'),
        'type': kwargs.get('type', 'button'),
        'button_class': kwargs.get('button_class'),
        'icon': kwargs.get('icon'),
        'icon_type': kwargs.get('icon_type', 'emoji'),
        'icon_position': kwargs.get('icon_position', 'left'),
        'icon_size': kwargs.get('icon_size', 'base'),
        'icon_color': kwargs.get('icon_color'),
        'disabled': str(kwargs.get('disabled', False)) in ('true', '1'),
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

    # Ajout des attributs supplémentaires
    if 'attrs' in kwargs:
        context['attributes'] = mark_safe(f"{context['attributes']} {kwargs['attrs']}")

    return context


# ? Input Tag
@register.inclusion_tag('components/input.html')
def input_field(**kwargs):
    context = {
        'type': kwargs.get('type', 'text'),
        'name': kwargs.get('name', ''),
        'id': kwargs.get('id', kwargs.get('name', '')),
        'value': kwargs.get('value', ''),
        'placeholder': kwargs.get('placeholder', ''),
        'container_class': kwargs.get('container_class', ''),
        'wrapper_class': kwargs.get('wrapper_class', 'relative'), 
        'label_class': kwargs.get('label_class', ''),
        'input_class': kwargs.get('input_class', ''),
        'label': kwargs.get('label', ''),
        'required': str(kwargs.get('required', False)) in ('true', '1'),
        'disabled': str(kwargs.get('disabled', False)) in ('true', '1'),
        'readonly': str(kwargs.get('readonly', False)) in ('true', '1'),
        'icon': kwargs.get('icon'),
        'icon_type': kwargs.get('icon_type', 'emoji'),
        'icon_position': kwargs.get('icon_position', 'left'),
        'icon_size': kwargs.get('icon_size', 'base'),
        'icon_color': kwargs.get('icon_color'),
    }

    attrs = []

    # Gestion des URLs dynamiques pour HTMX
    if 'url_name' in kwargs:
        method = kwargs.get('method', 'post').lower() 
        url_params = kwargs.get('url_params', [])

        if isinstance(url_params, str):
            url_params = [p.strip() for p in url_params.split(",")]

        try:
            url = reverse(kwargs['url_name'], args=url_params)
            attrs.append(f'hx-{method}="{url}"')
        except Exception as e:
            attrs.append(f'data-error="URL not found: {e}"')

    # Répartition des attributs
    for key, value in kwargs.items():
        if key.startswith(('hx-', 'data-', 'on', 'style')):
            attrs.append(f'{key}="{value}"')

    # Ajout des attributs supplémentaires
    if 'attrs' in kwargs:
        attrs.append(kwargs['attrs'])

    context['input_attributes'] = mark_safe(' '.join(attrs))

    return context
