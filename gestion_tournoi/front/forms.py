from django.forms import ModelForm
from tournois.models import Genre

#class GenreCreer(ModelForm):
class GenreCreer(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
