
from django.urls import path
from users import views

urlpatterns = [
    path('',            views.get_utilisateurs,   name='get_utilisateurs'),
    path('create/',     views.create_utilisateur, name='create'),
    path('<int:pk>/',   views.get_utilisateur, name='getbyid'),
    path('<int:pk>/edit/',   views.update_utilisateur, name='update'),
    path('<int:pk>/delete/', views.delete_utilisateur, name='delete'),
]
