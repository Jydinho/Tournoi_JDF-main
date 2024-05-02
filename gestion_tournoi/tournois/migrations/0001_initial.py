# Generated by Django 5.0.4 on 2024-05-02 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rue', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=20)),
                ('commune', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModeDeJeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('lien', models.CharField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='TypeDeTournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('nationalite', models.CharField(max_length=80)),
                ('fk_adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Jeu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('genres', models.ManyToManyField(to='tournois.genre')),
                ('modes_de_jeux', models.ManyToManyField(to='tournois.modedejeu')),
            ],
        ),
        migrations.CreateModel(
            name='Joueur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('pseudo', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=45, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('nationalite', models.CharField(max_length=80)),
                ('fk_adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.adresse')),
                ('jeux', models.ManyToManyField(to='tournois.jeu')),
            ],
        ),
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('nom_createur', models.CharField(max_length=100)),
                ('prenom_createur', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=254)),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('nombre_de_place', models.IntegerField()),
                ('paf', models.CharField(blank=True, max_length=10, null=True)),
                ('reglement', models.TextField()),
                ('fk_adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.adresse')),
                ('fk_jeu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.jeu')),
                ('sponsors', models.ManyToManyField(to='tournois.sponsor')),
                ('types_tournois', models.ManyToManyField(to='tournois.typedetournoi')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partie_jouees', models.IntegerField()),
                ('victoires', models.IntegerField()),
                ('defaites', models.IntegerField()),
                ('egalites', models.IntegerField()),
                ('fk_joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.joueur')),
                ('fk_tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.tournoi')),
            ],
        ),
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultat_un', models.IntegerField(blank='True', null='True')),
                ('resultat_deux', models.IntegerField(blank='True', null='True')),
                ('date_rencontre', models.DateTimeField()),
                ('fk_joueur1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joueur1', to='tournois.joueur')),
                ('fk_joueur2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joueur2', to='tournois.joueur')),
                ('fk_tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.tournoi')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('date_inscription', models.DateField()),
                ('fk_joueur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.joueur')),
                ('fk_tournoi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.tournoi')),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='fk_type_sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournois.typesponsor'),
        ),
    ]
