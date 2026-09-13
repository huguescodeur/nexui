from django.shortcuts import render

ROLE_CHOICES = [
    ("admin", "Administrator"),
    ("editor", "Editor"),
    ("viewer", "Viewer"),
]


def index(request):
    return render(request, "index.html", {"role_choices": ROLE_CHOICES})
