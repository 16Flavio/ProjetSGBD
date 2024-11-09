from email.policy import default
from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User, Group

class Classement(models.Model):
 niveau = models.IntegerField(primary_key=True)
 description = models.TextField(blank=True, null=True)

class Equipe(models.Model):
 nom_equipe = models.CharField(primary_key=True, max_length=50)

class MatchDeTournoi(models.Model):
 id_match = models.AutoField(primary_key=True)
 score = models.CharField(max_length=50, default=0)
 points_match = models.IntegerField(default=0)
 date_heure_match = models.DateTimeField(default= timezone.now)
 description = models.TextField(default='Equipe1/Equipe2')
 idtournoi = models.ForeignKey('Tournoi', on_delete=models.CASCADE, default=0)
 type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
 numero_terrain = models.ForeignKey('Terrain', on_delete=models.CASCADE, default=0)

class GroupPermission(models.Model):
 role = models.OneToOneField(Group, on_delete=models.CASCADE)
 description = models.TextField(blank=True, null=True)

class Sexe(models.Model):
 sexe = models.CharField(primary_key=True, max_length=50, default=0)

class Sports(models.Model):
 sport_type = models.CharField(primary_key=True, max_length=50)
 description = models.TextField(blank=True, null=True)

class Terrain(models.Model):
 numero_terrain = models.IntegerField(primary_key=True)
 commentaire = models.TextField(blank=True, null=True)

class Tournoi(models.Model):
 idtournoi = models.AutoField(primary_key=True)
 nom = models.CharField(max_length=50)
 description = models.TextField(blank=True, null=True)

class Meta:
  db_table = 'gui_tournoi'

class Type(models.Model):
 type = models.CharField(primary_key=True, max_length=50)
 description = models.TextField(blank=True, null=True)

class Utilisateur(models.Model):
 id = models.AutoField(primary_key=True)
 user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
 sexe = models.ForeignKey(Sexe, on_delete=models.CASCADE, default=0)
 sport_type = models.ForeignKey(Sports, on_delete=models.CASCADE, default=0)
 niveau = models.ForeignKey(Classement, on_delete=models.CASCADE, default=0)
 equipe = models.ManyToManyField(Equipe, blank=True)
 tournoi = models.ManyToManyField(Tournoi, blank=True)