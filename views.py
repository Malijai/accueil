from django.shortcuts import render


def accueil(request):
    # Accueil observatoire smj
    return render(request, "index.html")

