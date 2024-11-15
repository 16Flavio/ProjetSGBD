# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classement(models.Model):
    niveau = models.IntegerField(db_column='Niveau', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classement'


class Equipe(models.Model):
    nom_equipe = models.CharField(db_column='Nom_Equipe', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipe'


class Forme(models.Model):
    email = models.OneToOneField('Utilisateur', models.DO_NOTHING, db_column='Email', primary_key=True)  # Field name made lowercase. The composite primary key (Email, Nom_Equipe) found, that is not supported. The first column is selected.
    nom_equipe = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='Nom_Equipe')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forme'
        unique_together = (('email', 'nom_equipe'),)


class MatchDeTournoi(models.Model):
    id_match = models.AutoField(db_column='ID_Match', primary_key=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=50, blank=True, null=True)  # Field name made lowercase.
    points_match = models.IntegerField(db_column='Points_match', blank=True, null=True)  # Field name made lowercase.
    date_heure_match = models.DateTimeField(db_column='Date_Heure_Match', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idtournoi = models.ForeignKey('Tournoi', models.DO_NOTHING, db_column='idTournoi', blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Type', models.DO_NOTHING, db_column='Type', blank=True, null=True)  # Field name made lowercase.
    numÚro_terrain = models.ForeignKey('Terrain', models.DO_NOTHING, db_column='NumÚro_Terrain', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'match_de_tournoi'


class Participe(models.Model):
    email = models.OneToOneField('Utilisateur', models.DO_NOTHING, db_column='Email', primary_key=True)  # Field name made lowercase. The composite primary key (Email, idTournoi) found, that is not supported. The first column is selected.
    idtournoi = models.ForeignKey('Tournoi', models.DO_NOTHING, db_column='idTournoi')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participe'
        unique_together = (('email', 'idtournoi'),)


class Permission(models.Model):
    role = models.CharField(db_column='Role', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permission'


class Sexe(models.Model):
    sexe = models.CharField(db_column='Sexe', primary_key=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sexe'


class Sports(models.Model):
    sport_type = models.CharField(db_column='Sport_Type', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sports'


class Terrain(models.Model):
    numÚro_terrain = models.IntegerField(db_column='NumÚro_Terrain', primary_key=True)  # Field name made lowercase.
    commentaire = models.TextField(db_column='Commentaire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terrain'


class Tournoi(models.Model):
    idtournoi = models.AutoField(db_column='idTournoi', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tournoi'


class Type(models.Model):
    type = models.CharField(db_column='Type', primary_key=True, max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'


class Utilisateur(models.Model):
    email = models.CharField(db_column='Email', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sexe = models.ForeignKey(Sexe, models.DO_NOTHING, db_column='Sexe', blank=True, null=True)  # Field name made lowercase.
    sport_type = models.ForeignKey(Sports, models.DO_NOTHING, db_column='Sport_Type', blank=True, null=True)  # Field name made lowercase.
    niveau = models.ForeignKey(Classement, models.DO_NOTHING, db_column='Niveau', blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey(Permission, models.DO_NOTHING, db_column='Role', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilisateur'
