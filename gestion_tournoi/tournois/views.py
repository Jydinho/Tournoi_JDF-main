#from django.shortcuts import render
from .serializers import GenreSerializer, ModeDeJeuSerializer, JeuSerializer, TypeDeTournoiSerializer, AdresseSerializer, ClubSerializer, JoueurSerializer, TypeSponsorSerializer, SponsorSerializer, TournoiSerializer, RencontreSerializer, ScoreSerializer, InscriptionSerializer
from .models import Genre, ModeDeJeu, Jeu, TypeDeTournoi, Adresse, Club, Joueur, TypeSponsor, Sponsor, Tournoi, Rencontre, Score, Inscription
from rest_framework import viewsets

# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ModeDeJeuViewSet(viewsets.ModelViewSet):
    queryset = ModeDeJeu.objects.all()
    serializer_class = ModeDeJeuSerializer


class JeuViewSet(viewsets.ModelViewSet):
    queryset = Jeu.objects.all()
    serializer_class = JeuSerializer


class TypeDeTournoiViewSet(viewsets.ModelViewSet):
    queryset = TypeDeTournoi.objects.all()
    serializer_class = TypeDeTournoiSerializer


class AdresseViewSet(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset=Club.objects.all()
    serializer_class = ClubSerializer


class JoueurViewSet(viewsets.ModelViewSet):
    queryset=Joueur.objects.all()
    serializer_class = JoueurSerializer


class TypeSponsorViewSet(viewsets.ModelViewSet):
    queryset=TypeSponsor.objects.all()
    serializer_class = TypeSponsorSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset=Sponsor.objects.all()
    serializer_class = SponsorSerializer


class TournoiViewSet(viewsets.ModelViewSet):
    queryset=Tournoi.objects.all()
    serializer_class = TournoiSerializer


class RencontreViewSet(viewsets.ModelViewSet):
    queryset=Rencontre.objects.all()
    serializer_class = RencontreSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset=Score.objects.all()
    serializer_class = ScoreSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset=Inscription.objects.all()
    serializer_class = InscriptionSerializer


