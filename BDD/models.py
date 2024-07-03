from django.db import models
from Accounts.models import *
from django.core.exceptions import ValidationError
from Administrateurs.models import Hebergement


# Accessoire il y a dans l'hotel
class Accessoire(models.Model):
    hotel_accessoire = models.ForeignKey(
        Hebergement, on_delete=models.CASCADE, related_name='accessoires')
    nom_accessoire = models.CharField(max_length=100)
    description_accessoire = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Chambre


class Chambre(models.Model):
    hotel_chambre = models.ForeignKey(
        Hebergement, on_delete=models.CASCADE, related_name='chambres')
    type_chambre = models.CharField(max_length=100)
    prix_nuit_chambre = models.DecimalField(max_digits=8, decimal_places=2)
    disponible_chambre = models.BooleanField(default=True)
    # Champ pour le nombre de personnes dans la chambre
    nombre_personnes = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
