from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Formation


def is_admin(user):
    return user.is_staff or user.is_superuser


@login_required
@user_passes_test(is_admin, login_url='/acces-refuse/')
def dashboard(request):
    formations = Formation.objects.all()
    return render(request, 'formations/dashboard.html', {'formations': formations})


@login_required
@user_passes_test(is_admin, login_url='/acces-refuse/')
def ajouter_formation(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        duree = request.POST.get('duree')
        prix = request.POST.get('prix')
        if titre and duree and prix:
            Formation.objects.create(titre=titre, duree=duree, prix=prix)
            messages.success(request, 'Formation ajoutée avec succès !')
            return redirect('dashboard')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    return render(request, 'formations/form_formation.html', {'titre': 'Ajouter une Formation'})


@login_required
@user_passes_test(is_admin, login_url='/acces-refuse/')
def modifier_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.titre = request.POST.get('titre', formation.titre)
        formation.duree = request.POST.get('duree', formation.duree)
        formation.prix = request.POST.get('prix', formation.prix)
        formation.save()
        messages.success(request, 'Formation modifiée avec succès !')
        return redirect('dashboard')
    return render(request, 'formations/form_formation.html', {
        'titre': 'Modifier la Formation',
        'formation': formation
    })


@login_required
@user_passes_test(is_admin, login_url='/acces-refuse/')
def supprimer_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.delete()
        messages.success(request, 'Formation supprimée !')
        return redirect('dashboard')
    return render(request, 'formations/confirmer_suppression.html', {'formation': formation})
