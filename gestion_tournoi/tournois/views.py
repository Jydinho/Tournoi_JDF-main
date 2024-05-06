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

    def perform_create(self, serializer):
        data = serializer.save()        
        #self.update_score(instance)
        if data.status == 'finie':
            self.update_score_joueur1(data)
            self.update_score_joueur2(data)
    
    def perform_update(self, serializer):
        instance = serializer.save()        
        #self.update_score(instance)
        if instance.status == 'finie':
            self.update_score_joueur1(instance)
            self.update_score_joueur2(instance)
        

    def update_score_joueur1(self, rencontre):
        print("JEPASSEEEEEEEE||||||||||||||||||||||||||||||||||||||||||||||")
        score1, _ = Score.objects.get_or_create(fk_joueur_id=rencontre.fk_joueur1.id, fk_tournoi_id=rencontre.fk_tournoi.id)
        score1.partie_jouees+=1            
        if rencontre.resultat_un > rencontre.resultat_deux:
            score1.victoires+=1                                  
        elif rencontre.resultat_un < rencontre.resultat_deux:
            score1.defaites+=1                                
        else:
            score1.egalites+=1                                
        score1.save()
            
    def update_score_joueur2(self, rencontre):     
        score2, _ = Score.objects.get_or_create(fk_joueur_id=rencontre.fk_joueur2.id, fk_tournoi_id=rencontre.fk_tournoi.id) 
        score2.partie_jouees+=1
        if rencontre.resultat_un > rencontre.resultat_deux:
            score2.defaites+=1                    
        elif rencontre.resultat_un < rencontre.resultat_deux:                
            score2.victoires+=1 
        else:                
            score2.egalites+=1
        score2.save()
        
class ScoreViewSet(viewsets.ModelViewSet):
    queryset=Score.objects.all()
    serializer_class = ScoreSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset=Inscription.objects.all()
    serializer_class = InscriptionSerializer
