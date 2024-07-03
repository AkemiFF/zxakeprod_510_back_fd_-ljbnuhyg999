from django.db import models
from Accounts.models import ResponsableEtablissement
from django.core.validators import RegexValidator

# Create your models here.
class TourOperateur(models.Model):
    nom_operateur = models.CharField(max_length=100)
    responsable_TourOperateur = models.ForeignKey(ResponsableEtablissement, on_delete=models.CASCADE, related_name='tourOperateur')
    adresse_operateur = models.CharField(max_length=255)
    email_operateur = models.EmailField(unique=True)
    telephone_operateur = models.CharField(max_length=10, validators=[RegexValidator(
        regex=r'^(032|033|034|038)\d{7}$', message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    description_operateur = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_operateur

class Voyage(models.Model):
    tour_operateur = models.ForeignKey(TourOperateur, on_delete=models.CASCADE, related_name='voyages')
    nom_voyage = models.CharField(max_length=100)
    description_voyage = models.TextField()
    destination_voyage = models.CharField(max_length=255)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prix_voyage = models.DecimalField(max_digits=10, decimal_places=2)
    places_disponibles = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_voyage
    
class ImageVoyage(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='images')
    image = models.URLField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Image for {self.voyage.nom_voyage}"