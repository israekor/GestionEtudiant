from django.urls import path
from . import html_views

urlpatterns = [
    path('',                     html_views.list_utilisateurs,   name='html_list'),
    path('create/',              html_views.create_utilisateur,  name='html_create'),
    path('<int:pk>/',            html_views.detail_utilisateur,  name='html_detail'),
    path('<int:pk>/edit/',       html_views.update_utilisateur,  name='html_update'),
    path('<int:pk>/delete/',     html_views.delete_utilisateur,  name='html_delete'),
]