# Generated by Django 5.1.3 on 2024-12-03 12:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, unique=True)),
                ('heure_debut', models.DateTimeField(blank=True, null=True)),
                ('heure_fin', models.DateTimeField(blank=True, null=True)),
                ('executant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PieceUtilisee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('nombre_utilisee', models.PositiveIntegerField()),
                ('etat', models.CharField(choices=[('NEUF', 'Neuf'), ('RECYCLER', 'Recycler')], max_length=50)),
                ('ordre_travail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_panne.orderwork')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actions', models.TextField()),
                ('observation', models.TextField()),
                ('classe_action', models.CharField(choices=[('AUTOMATISME', 'Automatisme'), ('PLOMBERIE', 'Plomberie'), ('ELECTRIQUE', 'Électrique'), ('MECANIQUE', 'Mécanique'), ('UTILITAIRE', 'Utilitaire')], max_length=50)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ordre_travail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_panne.orderwork')),
                ('pieces_utilisees', models.ManyToManyField(to='blog_panne.pieceutilisee')),
            ],
        ),
    ]
