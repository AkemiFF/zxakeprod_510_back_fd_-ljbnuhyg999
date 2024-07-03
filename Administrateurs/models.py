from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class TypeResponsable(models.Model):
    type_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True,
    )

    def __str__(self):
        return self.type_name

# Responsable établissement
class ResponsableEtablissement(models.Model):
    email_responsable = models.EmailField()
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)
    mdp_responsable = models.CharField(max_length=100)
    numero_responsable = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^(032|033|034|038)\d{7}$', message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    type_responsable = models.ForeignKey(
        TypeResponsable, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom_responsable} {self.prenom_responsable} ({self.type_responsable})"

# Image Hebergement
class HebergementImage(models.Model):
    hebergement = models.ForeignKey('Hebergement', on_delete=models.CASCADE, related_name='images')
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
    responsable_hebergement = models.ForeignKey(ResponsableEtablissement, on_delete=models.CASCADE, related_name='hebergements')
    type_hebergement = models.CharField(max_length=100)  # Ajout du champ typehebergement
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
