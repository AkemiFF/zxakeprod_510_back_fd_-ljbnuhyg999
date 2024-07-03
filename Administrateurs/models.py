from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

from Accounts.models import ResponsableEtablissement


class TypeResponsable(models.Model):
    type_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True,
    )

    def __str__(self):
        return self.type_name


class HebergementImage(models.Model):
    hebergement = models.ForeignKey(
        'Hebergement', on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='hebergement_images')
    couverture = models.BooleanField(default=False)
    legende_hebergement = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Hebergement


class Hebergement(models.Model):
    nom_hebergement = models.CharField(max_length=100)
    description_hebergement = models.TextField()
    adresse_hebergement = models.CharField(max_length=200)
    ville_hebergement = models.CharField(max_length=100)
    nombre_etoile_hebergement = models.IntegerField()
    latitude_hebergement = models.FloatField()
    longitude_hebergement = models.FloatField()
    responsable_hebergement = models.ForeignKey(
        ResponsableEtablissement, on_delete=models.CASCADE, related_name='hebergements')
    type_hebergement = models.CharField(
        max_length=100)  # Ajout du champ typehebergement
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
