from django.forms import ModelForm
from tournois.models import Genre, ModeDeJeu, Jeu, TypeDeTournoi

#class GenreCreer(ModelForm):
class GenreCreer(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class ModeDeJeuCreer(ModelForm):
    class Meta:
        model = ModeDeJeu
        fields = '__all__'


class JeuCreer(ModelForm):
    class Meta:
        model = Jeu
        fields = ['id', 'nom', 'genres', 'modes_de_jeux']
        #fields = '__all__'

class TypeDeTournoiCreer(ModelForm):
    class Meta:
        model = TypeDeTournoi
        fields = '__all__'


