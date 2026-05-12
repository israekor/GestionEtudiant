from django.db import models

# Create your models here.


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    Etudiant = 'etudiant', 'Etudiant'


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=255)
    note = models.FloatField(default=None, null=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.Etudiant
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
