from django.shortcuts import render, get_object_or_404, redirect
from .models import Utilisateur
from .forms import UtilisateurForm

def list_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all().order_by('-created_at')
    return render(request, 'users/list.html', {'utilisateurs': utilisateurs})

def detail_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    return render(request, 'users/detail.html', {'utilisateur': utilisateur})

def create_utilisateur(request):
    form = UtilisateurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('html_list')
    return render(request, 'users/form.html', {'form': form, 'title': 'Nouvel utilisateur'})

def update_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    form = UtilisateurForm(request.POST or None, instance=utilisateur)
    if form.is_valid():
        form.save()
        return redirect('html_list')
    return render(request, 'users/form.html', {'form': form, 'title': 'Modifier utilisateur'})

def delete_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('html_list')
    return render(request, 'users/confirm_delete.html', {'utilisateur': utilisateur})