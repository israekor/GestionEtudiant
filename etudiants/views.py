from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from formations.models import Formation
from .models import Etudiant


@login_required
def liste_formations(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard')
    formations = Formation.objects.all()
    etudiant = Etudiant.objects.filter(user=request.user).first()
    return render(request, 'etudiants/liste_formations.html', {
        'formations': formations,
        'etudiant': etudiant,
    })


@login_required
def inscrire(request, pk):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard')
    formation = get_object_or_404(Formation, pk=pk)
    etudiant = Etudiant.objects.filter(user=request.user).first()
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        if nom and prenom and email:
            if etudiant:
                etudiant.nom = nom
                etudiant.prenom = prenom
                etudiant.email = email
                etudiant.formation = formation
                etudiant.save()
            else:
                Etudiant.objects.create(
                    user=request.user,
                    nom=nom, prenom=prenom,
                    email=email, formation=formation
                )
            messages.success(
                request, f'Inscription à "{formation.titre}" confirmée !')
            return redirect('liste_formations')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')
    return render(request, 'etudiants/inscription.html', {
        'formation': formation,
        'etudiant': etudiant,
    })


@login_required
def mon_profil(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard')
    etudiant = Etudiant.objects.filter(user=request.user).first()
    return render(request, 'etudiants/profil.html', {'etudiant': etudiant})
