from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),        # tes routes API → /api/
    path('', include('users.html_urls')),       # routes HTML → /
]