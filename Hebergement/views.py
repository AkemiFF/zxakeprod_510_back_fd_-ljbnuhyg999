# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Hebergement.serializers import ImageChambreSerializer, HebergementSerializer
from rest_framework import generics
from Hebergement.models import ImageChambre, Hebergement


class ImageChambreListAPIView(generics.ListAPIView):
    queryset = ImageChambre.objects.all()
    serializer_class = ImageChambreSerializer


@api_view(['GET'])
def get_count(request):
    try:
        number_hebergement = Hebergement.objects.count(pk=pk)
    except Hebergement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HebergementSerializer(number_hebergement)
    return Response(serializer.data)


