from django.contrib import admin
from django.urls import path
from gui.views import home, calendrier, save_customer, tournois, profil, joueurs

urlpatterns = [
    path("", home),
    path('home',home),
    path ("calendrier/", calendrier),
    path("tournois/",tournois),

    path("profil/",profil),
    path("joueurs/",joueurs),
    path ("save/", save_customer),
]
