from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


def submit_form(request):
    username = request.POST.get('username')
    if username:
        message = f"Formulaire soumis avec succès par <strong>{username} {id}</strong>!"
    else:
        message = "Nom non fourni."
    return JsonResponse({'message': message})

def update_user(request, id,fruit):
    username = request.POST.get('username')
    if username:
        message = f"Formulaire soumis avec succès par <strong>{username} {id}: {fruit}</strong>!"
    else:
        message = "Nom non fourni."
    return JsonResponse({'message': message})


def index(request):
    return render(request, 'index.html')

# Vue Django pour l'URL htmx

def htmx_view(request):
    return HttpResponse('<p>Réponse de HTMX</p>', content_type='text/html')



