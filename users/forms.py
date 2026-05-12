from django import forms
from .models import Utilisateur, Role

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model  = Utilisateur
        fields = ['nom', 'prenom', 'email', 'pwd', 'note', 'role']
        widgets = {
            'pwd': forms.PasswordInput(render_value=True),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'email': 'Email',
            'pwd': 'Mot de passe',
            'note': 'Note',
            'role': 'Rôle',
        }