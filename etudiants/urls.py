from django.urls import path
from . import views

urlpatterns = [
    path('formations/', views.liste_formations, name='liste_formations'),
    path('inscrire/<int:pk>/', views.inscrire, name='inscrire'),
    path('profil/', views.mon_profil, name='mon_profil'),
]
