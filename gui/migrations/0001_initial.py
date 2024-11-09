# Generated by Django 5.1.3 on 2024-11-08 20:37

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classement',
            fields=[
                ('niveau', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('nom_equipe', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sexe',
            fields=[
                ('sexe', models.CharField(default=0, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('sport_type', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('numero_terrain', models.IntegerField(primary_key=True, serialize=False)),
                ('commentaire', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('idtournoi', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDeTournoi',
            fields=[
                ('id_match', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.CharField(default=0, max_length=50)),
                ('points_match', models.IntegerField(default=0)),
                ('date_heure_match', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='Equipe1/Equipe2')),
                ('numero_terrain', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.terrain')),
                ('idtournoi', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.tournoi')),
                ('type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.type')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipe', models.ManyToManyField(blank=True, to='gui.equipe')),
                ('niveau', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.classement')),
                ('sexe', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.sexe')),
                ('sport_type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gui.sports')),
                ('tournoi', models.ManyToManyField(blank=True, to='gui.tournoi')),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]