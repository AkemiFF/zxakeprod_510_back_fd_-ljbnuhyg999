# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hebergement
from .serializers import HebergementSerializer

@api_view(['GET'])
def all_hebergements_view(request):
    try:
        hebergements = Hebergement.objects.prefetch_related('images').all()
        serializer = HebergementSerializer(hebergements, many=True)
        return Response(serializer.data)
    except Hebergement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
