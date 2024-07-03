# MyAccount/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TypeResponsableSerializer, ResponsableEtablissementSerializer, TypeCarteBancaireSerializer, ClientSerializer
from Accounts.models import TypeResponsable, ResponsableEtablissement, TypeCarteBancaire, Client


# Pour la partie TypeResponsable
@api_view(['GET'])
def type_responsable_detail(request, pk):
    try:
        type_responsable = TypeResponsable.objects.get(pk=pk)
    except TypeResponsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TypeResponsableSerializer(type_responsable)
    return Response(serializer.data)

@api_view(['POST'])
def type_responsable_create(request):
    serializer = TypeResponsableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def type_responsable_update(request, pk):
    try:
        type_responsable = TypeResponsable.objects.get(pk=pk)
    except TypeResponsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TypeResponsableSerializer(type_responsable, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def type_responsable_delete(request, pk):
    try:
        type_responsable = TypeResponsable.objects.get(pk=pk)
    except TypeResponsable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    type_responsable.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Pour la partie Responsable_etablissement
@api_view(['GET'])
def responsable_etablissement_detail(request, pk):
    try:
        responsable_etablissement = ResponsableEtablissement.objects.get(pk=pk)
    except ResponsableEtablissement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ResponsableEtablissementSerializer(responsable_etablissement)
    return Response(serializer.data)

@api_view(['POST'])
def responsable_etablissement_create(request):
    serializer = ResponsableEtablissementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def responsable_etablissement_update(request, pk):
    try:
        responsable_etablissement = ResponsableEtablissement.objects.get(pk=pk)
    except ResponsableEtablissement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ResponsableEtablissementSerializer(responsable_etablissement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def responsable_etablissement_delete(request, pk):
    try:
        responsable_etablissement = ResponsableEtablissement.objects.get(pk=pk)
    except ResponsableEtablissement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    responsable_etablissement.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Pour la partie TypeCarteBancaire
@api_view(['GET'])
def type_carte_bancaire_detail(request, pk):
    try:
        type_carte_bancaire = TypeCarteBancaire.objects.get(pk=pk)
    except TypeCarteBancaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TypeCarteBancaireSerializer(type_carte_bancaire)
    return Response(serializer.data)

@api_view(['POST'])
def type_carte_bancaire_create(request):
    serializer = TypeCarteBancaireSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def type_carte_bancaire_update(request, pk):
    try:
        type_carte_bancaire = TypeCarteBancaire.objects.get(pk=pk)
    except TypeCarteBancaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TypeCarteBancaireSerializer(type_carte_bancaire, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def type_carte_bancaire_delete(request, pk):
    try:
        type_carte_bancaire = TypeCarteBancaire.objects.get(pk=pk)
    except TypeCarteBancaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    type_carte_bancaire.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# Pour la partie Clients
@api_view(['GET'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['POST'])
def client_create(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def client_update(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def client_delete(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
