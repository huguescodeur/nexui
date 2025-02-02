from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse



def index(request):
    return render(request, 'index.html')

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





