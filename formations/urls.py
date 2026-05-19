from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('ajouter/', views.ajouter_formation, name='ajouter_formation'),
    path('modifier/<int:pk>/', views.modifier_formation, name='modifier_formation'),
    path('supprimer/<int:pk>/', views.supprimer_formation,
         name='supprimer_formation'),
]
