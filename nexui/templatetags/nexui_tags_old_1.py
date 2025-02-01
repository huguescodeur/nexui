from django import template 
from django.template.loader import render_to_string 
from django.utils.safestring import mark_safe 
 
register = template.Library() 
 
@register.inclusion_tag('components/button.html')
def button(**kwargs):
    context = {
        'label': 'Button',
        'type': 'button',
        'class': 'bg-blue-500 text-white hover:bg-blue-600',
        'icon': None,
        'icon_type': 'emoji',  # 'emoji', 'fa', ou 'unicode'
        'icon_position': 'left',
        'icon_size': 'base',
        'icon_color': None,  # nouvelle option pour la couleur de l'icône
        'disabled': False, 
    }

    if kwargs:
        context.update(kwargs)

    context['disabled'] = str(context['disabled']) in ('true', '1')

    return context



# @register.inclusion_tag('components/button.html')
# def button(**kwargs):
#     context = {
#         'label': 'Button',
#         'type': 'button',
#         'class': 'bg-blue-500 text-white hover:bg-blue-600',
#         'icon': None,  # Icône par défaut : aucune
#         'icon_position': 'left',  # Position de l’icône
#         'icon_size': 'base',  # Taille de l’icône
#         'disabled': False,  # Bouton désactivé ou non
#     }
    
#     if kwargs:
#         context.update(kwargs)
    
#     return context

# @register.inclusion_tag('components/button.html')
# def button(**kwargs):
#     context = {
#         'label': 'Button',
#         'type': 'button',
#         'class': 'bg-blue-500 text-white hover:bg-blue-600'
#     }
    
#     if kwargs:
#         context.update(kwargs)
    
#     return context