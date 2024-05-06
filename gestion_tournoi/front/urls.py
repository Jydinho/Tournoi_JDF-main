from django.urls import path
from . import views

urlpatterns = [
    path('joueur_liste', views.joueur_liste, name='joueur_liste'),
    path('genre_liste', views.genre_liste, name='genre_liste'),
    path('genre_creer', views.genre_creer, name='genre_creer'),  
    path('mode_de_jeu_liste', views.mode_de_jeu_liste, name='mode_de_jeu_liste'),
    path('mode_de_jeu_creer', views.mode_de_jeu_creer, name='mode_de_jeu_creer'),
    path('jeu_liste', views.jeu_liste, name='jeu_liste'),
    path('jeu_creer', views.jeu_creer, name='jeu_creer'),
    path('type_de_tournoi_liste', views.type_de_tournoi_liste, name='type_de_tournoi_liste'),    
    path('type_de_tournoi_creer', views.type_de_tournoi_creer, name='type_de_tournoi_creer'),
]
