from rest_framework import serializers
from .models import Genre, ModeDeJeu, Jeu, TypeDeTournoi, Adresse, Club, Joueur, TypeSponsor, Sponsor, Tournoi, Rencontre, Score, Inscription

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ModeDeJeuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModeDeJeu        
        fields = '__all__'


class JeuSerializer(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        write_only=True,
        source='genres' 
    )
    genre_detail = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='genre-detail',
        source='genres'
    )
    mode_de_jeu_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ModeDeJeu.objects.all(),
        write_only=True,
        source='modes_de_jeux'
    )
    mode_de_jeu_detail = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='modedejeu-detail',
        source='modes_de_jeux'
    )
    class Meta:
        model = Jeu
        fields = ['url', 'id', 'nom', 'genre_id', 'genre_detail', 'mode_de_jeu_id', 'mode_de_jeu_detail']


class TypeDeTournoiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeDeTournoi
        fields = '__all__'


class AdresseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adresse
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    adresse_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Adresse.objects.all(),
        write_only=True,
        source='fk_adresse'
    )
    adresse_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='adresse-detail',
        source='fk_adresse'
    )
    class Meta:
        model = Club
        fields = ['url', 'id', 'nom', 'nationalite', 'adresse_id', 'adresse_detail']


class JoueurSerializer(serializers.ModelSerializer):
    adresse_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Adresse.objects.all(),
        write_only=True,
        source='fk_adresse'
    )
    adresse_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='adresse-detail',
        source='fk_adresse'
    )
    jeu_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Jeu.objects.all(),
        write_only=True,
        source='jeux'
    )
    jeu_detail = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='jeu-detail',
        source='jeux'
    )
    class Meta:
        model = Joueur
        fields = ['url', 'id', 'nom', 'prenom', 'pseudo', 'email', 'telephone', 
                  'date_naissance', 'nationalite', 'adresse_id', 'adresse_detail',
                  'jeu_id', 'jeu_detail']
        

class TypeSponsorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeSponsor
        fields = '__all__'


class SponsorSerializer(serializers.ModelSerializer):
    type_sponsor_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=TypeSponsor.objects.all(),
        write_only=True,
        source='fk_type_sponsor'
    )
    type_sponsor_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='typesponsor-detail',
        source='fk_type_sponsor'
    )
    class Meta:
        model = Sponsor
        fields = ['url', 'id', 'nom', 'lien', 'contact', 'logo', 'type_sponsor_id', 'type_sponsor_detail']
        

class TournoiSerializer(serializers.ModelSerializer):
    type_tournoi_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=TypeDeTournoi.objects.all(),
        write_only=True,
        source='types_tournois'
    )
    type_tournoi_detail = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='typedetournoi-detail',
        source='types_tournois'
    )
    sponsor_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Sponsor.objects.all(),
        write_only=True,
        source='sponsors'
    )
    sponsor_detail = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='sponsor-detail',
        source='sponsors'
    )
    jeu_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Jeu.objects.all(),
        write_only=True,
        source='fk_jeu'
    )
    jeu_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='jeu-detail',
        source='fk_jeu'
    )
    adresse_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Adresse.objects.all(),
        write_only=True,
        source='fk_adresse'
    )
    adresse_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='adresse-detail',
        source='fk_adresse'
    )
    class Meta:
        model = Tournoi
        fields = ['url', 'id', 'nom', 'nom_createur', 'prenom_createur', 'email',
                  'date_debut', 'date_fin', 'nombre_de_place', 'paf', 'jeu_id', 'jeu_detail',
                  'adresse_id', 'adresse_detail', 'type_tournoi_id', 'type_tournoi_detail',
                  'sponsor_id', 'sponsor_detail']


class RencontreSerializer(serializers.ModelSerializer):
    joueur1_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Joueur.objects.all(),
        write_only=True,
        source='fk_joueur1'
    )
    joueur1_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='joueur1-detail',
        source='fk_joueur1'
    )
    joueur2_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Joueur.objects.all(),
        write_only=True,
        source='fk_joueur2'
    )
    joueur2_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='joueur2-detail',
        source='fk_joueur2'
    )
    tournoi_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Tournoi.objects.all(),
        write_only=True,
        source='fk_tournoi'
    )
    tournoi_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='tournoi-detail',
        source='fk_tournoi'
    )
    class Meta:
        model = Rencontre
        fields = ['url', 'id', 'joueur1_id', 'joueur1_detail', 'resultat_un', 'joueur2_id',
                  'joueur2_detail', 'resultat_deux', 'tournoi_id', 'tournoi_detail']
        

class ScoreSerializer(serializers.ModelSerializer):
    tournoi_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Tournoi.objects.all(),
        write_only=True,
        source='fk_tournoi'
    )
    tournoi_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='tournoi-detail',
        source='fk_tournoi'
    )
    joueur_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Joueur.objects.all(),
        write_only=True,
        source='fk_joueur'
    )
    joueur_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='joueur-detail',
        source='fk_joueur'
    )
    class Meta:
        model = Score
        fields = ['url', 'id', 'partie_jouees', 'victoires', 'defaites', 'egalites',
                  'tournoi_id', 'tournoi_detail', 'joueur_id', 'joueur_detail']
        

class InscriptionSerializer(serializers.ModelSerializer):
    joueur_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Joueur.objects.all(),
        write_only=True,
        source='fk_joueur'
    )
    joueur_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='joueur-detail',
        source='fk_joueur'
    )
    tournoi_id = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Tournoi.objects.all(),
        write_only=True,
        source='fk_tournoi'
    )
    tournoi_detail = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='tournoi-detail',
        source='fk_tournoi'
    )
    class Meta:
        model = Inscription
        fields = ['url', 'id', 'status', 'date_inscription', 'joueur_id', 'joueur_detail',
                  'tournoi_id', 'tournoi_detail']
        

    #film_set pour faire un reverse. réalisateur qui veux tous ses films.