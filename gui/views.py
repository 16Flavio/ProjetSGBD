from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'gui/home.html', context={"current_tab": "home"})
def calendrier(request):
    return render(request, 'gui/calendrier.html', context={"current_tab": "calendrier"})

def tournois(request):
    return render(request, 'gui/tournois.html', context={"current_tab": "tournois"})

def profil(request):
    return render(request, 'gui/profil.html', context={"current_tab": "profil"})

def joueurs(request):
    return render(request, 'gui/joueurs.html', context={"current_tab": "joueurs"})

def save_customer(request):
    customer_name = request.POST.get('customer_name', '')
    return render(request, "gui/welcome.html", context={'customer_name': customer_name})