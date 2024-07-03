from Accounts.models import ResponsableEtablissement
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from Accounts.models import *


class TypeHebergement(models.Model):
    type_name = models.CharField(
        max_length=50, unique=True, null=True, blank=True,
    )

    def __str__(self):
        return self.type_name


class HebergementImage(models.Model):
    hebergement = models.ForeignKey(
        'Hebergement', on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='image/hebergement_images')
    couverture = models.BooleanField(default=False)
    legende_hebergement = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.images.name


class AccessoireHebergement(models.Model):
    nom_accessoire = models.CharField(max_length=100)
    description_accessoire = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_accessoire


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
    type_hebergement = models.ForeignKey(
        TypeHebergement, null=True, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_hebergement


class HebergementAccessoire(models.Model):
    hebergement = models.ForeignKey(Hebergement, on_delete=models.CASCADE)
    accessoire = models.ForeignKey(
        AccessoireHebergement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hebergement.nom_hebergement} - {self.accessoire.nom_accessoire}"


class AccessoireChambre(models.Model):
    nom_accessoire = models.CharField(max_length=100)
    description_accessoire = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_accessoire


class Chambre(models.Model):
    type_chambre = models.CharField(max_length=100)
    nombre_min_personnes = models.IntegerField(default=1)
    nombre_max_personnes = models.IntegerField(default=1)

    def __str__(self):
        return self.type_chambre


class ChambrePersonaliser(models.Model):
    type_chambre = models.CharField(max_length=100)
    nombre_personnes = models.IntegerField(default=1)

    def __str__(self):
        return self.type_chambre


class HebergementChambre(models.Model):
    hebergement = models.ForeignKey(Hebergement, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, null=True)
    chambre_personaliser = models.ForeignKey(
        ChambrePersonaliser, on_delete=models.CASCADE, null=True, blank=True)
    prix_nuit_chambre = models.DecimalField(max_digits=8, decimal_places=2)
    disponible_chambre = models.BooleanField(default=True)
    accessoires = models.ManyToManyField(
        'AccessoireChambre', through='HebergementChambreAccessoire')

    def __str__(self):
        return f'{self.hebergement} - {self.chambre}'


class HebergementChambreAccessoire(models.Model):
    hebergement_chambre = models.ForeignKey(
        HebergementChambre, on_delete=models.CASCADE)
    accessoire_chambre = models.ForeignKey(
        AccessoireChambre, on_delete=models.CASCADE)

    note = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.hebergement_chambre} - {self.accessoire_chambre}'


class ImageChambre(models.Model):
    hebergement_chambre = models.ForeignKey(
        'HebergementChambre', on_delete=models.CASCADE, related_name='images_chambre')
    images = models.ImageField(upload_to='image/images_chambre')
    couverture = models.BooleanField(default=False)
    legende_chambre = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.images.name

# Reservation


class Reservation(models.Model):
    hotel_reserve = models.ForeignKey(
        Hebergement, on_delete=models.CASCADE, related_name='reservations')
    chambre_reserve = models.ForeignKey(
        Chambre, on_delete=models.CASCADE, related_name='reservations')
    client_reserve = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='reservations')
    date_debut_reserve = models.DateField()
    date_fin_reserve = models.DateField()
    nombre_personnes_reserve = models.IntegerField(
        default=1)  # Nombre de personnes pour la réservation
    prix_total_reserve = models.DecimalField(max_digits=10, decimal_places=2)
    est_validee_reserve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Message


class Message(models.Model):
    expediteur = models.ForeignKey(
        ResponsableEtablissement, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='messages_recus')
    sujet = models.CharField(max_length=255)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
