# serializers.py
from rest_framework import serializers
from .models import Hebergement, HebergementImage

class HebergementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HebergementImage
        fields = ('id', 'images', 'legende_hebergement', 'created_at', 'updated_at')

class HebergementSerializer(serializers.ModelSerializer):
    images = HebergementImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hebergement
        fields = ('id', 'nom_hebergement', 'description_hebergement', 'adresse_hebergement',
                  'ville_hebergement', 'nombre_etoile_hebergement', 'latitude_hebergement',
                  'longitude_hebergement', 'responsable_hebergement',
                  'type_hebergement', 'created_at', 'updated_at', 'images')
