from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/utilisateurs/', include('users.urls')),   # tes routes API existantes
    path('utilisateurs/', include('users.html_urls')),  # nouvelles routes HTML
]