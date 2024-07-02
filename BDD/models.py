from django.db import models
from django.core.validators import RegexValidator

# Les utilisateurs
# administrateur
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
class Responsable_etablissement(models.Model):
    email_responsable = models.EmailField()
    nom_responsable = models.CharField(max_length=100)
    prenom_responsable = models.CharField(max_length=100)
    mdp_responsable = models.CharField(max_length=100)
    numero_responsable = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^(032|033|034|038)\d{7}$',message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Client
class Client(models.Model):
    nom_client = models.CharField(max_length=100)
    prenom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    numero_client = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^(032|033|034|038)\d{7}$',message='Le numéro doit commencer par 032, 033, 034 ou 038 et contenir 7 chiffres supplémentaires.')])
    mdp_client = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
 
    
# Hotel
class Hotel(models.Model):
    nom_hotel = models.CharField(max_length=100)
    description_hotel = models.TextField()
    addresse_hotel = models.CharField(max_length=200)
    ville_hotel = models.CharField(max_length=100)
    nombre_etoile_hotel = models.IntegerField()
    latitude_hotel = models.FloatField()
    longitude_hotel = models.FloatField()
    responsable_hotel = models.ForeignKey(Responsable_etablissement, on_delete=models.CASCADE, related_name='hotels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Image hotel
class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image_hotel = models.ImageField(upload_to='hotel_images')
    legende_hotel = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
 # Accessoire il y a dans l'hotel
class Accessoire(models.Model):
    hotel_accessoire = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='accessoires')    
    nom_accessoire = models.CharField(max_length=100)
    description_accessoire = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Chambre
class Chambre(models.Model):
    hotel_chambre = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='chambres')
    type_chambre = models.CharField(max_length=100)
    prix_nuit_chambre = models.DecimalField(max_digits=8, decimal_places=2)
    disponible_chambre = models.BooleanField(default=True)
    nombre_personnes = models.IntegerField(default=1)  # Champ pour le nombre de personnes dans la chambre
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Reservation
class Reservation(models.Model):
    hotel_reserve = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations')
    chambre_reserve = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name='reservations')
    client_reserve = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reservations')
    date_debut_reserve = models.DateField()
    date_fin_reserve = models.DateField()
    nombre_personnes_reserve = models.IntegerField(default=1)  # Nombre de personnes pour la réservation
    prix_total_reserve = models.DecimalField(max_digits=10, decimal_places=2)
    est_validee_reserve = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Message
class Message(models.Model):
    expediteur = models.ForeignKey(Responsable_etablissement, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages_recus')
    sujet = models.CharField(max_length=255)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    

# Artisanat 
class Artisanat(models.Model):
    nom_artisanat = models.CharField(max_length=100)
    description_artisanat = models.TextField()
    prix_artisanat = models.DecimalField(max_digits=8, decimal_places=2)
    disponible_artisanat = models.BooleanField(default=True)
    image_artisanat = models.ImageField(upload_to='artisanat_images', blank=True)
    responsable_artisanat = models.ForeignKey(Responsable_etablissement, on_delete=models.CASCADE, related_name='produits_artisanat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Commande artisanat
class CommandeArtisanat(models.Model):
    responsable_commande = models.ForeignKey(Responsable_etablissement, on_delete=models.CASCADE, related_name='commandes')
    client_commande = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes')
    quantite_commande = models.IntegerField()
    prix_total_commande = models.DecimalField(max_digits=10, decimal_places=2)
    est_validee_commande = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)