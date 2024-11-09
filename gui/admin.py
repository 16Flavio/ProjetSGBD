from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import *

# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Type)
admin.site.register(Tournoi)
admin.site.register(MatchDeTournoi)
admin.site.register(Terrain)
admin.site.register(Classement)
#admin.site.register(Permission)
admin.site.register(Sports)
#admin.site.register(Forme)
admin.site.register(Equipe)
admin.site.register(Sexe)

