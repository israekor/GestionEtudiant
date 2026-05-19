from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard')
    return redirect('liste_formations')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('acces-refuse/', lambda request: __import__('django.shortcuts',
         fromlist=['render']).render(request, 'acces_refuse.html'), name='acces_refuse'),
    path('admin-formations/', include('formations.urls')),
    path('etudiant/', include('etudiants.urls')),
]
