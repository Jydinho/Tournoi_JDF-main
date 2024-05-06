from django.urls import path
from . import views

urlpatterns = [
    path('joueur_liste', views.joueur_liste, name='joueur_liste'),
    path('genre_liste', views.genre_liste, name='genre_liste'),
    path('genre_creer', views.genre_creer, name='genre_creer'),  
]
