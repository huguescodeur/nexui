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

    # Capture all HTMX-related attributes
    htmx_attrs = []

    # Construction de l'URL dynamique via reverse
    if 'url_name' in kwargs:
        method = kwargs.get('method', 'post').lower()

        # Récupérer les paramètres dynamiques de l'URL
        url_params = kwargs.get('url_params', [])

        # Si les paramètres sont en chaîne de caractères, les convertir en liste
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

    # Combine HTMX attributes
    context['attributes'] = mark_safe(' '.join(htmx_attrs))

    # Add any extra attributes if specified
    if 'attrs' in kwargs:
        context['attributes'] = mark_safe(f"{context['attributes']} {kwargs['attrs']}")

    return context

# from django import template
# from django.urls import reverse
# from django.utils.safestring import mark_safe

# register = template.Library()

# @register.inclusion_tag('components/button.html')
# def button(**kwargs):
#     context = {
#         'label': kwargs.get('label', 'Button'),
#         'type': 'button',
#         'class': kwargs.get('class', 'bg-blue-500 text-white hover:bg-blue-600'),
#         'icon': kwargs.get('icon'),
#         'icon_type': kwargs.get('icon_type', 'emoji'),
#         'icon_position': kwargs.get('icon_position', 'left'),
#         'icon_size': kwargs.get('icon_size', 'base'),
#         'icon_color': kwargs.get('icon_color'),
#         'disabled': str(kwargs.get('disabled', False)).lower() in ('true', '1'),
#     }

#     htmx_attrs = []

#     # Construction de l'URL dynamique via reverse
#     if 'url_name' in kwargs:
#         method = kwargs.get('method', 'post').lower()
#         # Résoudre l'URL dans le backend
#         url = reverse(kwargs['url_name'])  # Nous résolvons l'URL ici
#         htmx_attrs.append(f'hx-{method}="{url}"')

#     # Ajout des autres attributs HTMX
#     if 'target' in kwargs:
#         htmx_attrs.append(f'hx-target="{kwargs["target"]}"')
#     if 'swap' in kwargs:
#         htmx_attrs.append(f'hx-swap="{kwargs["swap"]}"')
#     if 'trigger' in kwargs:
#         htmx_attrs.append(f'hx-trigger="{kwargs["trigger"]}"')
#     if 'indicator' in kwargs:
#         htmx_attrs.append(f'hx-indicator="{kwargs["indicator"]}"')
#     if 'confirm' in kwargs:
#         htmx_attrs.append(f'hx-confirm="{kwargs["confirm"]}"')

#     # Assemblage des attributs
#     context['attributes'] = mark_safe(' '.join(htmx_attrs))

#     # Ajout des attributs supplémentaires si spécifiés
#     if 'attrs' in kwargs:
#         context['attributes'] = mark_safe(str(context['attributes']) + ' ' + kwargs['attrs'])

#     return context
