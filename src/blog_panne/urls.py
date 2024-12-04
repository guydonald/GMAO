from django.urls import path
from . import views

urlpatterns = [
    path('production/', views.home_pro, name='production'),
    path('maintenance/', views.home_main, name='maintenance'),
    path('administration/', views.home_admin, name='administration'),
    path('maintenance/<str:code>/', views.runwork, name='runwork'),
    path('enregistrer_heure_debut/<str:code>/', views.enregistrer_heure_debut, name='enregistrer_heure_debut'),
    path('enregistrer_heure_fin/<str:code>/', views.enregistrer_heure_fin, name='enregistrer_heure_fin'),
    path('verifier_heures/<str:code>/', views.verifier_heures, name='verifier_heures'),
    path('taches-effectues', views.tache_effectue, name='tache_effectue'),
    path('rapport/<str:code>/', views.faire_rapport, name='faire_rapport'),
path('ajouter-piece-utilisee/<str:code>/', views.ajouter_piece_utilisee, name='ajouter_piece_utilisee'),
]
