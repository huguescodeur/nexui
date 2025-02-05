from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse



# def index(request):
#     return render(request, 'index.html')
def index(request):
    if request.htmx:
        return render(request, "form.html")  # Seulement le formulaire
    return render(request, "index.html")


def search_suggestions(request):
    query = request.GET.get('query', '')
    suggestions = []

    # Simuler des suggestions basées sur la saisie de l'utilisateur
    if query:
        suggestions = [
            f'Suggestion {i}' for i in range(1, 6) if query.lower() in f'suggestion {i}'.lower()
        ]

    return JsonResponse({'suggestions': suggestions})

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





