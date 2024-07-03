# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Hebergement.serializers import ImageChambreSerializer
from rest_framework import generics
from Hebergement.models import ImageChambre


class ImageChambreListAPIView(generics.ListAPIView):
    queryset = ImageChambre.objects.all()
    serializer_class = ImageChambreSerializer
