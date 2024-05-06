from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournois.models import *
from .forms import GenreCreer, ModeDeJeuCreer, JeuCreer, TypeDeTournoiCreer


# Create your views here.
def genre_liste(request):
    if request.method == 'GET':    
        genre_list_db = Genre.objects.all()
        return render(request, 'front/genre_liste.html', {'genres' : genre_list_db})
    
def mode_de_jeu_liste(request):
    if request.method == 'GET':
        modes_de_jeux = ModeDeJeu.objects.all()
        return render(request, 'front/mode_de_jeu_liste.html', {'modes_de_jeux' : modes_de_jeux})

def jeu_liste(request):
    if request.method == 'GET':
        jeux = Jeu.objects.all()
        return render(request, 'front/jeu_liste.html', {'jeux' : jeux})

def type_de_tournoi_liste(request):
    if request.method == 'GET':
        type_de_tournoi = TypeDeTournoi.objects.all()
        return render(request, 'front/type_de_tournoi_liste.html', {'types_de_tournois' : type_de_tournoi})

def genre_creer(request):
    if request.method == 'POST':
        genre_create = GenreCreer(request.POST)
        if genre_create.is_valid():
            genre_create.save()
            return redirect('genre_liste')
        
    return render(request, 'front/genre_creer.html', {'genre' : GenreCreer})

def mode_de_jeu_creer(request):
    if request.method == 'POST':
        mode_de_jeu_create = ModeDeJeuCreer(request.POST)
        if mode_de_jeu_create.is_valid():
            mode_de_jeu_create.save()
            return redirect('mode_de_jeu_liste')
        
    return render(request, 'front/mode_de_jeu_creer.html', {'mode_de_jeu' : ModeDeJeuCreer})


    
def jeu_creer(request):
    if request.method == 'POST':
        jeu_create = JeuCreer(request.POST)
        if jeu_create.is_valid():
            jeu_create.save()
            return redirect('jeu_liste')
        
    return render(request, 'front/jeu_creer.html', {'jeu' : JeuCreer})
    

def type_de_tournoi_creer(request):
    if request.method == 'POST':
        type_de_tournoi_create = TypeDeTournoiCreer(request.POST)
        if type_de_tournoi_create.is_valid():
            type_de_tournoi_create.save()
            return redirect('type_de_tournoi_liste')
        
    return render(request, 'front/type_de_tournoi_creer.html', {'type_de_tournoi' : TypeDeTournoiCreer})




def joueur_liste(request):
    return HttpResponse("Joueur_liste")