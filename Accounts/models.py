from django.db import models
from django.core.validators import RegexValidator


class Administrateur(models.Model):
    nom_admin = models.CharField(max_length=100)
    prenom_admin = models.CharField(max_length=100)
    email_admin = models.EmailField()
    mdp_admin = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def set_password(self, raw_password):
    #     """
    #     Définit le mot de passe de l'administrateur en le hachant.
    #     """
    #     self.mdp_admin = make_password(raw_password)

# Responsable etablissement


class ResponsableEtablissement(models.Model):
    email_responsable = models.EmailField()
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)
    mdp_responsable = models.CharField(max_length=100)
    numero_responsable = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^(032|033|034|038)\d{7}$', message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Client


class Client(models.Model):
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    numero_client = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^(032|033|034|038)\d{7}$', message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    mdp_client = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
