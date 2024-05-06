from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournois.models import *
from .forms import GenreCreer


# Create your views here.
def genre_liste(request):
    if request.method == 'GET':    
        genre_list_db = Genre.objects.all()
        return render(request, 'front/genre_liste.html', {'genres' : genre_list_db})
    

def genre_creer(request):
    if request.method == 'POST':
        genre_create = GenreCreer(request.POST)
        if genre_create.is_valid():
            genre_create.save()
            return redirect('genre_liste')
        
    return render(request, 'front/genre_creer.html', {'genre' : GenreCreer})


def joueur_liste(request):
    return HttpResponse("Joueur_liste")