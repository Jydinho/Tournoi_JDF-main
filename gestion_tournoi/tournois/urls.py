from django.urls import path, include
from rest_framework.routers import DefaultRouter
#GenreViewSet, ModeDeJeuViewSet, JeuViewSet, TypeDeTournoiViewSet, AdresseViewSet, ClubViewSet,
#JoueurViewSet, TypeSponsorViewSet, SponsorViewSet, TournoiViewSet, RencontreViewSet, 
#ScoreViewSet, InscriptionViewSet
from . import views

router = DefaultRouter()
# Le r' permet de faire une espèce de regex pour corriger les liens
router.register(r'genre', views.GenreViewSet)
router.register(r'mode_de_jeu', views.ModeDeJeuViewSet)
router.register(r'jeu', views.JeuViewSet)
router.register(r'type_de_tournoi', views.TypeDeTournoiViewSet)
router.register(r'adresse', views.AdresseViewSet)
router.register(r'club', views.ClubViewSet)
router.register(r'joueur', views.JoueurViewSet)
router.register(r'type_de_sponsor', views.TypeSponsorViewSet)
router.register(r'sponsor', views.SponsorViewSet)
router.register(r'tournoi', views.TournoiViewSet)
router.register(r'rencontre', views.RencontreViewSet)
router.register(r'score', views.ScoreViewSet)
router.register(r'inscription', views.InscriptionViewSet)


#
#
#

urlpatterns = [
    path('', include(router.urls)),
]